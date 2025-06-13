# ClaudeScotus Style Guide

## Code Standards

**Python**: 3.11+ with `black` formatting, `ruff` linting  
**Bash**: POSIX-compliant, 2-space indentation  
**Markdown**: CommonMark with trailing newlines  
**JSON**: 2-space indentation, sorted keys

## File Organization

```
data/raw/         # Unprocessed case materials
data/processed/   # Analyzed data, predictions
scripts/          # Automation and utilities
```

## Prompt Engineering (≤80 lines)

```markdown
# Role: [Specific Role Name]
🗎 Context: [Relevant files with 🗎 prefix]
📋 Objective: [Clear, measurable goal]

## Requirements
- [Specific, testable requirement]

## Success Criteria
- [ ] [Checkable outcome]
```

## File Naming Convention

```
YYYY-MM-DD_HHMM_description.md      # Session docs
YYYY-MM-DD_ISS-###_slug.md         # Issue tickets
YYYY-MM-DD_role_decision.md        # Memory files
```

## Wind-down Template

```markdown
# Session Wind-down Summary
**Date**: YYYY-MM-DD  
**Role**: [Primary role used]  
**Issue**: #ISS-### (if applicable)

## Objectives Status
- ✅ [Completed] / ❌ [Incomplete] / 🔄 [Partial]

## Issues Created/Updated
- **ISS-###**: [Brief description] - [Status]

## Memory Paths Updated
- 🧠 `memory/[role]/decisions/YYYY-MM-DD_[topic].md`

## Context Handoff
**Critical information for fast resume:**
- [Key decision or blocker]
```

## Commit Message Format

```bash
#ISS-###: [Imperative verb] [brief description]

[Optional longer description]

🤖 Generated with [Claude Code](https://claude.ai/code)
Co-Authored-By: Claude <noreply@anthropic.com>
```

## Session Management

**Wind-down Triggers**: Token limit (>90%), natural stopping point, context switch  
**Resume Process**: Read last wind-down + check open issues + scan role memories  

## Quality Assurance

**Pre-commit**: Markdown trailing newlines, Python `black`/`ruff`, Bash `shfmt`  
**File References**: Always use 🗎 prefix for clarity  
**Memory Updates**: Document decisions, lessons, patterns after significant work

## Anti-Patterns

❌ Missing file references in prompts  
❌ Generic commit messages without issue tags  
❌ Wind-down summaries missing required sections  
❌ Starting sessions without context review