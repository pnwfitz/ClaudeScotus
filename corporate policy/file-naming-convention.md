# ClaudeScotus File Naming Convention

![Version](https://img.shields.io/badge/Version-1.0-blue) ![Scope](https://img.shields.io/badge/Scope-SCOTUS%20System-green) ![Authority](https://img.shields.io/badge/Authority-Technical%20Team-orange)

**Version**: 1.0  
**Scope**: SCOTUS prediction system files and session documentation  
**Authority**: System Architect + Data Specialist + Staff Engineer

## 📋 Table of Contents

<details>
<summary>Naming Standards</summary>

- [Standard File Naming Pattern](#standard-file-naming-pattern)
- [Category-Specific Conventions](#category-specific-conventions)
- [Anti-Patterns to Avoid](#anti-patterns-to-avoid)

</details>

<details>
<summary>Implementation & Tools</summary>

- [Tools and Automation](#tools-and-automation)
- [Implementation Guidelines](#implementation-guidelines)
- [Quality Standards](#quality-standards)

</details>

<details>
<summary>Maintenance & Evolution</summary>

- [Evolution and Maintenance](#evolution-and-maintenance)

</details>

---

## Standard File Naming Pattern

### Primary Convention: `YYYY-MM-DD_descriptive-name-with-hyphens.extension`

| Component | Format | Example | Purpose |
|-----------|--------|---------|----------|
| **Date** | YYYY-MM-DD | 2025-06-11 | Chronological sorting |
| **Separator** | _ | _ | Date/description separation |
| **Description** | kebab-case | baseemployee-architecture-implementation | Human-readable content |
| **Extension** | .md/.json/.yaml | .md | File type identification |

**Examples**:
```bash
2025-06-11_baseemployee-architecture-implementation.md
2025-06-11_supreme-court-prediction-methodology.md
2025-06-11_scotus-case-analysis-workflow.md
```

### Format Specifications

| Specification | Standard | Rationale | Benefits |
|---------------|----------|-----------|----------|
| **Date Format** | ISO 8601 (YYYY-MM-DD) | Universal standard | Chronological sorting, cross-platform compatibility |
| **Date Separator** | `_` (underscore) | Visual distinction | Clear separation between date and description |
| **Word Separator** | `-` (hyphen) | kebab-case standard | URL-safe, command-line friendly |
| **Description Length** | 3-8 words maximum | Readability | Balance between detail and brevity |
| **Case Style** | lowercase | Consistency | Prevents case-sensitivity issues |
| **Specificity** | Descriptive, not generic | Searchability | Easy file identification and discovery |

### Requirements Checklist

- [ ] **Date in YYYY-MM-DD format**
- [ ] **Underscore after date**
- [ ] **Hyphens between words in description**
- [ ] **3-8 words in description**
- [ ] **Lowercase throughout**
- [ ] **No spaces or special characters**
- [ ] **Descriptive, not generic content**

---

## Category-Specific Conventions

### Memory Files
**Pattern**: `YYYY-MM-DD_memory-type-specific-description.md`

**Examples**:
- `2025-06-11_baseemployee-architecture-decision.md`
- `2025-06-11_ceo-interaction-protocol-pattern.md`
- `2025-06-11_over-consultation-lesson-learned.md`

### Documentation Files
**Pattern**: `YYYY-MM-DD_document-type-and-purpose.md`

**Examples**:
- `2025-06-11_role-reference-guide-creation.md`
- `2025-06-11_session-winddown-procedure-implementation.md`
- `2025-06-11_corporate-memory-architecture-specification.md`

### Analysis Files
**Pattern**: `YYYY-MM-DD_case-name-or-analysis-type.md`

**Examples**:
- `2025-06-11_dobbs-v-jackson-prediction-analysis.md`
- `2025-06-11_justice-thomas-voting-pattern-analysis.md`
- `2025-06-11_scotus-term-2024-prediction-methodology.md`

### Session Files
**Pattern**: `YYYY-MM-DD_HHMM_session-type-description.md`

**Examples**:
- `2025-06-11_1400_role-architecture-optimization.md`
- `2025-06-11_0900_scotus-case-analysis-workflow.md`
- `2025-06-11_1600_prediction-accuracy-validation.md`

---

## Anti-Patterns to Avoid

| Anti-Pattern | Bad Example | Why It's Bad | Correct Approach |
|--------------|-------------|--------------|------------------|
| **Generic Names** | `document.md` | No context about purpose | `2025-06-11_scotus-prediction-methodology.md` |
| **Generic Names** | `update.md` | No indication of what's updated | `2025-06-11_baseemployee-architecture-update.md` |
| **Generic Names** | `notes.md` | Too vague for team use | `2025-06-11_session-planning-notes.md` |
| **Generic Names** | `final.md` | No content description | `2025-06-11_case-analysis-final-report.md` |
| **Version Numbers** | `requirements-v2.md` | Git handles versioning | `2025-06-11_scotus-requirements-update.md` |
| **Version Numbers** | `design-final-final.md` | Version confusion | `2025-06-11_system-design-specification.md` |
| **Version Numbers** | `document-revised.md` | Git shows history | `2025-06-11_role-guide-revision.md` |
| **Wrong Date Format** | `06-11-2025_document.md` | Non-ISO date format | `2025-06-11_document-description.md` |
| **Wrong Date Format** | `2025_06_11_document.md` | Wrong separators | `2025-06-11_document-description.md` |
| **Wrong Date Format** | `11-06-2025_document.md` | Ambiguous month/day | `2025-06-11_document-description.md` |
| **Special Characters** | `document (updated).md` | Spaces and parentheses | `2025-06-11_document-updated.md` |
| **Special Characters** | `document&update.md` | Special characters | `2025-06-11_document-update.md` |
| **Special Characters** | `document file.md` | Spaces break commands | `2025-06-11_document-file.md` |

### Common Mistakes Prevention

<details>
<summary>Click to expand mistake prevention guide</summary>

- [ ] **Avoid generic terms**: document, file, notes, update, final
- [ ] **No version numbers**: Use git for version control
- [ ] **Consistent date format**: Always YYYY-MM-DD
- [ ] **No special characters**: Stick to alphanumeric, hyphens, underscores
- [ ] **No spaces**: Use hyphens instead
- [ ] **Descriptive content**: Name should explain purpose

</details>

---

## Tools and Automation

### Git Integration
- **Commit Messages**: Reference prediction work and accuracy improvements
- **Branch Names**: Follow same convention for SCOTUS analysis work
- **Tag Names**: Use YYYY-MM-DD for prediction milestone releases

### Search and Discovery
- **Date Patterns**: `grep "2025-06-11" *.md` finds files from specific session date
- **Case Search**: Easy filtering by case names and analysis types
- **Prediction Search**: Descriptive names improve SCOTUS analysis discovery

### Claude Code Compatibility
- **File Operations**: Tab-completion works efficiently with this convention
- **Command Line**: No spaces or special characters requiring escaping
- **Git Integration**: Consistent naming supports effective version control

---

## Implementation Guidelines

### For New Files
1. **Start with date**: Always use YYYY-MM-DD format
2. **Add underscore**: Separate date from description with `_`
3. **Describe purpose**: 3-8 words explaining what this file contains
4. **Use hyphens**: Separate words with `-` in description
5. **Check uniqueness**: Ensure name distinguishes from existing files

### For Existing Files
1. **Session-Based Updates**: Rename files when updating for prediction accuracy
2. **Reference Updates**: Update documentation referencing old file names
3. **Git History**: Use `git mv` to preserve file history during renames
4. **Context Preservation**: Maintain session continuity during file updates

### For Directories
- **Descriptive names**: `memory/`, `data/`, `claude sessions/`, `issues/`
- **No dates in directories**: Directories contain multiple dated files
- **SCOTUS structure**: Follow prediction system organization patterns

---

## Quality Standards

### File Name Review Checklist

| Criteria | Requirement | Status | Notes |
|----------|-------------|--------|---------|
| **Date Format** | YYYY-MM-DD format | ☐ | Must use ISO 8601 standard |
| **Date Separator** | Underscore after date | ☐ | `_` separates date from description |
| **Word Separators** | Hyphens in description | ☐ | `-` separates words (kebab-case) |
| **Description Length** | 3-8 words describing content | ☐ | Balance detail and brevity |
| **Case Style** | Lowercase throughout | ☐ | Prevents case-sensitivity issues |
| **Character Safety** | No spaces or special characters | ☐ | Command-line and URL safe |
| **Uniqueness** | Distinct from existing files | ☐ | Clear identification |
| **Content Description** | SCOTUS prediction relevance | ☐ | Purpose should be obvious |

### Quick Validation

- [ ] **Date in YYYY-MM-DD format**
- [ ] **Underscore separating date from description**
- [ ] **Hyphens separating words in description**
- [ ] **3-8 words describing SCOTUS prediction content**
- [ ] **Lowercase throughout description**
- [ ] **No spaces or special characters**
- [ ] **Clear distinction from existing prediction files**

### Exceptions and Special Cases
- **README.md**: Standard convention, no date prefix needed
- **LICENSE**: Standard convention, no date prefix needed
- **CLAUDE.md**: Configuration file, no date prefix needed
- **Role files**: Template files (BaseEmployee.md, etc.), no date prefix needed
- **System files**: Configuration and template files maintain standard names

---

## Evolution and Maintenance

### Review Process
- **Session-Based**: Review convention effectiveness during session optimization
- **Prediction Focus**: Adapt for SCOTUS analysis needs while maintaining core pattern
- **Claude Code Integration**: Update convention based on workflow efficiency

### Success Metrics
- **File Discovery Time**: Session efficiency for locating prediction files
- **Naming Consistency**: Percentage of SCOTUS files following convention
- **Search Effectiveness**: Quality of case analysis and prediction file discovery
- **Session Continuity**: Ease of understanding context from file names alone

---

**Document Focus**:
- **Owners**: System Architect (structure), Data Specialist (organization), Staff Engineer (standards)
- **Context**: Product Manager (workflow), Finance Controller (efficiency)
- **Implementation**: All roles follow convention for SCOTUS prediction files
- **Quality**: Session review and git commit standards

*This convention creates systematic organization for SCOTUS prediction development and improves session efficiency through consistent, discoverable naming patterns.*