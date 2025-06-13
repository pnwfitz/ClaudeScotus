# Sample Case Structure - Students for Fair Admissions v. Harvard

**This is an example of how each case folder should be organized**

## Directory Structure
```
data/terms/2022-2023/cases/21-707_students-for-fair-admissions-v-harvard/
├── README.md                    # This file - case overview
├── briefs/
│   ├── petitioner_brief.pdf    # Students for Fair Admissions brief
│   ├── respondent_brief.pdf    # Harvard University brief
│   ├── amicus_briefs/
│   │   ├── united_states.pdf   # US Government amicus brief
│   │   ├── military_leaders.pdf # Veterans/Military amicus
│   │   └── fortune_500.pdf     # Business community amicus
│   └── cert_petition.pdf       # Original petition for certiorari
├── oral_arguments/
│   ├── transcript.pdf          # Official argument transcript
│   ├── audio.mp3              # Oral argument audio (if available)
│   └── argument_analysis.md    # Key moments and Justice questioning patterns
├── opinions/
│   ├── majority_opinion.pdf    # Chief Justice Roberts majority
│   ├── dissents/
│   │   ├── sotomayor_dissent.pdf  # Justice Sotomayor dissent
│   │   └── jackson_dissent.pdf    # Justice Jackson dissent
│   ├── concurrences/
│   │   ├── thomas_concurrence.pdf # Justice Thomas concurrence
│   │   └── gorsuch_concurrence.pdf # Justice Gorsuch concurrence
│   └── opinion_analysis.md     # Vote breakdown and reasoning analysis
└── metadata.json              # Structured case data
```

## Case README.md Content Template

```markdown
# Students for Fair Admissions v. Harvard (2023)

**Docket Number**: 21-707  
**Decision Date**: June 29, 2023  
**Vote**: 6-3 (Conservative majority)

## Case Summary
Supreme Court ruled that Harvard's race-conscious admissions program violates Equal Protection Clause, effectively ending affirmative action in higher education.

## ClaudeScotus Analysis
**Prediction Difficulty**: Medium  
**Conservative Coalition Strength**: High (6-3 split predictable)  
**Business Impact**: Broad - affects all higher education institutions

## Vote Breakdown
**Majority (6)**: Roberts (author), Thomas, Alito, Gorsuch, Kavanaugh, Barrett  
**Dissent (3)**: Sotomayor, Kagan, Jackson

## Key Legal Questions
1. Whether Harvard's race-conscious admissions program violates Equal Protection
2. Scope of diversity as compelling government interest
3. Future of race-conscious government programs

## Broader Implications
- Ends decades of affirmative action precedent
- Signals conservative approach to civil rights law
- Creates new framework for equal protection analysis

## Amateur Guide
**What Happened**: Supreme Court banned colleges from considering race in admissions  
**Why It Matters**: Changes how universities select students nationwide  
**Real Impact**: Likely to reduce minority enrollment at selective colleges
```

## Metadata.json Template

```json
{
  "docket_number": "21-707",
  "case_name": "Students for Fair Admissions v. Harvard",
  "short_name": "SFFA v. Harvard",
  "decision_date": "2023-06-29",
  "term": "2022-2023",
  "vote_breakdown": {
    "majority": ["Roberts", "Thomas", "Alito", "Gorsuch", "Kavanaugh", "Barrett"],
    "dissent": ["Sotomayor", "Kagan", "Jackson"],
    "vote_count": "6-3"
  },
  "opinion_authors": {
    "majority": "Roberts",
    "dissents": ["Sotomayor", "Jackson"],
    "concurrences": ["Thomas", "Gorsuch"]
  },
  "legal_areas": [
    "Constitutional Law",
    "Equal Protection",
    "Education Law",
    "Civil Rights"
  ],
  "case_type": "Constitutional Challenge",
  "lower_court": "First Circuit Court of Appeals",
  "lower_court_outcome": "Affirmed Harvard program",
  "supreme_court_outcome": "Reversed",
  "business_impact": "Broad regulatory changes affecting all higher education",
  "prediction_metrics": {
    "difficulty": "Medium",
    "coalition_strength": "High",
    "prediction_value": "High"
  }
}
```

## File Naming

- Cases: `[docket-number]_[case-name-hyphenated]`
- PDFs: Descriptive names (petitioner_brief.pdf, majority_opinion.pdf)
- Justice Files: `[lastname]_[opinion-type].pdf`
- Analysis: `.md` format

## Quality Standards

- Clear organization
- Complete documents
- Analysis-ready structure
- Consistent navigation

**This structure will be replicated for every major case across all three terms (2022-2024), providing the foundation for ClaudeScotus prediction accuracy validation.**