# Supreme Court Data Repository

## Structure

### Terms
- [2022-2023](terms/2022-2023/) - Jackson's first term
- [2023-2024](terms/2023-2024/) - Completed term  
- [2024-2025](terms/2024-2025/) - Current term

### Justice Profiles
- [Roberts](justices/roberts.md) - Chief Justice
- [Thomas](justices/thomas.md) - Senior Associate
- [Alito](justices/alito.md)
- [Sotomayor](justices/sotomayor.md)
- [Kagan](justices/kagan.md)
- [Gorsuch](justices/gorsuch.md)
- [Kavanaugh](justices/kavanaugh.md)
- [Barrett](justices/barrett.md)
- [Jackson](justices/jackson.md) - Newest

### Analysis
- [Predictions](analysis/predictions/) - Current predictions
- [Accuracy](analysis/accuracy_tracking/) - Performance metrics

## Case File Structure

Each case folder contains:
```
[docket-number]_[case-name]/
├── README.md           # Case summary and outcome
├── briefs/
│   ├── petitioner_brief.pdf
│   └── respondent_brief.pdf
├── oral_arguments/
│   └── transcript.pdf
├── opinions/
│   ├── majority_opinion.pdf
│   ├── dissents/
│   └── concurrences/
└── metadata.json       # Structured case data
```

## Usage

- Case predictions: Check case README.md files
- Justice analysis: `/justices/` directory
- Term cases: `/terms/[year]/cases/`