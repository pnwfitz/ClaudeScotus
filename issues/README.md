# ClaudeScotus Issue Tracking System

![Issues](https://img.shields.io/badge/Issues-Tracking%20System-blue) ![Status](https://img.shields.io/badge/Status-Active-green) ![Integration](https://img.shields.io/badge/Integration-Memory%20System-purple)

## 📋 Table of Contents

<details>
<summary>System Overview</summary>

- [Overview](#overview)
- [File Naming Convention](#file-naming-convention)
- [Label Taxonomy](#label-taxonomy)

</details>

<details>
<summary>Process & Workflow</summary>

- [Issue Management Rules](#issue-management-rules)
- [Quality Thresholds](#quality-thresholds)
- [Workflow Integration](#workflow-integration)

</details>

<details>
<summary>Tools & Integration</summary>

- [Template Usage](#template-usage)
- [CI/CD Integration](#cicd-integration)
- [Metrics Dashboard](#metrics-dashboard)

</details>

## Overview

This directory contains the project-wide issue and ticket system for ClaudeScotus. All enhancements, bugs, policy changes, and research tasks must be tracked through this system to ensure proper governance and memory retention.

### System Purpose

| Purpose | Description | Benefit |
|---------|-------------|----------|
| **Governance** | Systematic tracking of all changes | Audit trail and accountability |
| **Memory Integration** | Link issues to role memory updates | Continuous improvement |
| **SCOTUS Accuracy** | Track prediction-impacting issues | 80% accuracy target support |
| **Session Efficiency** | Monitor workflow bottlenecks | Optimized Claude Code sessions |
| **Quality Assurance** | Systematic resolution tracking | Professional delivery standards |

## File Naming Convention

### Standard Format

All issue files must follow this exact format:

```bash
YYYY-MM-DD_ISS-###_<slug>.md
```

| Component | Format | Example | Purpose |
|-----------|--------|---------|----------|
| **Date** | YYYY-MM-DD | 2025-06-11 | Issue creation date |
| **Prefix** | ISS-### | ISS-001 | Sequential issue number (zero-padded) |
| **Slug** | kebab-case | data-specialist-memory-triggers | Descriptive identifier |
| **Extension** | .md | .md | Markdown format |

### Examples

```bash
# Valid filenames
2025-06-11_ISS-001_data-specialist-memory-triggers.md
2025-06-11_ISS-002_pre-commit-hook-enforcement.md
2025-06-11_ISS-003_prediction-mvp-scope.md

# Invalid filenames
ISS-001_memory-issue.md           # Missing date
2025-06-11_memory_issue.md         # Missing ISS prefix
2025-06-11_ISS-1_memory-issue.md  # Not zero-padded
```

### Validation Rules

- [ ] **Date format**: ISO 8601 (YYYY-MM-DD)
- [ ] **Issue prefix**: ISS-### (zero-padded to 3 digits)
- [ ] **Slug format**: kebab-case (lowercase, hyphens)
- [ ] **File extension**: .md (Markdown)
- [ ] **Uniqueness**: No duplicate issue numbers

## Label Taxonomy

### Issue Types

| Type | Description | Examples | SCOTUS Impact |
|------|-------------|----------|---------------|
| **Bug** | System defects, broken functionality | Role consultation errors, prediction failures | Direct accuracy impact |
| **Enhancement** | Feature additions, improvements | New analysis capabilities, workflow optimizations | Accuracy and efficiency gains |
| **Policy** | Governance, process, documentation updates | Role guidelines, session protocols | Process quality |
| **Memory** | Role memory updates, learning integration | Pattern documentation, lesson capture | Continuous improvement |
| **Research** | Investigation, analysis, exploration tasks | Justice analysis, methodology research | Prediction methodology |

### Priority Matrix

| Priority | Impact | Urgency | Response Time | Examples |
|----------|--------|---------|---------------|----------|
| **P0** | Critical | Immediate | <4 hours | System broken, blocks all prediction work |
| **P1** | High | Urgent | <24 hours | Major prediction accuracy issues, role failures |
| **P2** | Medium | Important | <72 hours | Workflow inefficiencies, minor accuracy issues |
| **P3** | Low | Nice-to-have | <2 weeks | Documentation improvements, minor features |

### Status Lifecycle

```mermaid
flowchart LR
    A[Open] --> B[In Progress]
    B --> C[Review/PR]
    C --> D[Closed]
    C --> B[In Progress]
    D --> E[Archive]
```

| Status | Description | Actions Required | Next Steps |
|--------|-------------|------------------|------------|
| **Open** | Issue created, awaiting triage | PM assignment, priority setting | Move to In Progress |
| **In Progress** | Actively being worked on | Implementation work | Move to Review/PR |
| **Review/PR** | Implementation complete, under review | Quality validation, testing | Move to Closed or back to In Progress |
| **Closed** | Resolution implemented and verified | Memory updates, documentation | Archive after memory integration |

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

| Condition | Threshold | Impact | Escalation |
|-----------|-----------|--------|-----------|
| **P0 Issues Open** | >3 for >24 hours | System dysfunction | Immediate attention |
| **Cycle Time** | >14 days average | Workflow bottleneck | Process review |
| **Memory Integration** | <90% compliance | Learning loss | Memory audit |
| **SCOTUS Accuracy** | Prediction issues | Accuracy target risk | Legal review |

### Performance Metrics

<details>
<summary>Velocity Metrics</summary>

| Metric | Target | Current | Trend |
|--------|--------|---------|-------|
| **Issues Opened/Week** | <10 | 📈 Tracking | TBD |
| **Issues Closed/Week** | >8 | 📈 Tracking | TBD |
| **Net Issue Growth** | <2/week | 📈 Tracking | TBD |

</details>

<details>
<summary>Quality Metrics</summary>

| Metric | Target | Current | Validation |
|--------|--------|---------|------------|
| **Cycle Time P0** | <4 hours | 📈 Tracking | Automated |
| **Cycle Time P1** | <24 hours | 📈 Tracking | Automated |
| **Memory Integration** | 100% | 📈 Tracking | CI/CD |
| **SCOTUS Impact** | 0 prediction degradation | 📈 Tracking | Manual review |

</details>

### Metrics Dashboard

```bash
# Generate weekly metrics report
./scripts/issue-metrics.sh --week [YYYY-MM-DD]

# Validate memory integration
./scripts/memory-compliance.sh

# Check SCOTUS prediction impact
./scripts/prediction-health.sh
```

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