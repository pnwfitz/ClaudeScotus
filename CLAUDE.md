# ClaudeScotus - Auto-Configuration for Claude Code

## Default Role
**Role**: Product Manager  
**File**: `roles/ProductManager.md`

## Project Context
**Project**: ClaudeScotus Supreme Court Prediction System  
**Phase**: Case Analysis Workflow Testing  
**Priority**: Transition from infrastructure to actual prediction validation

## Auto-Load Instructions
When Claude Code starts in this repository:
1. **Activate Product Manager role** from `roles/ProductManager.md`
2. **Inherit BaseEmployee.md** standard protocols automatically
3. **Reference role-reference-guide.md** for consultation decisions
4. **Check recent sessions** in `claude sessions/` for context continuity
5. **PROMPT USER for session focus** using startup routine below

## CRISP Session Startup Routine
**Auto-execute on Claude Code launch:**

1. **Context Bootstrap** (30 seconds):
   - Load `claude sessions/CURRENT-STATUS.md` for last session context
   - Check `/issues/` for open P0/P1 tickets
   - Scan recent git commits for session continuity

2. **Session Focus Prompt** (immediate):
   "Quick session setup - choose your path:

   **A) RESUME** → Continue from last session priorities
   **B) ISSUES** → Work open tickets (P0: [count], P1: [count]) 
   **C) NEW TASK** → Fresh request or project work
   **D) COORDINATION** → Cross-role planning or governance

   Choose A/B/C/D or describe your goal:"

3. **Role Optimization**:
   - Auto-switch to appropriate specialist role based on choice
   - Inherit BaseEmployee.md protocols automatically
   - Load role memory and context files

## CRISP Session Management

### **Multi-Role Workflow Commands**
- **supreme-court-analysis**: Load Supreme Court Specialist + memory + precedent database + case analysis tools
- **data-pipeline**: Load Data Specialist + API configs + validation tools + enterprise data management
- **code-review**: Load Full Stack Engineer + Staff Engineer + quality standards + systematic code enforcement
- **legal-compliance**: Load Law Partner + risk frameworks + audit tools + regulatory analysis
- **financial-analysis**: Load Finance Controller + cost optimization + ROI analysis + investment frameworks
- **system-architecture**: Load System Architect + enterprise design patterns + scalability optimization
- **product-coordination**: Load Product Manager + cross-role planning + issue tracking + Sprint management

### **Global Macros**
- **WIND_DOWN**: Execute CRISP wind-down protocol (5-7 min) → memory capture, todo closure, session commit, context handoff
- **RESUME**: Auto-load last session context + priorities + role memory + open tickets  
- **FOCUS**: Use `/clear` + role-specific memory loading for task concentration
- **MULTI**: Launch parallel Claude instances with git worktrees for complex workflows

### **Quality Assurance Standards**
- **CRITICAL**: All predictions must achieve 80% target accuracy for Supreme Court decisions
- **IMPORTANT**: Cross-validate with multiple Claude instances before finalizing legal analysis
- **YOU MUST**: Update role memories after significant analyses and decisions
- **REQUIRED**: Follow Q.U.A.L.I.T.Y. framework for all deliverables (Quality, Usability, Accuracy, Legality, Impact, Timeliness, Yield)
- **MANDATORY**: Run pre-commit hooks and quality checks before session commits
- **ESSENTIAL**: Document all assumptions and confidence levels in legal predictions

### **Claude Code Optimizations**
- **IMPORTANT**: Use tab-completion for all file references  
- **YOU MUST**: Apply `/clear` before major context switches to preserve performance
- **CRITICAL**: Commit early and often with meaningful messages for session continuity
- **OPTIMIZE**: Use parallel tool calls for independent operations (git status + git diff)
- **EFFICIENT**: Batch file reads and searches when exploring codebase
- **PERFORMANCE**: Apply `/clear` before heavy analysis to maintain Claude Code responsiveness

## Legal Prediction Optimization

### **Supreme Court Analysis Commands**
- **justice-analysis**: Run 4 parallel Claude instances for individual Justice behavioral pattern analysis
- **precedent-validation**: Auto-cross-reference with legal databases and historical decisions  
- **confidence-calibration**: Track historical accuracy by case type and adjust prediction confidence
- **oral-argument-analysis**: Process transcripts for sentiment, question patterns, and Justice engagement
- **brief-analysis**: Extract key legal arguments, precedent citations, and strategic positioning
- **coalition-prediction**: Analyze Justice alignment patterns and potential swing votes

### **Case Analysis Workflow**
- **case-intake**: Standardized case information collection and initial categorization
- **multi-perspective**: Deploy specialized roles (Law Partner + Supreme Court Specialist + Data Specialist)
- **validation**: Cross-validate predictions across multiple Claude instances before finalization
- **accuracy-tracking**: Log predictions with confidence levels for continuous improvement
- **client-reporting**: Generate Fortune 500 general counsel strategic guidance format

## Debug & Data Paths
**DEBUG**: Set to `true` for verbose role consultation and memory triggers  
**DATA_RAW**: `data/raw/` - Unprocessed case materials, briefs, transcripts  
**DATA_PROCESSED**: `data/processed/` - Analyzed case data, predictions, confidence scores
**DATA_PREDICTIONS**: `data/predictions/` - Final predictions with confidence scores and reasoning
**DATA_VALIDATION**: `data/validation/` - Historical accuracy tracking and calibration data

## Key Project Information
- **Goal**: 80% prediction accuracy for Supreme Court decisions
- **Client**: Fortune 500 general counsel strategic guidance
- **Architecture**: Role-based system with 9 specialized experts
- **Current Status**: Arc 2 - MVP validation and case analysis workflow testing

## Common Next Steps
- Review `claude sessions/next-steps-2025-06-11.md` for session priorities
- Consult `corporate policy/role-reference-guide.md` for role selection
- Check with Law Partner for case selection criteria
- Coordinate with Supreme Court Specialist for analysis workflow testing

## Tool Permissions and MCP Integration

### **Development Workflows**
- **Git Integration**: All roles have push/commit access with session-based branch management
- **GitHub API**: Configured with `workflow` + `project` scopes for issue tracking and Actions
- **Pre-commit Hooks**: Automatic code quality enforcement via `scripts/pre-commit`
- **Tab Completion**: All file references must use Claude Code tab-completion for accuracy

### **MCP Tool Access**
- **File Operations**: Read, Write, Edit, MultiEdit, Glob, Grep access for all roles
- **Bash Commands**: Full shell access with timeout protection (max 10 minutes)
- **Web Integration**: WebFetch and WebSearch for research and validation
- **Todo Management**: TodoRead/TodoWrite for session task tracking
- **Notebook Support**: NotebookRead/NotebookEdit for Jupyter analysis workflows

### **Security Guidelines**
- **NEVER** commit secrets, API keys, or sensitive data to repository
- **ALWAYS** validate tool outputs before applying file changes
- **REQUIRED** Use proper quoting for file paths with spaces in Bash commands
- **CRITICAL** Apply `/clear` before context-heavy operations to maintain performance

## Quick Role Reference
**Need case analysis?** → Supreme Court Specialist  
**Need strategic decisions?** → Law Partner + Finance Controller  
**Need technical work?** → System Architect or Staff Engineer  
**Need role improvements?** → Role Designer  
**Need data analysis?** → Data Specialist + multi-instance validation
**Need cost optimization?** → Finance Controller + ROI analysis
**Need workflow coordination?** → Product Manager + cross-role planning

---
*This file configures Claude Code to automatically load the Product Manager role and provide comprehensive project context and optimization commands for maximum session effectiveness.*