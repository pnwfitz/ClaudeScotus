# ClaudeScotus Issue Tracking System

## Overview
This directory contains the project-wide issue and ticket system for ClaudeScotus. All enhancements, bugs, policy changes, and research tasks must be tracked through this system to ensure proper governance and memory retention.

## File Naming Convention
All issue files must follow this exact format:
```
YYYY-MM-DD_ISS-###_<slug>.md
```

**Examples:**
- `2025-06-11_ISS-001_data-specialist-memory-triggers.md`
- `2025-06-11_ISS-002_pre-commit-hook-enforcement.md`
- `2025-06-11_ISS-003_prediction-mvp-scope.md`

**Components:**
- **YYYY-MM-DD**: Issue creation date
- **ISS-###**: Sequential issue number (zero-padded to 3 digits)
- **<slug>**: Descriptive kebab-case slug

## Label Taxonomy

### Types
- **Bug**: System defects, broken functionality
- **Enhancement**: Feature additions, improvements
- **Policy**: Governance, process, documentation updates
- **Memory**: Role memory updates, learning integration
- **Research**: Investigation, analysis, exploration tasks

### Priorities
- **P0**: Critical - System broken, blocks all work
- **P1**: High - Major impact, blocks significant functionality
- **P2**: Medium - Moderate impact, affects efficiency
- **P3**: Low - Minor impact, nice-to-have improvements

### Status Lifecycle
1. **Open**: Issue created, awaiting triage
2. **In Progress**: Actively being worked on
3. **Review/PR**: Implementation complete, under review
4. **Closed**: Resolution implemented and verified

## Issue Management Rules

### Creation Requirements
- All issues must use the `ISSUE_TEMPLATE.md` format
- Must include impact assessment and acceptance criteria
- Owner initially "Unassigned" until PM assigns during triage

### Commit Integration
- Every commit must reference an issue: `#ISS-###`
- Pre-commit hooks enforce this requirement
- No commits allowed without proper issue tagging

### Memory Integration
- Closed issues must trigger updates to relevant role memories
- Lessons learned must be documented in appropriate `memory/` folders
- CI checks enforce memory updates for closed tickets

## Quality Thresholds

### Red Flag Conditions
- More than 3 open P0 issues for >24 hours
- Average cycle time >14 days across all issues
- Closed issues without corresponding memory updates

### Metrics Tracked
- Issue velocity (opened vs closed per week)
- Cycle time by priority level
- Memory integration compliance rate
- Role engagement patterns

## Workflow Integration

### For Product Manager
- Daily triage of new issues
- Weekly velocity and cycle time review
- Assignment of owners based on role expertise
- Policy compliance enforcement

### For All Roles
- Check for relevant open issues before starting work
- Create issues for all non-trivial changes
- Update issue status during work progression
- Document lessons in role memories upon closure

## Template Usage
Use `/issues/ISSUE_TEMPLATE.md` as the starting point for all new issues. The template ensures consistent structure and required information capture.

## CI/CD Integration
- GitHub Actions validate issue file structure
- Pre-commit hooks enforce issue tagging
- Nightly audits check memory integration compliance
- Automated reports flag threshold violations

---
*Established: 2025-06-11 | Version: 1.0 | Maintained by: Product Manager*