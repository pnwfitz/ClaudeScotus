# CRISP Session Wind-Down Procedure

**Version**: 2.0  
**Purpose**: Claude Code session closure with memory preservation for SCOTUS prediction work  
**Target Time**: 5-7 minutes maximum

## CRISP Wind-Down Protocol

### ⚡ **1. MEMORY CAPTURE** (2 minutes)
```
Role Memory Update:
- SCOTUS analysis insights → memory/[role]_decisions/
- Prediction patterns → memory/[role]_patterns/ 
- Session learnings → memory/[role]_lessons/
```

**Session Focus**:
- Use `/clear` to focus on session summary
- Update role memory with prediction-relevant insights
- Capture accuracy improvements and methodology refinements

### ⚡ **2. ISSUE TRACKING** (1 minute)
```
SCOTUS Prediction Work:
✅ Mark completed prediction tasks as DONE
🔄 Update analysis progress with current status  
📋 Create issues for prediction improvements
🔺 Set P0/P1 priorities for accuracy goals
```

**Git Integration**: 
- Commit issue updates with prediction context
- Reference issue numbers (#ISS-###) in commits

### ⚡ **3. SESSION COMMIT + PUSH** (2 minutes)
```bash
# Single commit with SCOTUS prediction context
git add .
git commit -m "Session wind-down: [ROLE] - [SCOTUS-ACCOMPLISHMENT]

Completed:
- [Prediction analysis/technical work]
- [Accuracy improvements/methodology]

Next session: [Priority for prediction development]

🤖 Generated with Claude Code"

git push
```

**Context Preservation**: 
- Commit preserves SCOTUS prediction progress locally
- Push failures don't block session wind-down
- Next session can retry push and continue prediction work

### ⚡ **4. CONTEXT HANDOFF** (1-2 minutes)
**Update**: `claude sessions/CURRENT-STATUS.md`
```markdown
# SCOTUS Prediction Session Handoff

## Last Session Summary
**Role**: [Current role]  
**Date**: [Session date]  
**Focus**: [SCOTUS prediction work completed]

## Next Session Priorities
1. **P0**: [Critical prediction/accuracy work]
2. **P1**: [Important analysis/technical work]  
3. **P2**: [Optimization opportunities]

## Context for Resume
- Role: [Recommended role for next work]
- Files: [Key prediction/analysis files]
- Issues: [Open prediction improvement tickets]

## Quick Resume
"[Next step for SCOTUS prediction development]"
```

## SCOTUS Prediction Session Optimizations

### **Prediction-Focused Workflow**:
- **Git Integration**: Commit messages reference prediction accuracy and methodology
- **File Operations**: Tab-completion for case files and analysis documents
- **Memory Management**: Focus on prediction insights and accuracy improvements

### **Multi-Instance Validation**:
For SCOTUS prediction validation:
- Consolidate prediction analysis from multiple instances
- Validate accuracy across different approaches
- Primary instance commits consolidated prediction results

### **Context Window Management**:
- Run `/clear` before final prediction documentation
- Focus on prediction accuracy and methodology insights
- Preserve essential case analysis context for next session

## Quality Gates

**MUST HAVE**:
✅ SCOTUS prediction work committed to git  
✅ Next session priority for prediction accuracy identified  
✅ Role memory updated with prediction insights  
✅ Critical analysis context documented for handoff

**SHOULD HAVE**:
⭐ Prediction accuracy patterns identified for optimization  
⭐ Analysis methodology improvements captured  
⭐ Cross-role prediction validation notes preserved

## Emergency Wind-Down (30 seconds)
```bash
# If SCOTUS prediction session must end immediately
git add . && git commit -m "Emergency session end - SCOTUS prediction work in progress"
git push || echo "Push failed - will retry next session"
echo "NEXT: [critical prediction work step]" > claude sessions/EMERGENCY-RESUME.md
```

**Prediction Work Preservation**: 
- Emergency commit preserves SCOTUS analysis work locally
- Push failure doesn't lose prediction progress
- Next session continues prediction development from preserved state

---

**CRISP = Context, Rapid, Intelligent, Systematic, Preserved**  
*Optimized for SCOTUS prediction development with Claude Code session management*