# Case Document Requirements - ClaudeScotus Collection

**Last Updated**: 2025-06-11  
**Scope**: Phase 1 - Document Collection Only  
**Source Constraint**: CourtListener API only

## **Required Documents Per Case**

### **1. Supreme Court Opinion**
- **File**: `opinions/majority_opinion.pdf`
- **Description**: Primary Supreme Court decision
- **Required**: Yes
- **Source**: CourtListener API

### **2. Dissenting Opinions**
- **File**: `opinions/dissents/[justice]_dissent.pdf`
- **Description**: All dissenting opinions by Justice
- **Required**: If dissents exist
- **Source**: CourtListener API

### **3. Concurring Opinions**
- **File**: `opinions/concurrences/[justice]_concurrence.pdf`
- **Description**: All concurring opinions by Justice
- **Required**: If concurrences exist
- **Source**: CourtListener API

### **4. Petitioner Brief**
- **File**: `briefs/petitioner_brief.pdf`
- **Description**: Main arguing party's legal brief
- **Required**: Yes
- **Source**: CourtListener API

### **5. Respondent Brief**
- **File**: `briefs/respondent_brief.pdf`
- **Description**: Defending party's response brief
- **Required**: Yes
- **Source**: CourtListener API

### **6. Oral Argument Transcript**
- **File**: `oral_arguments/transcript.pdf`
- **Description**: Complete Q&A session transcript
- **Required**: If oral arguments held
- **Source**: CourtListener API

### **7. Lower Court Decision**
- **File**: `opinions/lower_court_decision.pdf`
- **Description**: Circuit/District court ruling being reviewed
- **Required**: Yes
- **Source**: CourtListener API

### **8. Cert Petition**
- **File**: `briefs/cert_petition.pdf`
- **Description**: Original petition for Supreme Court review
- **Required**: Yes
- **Source**: CourtListener API

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

## **Success Criteria Per Case**
- [ ] All 8 document types attempted for collection
- [ ] File structure properly populated
- [ ] Missing documents documented in README.md
- [ ] CourtListener API source URLs recorded in metadata.json

## **Collection Constraints**
- **API Only**: No direct Supreme Court website downloads
- **No Fallback Sources**: No Justia or other supplemental sources
- **Document What's Missing**: Track API limitations systematically

## **Phase 1 Goal**
Test what percentage of required documents we can obtain from CourtListener API alone before considering additional sources.

---

**This document defines exact requirements to prevent hallucination and scope creep during technical implementation.**