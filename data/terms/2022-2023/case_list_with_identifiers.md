# Supreme Court 2022-2023 Term - Complete Case List with API Identifiers

## Overview

This document provides the complete list of all 58 Supreme Court cases from the 2022-2023 term with all necessary identifiers for CourtListener API queries.

**Term Period**: October 3, 2022 - June 29, 2023  
**Total Cases**: 58  
**Source**: Wikipedia 2022 term opinions table

## API Requirements Summary

**Primary Identifiers Needed**:
- **Docket Number**: Format `21-XXXX` or `22-XXXX` (e.g., 21-707, 22-174)
- **Case Name**: Full case name for searches
- **CourtListener ID**: Internal database ID (obtained from API)
- **Court**: Always `scotus` for Supreme Court

**API Endpoints**:
- **Dockets**: `/api/rest/v4/dockets/?court=scotus&docket_number=21-707`
- **Opinions**: `/api/rest/v4/opinions/?cluster__docket__court=scotus&cluster__docket__docket_number=21-707`
- **Oral Arguments**: `/api/rest/v4/oral-arguments/?docket__court=scotus&docket__docket_number=21-707`

## Complete Case List (All 58 Cases)

### 1. Arellano v. McDonough
- **Docket Number**: `21-432`
- **Case Name**: `Arellano v. McDonough`
- **Folder Name**: `21-432_arellano-v-mcdonough`
- **Issue**: Veterans' benefits and equitable tolling
- **Status**: Existing case folder

### 2. In re Grand Jury
- **Docket Number**: `TBD`
- **Case Name**: `In re Grand Jury`
- **Folder Name**: `TBD_in-re-grand-jury`
- **Issue**: Grand jury proceedings
- **Status**: Needs docket number research

### 3. Cruz v. Arizona
- **Docket Number**: `TBD`
- **Case Name**: `Cruz v. Arizona`
- **Folder Name**: `TBD_cruz-v-arizona`
- **Issue**: Criminal law
- **Status**: Needs docket number research

### 4. Helix Energy Solutions Group, Inc. v. Hewitt
- **Docket Number**: `21-984`
- **Case Name**: `Helix Energy Solutions Group, Inc. v. Hewitt`
- **Folder Name**: `21-984_helix-energy-v-hewitt`
- **Issue**: Fair Labor Standards Act and overtime
- **Status**: Existing case folder

### 5. Bartenwerfer v. Buckley
- **Docket Number**: `TBD`
- **Case Name**: `Bartenwerfer v. Buckley`
- **Folder Name**: `TBD_bartenwerfer-v-buckley`
- **Issue**: Bankruptcy law
- **Status**: Needs docket number research

### 6. Bittner v. United States
- **Docket Number**: `TBD`
- **Case Name**: `Bittner v. United States`
- **Folder Name**: `TBD_bittner-v-united-states`
- **Issue**: Tax law
- **Status**: Needs docket number research

### 7. Delaware v. Pennsylvania
- **Docket Number**: `TBD`
- **Case Name**: `Delaware v. Pennsylvania`
- **Folder Name**: `TBD_delaware-v-pennsylvania`
- **Issue**: Interstate disputes
- **Status**: Needs docket number research

### 8. Luna Perez v. Sturgis Public Schools
- **Docket Number**: `TBD`
- **Case Name**: `Luna Perez v. Sturgis Public Schools`
- **Folder Name**: `TBD_luna-perez-v-sturgis-public-schools`
- **Issue**: Education law
- **Status**: Needs docket number research

### 9. Wilkins v. United States
- **Docket Number**: `TBD`
- **Case Name**: `Wilkins v. United States`
- **Folder Name**: `TBD_wilkins-v-united-states`
- **Issue**: Federal claims
- **Status**: Needs docket number research

### 10. Axon Enterprise, Inc. v. Federal Trade Commission
- **Docket Number**: `TBD`
- **Case Name**: `Axon Enterprise, Inc. v. Federal Trade Commission`
- **Folder Name**: `TBD_axon-enterprise-v-ftc`
- **Issue**: Administrative law
- **Status**: Needs docket number research

### 11. New York v. New Jersey
- **Docket Number**: `TBD`
- **Case Name**: `New York v. New Jersey`
- **Folder Name**: `TBD_new-york-v-new-jersey`
- **Issue**: Interstate disputes
- **Status**: Needs docket number research

### 12. Reed v. Goertz
- **Docket Number**: `21-1107`
- **Case Name**: `Reed v. Goertz`
- **Folder Name**: `21-1107_reed-v-goertz`
- **Issue**: Habeas corpus and DNA testing
- **Status**: Existing case folder

### 13. Türkiye Halk Bankası A.Ş. v. United States
- **Docket Number**: `TBD`
- **Case Name**: `Türkiye Halk Bankası A.Ş. v. United States`
- **Folder Name**: `TBD_turkiye-halk-bankasi-v-united-states`
- **Issue**: Foreign sovereign immunity
- **Status**: Needs docket number research

### 14. MOAC Mall Holdings LLC v. Transform Holdco LLC
- **Docket Number**: `TBD`
- **Case Name**: `MOAC Mall Holdings LLC v. Transform Holdco LLC`
- **Folder Name**: `TBD_moac-mall-holdings-v-transform-holdco`
- **Issue**: Commercial law
- **Status**: Needs docket number research

### 15. Ciminelli v. United States
- **Docket Number**: `TBD`
- **Case Name**: `Ciminelli v. United States`
- **Folder Name**: `TBD_ciminelli-v-united-states`
- **Issue**: Criminal law
- **Status**: Needs docket number research

### 16. Percoco v. United States
- **Docket Number**: `TBD`
- **Case Name**: `Percoco v. United States`
- **Folder Name**: `TBD_percoco-v-united-states`
- **Issue**: Criminal law
- **Status**: Needs docket number research

### 17. Financial Oversight and Management Board for Puerto Rico v. Centro de Periodismo Investigativo, Inc.
- **Docket Number**: `TBD`
- **Case Name**: `Financial Oversight and Management Board for Puerto Rico v. Centro de Periodismo Investigativo, Inc.`
- **Folder Name**: `TBD_puerto-rico-board-v-centro-periodismo`
- **Issue**: Puerto Rico governance
- **Status**: Needs docket number research

### 18. National Pork Producers Council v. Ross
- **Docket Number**: `21-468`
- **Case Name**: `National Pork Producers Council v. Ross`
- **Folder Name**: `21-468_national-pork-producers-v-ross`
- **Issue**: Dormant Commerce Clause
- **Status**: Existing case folder

### 19. Santos-Zacaria v. Garland
- **Docket Number**: `TBD`
- **Case Name**: `Santos-Zacaria v. Garland`
- **Folder Name**: `TBD_santos-zacaria-v-garland`
- **Issue**: Immigration law
- **Status**: Needs docket number research

### 20. Polselli v. Internal Revenue Service
- **Docket Number**: `TBD`
- **Case Name**: `Polselli v. Internal Revenue Service`
- **Folder Name**: `TBD_polselli-v-irs`
- **Issue**: Tax law
- **Status**: Needs docket number research

### 21. Ohio Adjutant General's Department v. Federal Labor Relations Authority
- **Docket Number**: `TBD`
- **Case Name**: `Ohio Adjutant General's Department v. Federal Labor Relations Authority`
- **Folder Name**: `TBD_ohio-adjutant-general-v-flra`
- **Issue**: Labor law
- **Status**: Needs docket number research

### 22. Twitter, Inc. v. Taamneh
- **Docket Number**: `21-1496`
- **Case Name**: `Twitter, Inc. v. Taamneh`
- **Folder Name**: `21-1496_twitter-v-taamneh`
- **Issue**: Social media liability for terrorism
- **Status**: Existing case folder

### 23. Andy Warhol Foundation for the Visual Arts, Inc. v. Goldsmith
- **Docket Number**: `21-869`
- **Case Name**: `Andy Warhol Foundation for the Visual Arts, Inc. v. Goldsmith`
- **Folder Name**: `21-869_warhol-foundation-v-goldsmith`
- **Issue**: Fair use and transformative works
- **Status**: Existing case folder

### 24. Amgen Inc. v. Sanofi
- **Docket Number**: `TBD`
- **Case Name**: `Amgen Inc. v. Sanofi`
- **Folder Name**: `TBD_amgen-v-sanofi`
- **Issue**: Patent law
- **Status**: Needs docket number research

### 25. Gonzalez v. Google LLC
- **Docket Number**: `21-1333`
- **Case Name**: `Gonzalez v. Google LLC`
- **Folder Name**: `21-1333_gonzalez-v-google`
- **Issue**: Section 230 and algorithm liability
- **Status**: Existing case folder

### 26. Calcutt v. FDIC
- **Docket Number**: `TBD`
- **Case Name**: `Calcutt v. FDIC`
- **Folder Name**: `TBD_calcutt-v-fdic`
- **Issue**: Banking law
- **Status**: Needs docket number research

### 27. Tyler v. Hennepin County
- **Docket Number**: `22-166`
- **Case Name**: `Tyler v. Hennepin County`
- **Folder Name**: `22-166_tyler-v-hennepin-county`
- **Issue**: Property rights and tax sales
- **Status**: Existing case folder

### 28. Sackett v. EPA
- **Docket Number**: `21-454`
- **Case Name**: `Sackett v. EPA`
- **Folder Name**: `21-454_sackett-v-epa`
- **Issue**: Clean Water Act jurisdiction
- **Status**: Existing case folder

### 29. Dupree v. Younger
- **Docket Number**: `22-210`
- **Case Name**: `Dupree v. Younger`
- **Folder Name**: `22-210_dupree-v-younger`
- **Issue**: Federal sentencing guidelines
- **Status**: Existing case folder

### 30. United States ex rel. Schutte v. Supervalu Inc.
- **Docket Number**: `TBD`
- **Case Name**: `United States ex rel. Schutte v. Supervalu Inc.`
- **Folder Name**: `TBD_schutte-v-supervalu`
- **Issue**: False Claims Act
- **Status**: Needs docket number research

### 31. Slack Technologies, LLC v. Pirani
- **Docket Number**: `TBD`
- **Case Name**: `Slack Technologies, LLC v. Pirani`
- **Folder Name**: `TBD_slack-technologies-v-pirani`
- **Issue**: Securities law
- **Status**: Needs docket number research

### 32. Glacier Northwest, Inc. v. Teamsters
- **Docket Number**: `21-1449`
- **Case Name**: `Glacier Northwest, Inc. v. International Brotherhood of Teamsters`
- **Folder Name**: `21-1449_glacier-northwest-v-teamsters`
- **Issue**: Labor law and property damage
- **Status**: Existing case folder

### 33. Allen v. Milligan
- **Docket Number**: `21-1086`
- **Case Name**: `Allen v. Milligan`
- **Folder Name**: `21-1086_allen-v-milligan`
- **Issue**: Voting Rights Act and redistricting
- **Status**: Existing case folder

### 34. Dubin v. United States
- **Docket Number**: `TBD`
- **Case Name**: `Dubin v. United States`
- **Folder Name**: `TBD_dubin-v-united-states`
- **Issue**: Criminal law
- **Status**: Needs docket number research

### 35. Jack Daniel's Properties, Inc. v. VIP Products LLC
- **Docket Number**: `TBD`
- **Case Name**: `Jack Daniel's Properties, Inc. v. VIP Products LLC`
- **Folder Name**: `TBD_jack-daniels-v-vip-products`
- **Issue**: Trademark law
- **Status**: Needs docket number research

### 36. Health and Hospital Corporation of Marion County v. Talevski
- **Docket Number**: `TBD`
- **Case Name**: `Health and Hospital Corporation of Marion County v. Talevski`
- **Folder Name**: `TBD_marion-county-v-talevski`
- **Issue**: Civil rights law
- **Status**: Needs docket number research

### 37. Smith v. United States
- **Docket Number**: `TBD`
- **Case Name**: `Smith v. United States`
- **Folder Name**: `TBD_smith-v-united-states`
- **Issue**: Criminal law
- **Status**: Needs docket number research

### 38. Haaland v. Brackeen
- **Docket Number**: `21-376`
- **Case Name**: `Haaland v. Brackeen`
- **Folder Name**: `21-376_haaland-v-brackeen`
- **Issue**: Indian Child Welfare Act
- **Status**: Existing case folder

### 39. Lac du Flambeau Band of Lake Superior Chippewa Indians v. Coughlin
- **Docket Number**: `TBD`
- **Case Name**: `Lac du Flambeau Band of Lake Superior Chippewa Indians v. Coughlin`
- **Folder Name**: `TBD_lac-du-flambeau-v-coughlin`
- **Issue**: Tribal law
- **Status**: Needs docket number research

### 40. United States ex rel. Polansky v. Executive Health Resources, Inc.
- **Docket Number**: `TBD`
- **Case Name**: `United States ex rel. Polansky v. Executive Health Resources, Inc.`
- **Folder Name**: `TBD_polansky-v-executive-health`
- **Issue**: False Claims Act
- **Status**: Needs docket number research

### 41. Lora v. United States
- **Docket Number**: `TBD`
- **Case Name**: `Lora v. United States`
- **Folder Name**: `TBD_lora-v-united-states`
- **Issue**: Criminal law
- **Status**: Needs docket number research

### 42. Jones v. Hendrix
- **Docket Number**: `TBD`
- **Case Name**: `Jones v. Hendrix`
- **Folder Name**: `TBD_jones-v-hendrix`
- **Issue**: Habeas corpus
- **Status**: Needs docket number research

### 43. Yegiazaryan v. Smagin
- **Docket Number**: `TBD`
- **Case Name**: `Yegiazaryan v. Smagin`
- **Folder Name**: `TBD_yegiazaryan-v-smagin`
- **Issue**: International law
- **Status**: Needs docket number research

### 44. Arizona v. Navajo Nation
- **Docket Number**: `TBD`
- **Case Name**: `Arizona v. Navajo Nation`
- **Folder Name**: `TBD_arizona-v-navajo-nation`
- **Issue**: Water rights
- **Status**: Needs docket number research

### 45. Pugin v. Garland
- **Docket Number**: `TBD`
- **Case Name**: `Pugin v. Garland`
- **Folder Name**: `TBD_pugin-v-garland`
- **Issue**: Immigration law
- **Status**: Needs docket number research

### 46. Samia v. United States
- **Docket Number**: `TBD`
- **Case Name**: `Samia v. United States`
- **Folder Name**: `TBD_samia-v-united-states`
- **Issue**: Criminal law
- **Status**: Needs docket number research

### 47. United States v. Texas
- **Docket Number**: `TBD`
- **Case Name**: `United States v. Texas`
- **Folder Name**: `TBD_united-states-v-texas`
- **Issue**: Immigration law
- **Status**: Needs docket number research

### 48. Coinbase, Inc. v. Bielski
- **Docket Number**: `TBD`
- **Case Name**: `Coinbase, Inc. v. Bielski`
- **Folder Name**: `TBD_coinbase-v-bielski`
- **Issue**: Arbitration law
- **Status**: Needs docket number research

### 49. United States v. Hansen
- **Docket Number**: `TBD`
- **Case Name**: `United States v. Hansen`
- **Folder Name**: `TBD_united-states-v-hansen`
- **Issue**: Immigration law
- **Status**: Needs docket number research

### 50. Moore v. Harper
- **Docket Number**: `21-1271`
- **Case Name**: `Moore v. Harper`
- **Folder Name**: `21-1271_moore-v-harper`
- **Issue**: Independent state legislature theory
- **Status**: Existing case folder

### 51. Counterman v. Colorado
- **Docket Number**: `22-138`
- **Case Name**: `Counterman v. Colorado`
- **Folder Name**: `22-138_counterman-v-colorado`
- **Issue**: True threats and First Amendment
- **Status**: Existing case folder

### 52. Mallory v. Norfolk Southern Railway Co.
- **Docket Number**: `TBD`
- **Case Name**: `Mallory v. Norfolk Southern Railway Co.`
- **Folder Name**: `TBD_mallory-v-norfolk-southern`
- **Issue**: Personal jurisdiction
- **Status**: Needs docket number research

### 53. Students for Fair Admissions, Inc. v. President and Fellows of Harvard College
- **Docket Number**: `20-1199`
- **Case Name**: `Students for Fair Admissions, Inc. v. President and Fellows of Harvard College`
- **Folder Name**: `20-1199_students-for-fair-admissions-v-harvard`
- **Issue**: Affirmative action in college admissions
- **Status**: Existing case folder (needs docket correction)

### 54. Abitron Austria GmbH v. Hetronic International, Inc.
- **Docket Number**: `21-1043`
- **Case Name**: `Abitron Austria GmbH v. Hetronic International, Inc.`
- **Folder Name**: `21-1043_abitron-austria-v-hetronic`
- **Issue**: Extraterritorial application of trademark law
- **Status**: Existing case folder

### 55. Groff v. DeJoy
- **Docket Number**: `22-174`
- **Case Name**: `Groff v. DeJoy`
- **Folder Name**: `22-174_groff-v-dejoy`
- **Issue**: Religious accommodation in workplace
- **Status**: Existing case folder

### 56. Biden v. Nebraska
- **Docket Number**: `TBD`
- **Case Name**: `Biden v. Nebraska`
- **Folder Name**: `TBD_biden-v-nebraska`
- **Issue**: Student loan forgiveness
- **Status**: Needs docket number research

### 57. Department of Education v. Brown
- **Docket Number**: `TBD`
- **Case Name**: `Department of Education v. Brown`
- **Folder Name**: `TBD_department-education-v-brown`
- **Issue**: Student loan forgiveness
- **Status**: Needs docket number research

### 58. 303 Creative LLC v. Elenis
- **Docket Number**: `21-476`
- **Case Name**: `303 Creative LLC v. Elenis`
- **Folder Name**: `21-476_303-creative-v-elenis`
- **Issue**: Free speech vs anti-discrimination law
- **Status**: Existing case folder

## Case Status Summary

**Cases with Known Docket Numbers**: 15/58 (26%)  
**Cases Needing Docket Research**: 43/58 (74%)  
**Existing Case Folders**: 15/58 (26%)  
**New Folders Needed**: 43/58 (74%)

## API Query Commands

### Get All 2022-2023 Term Cases
```bash
# Get all Supreme Court dockets from 2022-2023 term
curl -H "Authorization: Token cc8cf79b1d5393f6e71126830caab5fcd57de76b" \
  "https://www.courtlistener.com/api/rest/v4/dockets/?court=scotus&date_argued__gte=2022-10-01&date_argued__lte=2023-06-30" \
  > 2022_2023_all_dockets.json
```

### Get Specific Case Data
```bash
# Example: Get known case data
curl -H "Authorization: Token cc8cf79b1d5393f6e71126830caab5fcd57de76b" \
  "https://www.courtlistener.com/api/rest/v4/dockets/?court=scotus&docket_number=21-432"
```

## Batch Collection Script

### Python Script to Collect All Cases
```python
import requests
import json
import time

# Known cases with docket numbers
KNOWN_CASES = [
    {"docket": "21-432", "name": "arellano-v-mcdonough"},
    {"docket": "21-984", "name": "helix-energy-v-hewitt"},
    {"docket": "21-1107", "name": "reed-v-goertz"},
    {"docket": "21-468", "name": "national-pork-producers-v-ross"},
    {"docket": "21-1496", "name": "twitter-v-taamneh"},
    {"docket": "21-869", "name": "warhol-foundation-v-goldsmith"},
    {"docket": "21-1333", "name": "gonzalez-v-google"},
    {"docket": "22-166", "name": "tyler-v-hennepin-county"},
    {"docket": "21-454", "name": "sackett-v-epa"},
    {"docket": "22-210", "name": "dupree-v-younger"},
    {"docket": "21-1449", "name": "glacier-northwest-v-teamsters"},
    {"docket": "21-1086", "name": "allen-v-milligan"},
    {"docket": "21-376", "name": "haaland-v-brackeen"},
    {"docket": "21-1271", "name": "moore-v-harper"},
    {"docket": "22-138", "name": "counterman-v-colorado"},
    {"docket": "20-1199", "name": "students-for-fair-admissions-v-harvard"},
    {"docket": "21-1043", "name": "abitron-austria-v-hetronic"},
    {"docket": "22-174", "name": "groff-v-dejoy"},
    {"docket": "21-476", "name": "303-creative-v-elenis"}
]

def collect_all_cases():
    token = "cc8cf79b1d5393f6e71126830caab5fcd57de76b"
    headers = {"Authorization": f"Token {token}"}
    
    for case in KNOWN_CASES:
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

## Next Steps

1. **Research Missing Docket Numbers**: Use CourtListener API to find docket numbers for all 43 cases
2. **Create Remaining Case Folders**: Generate folder structure for all 58 cases
3. **Update Existing Systems**: Modify tracking tables and prediction system to reference all cases
4. **Batch Collection**: Run automated document collection for all 58 cases

---

**Purpose**: Complete case inventory for 2022-2023 Supreme Court term  
**Coverage**: All 58 cases decided during the term  
**Status**: 15 cases with known docket numbers, 43 cases need research  
**Maintenance**: Update as docket numbers are identified and verified