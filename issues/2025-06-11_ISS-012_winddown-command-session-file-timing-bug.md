# Winddown Command Session File Timing Bug
**Issue ID**: ISS-012  
**Opened By**: Product Manager  
**Roles Affected**: All roles using /winddown command  
**Type**: Bug  
**Priority**: P2  
**Status**: Open  

## Context  
The `/winddown` custom command has a timing bug where session documentation files are created AFTER the git commit step, causing session files to not be included in the GitHub push. This was discovered when the `2025-06-11_1540_winddown-optimization-session.md` file was created locally but missing from GitHub.

## Impact  
**Session Documentation Impact**:
- Session files not automatically pushed to GitHub with /winddown command
- Historical session tracking incomplete on GitHub
- Manual intervention required to commit and push session files
- Breaks the "one command does everything" design principle of /winddown

## Proposed Resolution  
* Reorder `/winddown` command steps to create session documentation BEFORE git commit
* Move "SESSION DOCUMENTATION" step from position 4 to position 3
* Move "SESSION COMMIT" step from position 3 to position 4
* Ensure all session artifacts are included in single commit and push

**Corrected Flow**:
```
1. MEMORY CAPTURE (2 min)
2. TODO CLOSURE (1 min)  
3. SESSION DOCUMENTATION (1-2 min) ← Move before commit
4. SESSION COMMIT (1 min) ← Move after documentation
5. FINAL PUSH (30 sec)
```

## Acceptance Criteria  
**Done means**:
- [ ] `/winddown` command updated with corrected step order
- [ ] Session documentation created before git commit step
- [ ] All session files automatically included in GitHub push
- [ ] No manual intervention required for complete session closure
- [ ] Command tested to verify session files appear on GitHub immediately
- [ ] Documentation updated to reflect correct workflow sequence

## Owner  
Unassigned (PM to assign during triage)