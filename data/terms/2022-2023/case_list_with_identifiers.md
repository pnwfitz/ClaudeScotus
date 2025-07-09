# Supreme Court 2022-2023 Term - Case List with API Identifiers

## Overview

This document provides the complete list of Supreme Court cases from the 2022-2023 term with all necessary identifiers for CourtListener API queries.

## API Requirements Summary

**Primary Identifiers Needed**:
- **Docket Number**: Format `22-XXXX` (e.g., 22-451)
- **Case Name**: Full case name for searches
- **CourtListener ID**: Internal database ID (obtained from API)
- **Court**: Always `scotus` for Supreme Court

**API Endpoints**:
- **Dockets**: `/api/rest/v4/dockets/?court=scotus&docket_number=22-451`
- **Opinions**: `/api/rest/v4/opinions/?cluster__docket__court=scotus&cluster__docket__docket_number=22-451`
- **Oral Arguments**: `/api/rest/v4/oral-arguments/?docket__court=scotus&docket__docket_number=22-451`

## Major Decided Cases (2022-2023 Term)

### 1. Students for Fair Admissions v. Harvard
- **Docket Number**: `21-707`
- **Case Name**: `Students for Fair Admissions, Inc. v. President and Fellows of Harvard College`
- **Folder Name**: `21-707_students-for-fair-admissions-v-harvard`
- **Issue**: Affirmative action in college admissions
- **Decision Date**: June 29, 2023
- **Vote**: 6-3 (struck down affirmative action)

### 2. Students for Fair Admissions v. UNC
- **Docket Number**: `21-1194`
- **Case Name**: `Students for Fair Admissions, Inc. v. University of North Carolina`
- **Folder Name**: `21-1194_students-for-fair-admissions-v-unc`
- **Issue**: Affirmative action in college admissions
- **Decision Date**: June 29, 2023
- **Vote**: 6-3 (consolidated with Harvard case)

### 3. Moore v. Harper
- **Docket Number**: `21-1271`
- **Case Name**: `Moore v. Harper`
- **Folder Name**: `21-1271_moore-v-harper`
- **Issue**: Independent state legislature theory
- **Decision Date**: June 27, 2023
- **Vote**: 6-3 (rejected theory)

### 4. 303 Creative LLC v. Elenis
- **Docket Number**: `21-476`
- **Case Name**: `303 Creative LLC v. Elenis`
- **Folder Name**: `21-476_303-creative-v-elenis`
- **Issue**: Free speech vs anti-discrimination law
- **Decision Date**: June 30, 2023
- **Vote**: 6-3 (sided with business)

### 5. Groff v. DeJoy
- **Docket Number**: `22-174`
- **Case Name**: `Groff v. DeJoy`
- **Folder Name**: `22-174_groff-v-dejoy`
- **Issue**: Religious accommodation in workplace
- **Decision Date**: June 29, 2023
- **Vote**: 9-0 (unanimous)

### 6. Counterman v. Colorado
- **Docket Number**: `22-138`
- **Case Name**: `Counterman v. Colorado`
- **Folder Name**: `22-138_counterman-v-colorado`
- **Issue**: True threats and First Amendment
- **Decision Date**: June 27, 2023
- **Vote**: 7-2 (required subjective intent)

### 7. Sackett v. EPA
- **Docket Number**: `21-454`
- **Case Name**: `Sackett v. EPA`
- **Folder Name**: `21-454_sackett-v-epa`
- **Issue**: Clean Water Act jurisdiction
- **Decision Date**: May 25, 2023
- **Vote**: 9-0 (limited EPA jurisdiction)

### 8. National Pork Producers v. Ross
- **Docket Number**: `21-468`
- **Case Name**: `National Pork Producers Council v. Ross`
- **Folder Name**: `21-468_national-pork-producers-v-ross`
- **Issue**: Dormant Commerce Clause
- **Decision Date**: May 11, 2023
- **Vote**: 5-4 (upheld California law)

### 9. Tyler v. Hennepin County
- **Docket Number**: `22-166`
- **Case Name**: `Tyler v. Hennepin County`
- **Folder Name**: `22-166_tyler-v-hennepin-county`
- **Issue**: Property rights and tax sales
- **Decision Date**: May 25, 2023
- **Vote**: 9-0 (unanimous)

### 10. Allen v. Milligan
- **Docket Number**: `21-1086`
- **Case Name**: `Allen v. Milligan`
- **Folder Name**: `21-1086_allen-v-milligan`
- **Issue**: Voting Rights Act and redistricting
- **Decision Date**: June 8, 2023
- **Vote**: 5-4 (maintained VRA protections)

### 11. Andy Warhol Foundation v. Goldsmith
- **Docket Number**: `21-869`
- **Case Name**: `Andy Warhol Foundation for the Visual Arts, Inc. v. Goldsmith`
- **Folder Name**: `21-869_warhol-foundation-v-goldsmith`
- **Issue**: Fair use and transformative works
- **Decision Date**: May 18, 2023
- **Vote**: 7-2 (limited fair use)

### 12. Glacier Northwest v. Teamsters
- **Docket Number**: `21-1449`
- **Case Name**: `Glacier Northwest, Inc. v. International Brotherhood of Teamsters`
- **Folder Name**: `21-1449_glacier-northwest-v-teamsters`
- **Issue**: Labor law and property damage
- **Decision Date**: June 1, 2023
- **Vote**: 8-1 (allowed state tort claims)

### 13. Arellano v. McDonough
- **Docket Number**: `21-432`
- **Case Name**: `Arellano v. McDonough`
- **Folder Name**: `21-432_arellano-v-mcdonough`
- **Issue**: Veterans' benefits and equitable tolling
- **Decision Date**: May 16, 2023
- **Vote**: 7-2 (limited equitable tolling)

### 14. Reed v. Goertz
- **Docket Number**: `21-1107`
- **Case Name**: `Reed v. Goertz`
- **Folder Name**: `21-1107_reed-v-goertz`
- **Issue**: Habeas corpus and DNA testing
- **Decision Date**: April 19, 2023
- **Vote**: 6-3 (reversed conviction)

### 15. Helix Energy Solutions v. Hewitt
- **Docket Number**: `21-984`
- **Case Name**: `Helix Energy Solutions Group, Inc. v. Hewitt`
- **Folder Name**: `21-984_helix-energy-v-hewitt`
- **Issue**: Fair Labor Standards Act and overtime
- **Decision Date**: February 22, 2023
- **Vote**: 6-3 (required overtime pay)

## Additional Cases

### 16. Twitter v. Taamneh
- **Docket Number**: `21-1496`
- **Case Name**: `Twitter, Inc. v. Taamneh`
- **Folder Name**: `21-1496_twitter-v-taamneh`
- **Issue**: Social media liability for terrorism
- **Decision Date**: May 18, 2023
- **Vote**: 9-0 (limited liability)

### 17. Gonzalez v. Google
- **Docket Number**: `21-1333`
- **Case Name**: `Gonzalez v. Google LLC`
- **Folder Name**: `21-1333_gonzalez-v-google`
- **Issue**: Section 230 and algorithm liability
- **Decision Date**: May 18, 2023
- **Vote**: 9-0 (dismissed without ruling)

### 18. Haaland v. Brackeen
- **Docket Number**: `21-376`
- **Case Name**: `Haaland v. Brackeen`
- **Folder Name**: `21-376_haaland-v-brackeen`
- **Issue**: Indian Child Welfare Act
- **Decision Date**: June 15, 2023
- **Vote**: 7-2 (upheld ICWA)

### 19. Abitron Austria v. Hetronic
- **Docket Number**: `21-1043`
- **Case Name**: `Abitron Austria GmbH v. Hetronic International, Inc.`
- **Folder Name**: `21-1043_abitron-austria-v-hetronic`
- **Issue**: Extraterritorial application of trademark law
- **Decision Date**: May 30, 2023
- **Vote**: 9-0 (limited extraterritorial reach)

### 20. Dupree v. Younger
- **Docket Number**: `22-210`
- **Case Name**: `Dupree v. Younger`
- **Folder Name**: `22-210_dupree-v-younger`
- **Issue**: Federal sentencing guidelines
- **Decision Date**: May 11, 2023
- **Vote**: 8-1 (limited guideline application)

## API Query Commands

### Get All 2022-2023 Term Cases
```bash
# Get dockets starting with 21- and 22- (cases from 2022-2023 term)
curl -H "Authorization: Token cc8cf79b1d5393f6e71126830caab5fcd57de76b" \
  "https://www.courtlistener.com/api/rest/v4/dockets/?court=scotus&docket_number__startswith=21-" \
  > 21_dockets.json

curl -H "Authorization: Token cc8cf79b1d5393f6e71126830caab5fcd57de76b" \
  "https://www.courtlistener.com/api/rest/v4/dockets/?court=scotus&docket_number__startswith=22-" \
  > 22_dockets.json
```

### Get Specific Case Data
```bash
# Example: Get Arellano v. McDonough case data
curl -H "Authorization: Token cc8cf79b1d5393f6e71126830caab5fcd57de76b" \
  "https://www.courtlistener.com/api/rest/v4/dockets/?court=scotus&docket_number=21-432"
```

## Batch Collection Script

### Python Script to Collect All Cases
```python
import requests
import json
import time

CASES = [
    {"docket": "21-707", "name": "students-for-fair-admissions-v-harvard"},
    {"docket": "21-1194", "name": "students-for-fair-admissions-v-unc"},
    {"docket": "21-1271", "name": "moore-v-harper"},
    {"docket": "21-476", "name": "303-creative-v-elenis"},
    {"docket": "22-174", "name": "groff-v-dejoy"},
    {"docket": "22-138", "name": "counterman-v-colorado"},
    {"docket": "21-454", "name": "sackett-v-epa"},
    {"docket": "21-468", "name": "national-pork-producers-v-ross"},
    {"docket": "22-166", "name": "tyler-v-hennepin-county"},
    {"docket": "21-1086", "name": "allen-v-milligan"},
    {"docket": "21-869", "name": "warhol-foundation-v-goldsmith"},
    {"docket": "21-1449", "name": "glacier-northwest-v-teamsters"},
    {"docket": "21-432", "name": "arellano-v-mcdonough"},
    {"docket": "21-1107", "name": "reed-v-goertz"},
    {"docket": "21-984", "name": "helix-energy-v-hewitt"},
    {"docket": "21-1496", "name": "twitter-v-taamneh"},
    {"docket": "21-1333", "name": "gonzalez-v-google"},
    {"docket": "21-376", "name": "haaland-v-brackeen"},
    {"docket": "21-1043", "name": "abitron-austria-v-hetronic"},
    {"docket": "22-210", "name": "dupree-v-younger"}
]

def collect_all_cases():
    token = "cc8cf79b1d5393f6e71126830caab5fcd57de76b"
    headers = {"Authorization": f"Token {token}"}
    
    for case in CASES:
        docket = case["docket"]
        name = case["name"]
        
        print(f"Collecting {name} ({docket})")
        
        # Create case folder
        folder_name = f"{docket}_{name}"
        os.makedirs(f"data/terms/2022-2023/cases/{folder_name}", exist_ok=True)
        
        # Create README to trigger hook
        readme_path = f"data/terms/2022-2023/cases/{folder_name}/README.md"
        with open(readme_path, 'w') as f:
            f.write(f"# {name.replace('-', ' ').title()}\n\n")
            f.write(f"**Docket Number**: {docket}\n")
            f.write(f"**Term**: 2022-2023\n\n")
            f.write("## Case Overview\n\n")
            f.write("To be filled in after document collection.\n")
        
        time.sleep(5)  # Allow hook to complete
```

## Data Validation Checklist

### Required Information for Each Case
- [ ] **Docket Number**: Format `XX-XXXX`
- [ ] **Case Name**: Full official case name
- [ ] **Folder Name**: `docket_case-name` format
- [ ] **CourtListener ID**: Retrieved from API
- [ ] **Decision Date**: When case was decided
- [ ] **Vote Split**: How justices voted

### API Identifiers Needed
- [ ] **Court**: `scotus` (constant)
- [ ] **Docket Number**: Primary identifier
- [ ] **Case Name**: For search queries
- [ ] **Internal IDs**: Retrieved from API calls

## Next Steps

1. **Validate case list**: Cross-reference with official Supreme Court records
2. **Test API queries**: Verify all docket numbers return valid data
3. **Batch collection**: Use list to collect all cases systematically
4. **Verify completeness**: Ensure all major 2022-2023 cases are included

---

**Purpose**: Provide complete case identifiers for automated data collection  
**Usage**: Reference for API queries and batch processing  
**Maintenance**: Update as additional cases are identified or corrected