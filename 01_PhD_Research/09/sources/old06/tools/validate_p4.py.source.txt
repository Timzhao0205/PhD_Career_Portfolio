#!/usr/bin/env python3
"""Deterministic mechanical validation for P4 scorecards."""

from __future__ import annotations

import collections
import json
import math
import pathlib
import re
import sys
from typing import Any, Iterable


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCORECARD_DIR = ROOT / "30_SCREENING" / "SCORECARDS"
EVIDENCE_DIR = ROOT / "30_SCREENING" / "EVIDENCE"

EXPECTED_SUBSET_SIZES = {"S1": 17, "S2": 16, "S3": 16, "S4": 16}
PASS_VERDICTS = {"pass", "pass_marginal"}
FAIL_VERDICTS = {"fail", "blocked"}
ALL_VERDICTS = PASS_VERDICTS | FAIL_VERDICTS
CONFIDENCE_VALUES = {"low", "medium", "high"}

SCORE_WEIGHTS = {
    "demonstrated_demand": 16,
    "frontier_coolness_vision": 15,
    "high_end_niche_quality": 10,
    "competition_whitespace": 9,
    "reachable_validation_budget": 9,
    "technical_elegance_controllability": 11,
    "tenx_technical_edge": 7,
    "us_china_dual_market_leverage": 10,
    "launch_window_fit_2030": 8,
    "expansion_economics": 3,
    "founder_skill_transfer": 2,
}

# One-decimal scorecards can differ from an unrounded calculation by 0.05.
WEIGHT_TOLERANCE = 0.051
TOTAL_TOLERANCE = 0.051

FULL_SOURCE_ID_RE = re.compile(
    r"(?<![A-Za-z0-9])(?:L\d{2}-\d{3}|P3R2-[A-G]-\d{2}-S\d{2})(?![A-Za-z0-9])"
)
ATLAS_SHORTHAND_RE = re.compile(
    r"(?<![A-Za-z0-9])L(\d{2})-(\d{3})((?:/\d{3})+)"
)
P4_SHORTHAND_RE = re.compile(
    r"(?<![A-Za-z0-9])(P3R2-[A-G]-\d{2})-S(\d{2})((?:/S?\d{2})+)"
)
LOCAL_SOURCE_ID_RE = re.compile(
    r"(?<![A-Za-z0-9-])S(\d{2})(?![A-Za-z0-9])"
)
P4_SOURCE_ID_RE = re.compile(r"^(P3R2-[A-G]-\d{2})-S\d{2}$")

EXCLUDED_MARKET_RE = re.compile(r"\b(?:India|Indian|Singapore|Singaporean)\b", re.I)
COMMERCIAL_CONTEXT_RE = re.compile(
    r"\b(?:market|buyer|customer|procurement|tender|sales?|sell|sold|revenue|"
    r"beachhead|entry|TAM|SAM|pricing|price|demand|competitor|incumbent|pilot|"
    r"factory|plant|utility|operator|government|regulator|policy|supply[ -]chain|"
    r"geograph(?:y|ic|ical)|launch|commercial)\b",
    re.I,
)
EXCLUSION_CONTEXT_RE = re.compile(
    r"\b(?:exclude(?:d|s|ing)?|not|no|never|without|outside|out[ -]of[ -]scope|"
    r"foreclos(?:e|ed|ure)|prohibit(?:ed|s)?|ineligible|cannot|must[ -]not|"
    r"may[ -]not|does[ -]not|do[ -]not|irrelevant)\b",
    re.I,
)

SENTINEL_LINE_RE = re.compile(
    r"(?im)^\s*(?:<<<[^\r\n]*>>>|\[(?:APPEND|TRUNCATED)\]|"
    r"__(?:APPEND|TRUNCATED)__|(?:APPEND|TRUNCATED)_HERE)\s*,?\s*$"
)


class DuplicateJsonKey(ValueError):
    pass


def display_path(path: pathlib.Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateJsonKey(f"duplicate JSON object key {key!r}")
        result[key] = value
    return result


def reject_nonfinite_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON number {value}")


def load_json(path: pathlib.Path, errors: list[str]) -> Any | None:
    label = display_path(path)
    if not path.is_file():
        errors.append(f"{label}: missing file")
        return None
    try:
        text = path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        errors.append(f"{label}: cannot read as UTF-8: {exc}")
        return None
    if "\x00" in text:
        errors.append(f"{label}: contains a NUL/truncation artifact")
    if "<<<APPEND>>>" in text:
        errors.append(f"{label}: contains sentinel '<<<APPEND>>>'")
    else:
        marker = SENTINEL_LINE_RE.search(text)
        if marker:
            errors.append(f"{label}: contains sentinel {marker.group(0).strip()!r}")
    try:
        return json.loads(
            text,
            object_pairs_hook=reject_duplicate_keys,
            parse_constant=reject_nonfinite_constant,
        )
    except (json.JSONDecodeError, DuplicateJsonKey, ValueError) as exc:
        errors.append(f"{label}: invalid JSON: {exc}")
        return None


def idea_list(payload: Any, label: str, errors: list[str]) -> list[Any] | None:
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict) and isinstance(payload.get("ideas"), list):
        return payload["ideas"]
    errors.append(f"{label}: root must be an array or an object with an 'ideas' array")
    return None


def collect_idea_ids(records: list[Any], label: str, errors: list[str]) -> list[str]:
    result: list[str] = []
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            errors.append(f"{label}[{index}]: idea record must be an object")
            continue
        idea_id = record.get("idea_id")
        if not isinstance(idea_id, str) or not idea_id.strip():
            errors.append(f"{label}[{index}]: missing non-empty idea_id")
            continue
        result.append(idea_id.strip())
    return result


def describe_set_delta(actual: set[str], expected: set[str]) -> str:
    parts = []
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    if missing:
        parts.append(f"missing={missing}")
    if extra:
        parts.append(f"extra={extra}")
    return "; ".join(parts) or "no set difference"


def is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def extract_citations(text: str, idea_id: str) -> set[str]:
    citations = set(FULL_SOURCE_ID_RE.findall(text))
    for lane, first, tail in ATLAS_SHORTHAND_RE.findall(text):
        citations.add(f"L{lane}-{first}")
        citations.update(f"L{lane}-{suffix}" for suffix in tail.split("/") if suffix)
    for cited_idea, first, tail in P4_SHORTHAND_RE.findall(text):
        citations.add(f"{cited_idea}-S{first}")
        citations.update(
            f"{cited_idea}-S{suffix.lstrip('S')}"
            for suffix in tail.split("/")
            if suffix
        )
    # Do not reinterpret the Sxx portion of a fully qualified (possibly cross-idea)
    # citation as a local citation. Standalone S01 and S01/S02 shorthand remains valid.
    local_text = P4_SHORTHAND_RE.sub("", text)
    local_text = FULL_SOURCE_ID_RE.sub("", local_text)
    citations.update(
        f"{idea_id}-S{suffix}" for suffix in LOCAL_SOURCE_ID_RE.findall(local_text)
    )
    return citations


def source_record_problems(record: dict[str, Any], idea_id: str, source_id: str) -> list[str]:
    problems = []
    if record.get("accepted") is not True:
        problems.append("accepted is not true")
    if record.get("fetched") is not True:
        problems.append("fetched is not true")
    if record.get("source_type") == "discovery_only":
        problems.append("source_type is discovery_only")
    if record.get("tier") not in {"T1", "T2", "T3"}:
        problems.append("tier is not T1/T2/T3")
    if not isinstance(record.get("locator"), str) or not record["locator"].strip():
        problems.append("locator is empty")
    if not isinstance(record.get("claim_supported"), str) or not record["claim_supported"].strip():
        problems.append("claim_supported is empty")

    audit = record.get("india_origin_audit")
    allowed_origin = {"verified_non_india_origin", "verified_multinational_allowed"}
    if not isinstance(audit, dict):
        problems.append("India-origin audit is missing")
    else:
        status = audit.get("status")
        if status not in allowed_origin:
            problems.append(f"India-origin status is {status!r}")
        if not audit.get("audited_at"):
            problems.append("India-origin audit date is empty")
        if not isinstance(audit.get("methods"), list) or not audit.get("methods"):
            problems.append("India-origin audit methods are empty")
        if not isinstance(audit.get("evidence_urls"), list) or not audit.get("evidence_urls"):
            problems.append("India-origin audit evidence_urls are empty")

        institutions = audit.get("institutions")
        india_institution = False
        if isinstance(institutions, list):
            for institution in institutions:
                if isinstance(institution, dict):
                    country = str(institution.get("country", "")).strip().upper()
                    if country in {"IN", "IND", "INDIA"}:
                        india_institution = True
                        break
        if status == "verified_non_india_origin" and india_institution:
            problems.append("non-India audit status contradicts an India institution")
        if status == "verified_multinational_allowed":
            if record.get("source_type") != "academic_peer_reviewed":
                problems.append("multinational exception is not an academic source")
            count = audit.get("non_indian_affiliation_count")
            if not is_number(count) or count < 1:
                problems.append("multinational exception lacks a verified non-Indian affiliation")

    if record.get("source_type") == "academic_peer_reviewed":
        if record.get("peer_review_status") != "verified":
            problems.append("academic peer review is not verified")
        if not isinstance(record.get("peer_review_evidence_url"), str) or not record[
            "peer_review_evidence_url"
        ].strip():
            problems.append("peer-review evidence URL is empty")
        if not (record.get("doi") or record.get("url")):
            problems.append("academic source lacks DOI/publisher URL")
        url = str(record.get("url", "")).lower()
        if any(host in url for host in ("arxiv.org", "ssrn.com", "biorxiv.org", "medrxiv.org")):
            problems.append("academic source points to a preprint host")

    p4_match = P4_SOURCE_ID_RE.fullmatch(source_id)
    if p4_match:
        source_idea = p4_match.group(1)
        if source_idea != idea_id:
            problems.append(f"idea-local evidence belongs to {source_idea}, not {idea_id}")
        idea_ids = record.get("idea_ids")
        if not isinstance(idea_ids, list) or idea_id not in idea_ids:
            problems.append(f"idea_ids does not contain {idea_id}")
    return problems


def validate_citations(
    text: str,
    idea_id: str,
    location: str,
    source_index: dict[str, list[dict[str, Any]]],
    errors: list[str],
) -> set[str]:
    citations = extract_citations(text, idea_id)
    for source_id in sorted(citations):
        candidates = source_index.get(source_id, [])
        if not candidates:
            errors.append(
                f"{location}: unresolved citation {source_id}; not found in the canonical ledger "
                "or P4 evidence source ledgers"
            )
            continue
        candidate_problems = [source_record_problems(c, idea_id, source_id) for c in candidates]
        if not any(not problems for problems in candidate_problems):
            summaries = sorted({"; ".join(problems) for problems in candidate_problems})
            detail = " | ".join(summaries[:3])
            errors.append(f"{location}: citation {source_id} has no eligible record ({detail})")
    return citations


def iter_strings(value: Any, path: str = "") -> Iterable[tuple[str, str]]:
    if isinstance(value, str):
        yield path, value
    elif isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}" if path else str(key)
            yield from iter_strings(child, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from iter_strings(child, f"{path}[{index}]")


def validate_excluded_markets(record: dict[str, Any], location: str, errors: list[str]) -> None:
    for field_path, text in iter_strings(record):
        for segment in re.split(r"(?<=[.!?;])\s+|[\r\n]+", text):
            if (
                EXCLUDED_MARKET_RE.search(segment)
                and COMMERCIAL_CONTEXT_RE.search(segment)
                and not EXCLUSION_CONTEXT_RE.search(segment)
            ):
                snippet = re.sub(r"\s+", " ", segment).strip()
                if len(snippet) > 220:
                    snippet = snippet[:217] + "..."
                errors.append(
                    f"{location}.{field_path}: excluded-market commercial reference: {snippet!r}"
                )


def validate_score_range(
    value: Any,
    total: float | None,
    location: str,
    errors: list[str],
) -> None:
    if not isinstance(value, list) or len(value) != 2 or not all(is_number(x) for x in value):
        errors.append(f"{location}: must be a two-number [low, high] array")
        return
    low, high = float(value[0]), float(value[1])
    if not (0 <= low <= high <= 100):
        errors.append(f"{location}: invalid bounds {value!r}; require 0 <= low <= high <= 100")
    if total is not None and not (low - TOTAL_TOLERANCE <= total <= high + TOTAL_TOLERANCE):
        errors.append(f"{location}: score_total {total:g} is outside range {value!r}")


def validate_score_record(
    record: dict[str, Any],
    location: str,
    frozen_ids: set[str],
    source_index: dict[str, list[dict[str, Any]]],
    errors: list[str],
) -> None:
    required_fields = {
        "idea_id",
        "physics_build_review",
        "gates",
        "eliminated",
        "elimination_reason",
        "scores",
        "score_total",
        "score_range",
        "confidence",
        "uncertainty_notes",
        "redteam_flags_for_p5",
    }
    missing_fields = sorted(required_fields - set(record))
    if missing_fields:
        errors.append(f"{location}: missing required fields {missing_fields}")

    idea_id_value = record.get("idea_id")
    idea_id = idea_id_value.strip() if isinstance(idea_id_value, str) else ""
    if not idea_id:
        errors.append(f"{location}.idea_id: must be a non-empty string")
        idea_id = "<missing-idea-id>"
    elif idea_id not in frozen_ids:
        errors.append(f"{location}.idea_id: {idea_id!r} is not in the frozen longlist")

    physics = record.get("physics_build_review")
    if not isinstance(physics, str) or not physics.strip():
        errors.append(f"{location}.physics_build_review: must be a non-empty string")

    gates = record.get("gates")
    gate_verdicts: dict[str, str] = {}
    if not isinstance(gates, dict):
        errors.append(f"{location}.gates: must be an object containing G1-G7")
    else:
        expected_gates = {f"G{number}" for number in range(1, 8)}
        missing_gates = sorted(expected_gates - set(gates))
        if missing_gates:
            errors.append(f"{location}.gates: missing {missing_gates}")
        for gate in sorted(expected_gates & set(gates)):
            gate_value = gates[gate]
            gate_location = f"{location}.gates.{gate}"
            if not isinstance(gate_value, dict):
                errors.append(f"{gate_location}: must be an object")
                continue
            verdict = gate_value.get("verdict")
            if not isinstance(verdict, str) or verdict not in ALL_VERDICTS:
                errors.append(
                    f"{gate_location}.verdict: must be one of {sorted(ALL_VERDICTS)}, got {verdict!r}"
                )
            else:
                gate_verdicts[gate] = verdict
            rationale = gate_value.get("rationale")
            if not isinstance(rationale, str) or not rationale.strip():
                errors.append(f"{gate_location}.rationale: must be a non-empty string")
            else:
                validate_citations(
                    rationale,
                    idea_id,
                    f"{gate_location}.rationale",
                    source_index,
                    errors,
                )

    eliminated = record.get("eliminated")
    if not isinstance(eliminated, bool):
        errors.append(f"{location}.eliminated: must be true or false")
    failed_gates = sorted(gate for gate, verdict in gate_verdicts.items() if verdict in FAIL_VERDICTS)
    nonpassing_gates = sorted(
        gate for gate, verdict in gate_verdicts.items() if verdict not in PASS_VERDICTS
    )
    if failed_gates and eliminated is not True:
        errors.append(
            f"{location}: failed/blocked gates {failed_gates} require eliminated=true"
        )
    if eliminated is False and nonpassing_gates:
        errors.append(f"{location}: survivor has non-passing gates {nonpassing_gates}")
    if eliminated is True and len(gate_verdicts) == 7 and not failed_gates:
        errors.append(f"{location}: eliminated=true but no gate verdict is fail or blocked")

    elimination_reason = record.get("elimination_reason")
    if eliminated is True:
        if not isinstance(elimination_reason, str) or not elimination_reason.strip():
            errors.append(f"{location}.elimination_reason: eliminated idea requires a reason")
    elif eliminated is False and elimination_reason not in (None, ""):
        errors.append(f"{location}.elimination_reason: survivor must use null or an empty string")

    scores = record.get("scores")
    score_total_value = record.get("score_total")
    score_range = record.get("score_range")
    if scores is None:
        errors.append(f"{location}.scores: every idea requires all 11 score fields")
        total: float | None = None
        if not is_number(score_total_value):
            errors.append(f"{location}.score_total: every idea requires a finite number")
        else:
            total = float(score_total_value)
            if not 0 <= total <= 100:
                errors.append(f"{location}.score_total: {total:g} is outside [0, 100]")
        validate_score_range(score_range, total, f"{location}.score_range", errors)
    elif not isinstance(scores, dict):
        errors.append(f"{location}.scores: must be an object or null for an eliminated idea")
    else:
        expected_scores = set(SCORE_WEIGHTS)
        missing_scores = sorted(expected_scores - set(scores))
        extra_scores = sorted(set(scores) - expected_scores)
        if missing_scores:
            errors.append(f"{location}.scores: missing score fields {missing_scores}")
        if extra_scores:
            errors.append(f"{location}.scores: unexpected score fields {extra_scores}")

        weighted_values: list[float] = []
        all_weighted_valid = len(scores) == len(SCORE_WEIGHTS)
        for score_name, weight in SCORE_WEIGHTS.items():
            if score_name not in scores:
                all_weighted_valid = False
                continue
            score = scores[score_name]
            score_location = f"{location}.scores.{score_name}"
            if not isinstance(score, dict):
                errors.append(f"{score_location}: must be an object")
                all_weighted_valid = False
                continue
            for field in ("raw", "weighted", "evidence"):
                if field not in score:
                    errors.append(f"{score_location}: missing {field!r}")

            raw = score.get("raw")
            weighted = score.get("weighted")
            if not is_number(raw):
                errors.append(f"{score_location}.raw: must be a finite number in [0, 5]")
            elif not 0 <= float(raw) <= 5:
                errors.append(f"{score_location}.raw: {raw!r} is outside [0, 5]")
            if not is_number(weighted):
                errors.append(f"{score_location}.weighted: must be a finite number")
                all_weighted_valid = False
            else:
                weighted_value = float(weighted)
                weighted_values.append(weighted_value)
                if is_number(raw):
                    expected_weighted = float(raw) * weight / 5.0
                    if not math.isclose(
                        weighted_value,
                        expected_weighted,
                        rel_tol=0.0,
                        abs_tol=WEIGHT_TOLERANCE,
                    ):
                        errors.append(
                            f"{score_location}.weighted: {weighted_value:g} != raw {float(raw):g} "
                            f"* weight {weight} / 5 ({expected_weighted:g})"
                        )

            evidence = score.get("evidence")
            if not isinstance(evidence, str) or not evidence.strip():
                errors.append(f"{score_location}.evidence: must be a non-empty string")
            else:
                citations = validate_citations(
                    evidence,
                    idea_id,
                    f"{score_location}.evidence",
                    source_index,
                    errors,
                )
                if is_number(raw) and float(raw) > 3 and not citations:
                    errors.append(
                        f"{score_location}.evidence: raw score {float(raw):g} > 3 requires "
                        "at least one source-ID citation"
                    )

        total: float | None = None
        if not is_number(score_total_value):
            errors.append(f"{location}.score_total: scored idea requires a finite number")
        else:
            total = float(score_total_value)
            if not 0 <= total <= 100:
                errors.append(f"{location}.score_total: {total:g} is outside [0, 100]")
            if all_weighted_valid and len(weighted_values) == len(SCORE_WEIGHTS):
                weighted_sum = sum(weighted_values)
                if not math.isclose(
                    total,
                    weighted_sum,
                    rel_tol=0.0,
                    abs_tol=TOTAL_TOLERANCE,
                ):
                    errors.append(
                        f"{location}.score_total: {total:g} != sum(weighted) {weighted_sum:g}"
                    )
        validate_score_range(score_range, total, f"{location}.score_range", errors)

    confidence = record.get("confidence")
    if confidence not in CONFIDENCE_VALUES:
        errors.append(
            f"{location}.confidence: must be one of {sorted(CONFIDENCE_VALUES)}, got {confidence!r}"
        )
    uncertainty = record.get("uncertainty_notes")
    if not isinstance(uncertainty, str) or not uncertainty.strip():
        errors.append(f"{location}.uncertainty_notes: must be a non-empty string")
    flags = record.get("redteam_flags_for_p5")
    if not isinstance(flags, list) or not flags:
        errors.append(f"{location}.redteam_flags_for_p5: must be a non-empty array")
    elif any(not isinstance(flag, str) or not flag.strip() for flag in flags):
        errors.append(f"{location}.redteam_flags_for_p5: every flag must be a non-empty string")

    validate_excluded_markets(record, location, errors)


def load_source_index(errors: list[str]) -> dict[str, list[dict[str, Any]]]:
    source_index: dict[str, list[dict[str, Any]]] = collections.defaultdict(list)
    source_files = [ROOT / "90_BIBLIOGRAPHY" / "sources.json"]
    source_files.extend(EVIDENCE_DIR / f"P4-G{number:02d}_sources.json" for number in range(1, 14))
    for path in source_files:
        payload = load_json(path, errors)
        if payload is None:
            continue
        label = display_path(path)
        if not isinstance(payload, list):
            errors.append(f"{label}: source ledger root must be an array")
            continue
        for index, record in enumerate(payload):
            if not isinstance(record, dict):
                errors.append(f"{label}[{index}]: source record must be an object")
                continue
            source_id = record.get("id")
            if not isinstance(source_id, str) or not source_id.strip():
                errors.append(f"{label}[{index}]: source record has no non-empty id")
                continue
            source_index[source_id.strip()].append(record)
    return dict(source_index)


def report(errors: list[str], mode: str, validated_records: list[dict[str, Any]]) -> int:
    if errors:
        unique_errors = sorted(set(errors))
        print(f"P4 VALIDATION FAIL: mode={mode} errors={len(unique_errors)}")
        for error in unique_errors[:200]:
            print(f"- {error}")
        if len(unique_errors) > 200:
            print(f"- ... {len(unique_errors) - 200} additional errors omitted")
        return 1

    survivors = sum(record.get("eliminated") is False for record in validated_records)
    eliminated = sum(record.get("eliminated") is True for record in validated_records)
    print(
        f"P4 VALIDATION PASS: mode={mode} ideas={len(validated_records)} "
        f"survivors={survivors} eliminated={eliminated}"
    )
    return 0


def main() -> int:
    errors: list[str] = []

    longlist_path = ROOT / "30_SCREENING" / "LONGLIST.json"
    longlist_payload = load_json(longlist_path, errors)
    if longlist_payload is None:
        return report(errors, "unavailable", [])
    longlist_records = idea_list(longlist_payload, display_path(longlist_path), errors)
    if longlist_records is None:
        return report(errors, "unavailable", [])
    frozen_id_list = collect_idea_ids(longlist_records, display_path(longlist_path), errors)
    frozen_counts = collections.Counter(frozen_id_list)
    duplicate_frozen = sorted(idea_id for idea_id, count in frozen_counts.items() if count != 1)
    if len(longlist_records) != 65:
        errors.append(
            f"{display_path(longlist_path)}: expected exactly 65 records, found {len(longlist_records)}"
        )
    if len(frozen_counts) != 65:
        errors.append(
            f"{display_path(longlist_path)}: expected 65 unique idea IDs, found {len(frozen_counts)}"
        )
    if duplicate_frozen:
        errors.append(f"{display_path(longlist_path)}: duplicate idea IDs {duplicate_frozen}")
    frozen_ids = set(frozen_id_list)

    subset_ids: dict[str, list[str]] = {}
    for batch, expected_size in EXPECTED_SUBSET_SIZES.items():
        path = SCORECARD_DIR / f"_subset_{batch}.json"
        payload = load_json(path, errors)
        if payload is None:
            continue
        records = idea_list(payload, display_path(path), errors)
        if records is None:
            continue
        ids = collect_idea_ids(records, display_path(path), errors)
        subset_ids[batch] = ids
        counts = collections.Counter(ids)
        duplicates = sorted(idea_id for idea_id, count in counts.items() if count != 1)
        if len(records) != expected_size:
            errors.append(
                f"{display_path(path)}: expected {expected_size} records, found {len(records)}"
            )
        if duplicates:
            errors.append(f"{display_path(path)}: duplicate idea IDs {duplicates}")
        if set(ids) - frozen_ids:
            errors.append(
                f"{display_path(path)}: contains IDs outside frozen longlist "
                f"{sorted(set(ids) - frozen_ids)}"
            )

    all_subset_ids = [idea_id for ids in subset_ids.values() for idea_id in ids]
    subset_counts = collections.Counter(all_subset_ids)
    overlapping_subset_ids = sorted(
        idea_id for idea_id, count in subset_counts.items() if count != 1
    )
    if overlapping_subset_ids:
        errors.append(f"score subsets do not partition uniquely; repeated IDs {overlapping_subset_ids}")
    if set(all_subset_ids) != frozen_ids:
        errors.append(
            "score subset union does not exactly match frozen longlist: "
            + describe_set_delta(set(all_subset_ids), frozen_ids)
        )

    source_index = load_source_index(errors)
    authoritative_path = SCORECARD_DIR / "P4_SCORES_ALL.json"
    mode = "authoritative" if authoritative_path.is_file() else "batches"
    scored_records: list[dict[str, Any]] = []
    record_locations: list[str] = []

    if mode == "authoritative":
        payload = load_json(authoritative_path, errors)
        if payload is not None:
            records = idea_list(payload, display_path(authoritative_path), errors)
            if records is not None:
                ids = collect_idea_ids(records, display_path(authoritative_path), errors)
                counts = collections.Counter(ids)
                duplicates = sorted(idea_id for idea_id, count in counts.items() if count != 1)
                if len(records) != 65:
                    errors.append(
                        f"{display_path(authoritative_path)}: expected exactly 65 ideas, found {len(records)}"
                    )
                if duplicates:
                    errors.append(
                        f"{display_path(authoritative_path)}: duplicate idea IDs {duplicates}"
                    )
                if set(ids) != frozen_ids:
                    errors.append(
                        f"{display_path(authoritative_path)}: membership does not match frozen longlist: "
                        + describe_set_delta(set(ids), frozen_ids)
                    )
                for index, record in enumerate(records):
                    if isinstance(record, dict):
                        scored_records.append(record)
                        record_locations.append(
                            f"{display_path(authoritative_path)}.ideas[{index}]"
                        )
    else:
        for batch in EXPECTED_SUBSET_SIZES:
            path = SCORECARD_DIR / f"P4_SCORES_{batch}.json"
            payload = load_json(path, errors)
            if payload is None:
                continue
            records = idea_list(payload, display_path(path), errors)
            if records is None:
                continue
            ids = collect_idea_ids(records, display_path(path), errors)
            expected = set(subset_ids.get(batch, []))
            counts = collections.Counter(ids)
            duplicates = sorted(idea_id for idea_id, count in counts.items() if count != 1)
            if duplicates:
                errors.append(f"{display_path(path)}: duplicate idea IDs {duplicates}")
            if len(records) != EXPECTED_SUBSET_SIZES[batch]:
                errors.append(
                    f"{display_path(path)}: expected {EXPECTED_SUBSET_SIZES[batch]} ideas, "
                    f"found {len(records)}"
                )
            if set(ids) != expected:
                errors.append(
                    f"{display_path(path)}: membership does not match _subset_{batch}.json: "
                    + describe_set_delta(set(ids), expected)
                )
            for index, record in enumerate(records):
                if isinstance(record, dict):
                    scored_records.append(record)
                    record_locations.append(f"{display_path(path)}.ideas[{index}]")

        all_scored_ids = [
            record.get("idea_id").strip()
            for record in scored_records
            if isinstance(record.get("idea_id"), str) and record.get("idea_id").strip()
        ]
        scored_counts = collections.Counter(all_scored_ids)
        duplicates = sorted(idea_id for idea_id, count in scored_counts.items() if count != 1)
        if len(scored_records) != 65:
            errors.append(f"batch scorecards cover {len(scored_records)} records; expected exactly 65")
        if duplicates:
            errors.append(f"batch scorecards repeat idea IDs {duplicates}")
        if set(all_scored_ids) != frozen_ids:
            errors.append(
                "batch scorecard union does not exactly match frozen longlist: "
                + describe_set_delta(set(all_scored_ids), frozen_ids)
            )

    for record, location in zip(scored_records, record_locations):
        validate_score_record(record, location, frozen_ids, source_index, errors)

    return report(errors, mode, scored_records)


if __name__ == "__main__":
    sys.exit(main())
