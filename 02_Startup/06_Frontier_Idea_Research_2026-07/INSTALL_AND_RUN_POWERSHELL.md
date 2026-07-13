# Replace the old folder and run — Windows PowerShell

This archive contains the complete `06_Frontier_Idea_Research_2026-07` folder. Stop any running
Claude process before replacing the old folder.

Place/extract this folder directly under:

```text
D:\timzhao\Downloads\PhD_Career_Portfolio\02_Startup
```

The resulting launcher path must be:

```text
D:\timzhao\Downloads\PhD_Career_Portfolio\02_Startup\06_Frontier_Idea_Research_2026-07\RUN_FRONTIER_RESEARCH.ps1
```

Then run:

```powershell
cd 'D:\timzhao\Downloads\PhD_Career_Portfolio\02_Startup\06_Frontier_Idea_Research_2026-07'
.\RUN_FRONTIER_RESEARCH.ps1 -Resume -SkipModelProbe
```

Omit `-SkipModelProbe` to recheck Fable 5 and Sonnet 5 availability first:

```powershell
.\RUN_FRONTIER_RESEARCH.ps1 -Resume
```

The single command resumes at P2A. It audits source origins, replaces missing evidence if needed,
repairs the atlas, obtains Fable 5/xhigh P2A sign-off, and then automatically performs the
US/China-weighted P3 round using Fable 5/xhigh generation plus an independent Fable 5/xhigh
elegance review. P3 assumes company launch in 2030 and evaluates preparation through 2029 plus
the 2030–2034 opportunity window. If usage runs out, execute the same
`-Resume -SkipModelProbe` command later.
