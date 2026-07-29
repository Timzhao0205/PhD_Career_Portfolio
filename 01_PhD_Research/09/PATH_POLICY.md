# Windows path policy

- Extract to `C:\AI\PAP06N` when possible.
- The package uses short top-level names and contains no filename invalid on
  Windows.
- The longest packaged path is validated against a 240-character installed
  path target under `C:\AI\PAP06N`.
- Do not extract into a deeply nested Downloads/OneDrive hierarchy.
- Outputs use short stage IDs and `attempt-N` directories.
- No runtime archive extraction or path reconstruction occurs.
