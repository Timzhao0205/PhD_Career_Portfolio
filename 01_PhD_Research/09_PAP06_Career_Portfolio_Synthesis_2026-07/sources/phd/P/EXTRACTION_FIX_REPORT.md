# Extraction repair report

Status: PASS

The source ZIP passed CRC testing. The extraction failure was caused by path
depth, not corrupted compressed data.

## Path repair

- Archive root: `PHD_HYBRID_2026-07-27` -> `P`
- Research root: `01_PhD_Research` -> `01`
- Prior strategy folder: `06_PhD_Strategy_and_HSX_Publication_2026-07` -> `06`
- Longest source archive path: 210 characters
- Longest repaired archive path: 136 characters
- Original files retained: 975
- Text files with updated internal path references: 89
- Source SHA-256: `52cdf744aab33c6c2a477c5652461e7881d7af8bf3a0cbd2bc25be1849dd3af1`

No Windows-illegal characters, reserved device names, trailing dots/spaces,
absolute paths, parent traversal paths, duplicate entries, case-insensitive
collisions, encryption, or symlinks were retained.

`PATH_RENAMES.csv` records every original-to-fixed archive path.
`TEXT_PATH_PATCHES.csv` records each text file whose internal path references
were updated. `FILE_MANIFEST_SHA256.csv` provides file-level SHA-256 hashes.
