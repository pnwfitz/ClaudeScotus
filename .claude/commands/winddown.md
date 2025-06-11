# CRISP Session Wind-Down Protocol

Execute the complete CRISP wind-down procedure for ClaudeScotus sessions. Target completion: 5-7 minutes.

## Auto-Execute Wind-Down Steps

### ⚡ **1. MEMORY CAPTURE** (2 minutes)
Update role memory with session insights:
- Extract key decisions made → `memory/[role]_decisions/`
- Identify patterns discovered → `memory/[role]_patterns/` 
- Document lessons learned → `memory/[role]_lessons/`
- Apply memory triggers from current role definition
- Update role metrics if performance data exists

**Context Management**: Use `/clear` to focus on session summary before memory updates.

### ⚡ **2. TODO CLOSURE** (1 minute)
Systematic issue and task management:
- ✅ Mark completed todos as DONE using TodoWrite
- 🔄 Update in-progress todos with current status  
- 📋 Create new issues for incomplete work with proper ISS-### numbering
- 🔺 Set priority levels (P0/P1/P2/P3) for next session
- Reference issue numbers in subsequent commits

### ⚡ **3. SESSION DOCUMENTATION** (1-2 minutes)
Create timestamped session file and update handoff:

**Session File**: `claude sessions/YYYY-MM-DD_HHMM_session-type.md`
```markdown
# Claude Session - [Session Focus]
**Date**: [YYYY-MM-DD]  
**Start Time**: [HHMM]  
**Session Type**: [Brief description of session type/focus]

## Session Objectives
- [List objectives - mark ✅ for completed, ⚠️ for partial, ❌ for failed]

## Key Deliverables Created
- [List files created/modified with ✅ status]

## Tickets Created This Session
- [List new ISS-### tickets with titles and priorities]

## Tickets Cleared This Session  
- [List completed ISS-### tickets with brief resolution summary]

## Critical Issues Identified & Fixed
1. **[Issue Name]**: [Description] - [Resolution]

## Session Highlights
[Key accomplishments, decisions, patterns discovered]

## Major Accomplishments
[Numbered list of significant achievements]

## Issues Still In Progress
- [Items that need follow-up]

## Technical Status
- [Git commits, file changes, integration status]

## Next Session Priorities
1. [Priority items for continuation]
```

**Handoff File**: Update `claude sessions/CURRENT-STATUS.md`
```markdown
# ClaudeScotus Session Handoff

## Last Session Summary
**Role**: [Current role]  
**Date**: [Session date]  
**Focus**: [Primary accomplishment]

## Next Session Priorities
1. **P0**: [Critical next step]
2. **P1**: [Important follow-up]  
3. **P2**: [Nice-to-have]

## Context Needed
- Role: [Recommended starting role]
- Files: [Key files to review]
- Issues: [Open ticket numbers]

## Quick Resume
"[One sentence describing where to pick up]"
```

### ⚡ **4. SESSION COMMIT** (1 minute)
Single comprehensive commit with ALL session work including documentation:

```bash
git add .
git commit -m "Session wind-down: [ROLE] [PRIMARY_ACCOMPLISHMENT] [NEXT_PRIORITY]

Completed:
- [Key achievement 1]
- [Key achievement 2]

Next session priority: [Top 1-2 items]

🤖 Generated with Claude Code"
```

**Complete Preservation**: All work AND session documentation committed together locally.

### ⚡ **5. FINAL PUSH** (30 seconds)
Push all session work to GitHub:

```bash
git push
```

**GitHub Integration**: 
- Verify `gh auth status` if push fails
- Session work preserved locally even if push fails
- All context and handoff documentation included in push

## Quality Verification

**MUST HAVE** before session end:
- ✅ All work committed to git and pushed to GitHub
- ✅ Next session priority clearly identified  
- ✅ Role memory updated with key session insights  
- ✅ Critical context documented for seamless handoff

**SHOULD HAVE** for optimization:
- ⭐ Session patterns identified for future workflow improvements
- ⭐ Role performance metrics updated with session data
- ⭐ Cross-role collaboration notes captured if applicable

## Emergency Protocol
If session must end immediately (30 seconds):
```bash
git add . && git commit -m "Emergency session end - work in progress"
git push || echo "Push failed - will retry next session"
echo "NEXT: [one critical next step]" > claude sessions/EMERGENCY-RESUME.md
```

---

**CRISP = Context, Rapid, Intelligent, Systematic, Preserved**

Execute this complete protocol to ensure optimal session closure and seamless next-session startup. All work preserved, context maintained, quality assured.