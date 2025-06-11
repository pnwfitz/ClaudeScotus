# ClaudeScotus Style Guide
**Version**: 1.0  
**Created**: 2025-06-11  
**Issue**: #ISS-006  

## Code Standards

### Languages & Formatters
- **Python**: 3.11+ with `black` formatting and `ruff` linting
- **Bash**: POSIX-compliant with `shfmt -i 2` (2-space indentation)
- **Markdown**: CommonMark specification with trailing newlines
- **JSON**: 2-space indentation, sorted keys where appropriate

### Code Quality
```bash
# Required formatters and linters
black --line-length 88 --target-version py311 .
ruff check --fix .
shfmt -i 2 -w scripts/
```

### File Organization
```
data/
├── raw/              # Unprocessed case materials
└── processed/        # Analyzed data, predictions

scripts/              # Automation and utilities
├── pre-commit*       # Git hooks
└── validation/       # CI/CD scripts

docs/                 # Generated documentation
└── api/              # Role interface documentation
```

## Prompt Engineering Standards

### Prompt Structure (≤80 lines)
```markdown
# Role: [Specific Role Name]
🗎 Context: [Cite relevant files with 🗎 prefix]
📋 Objective: [Clear, measurable goal]

## Requirements
- [Specific, testable requirement]
- [Another requirement]

## Constraints
- Line wrapping ≤120 characters
- Reference files with absolute paths
- Include expected output format

## Success Criteria
- [ ] [Checkable outcome]
- [ ] [Another outcome]
```

### File References
Always cite files with 🗎 prefix for clarity:
- 🗎 `roles/SupremeCourtSpecialist.md`
- 🗎 `memory/law_partner_decisions/2025-06-11_case_analysis.md`
- 🗎 `issues/2025-06-11_ISS-006_docs-style-winddown-refinement.md`

## Documentation Standards

### File Naming Convention
```
YYYY-MM-DD_HHMM_description.md      # Session docs
YYYY-MM-DD_ISS-###_slug.md         # Issue tickets
YYYY-MM-DD_role_decision.md        # Memory files
```

### Wind-down Template
```markdown
# Session Wind-down Summary
**Date**: YYYY-MM-DD  
**Duration**: [Start] - [End]  
**Role**: [Primary role used]  
**Issue**: #ISS-### (if applicable)

## Objectives Status
- ✅ [Completed objective with outcome]
- ❌ [Incomplete objective with blocker]
- 🔄 [Partial objective with next steps]

## Issues Created/Updated
- **ISS-###**: [Brief description] - [Status]
- **ISS-###**: [Brief description] - [Status]

## Next-Step Tickets
**Priority assignments for session continuation:**
- [ ] **P0**: [Critical issue] → [Assigned role]
- [ ] **P1**: [High priority] → [Assigned role]
- [ ] **P2**: [Medium priority] → [Assigned role]

## Memory Paths Updated
- 🧠 `memory/[role]/decisions/YYYY-MM-DD_[decision_topic].md`
- 🧠 `memory/[role]/lessons/YYYY-MM-DD_[lesson_learned].md`
- 🧠 `memory/shared/patterns/YYYY-MM-DD_[cross_role_pattern].md`

## Context Handoff
**Critical information for fast resume:**
- [Key decision or blocker]
- [Important discovery or pattern]
- [Stakeholder context or constraint]

## Commit References
- **Primary**: [commit_sha] - [brief description]
- **Secondary**: [commit_sha] - [brief description]

---
*Wind-down completed: [timestamp]*
```

## Commit Message Standards

### Format Pattern
```bash
#ISS-###: [Imperative verb] [brief description]

[Optional longer description explaining why]
[Reference to related issues or decisions]

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

### Examples
```bash
#ISS-006: Add comprehensive style guide and wind-down protocols

Establishes consistent code formatting, prompt engineering standards,
and systematic session management procedures.

#ISS-003: Implement MVP prediction scope specification

Defines 80% accuracy target, Fortune 500 client deliverables,
and 8-week validation timeline for Supreme Court predictions.
```

## Session Management

### Wind-down Triggers
Execute `WIND_DOWN` macro when:
- Token count approaches limit (>90% context window)
- Natural stopping point reached
- Switching to different work stream
- End of allocated session time

### Resume Checklist
Execute `RESUME` macro by:
1. Reading last `claude sessions/*_wind_down.md`
2. Checking `/issues/` for open P0/P1 tickets
3. Scanning relevant `memory/[role]/` for recent decisions
4. Using CLAUDE.md startup routine for work prioritization

## Role-Specific Standards

### Memory Documentation
- **Decisions**: Major choices with rationale and impact
- **Lessons**: Insights from successes/failures
- **Patterns**: Recurring themes across sessions
- **Context**: Background information for future reference

### Consultation Protocols
- Reference 🗎 `corporate policy/role-reference-guide.md` for role selection
- Use green/yellow/red flag framework from individual role files
- Create issues for cross-role coordination needs
- Document consultation outcomes in appropriate memories

## Quality Assurance

### Pre-commit Validation
- Markdown files must end with trailing newline
- Wind-down files must contain required template sections
- Python code must pass `black` and `ruff` checks
- Bash scripts must pass `shfmt` formatting

### CI/CD Integration
- Issue file structure validation
- Memory integration compliance auditing
- Style guide adherence checking
- Documentation link validation

## Anti-Patterns to Avoid

### Code & Documentation
- ❌ Inconsistent indentation or formatting
- ❌ Missing file references in prompts
- ❌ Generic commit messages without issue tags
- ❌ Wind-down summaries missing required sections

### Session Management
- ❌ Ending sessions without proper wind-down
- ❌ Starting sessions without context review
- ❌ Creating issues without proper categorization
- ❌ Forgetting to update role memories

---

## Version History
- **v1.0** (2025-06-11): Initial comprehensive style guide

*This guide ensures consistent quality and systematic workflow management across all ClaudeScotus development activities.*