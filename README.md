# ClaudeScotus
# SCOTUS Prediction System

An experimental system to predict Supreme Court decisions using LLM-based analysis and role-based prompt engineering.

## Claude Code Configuration

**Default Role**: Product Manager  
When starting Claude Code sessions in this repository, automatically activate the Product Manager role for project coordination and stakeholder alignment.

```bash
# Auto-load command for Claude Code
claude --role="ProductManager" --context="ClaudeScotus"
```

## Overview

This project predicts SCOTUS rulings through:
1. **Legal Analysis**: Supreme Court Specialist analyzes briefs, decisions, and oral arguments
2. **Justice Modeling**: Individual Justice-specific prediction models
3. **Strategic Synthesis**: Law Partner transforms analysis into Fortune 500 executive briefings
4. **System Architecture**: Full software engineering practices using role-based development

## Project Status

✅ **Architecture Complete** - Role-based system with BaseEmployee.md inheritance  
✅ **Role Ecosystem** - 9 specialized roles with organizational reference guide  
🎯 **Next Phase** - Case analysis workflow testing and prediction validation

## Role-Based Architecture

### Leadership & Strategy
- **Law Partner**: Strategic decision authority, client deliverables
- **Finance Controller**: Budget management, efficiency oversight

### Project Coordination  
- **Product Manager**: Project orchestration, stakeholder alignment *(Default Role)*
- **Role Designer**: Role creation, system evolution

### Legal Expertise
- **Supreme Court Specialist**: Primary legal analysis, case research
- **Data Specialist**: Legal data processing, evidence compilation

### Software Engineering
- **System Architect**: Technical foundation, system design
- **Staff Engineer**: Technical leadership, code quality
- **Full-Stack Engineer**: Implementation, feature development

*See `corporate policy/role-reference-guide.md` for complete organizational chart and usage guidelines.*

## Current System Architecture

```
ClaudeScotus/
├── roles/                    # Role-based prompt system
│   ├── BaseEmployee.md       # Foundation template (inheritance)
│   ├── ProductManager.md     # Default role
│   ├── LawPartner.md        # Strategic authority
│   ├── SupremeCourtSpecialist.md  # Legal analysis
│   └── [6 other specialized roles]
├── corporate policy/         # Governance and protocols
│   ├── role-reference-guide.md    # Org chart & usage guide
│   ├── meeting-protocols.md       # Efficiency standards
│   └── session-winddown-procedure.md
└── claude sessions/         # Session documentation & continuity
```

## Methodology

### Text-Based System Design
- **No databases**: Simple file-based organization
- **Prompt engineering**: Iterative role refinement and optimization  
- **Git workflows**: Version control for roles, analysis, and documentation
- **Session continuity**: Complete documentation for context preservation

### Prediction Workflow
1. **Case Intake**: Supreme Court Specialist analyzes legal materials
2. **Justice Modeling**: Individual Justice prediction analysis
3. **Confidence Scoring**: Systematic uncertainty quantification
4. **Strategic Synthesis**: Law Partner creates executive briefings
5. **Validation**: Historical case testing and accuracy measurement

## Goals & Success Metrics

### Primary Objectives
- **80% prediction accuracy** with proper confidence calibration
- **Fortune 500 utility** - actionable intelligence for corporate legal teams
- **System maintainability** - sustainable role-based architecture

### Quality Standards
- **Professional output**: Law firm partner-quality briefings
- **Transparent uncertainty**: Clear confidence intervals and limitations
- **Iterative improvement**: Learning from each case analysis

## Getting Started

### For New Users
1. **Start with Product Manager role** (auto-loads by default)
2. **Review role reference guide**: `corporate policy/role-reference-guide.md`
3. **Check recent sessions**: `claude sessions/` for current context
4. **Follow meeting protocols**: Efficient consultation and decision-making

### For Case Analysis
1. **Activate Supreme Court Specialist** for legal research and analysis
2. **Use Law Partner** for strategic synthesis and client deliverables
3. **Consult System Architect** for technical workflow optimization
4. **Reference role guide** for optimal role selection patterns

## Development Philosophy

- **Efficiency over perfection** - Ship working predictions, iterate based on results
- **Role specialization** - Clear expertise boundaries with systematic consultation
- **User-centered design** - Optimize for Fortune 500 general counsel decision-making
- **Systematic learning** - Document patterns, failures, and improvements

## Three-Arc Roadmap

| Phase | Status | Focus | Key Deliverables | Success Metrics |
|-------|--------|-------|------------------|------------------|
| **Arc 1: Infrastructure** | ✅ Complete | Role ecosystem & governance | 9 specialized roles, BaseEmployee inheritance, issue tracking, memory systems | 100% role compliance, systematic documentation |
| **Arc 2: MVP Validation** | 🎯 In Progress | Case analysis workflow testing | Historical prediction validation, confidence calibration, client deliverable format | 80% accuracy on test cases, Fortune 500 utility validation |
| **Arc 3: Production Scale** | 📋 Planned | Legal data pipeline & optimization | Automated case intake, Justice-specific modeling, prediction accuracy improvement | <5-day cycle time, systematic client feedback integration |

## Session Wind-down & Fast-Resume Protocol

### Wind-down Procedure
When approaching token limits or ending a session, execute the `WIND_DOWN` macro:

**Required Wind-down Summary Contents:**
- **Objectives**: ✅ Completed / ❌ Incomplete / 🔄 Partial
- **Issues Created/Closed**: Reference all ISS-### tickets
- **Next-step Tickets**: Priority assignments for continuation
- **Memory Paths**: Role memories updated with key decisions/lessons
- **Context Handoff**: Critical information for fast resume
- **GitHub Push**: Push all commits to remote repository

**Storage Locations:**
- Primary: `claude sessions/YYYY-MM-DD_HHMM_wind_down.md`
- Role-specific: `memory/<role>/lessons/YYYY-MM-DD_session_lessons.md`
- Issues: Update status and create follow-up tickets as needed

### Fast-Resume Procedure
To reopen the project efficiently:

1. **Load Last Wind-down**: Read most recent `claude sessions/*_wind_down.md`
2. **Check Open Issues**: Review `/issues/` for assigned P0/P1 tickets
3. **Role Context**: Check relevant `memory/<role>/` for recent decisions
4. **Set Session Focus**: Use CLAUDE.md startup routine for work prioritization

**Resume Checklist:**
- [ ] Last wind-down summary reviewed
- [ ] Open P0/P1 issues identified
- [ ] Role memories scanned for context
- [ ] Session focus selected (issues/specific/coordination)
- [ ] Work prioritization established

---

## Quick Reference

**Need help with role selection?** → `corporate policy/role-reference-guide.md`  
**Want to start case analysis?** → Activate Supreme Court Specialist  
**Planning project work?** → Product Manager (auto-loads)  
**Technical questions?** → System Architect or Staff Engineer  
**Strategic decisions?** → Law Partner + Finance Controller  
**Session management?** → Use `WIND_DOWN` and `RESUME` macros in CLAUDE.md

*Built with Claude Code, GitHub, and systematic prompt engineering*