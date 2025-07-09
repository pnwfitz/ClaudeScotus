# Supreme Court Case Metadata Framework

## Overview

This document outlines the comprehensive metadata to collect for each Supreme Court case beyond the required documents. This information helps predict case outcomes by understanding advocate relationships, court dynamics, and case characteristics.

**Priority Level**: "Nice to Have" - Collect when available to enhance prediction accuracy

## Lawyer/Advocate Metadata

### Lead Counsel Analysis
- [ ] **Lead Counsel Names** - Primary advocates for each side
  - Petitioner lead counsel: [Name, Firm]
  - Respondent lead counsel: [Name, Firm]
  - Government counsel (if applicable): [Name, Title]

- [ ] **Supreme Court Track Record** - Historical performance before specific justices
  - Total Supreme Court arguments: [Number]
  - Win rate before current Court: [Percentage]
  - Specific justice relationships: [Notes on prior interactions]

### Professional Background
- [ ] **Clerking History** - Creates familiarity/relationships with justices
  - Justice clerked for: [Justice name, years]
  - Circuit court clerkships: [Court, judge, years]
  - Influence on justice relationships: [Assessment]

- [ ] **Solicitor General Office Alumni** - Former SG lawyers get special credibility
  - Years in SG office: [Start-end dates]
  - Cases argued as SG: [Number, notable cases]
  - Current SG relationship: [Assessment]

### Experience Factors
- [ ] **Supreme Court Bar Frequency** - Experience arguing before Court
  - First-time advocate: [Yes/No]
  - Frequency of arguments: [Per year average]
  - Recent argument history: [Last 3 years]

- [ ] **Law Firm Profile** - Institutional credibility
  - Firm type: [BigLaw/Boutique/Public Interest/Government]
  - Supreme Court practice specialization: [Yes/No]
  - Firm reputation in relevant area: [Assessment]

## Lower Court Metadata

### Circuit/Court Information
- [ ] **Circuit of Origin** - Some circuits have reputations with specific justices
  - Circuit: [1st, 2nd, 3rd, etc.]
  - Circuit reputation: [Conservative/Liberal/Moderate]
  - Justice relationships: [Known preferences for/against circuit]

- [ ] **Panel Composition** - Which judges wrote/joined the opinion
  - Panel judges: [Names and appointing president]
  - Author of majority: [Judge name, background]
  - Political composition: [Republican/Democratic appointees]

### Decision Characteristics
- [ ] **Vote Breakdown** - Unanimous vs. split, dissenting reasoning
  - Vote: [Unanimous/2-1/other]
  - Dissent reasoning: [Constitutional/statutory/procedural]
  - Dissent strength: [Vigorous/mild/technical]

- [ ] **Procedural History** - How case reached Supreme Court
  - En banc vs. panel: [Which heard the case]
  - Multiple reversals: [Number of times case bounced between courts]
  - Cert petition history: [First petition/second petition]

## Case Characteristics

### Legal Framework
- [ ] **Area of Law** - Primary legal domain
  - Primary: [Constitutional/Statutory/Administrative/Criminal/Civil Rights]
  - Secondary: [Specific sub-area]
  - Complexity: [Simple/Moderate/Complex]

- [ ] **Government Involvement** - US as party affects dynamics
  - Government role: [Petitioner/Respondent/Not involved/Amicus]
  - Government position: [Supporting petitioner/respondent]
  - SG office involvement: [Direct representation/amicus brief]

### Constitutional/Legal Issues
- [ ] **State vs. Federal Law** - Federalism implications
  - Primary law: [Federal statute/State law/Constitutional provision]
  - Federalism implications: [States' rights/Federal supremacy/None]
  - Preemption issues: [Yes/No]

- [ ] **Procedural Posture** - How case reached Supreme Court
  - Lower court decision: [Summary judgment/Jury verdict/Injunction/Motion to dismiss]
  - Standard of review: [De novo/Abuse of discretion/Clearly erroneous]
  - Jurisdictional issues: [Yes/No]

### Case Quality
- [ ] **Cert Vehicle Quality** - Clean facts vs. messy circumstances
  - Factual clarity: [Clean/Complicated/Messy]
  - Legal issue clarity: [Pure legal question/Fact-dependent/Mixed]
  - Unusual circumstances: [Standard case/Unusual facts/Emergency posture]

## Timing/Context Metadata

### Supreme Court Calendar
- [ ] **Term Timing** - When case was argued/decided
  - Argument date: [Month/Year]
  - Decision date: [Month/Year]
  - Term position: [Early/Mid/Late term]

- [ ] **Election Context** - Sensitive cases near elections
  - Election proximity: [Months to next election]
  - Political sensitivity: [High/Medium/Low]
  - Likely campaign issue: [Yes/No]

### Judicial Environment
- [ ] **Related Pending Cases** - Whether similar issues are in pipeline
  - Similar cases pending: [Number, case names]
  - Conflicting circuit decisions: [Yes/No]
  - Court's apparent interest: [High/Medium/Low]

- [ ] **Media Attention Level** - High-profile cases may get different treatment
  - Media coverage: [High/Medium/Low/None]
  - Public interest: [High/Medium/Low]
  - Protest activity: [Yes/No]

## Stakeholder Alignment

### Amicus Brief Analysis
- [ ] **Number of Amicus Briefs**
  - Supporting petitioner: [Number]
  - Supporting respondent: [Number]
  - Supporting neither: [Number]

- [ ] **Key Amicus Participants**
  - US Government position: [Supporting petitioner/respondent/neither]
  - State governments: [Number supporting each side]
  - Business groups: [Chamber of Commerce position]
  - Labor groups: [AFL-CIO position]

### Interest Group Alignment
- [ ] **State Government Positions** - How many states on each side
  - States supporting petitioner: [Number, lead states]
  - States supporting respondent: [Number, lead states]
  - State AG political party: [Republican/Democratic breakdown]

- [ ] **Business vs. Labor Alignment** - Economic interests
  - Business community: [United/Divided/Neutral]
  - Labor unions: [United/Divided/Neutral]
  - Cross-cutting alliances: [Unusual alignments]

## Metadata Collection Template

```json
{
  "case_metadata": {
    "advocates": {
      "petitioner_counsel": {
        "name": "",
        "firm": "",
        "sc_experience": "",
        "clerking_history": "",
        "sg_alumni": false
      },
      "respondent_counsel": {
        "name": "",
        "firm": "",
        "sc_experience": "",
        "clerking_history": "",
        "sg_alumni": false
      }
    },
    "lower_court": {
      "circuit": "",
      "panel_composition": [],
      "vote_breakdown": "",
      "en_banc": false,
      "multiple_reversals": 0
    },
    "case_characteristics": {
      "area_of_law": "",
      "government_role": "",
      "state_v_federal": "",
      "procedural_posture": "",
      "cert_vehicle_quality": ""
    },
    "timing_context": {
      "argument_date": "",
      "election_proximity": "",
      "related_cases": [],
      "media_attention": ""
    },
    "stakeholder_alignment": {
      "amicus_briefs": {
        "supporting_petitioner": 0,
        "supporting_respondent": 0
      },
      "state_positions": {
        "supporting_petitioner": 0,
        "supporting_respondent": 0
      },
      "business_labor_alignment": ""
    }
  }
}
```

## Metadata Sources

### Primary Sources
- **Supreme Court Bar Directory** - Advocate background information
- **Legal directories** (Martindale-Hubbell, Chambers) - Firm and lawyer profiles
- **Circuit court websites** - Lower court decision information
- **Legal news sources** - Media coverage and context

### Secondary Sources
- **Academic databases** - Empirical research on Court patterns
- **Interest group websites** - Stakeholder positions and amicus participation
- **Government websites** - Official positions and policy context
- **Professional associations** - Bar organization information

## Usage Guidelines

### Priority Levels
1. **High Priority**: Advocate experience, government involvement, circuit of origin
2. **Medium Priority**: Amicus alignment, timing context, case characteristics
3. **Low Priority**: Media attention, election proximity, unusual circumstances

### Data Quality Standards
- **Verify** advocate information through multiple sources
- **Cross-reference** lower court information with official records
- **Document** sources for all metadata claims
- **Update** metadata as new information becomes available

### Predictive Value
This metadata enhances prediction accuracy by providing context that pure legal analysis might miss. Focus collection efforts on high-value metadata that historically correlates with case outcomes.

---

**Purpose**: This framework ensures comprehensive metadata collection to enhance Supreme Court case prediction accuracy beyond pure legal document analysis.

**Integration**: Use alongside CASE_DOCUMENT_REQUIREMENTS.md for complete case preparation and analysis.