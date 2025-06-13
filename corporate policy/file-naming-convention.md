# ClaudeScotus File Naming Convention

**Version**: 1.0  
**Scope**: SCOTUS prediction system files and session documentation  
**Authority**: System Architect + Data Specialist + Staff Engineer

---

## Standard File Naming Pattern

### Primary Convention: `YYYY-MM-DD_descriptive-name-with-hyphens.extension`

**Examples**:
- `2025-06-11_baseemployee-architecture-implementation.md`
- `2025-06-11_supreme-court-prediction-methodology.md`
- `2025-06-11_scotus-case-analysis-workflow.md`

### Date Format: ISO 8601 (YYYY-MM-DD)
- **Rationale**: Ensures chronological sorting in all file systems
- **Consistency**: Works across operating systems and tools
- **Searchability**: Easy to filter by date ranges

### Separator: Underscore after date, hyphens within description
- **Date Separator**: `_` (underscore) separates date from description
- **Word Separator**: `-` (hyphen) separates words within description
- **Rationale**: Clear visual distinction between date and content description

### Description Requirements:
- **Length**: 3-8 words maximum for readability
- **Content**: Describes primary purpose or topic, not generic terms
- **Style**: Lowercase with hyphens (kebab-case)
- **Specificity**: Specific enough to distinguish from similar files

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

### ❌ Generic or Vague Names
- `document.md` (what document?)
- `update.md` (update to what?)
- `notes.md` (notes about what?)
- `final.md` (final version of what?)

### ❌ Version Numbers in Filenames
- `requirements-v2.md` (use git for versioning)
- `design-final-final.md` (git handles versions)
- `document-revised.md` (git shows revision history)

### ❌ Inconsistent Date Formats
- `06-11-2025_document.md` (wrong date format)
- `2025_06_11_document.md` (wrong separators)
- `11-06-2025_document.md` (ambiguous month/day)

### ❌ Special Characters or Spaces
- `document (updated).md` (spaces and parentheses)
- `document&update.md` (special characters)
- `document file.md` (spaces cause command line issues)

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
- [ ] Date in YYYY-MM-DD format
- [ ] Underscore separating date from description
- [ ] Hyphens separating words in description
- [ ] 3-8 words describing SCOTUS prediction content
- [ ] Lowercase throughout description
- [ ] No spaces or special characters
- [ ] Clear distinction from existing prediction files

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