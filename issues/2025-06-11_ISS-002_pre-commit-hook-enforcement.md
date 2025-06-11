# Implement pre-commit hook enforcing "#ISS-###" tag
**Issue ID**: ISS-002  
**Opened By**: Product Manager  
**Roles Affected**: System Architect, Staff Engineer, Full-Stack Engineer  
**Type**: Enhancement  
**Priority**: P1  
**Status**: Open  

## Context  
The project requires strict governance ensuring all commits reference valid issue IDs. Currently, there is no automated enforcement preventing commits without proper "#ISS-###" tags, which breaks traceability and accountability in the development process.

## Impact  
- Commits without issue references break governance and audit trails
- Manual enforcement is unreliable and creates inconsistent practices
- Lost context linking changes to their business justification
- Difficulty tracking which changes address which requirements
- Policy violations that undermine the entire issue tracking system

## Proposed Resolution  
* Create `/scripts/pre-commit` bash script that scans commit messages
* Block commits that don't contain valid "#ISS-###" pattern
* Provide clear error message with examples when commit is rejected
* Ensure script works with both direct git commits and GitHub integrations
* Add installation instructions to project documentation
* Test with valid and invalid commit message examples

## Acceptance Criteria  
- Pre-commit script successfully blocks commits without issue tags
- Script accepts commits with valid "#ISS-###" format
- Error messages clearly explain the requirement and provide examples
- Script handles edge cases (merge commits, initial commit, etc.)
- Installation documentation added to appropriate policy files
- Test suite demonstrates all scenarios work correctly

## Owner  
System Architect