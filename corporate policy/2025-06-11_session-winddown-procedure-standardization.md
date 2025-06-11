# CRISP Session Wind-Down Procedure - ClaudeScotus

**Version**: 2.0 (Claude Code Optimized)  
**Purpose**: Fast, systematic session closure with memory preservation  
**Target Time**: 5-7 minutes maximum

## CRISP Wind-Down Protocol

### ⚡ **1. MEMORY CAPTURE** (2 minutes)
```
Role Memory Update:
- Key decisions made → role/memory/[role]_decisions/
- Patterns discovered → role/memory/[role]_patterns/ 
- Lessons learned → role/memory/[role]_lessons/
```

**Auto-Commands**:
- Use `/clear` to focus context on session summary
- Apply memory triggers from role definitions
- Update role metrics if performance data exists

### ⚡ **2. TODO CLOSURE** (1 minute)
```
Issue Management:
✅ Mark completed todos as DONE
🔄 Update in-progress todos with current status  
📋 Create new issues for incomplete work
🔺 Set priority levels for next session
```

**Git Integration**: 
- Commit todo list updates immediately
- Reference issue numbers in commits

### ⚡ **3. SESSION COMMIT + PUSH** (2 minutes)
```bash
# Single commit with complete session context
git add .
git commit -m "Session wind-down: [ROLE] [ACCOMPLISHMENT] [NEXT-PRIORITY]

Completed:
- [Key achievement 1]
- [Key achievement 2]

Next session priority: [Top 1-2 items]

🤖 Generated with Claude Code"

# Push to GitHub for persistence
git push
```

**GitHub Integration**: 
- Use `gh auth status` to verify authentication before push
- If auth fails, session context is still preserved locally via commit
- Next session can retry push after re-authentication

### ⚡ **4. CONTEXT HANDOFF** (1-2 minutes)
**Create/Update**: `claude sessions/CURRENT-STATUS.md`
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

## Claude Code Optimizations

### **Use Built-in Patterns**:
- **Git Integration**: Let Claude handle commit message composition
- **File Operations**: Use tab-completion for fast file references
- **Memory Management**: Leverage Claude's context awareness

### **Multi-Instance Cleanup**:
If multiple Claude instances were used:
- Close secondary instances first
- Consolidate findings in primary instance
- Single commit from primary instance only

### **Context Window Management**:
- Run `/clear` before final documentation
- Focus on essential handoff information only
- Avoid copying large file contents into session notes

## Quality Gates

**MUST HAVE**:
✅ All work committed to git  
✅ Next session priority identified  
✅ Role memory updated with key insights  
✅ Critical context documented for handoff

**SHOULD HAVE**:
⭐ Session patterns identified for future optimization  
⭐ Role performance metrics updated  
⭐ Cross-role collaboration notes captured

## Emergency Wind-Down (30 seconds)
```bash
# If session must end immediately
git add . && git commit -m "Emergency session end - work in progress"
git push || echo "Push failed - will retry next session"
echo "NEXT: [one critical next step]" > claude sessions/EMERGENCY-RESUME.md
```

**Failure Handling**: 
- Emergency commit always succeeds (preserves work locally)
- Push failure doesn't block emergency wind-down
- Next session will detect unpushed commits and retry

---

**CRISP = Context, Rapid, Intelligent, Systematic, Preserved**  
*Optimized for Claude Code's git integration, context management, and multi-instance workflows*