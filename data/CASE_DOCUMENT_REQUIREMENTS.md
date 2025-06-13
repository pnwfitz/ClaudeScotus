# Case Document Requirements

**Updated**: 2025-06-11  
**Source**: CourtListener API

## Required Documents

1. **Supreme Court Opinion** - `opinions/majority_opinion.pdf`
2. **Dissenting Opinions** - `opinions/dissents/[justice]_dissent.pdf` (if exist)
3. **Concurring Opinions** - `opinions/concurrences/[justice]_concurrence.pdf` (if exist)
4. **Petitioner Brief** - `briefs/petitioner_brief.pdf`
5. **Respondent Brief** - `briefs/respondent_brief.pdf`
6. **Oral Argument Transcript** - `oral_arguments/transcript.pdf` (if held)
7. **Lower Court Decision** - `opinions/lower_court_decision.pdf`
8. **Cert Petition** - `briefs/cert_petition.pdf`

## **File Structure Per Case**
```
data/terms/2022-2023/cases/[docket-number]_[case-name]/
├── README.md
├── metadata.json
├── briefs/
│   ├── petitioner_brief.pdf
│   ├── respondent_brief.pdf
│   └── cert_petition.pdf
├── oral_arguments/
│   └── transcript.pdf
└── opinions/
    ├── majority_opinion.pdf
    ├── lower_court_decision.pdf
    ├── dissents/
    │   └── [justice]_dissent.pdf
    └── concurrences/
        └── [justice]_concurrence.pdf
```

## Success Criteria
- All document types attempted
- File structure populated
- Missing documents noted in README
- Source URLs in metadata.json

## Constraints
- CourtListener API only
- No fallback sources
- Document API limitations

## Goal
Test CourtListener API coverage before considering additional sources.