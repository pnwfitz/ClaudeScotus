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

## Repository Evolution

### Infrastructure Phase (Complete)
- ✅ Role ecosystem creation and optimization
- ✅ BaseEmployee.md inheritance architecture  
- ✅ Organizational governance and protocols
- ✅ Session continuity and documentation systems

### Current Phase (In Progress)
- 🎯 Case analysis workflow testing
- 🎯 Historical case prediction validation
- 🎯 Confidence calibration and accuracy measurement

### Future Phases
- Legal data pipeline automation
- Justice-specific modeling refinement
- Client deliverable format optimization
- Prediction accuracy improvement iteration

---

## Quick Reference

**Need help with role selection?** → `corporate policy/role-reference-guide.md`  
**Want to start case analysis?** → Activate Supreme Court Specialist  
**Planning project work?** → Product Manager (auto-loads)  
**Technical questions?** → System Architect or Staff Engineer  
**Strategic decisions?** → Law Partner + Finance Controller

*Built with Claude Code, GitHub, and systematic prompt engineering*