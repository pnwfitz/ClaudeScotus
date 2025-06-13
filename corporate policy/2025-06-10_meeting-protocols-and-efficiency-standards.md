# ClaudeScotus Session Coordination Standards
**Version**: 2.0  
**Focus**: Claude Code session-based coordination for SCOTUS prediction development

## Session Philosophy
Claude Code sessions optimize for focused work with specific role expertise. Multi-role coordination uses structured handoffs and documented decision points rather than traditional meetings.

## Session Coordination Patterns

### Technical Architecture Sessions
**Approach**: System Architect primary session → documented handoff → Staff Engineer review  
**Context**: Technical specifications in git commits and memory files  
**Output**: Architecture decisions logged in `/memory/system_architect_decisions/`

### SCOTUS Analysis Sessions
**Approach**: Supreme Court Specialist analysis → Law Partner strategic review  
**Context**: Case files and precedent research documented in `/data/`  
**Output**: Predictions with confidence levels in `/data/predictions/`

### Code Quality Sessions
**Approach**: Staff Engineer standards → Full-Stack Engineer implementation  
**Context**: Quality standards in role definitions and commit hooks  
**Output**: Code quality metrics and improved implementation patterns

## Session Handoff Standards

### Required Session Elements:
1. **Context Documentation** in role memory files
2. **Decision Logging** in git commits with issue references
3. **Next Session Preparation** in `CURRENT-STATUS.md`
4. **Quality Gates** met before session wind-down

### Session Handoff Template:
```
## Session Context
Role: [Current role]
Focus: [Primary objective]
Files Modified: [Key changes]

## Decisions Made:
- [Decision] → [Rationale] → [Next Steps]

## Next Session Needs:
- Role: [Recommended role]
- Priority: [P0/P1/P2]
- Context: [Key files/issues to review]
```

## Role-Specific Session Responsibilities

### Finance Controller (Efficiency Optimization):
- Monitor Claude Code session performance and context usage
- Identify workflow bottlenecks and optimization opportunities
- Track prediction accuracy ROI and session effectiveness

### Product Manager (Coordination):
- Manage issue tracking and session priority queues
- Coordinate role handoffs and context preservation
- Document cross-role dependencies and resolution paths

### System Architect (Technical Foundation):
- Ensure technical decisions support SCOTUS prediction accuracy
- Document architectural decisions in memory system
- Validate technical approaches against prediction requirements

### Law Partner (Strategic Oversight):
- Frame legal analysis in terms of prediction methodology
- Validate Supreme Court Specialist output for accuracy
- Ensure analysis maintains professional legal standards

## Preferred Coordination Methods

### Git-Based Documentation:
- Technical decisions in commit messages and memory files
- Legal analysis documented in `/data/analysis/`
- Code reviews through git diff and quality standards
- Session continuity through `CURRENT-STATUS.md`

### Issue Tracking System:
- Feature development tracked in `/issues/`
- Technical debt and optimization opportunities
- Prediction accuracy improvements and methodology refinements
- Cross-role dependencies and handoff requirements

### Role Memory System:
- Session learnings preserved in role-specific memory directories
- Decision rationale and context for future reference
- Pattern recognition and workflow optimization insights

## Session Quality Metrics

### Efficiency Targets:
- **Issue Resolution**: >80% of P0/P1 issues resolved within 3 sessions
- **Context Preservation**: >95% session handoffs include complete context
- **Prediction Accuracy**: SCOTUS predictions achieve 80% accuracy target
- **Session Focus**: Clear role activation and scope maintenance

### Session Tracking:
- Git commit frequency and quality (meaningful progress markers)
- Role memory updates and knowledge preservation
- Issue lifecycle management and resolution patterns
- Prediction validation and accuracy improvement trends

## Session Issue Resolution

### Context Overload:
1. Apply `/clear` command to focus session scope
2. Document essential context in memory files
3. Use role-specific memory triggers for context recovery
4. Consider role switching if expertise mismatch

### Blocked Progress:
1. Document blocking issues in `/issues/` with clear next steps
2. Identify appropriate role for resolution
3. Update `CURRENT-STATUS.md` with handoff context
4. Escalate to Law Partner for SCOTUS prediction methodology questions

### Quality Standards Issues:
1. Finance Controller evaluates session efficiency patterns
2. Product Manager updates issue tracking and priority systems
3. System Architect reviews technical workflow bottlenecks
4. Role Designer optimizes role definitions based on session learnings

## Session Anti-Patterns to Avoid

### Inefficient Session Activities:
- **Role Confusion**: Using wrong role for task domain
- **Context Dumping**: Reading large files instead of targeted analysis
- **Scope Creep**: Expanding beyond session role expertise
- **Memory Neglect**: Failing to update role memory with insights

### Session Red Flags:
- Session objectives unclear or too broad for single role
- Context window exhaustion without using `/clear`
- Multiple sessions on same issue without progress documentation
- Role switching without proper context handoff

## Issue Tracking Integration

### Issue Creation Requirements:
All SCOTUS prediction work and technical improvements tracked through `/issues/`:
- **Prediction Methodology**: Analysis improvements and accuracy optimization
- **Technical Debt**: Code quality and architecture enhancement needs
- **Data Pipeline**: Case analysis workflow and validation improvements
- **Role Optimization**: Performance issues and workflow refinements

### Commit Integration:
- All commits reference issue tags (#ISS-###) for traceability
- Pre-commit hooks enforce quality standards and issue tagging
- Session outcomes create specific issues for follow-up work

### Memory Integration:
- Completed issues trigger role memory updates
- Session learnings documented in role-specific memory directories
- Pattern recognition and workflow improvements preserved for future sessions

## Continuous Improvement

### Session-Based Review:
1. Finance Controller tracks session efficiency and Claude Code performance
2. Role memory system captures learnings and optimization opportunities
3. Product Manager updates issue tracking based on workflow insights
4. Role Designer refines role definitions based on session effectiveness

### Performance Triggers:
- SCOTUS prediction accuracy below 80% target
- Session context management becoming inefficient
- Role expertise gaps affecting prediction quality
- Git workflow or issue tracking bottlenecks

---

**Document Focus**: Session-based coordination for SCOTUS prediction development  
**Owners**: Product Manager (coordination), Role Designer (optimization)  
**Context**: Supports Claude Code workflow optimization and prediction accuracy goals