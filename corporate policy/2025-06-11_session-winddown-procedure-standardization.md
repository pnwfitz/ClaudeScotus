# Session Wind Down Procedure - ClaudeScotus

**Version**: 1.0  
**Purpose**: Standardized procedure for ending Claude Code sessions and preserving session context

## Wind Down Steps

### 1. Session Documentation
- **Terminal Transcript**: Save complete terminal session to `claude sessions/` folder
- **Exception**: Skip saving if session crashed (data already preserved from previous session)
- **Format**: YYYY-MM-DD_HHMM_session-type.md with complete transcript
- **Security**: Redact any sensitive information (API keys, tokens, credentials)

### 2. Prompt Inventory
- **User Prompts**: Extract and document all user prompts from the session
- **Purpose**: Track user intent patterns and frequently requested actions
- **Format**: Numbered list with brief context for each prompt
- **File**: Save to session documentation under "User Prompts" section

### 3. Accomplishment Summary
- **Executive Summary**: High-level overview of what was completed
- **Key Deliverables**: Specific files created, updated, or refactored
- **Issues Resolved**: Problems addressed and solutions implemented
- **Metrics**: Quantify improvements (lines reduced, efficiency gains, etc.)

### 4. Previous Session Comparison
- **Review Prior Goals**: Check previous session's "Next Steps" document
- **Completion Assessment**: Evaluate what was accomplished vs. planned
- **Variance Analysis**: Note any deviations and reasons
- **Lessons Learned**: Document insights from comparing plan vs. actual

### 5. Next Session Planning
- **Immediate Priorities**: High-priority tasks for next session start
- **Context Requirements**: What context will be needed to continue
- **Dependencies**: Any blockers or prerequisites to address
- **Success Criteria**: How to measure progress in next session

### 6. Repository Update
- **Commit All Changes**: Ensure all session work is committed to git
- **Meaningful Messages**: Clear commit descriptions with scope and impact
- **Push to Remote**: Sync all changes to GitHub for persistence
- **Verification**: Confirm all files are visible on GitHub

## Quality Standards

- **Completeness**: All session artifacts preserved and documented
- **Clarity**: Future sessions can easily understand context and next steps
- **Security**: No sensitive information exposed in documentation
- **Efficiency**: Wind down process should take 10-15 minutes maximum

## File Locations

- **Session Documentation**: `claude sessions/YYYY-MM-DD_HHMM_session-type.md`
- **Executive Summary**: Include in session documentation
- **Next Steps**: `claude sessions/next-steps-YYYY-MM-DD.md`
- **Wind Down Logs**: Update this procedure based on lessons learned

---

**Implementation Note**: This procedure should be executed at the end of every Claude Code session to maintain project continuity and context preservation.