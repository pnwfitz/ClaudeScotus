# ClaudeScotus
**Supreme Court Prediction System**

An experimental system to predict Supreme Court decisions using LLM-based analysis and role-based prompt engineering.

## 📋 Table of Contents

| Quick Navigation | Documentation | Workflows |
|-----------------|---------------|-----------|
| [🚀 Getting Started](#-getting-started) | [📊 Current Status](#-project-status) | [⚖️ Case Analysis](#for-case-analysis) |
| [🏗️ Architecture](#-role-based-architecture) | [📁 File Structure](#current-system-architecture) | [🔄 Session Management](#session-wind-down--fast-resume-protocol) |
| [🎯 Goals & Metrics](#-goals--success-metrics) | [🔧 Configuration](#claude-code-configuration) | [📖 Role Reference](#quick-reference) |

---

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

## 📊 Project Status

| Component | Status | Progress | Next Steps |
|-----------|--------|----------|------------|
| **🏗️ Architecture** | ✅ Complete | Role-based system with BaseEmployee.md inheritance | [Begin Arc 2 validation](#three-arc-roadmap) |
| **👥 Role Ecosystem** | ✅ Complete | 9 specialized roles with org reference guide | [Human name assignments](issues/2025-06-11_ISS-014_human-name-assignment-rollout.md) |
| **🔄 Current Phase** | 🎯 Active | Case analysis workflow testing | [SCOTUS prediction validation](#for-case-analysis) |

**🎯 Focus:** Arc 2 - MVP Validation → 80% prediction accuracy target

## 🏗️ Role-Based Architecture

| Role Category | Role | Primary Function | Quick Activate |
|---------------|------|------------------|----------------|
| **👥 Leadership** | [Law Partner](roles/LawPartner.md) | Strategic authority, client deliverables | Supreme Court decisions |
|  | [Finance Controller](roles/FinanceController.md) | Budget management, efficiency oversight | Cost optimization |
| **📋 Coordination** | [Product Manager](roles/ProductManager.md) | Project orchestration *(Default)* | Project planning |
|  | [Role Designer](roles/RoleDesign.md) | System evolution, Maya Chen | Role improvements |
| **⚖️ Legal** | [Supreme Court Specialist](roles/SupremeCourtSpecialist.md) | Primary legal analysis | Case analysis |
|  | [Data Specialist](roles/DataSpecialist.md) | Legal data processing | CourtListener API |
| **💻 Engineering** | [System Architect](roles/SystemArchitect.md) | Technical foundation | Architecture decisions |
|  | [Staff Engineer](roles/StaffEngineer.md) | Code quality, leadership | Code reviews |
|  | [Full-Stack Engineer](roles/FullStackEngineer.md) | Implementation | Feature development |

**📖 Complete Guide:** [`corporate policy/role-reference-guide.md`](corporate%20policy/2025-06-11_role-reference-guide-organizational-chart.md)

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

## 🚀 Getting Started

### For New Users
| Step | Action | Quick Link |
|------|--------|------------|
| **1** | Start with Product Manager role *(auto-loads)* | [CLAUDE.md startup routine](CLAUDE.md#crisp-session-startup-routine) |
| **2** | Review role reference guide | [`role-reference-guide.md`](corporate%20policy/2025-06-11_role-reference-guide-organizational-chart.md) |
| **3** | Check recent sessions for context | [`claude sessions/`](claude%20sessions/) |
| **4** | Follow meeting protocols | [Efficiency standards](corporate%20policy/2025-06-10_meeting-protocols-and-efficiency-standards.md) |

### For Case Analysis
| Workflow | Role | Purpose | Quick Start |
|----------|------|---------|-------------|
| **🔍 Legal Research** | [Supreme Court Specialist](roles/SupremeCourtSpecialist.md) | Case analysis, precedent mapping | CourtListener case intake |
| **📊 Strategic Synthesis** | [Law Partner](roles/LawPartner.md) | Client deliverables, Fortune 500 briefings | Executive recommendations |
| **⚙️ Technical Optimization** | [System Architect](roles/SystemArchitect.md) | Workflow automation | Pipeline improvements |
| **📋 Coordination** | [Product Manager](roles/ProductManager.md) | Multi-role orchestration | Session planning |

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