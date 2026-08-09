# Package verification report

Build date: 2026-08-05

## Completed before packaging

- Supplied manuscript source ZIP passed full CRC testing and contains the
  expected 17 entries.
- Submission PDF has a valid PDF header, is unencrypted, contains nine pages,
  and was text-extracted and visually inspected at the packaging disclosure.
- Immutable SHA-256 values were recomputed for the original source ZIP,
  submission PDF, and extracted TeX file.
- Both JSON files parsed successfully.
- All three CSV files parsed with a constant column count; the model log has 18
  columns and the prior-art seed table has 10.
- Eight Claude Code stage agents have complete frontmatter and match the model/
  effort table.
- Package contains no empty files, no Windows-invalid names, and a maximum
  relative path of 56 characters. At `C:\HSX_IP`, the corresponding full path is
  approximately 66 characters.
- The original manuscript ZIP and final delivery ZIP were tested for archive
  integrity.
- The workflow contains no `Verified current sources < 30` or similar numeric
  acceptance rule. Evidence gates are based on coverage and traceability.

## Validation performed on the user's Windows machine before any model call

`PREFLIGHT.ps1`, invoked automatically by `START.ps1`, uses the native PowerShell
AST parser to check both `.ps1` files, validates all JSON and stage agent policies,
checks seed schemas/coverage, authenticates Claude Code, requires version
2.1.219 or newer, opens the source ZIP through .NET, checks the PDF header,
recomputes all hashes, and rejects unsafe Windows paths or filenames.

If a prerequisite fails, it prints the exact failing condition and exits before
Claude Code starts. No generic package-validation message is used.

The build environment was Linux and therefore did not execute Windows
PowerShell itself. The runtime AST self-check is included specifically so the
native Windows parser validates the scripts before Claude launches.
