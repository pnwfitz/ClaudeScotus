# Corporate File Naming Convention

**Version**: 1.0  
**Effective Date**: 2025-06-11  
**Scope**: All ClaudeScotus files and future corporate projects  
**Authority**: System Architect + Data Specialist + Staff Engineer consensus

---

## Standard File Naming Pattern

### Primary Convention: `YYYY-MM-DD_descriptive-name-with-hyphens.extension`

**Examples**:
- `2025-06-11_baseemployee-architecture-implementation.md`
- `2025-06-11_supreme-court-prediction-methodology.md`
- `2025-06-11_fortune-500-client-briefing-template.md`

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
- `2025-06-11_justice-thomas-constitutional-framework.md`
- `2025-06-11_supreme-court-term-2024-methodology.md`

### Session Files
**Pattern**: `YYYY-MM-DD_HHMM_session-type-description.md`

**Examples**:
- `2025-06-11_1400_role-architecture-optimization.md`
- `2025-06-11_0900_case-analysis-workflow-testing.md`
- `2025-06-11_1600_strategic-planning-session.md`

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
- **Commit Messages**: Should reference primary file being changed
- **Branch Names**: Follow same convention when branch represents specific work
- **Tag Names**: Use YYYY-MM-DD for release/milestone tags

### Search and Discovery
- **Grep Patterns**: `grep "2025-06-11" *.md` finds all files from specific date
- **Date Range Search**: Easy filtering by date prefixes
- **Content Search**: Descriptive names improve search relevance

### Cross-Platform Compatibility
- **Windows/Mac/Linux**: All systems sort identically with this convention
- **Command Line**: No spaces or special characters that require escaping
- **Web Systems**: URLs and links work consistently

---

## Implementation Guidelines

### For New Files
1. **Start with date**: Always use YYYY-MM-DD format
2. **Add underscore**: Separate date from description with `_`
3. **Describe purpose**: 3-8 words explaining what this file contains
4. **Use hyphens**: Separate words with `-` in description
5. **Check uniqueness**: Ensure name distinguishes from existing files

### For Existing Files
1. **Gradual Migration**: Rename files when substantially updating content
2. **Maintain References**: Update any documentation that references old names
3. **Git History**: Use `git mv` to preserve file history during renames
4. **Communication**: Notify team of renames that affect shared workflows

### For Directories
- **Use descriptive names**: `memory/`, `corporate policy/`, `claude sessions/`
- **Avoid dates in directory names**: Directories contain multiple dated files
- **Consistent structure**: Follow established patterns for new directories

---

## Quality Standards

### File Name Review Checklist
- [ ] Date in YYYY-MM-DD format
- [ ] Underscore separating date from description
- [ ] Hyphens separating words in description
- [ ] 3-8 words describing content purpose
- [ ] Lowercase throughout description
- [ ] No spaces or special characters
- [ ] Distinguishable from existing files

### Exceptions and Special Cases
- **README.md**: Standard convention, no date prefix needed
- **LICENSE**: Standard convention, no date prefix needed
- **CLAUDE.md**: Configuration file, no date prefix needed
- **BaseEmployee.md**: Template file, no date prefix needed
- **BaseMemory.md**: Template file, no date prefix needed

---

## Evolution and Maintenance

### Review Process
- **Quarterly**: Review convention effectiveness and usage patterns
- **Project Basis**: Adapt for project-specific needs while maintaining core pattern
- **Tool Integration**: Update convention based on tool capabilities and requirements

### Success Metrics
- **File Discovery Time**: How quickly team members locate relevant files
- **Naming Consistency**: Percentage of files following convention
- **Search Effectiveness**: Quality of search results using naming patterns
- **Cross-Project Reuse**: Ease of understanding files from other projects

---

**Document Control**:
- **Owners**: System Architect (technical structure), Data Specialist (information architecture), Staff Engineer (quality standards)
- **Approvers**: Product Manager (workflow integration), Finance Controller (efficiency impact)
- **Implementation**: All roles must follow convention for new files
- **Enforcement**: Code review and documentation review processes

*This convention creates systematic file organization that scales across corporate projects and improves team efficiency through consistent, discoverable naming patterns.*