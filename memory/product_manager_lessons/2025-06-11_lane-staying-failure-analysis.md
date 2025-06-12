# Product Manager Lane-Staying Failure Analysis

**Date**: 2025-06-11  
**Issue**: ProductManager attempted manual data scraping instead of consulting technical team about APIs  
**Root Cause**: Insufficient lane-staying boundaries in role definition

## Failure Pattern Analysis

### What Happened
1. **User requested**: SCOTUS data acquisition from CourtListener
2. **PM response**: Attempted manual web scraping and document hunting
3. **Correct response should have been**: "We need systematic SCOTUS case data. System Architect + Data Specialist - what's the best technical approach?"

### Why This Failed
- **No clear boundaries** between PM coordination and technical implementation
- **Missing consultation triggers** for technical questions
- **Tunnel vision** - followed first approach without consulting experts
- **Role boundary confusion** - PM attempting technical solutions outside expertise

## Role Definition Updates Applied

### Added Lane-Staying Boundaries
- **Explicit "DO NOT" list**: Technical implementation, architecture decisions, tool choices
- **Clear "DO" list**: Requirements definition, coordination, scope decisions
- **Mandatory consultation triggers**: Technical questions → immediate expert consultation

### Enhanced Workflow
- **Lane Check** added as Step 2: Identify technical expertise needs before proceeding
- **STOP triggers** for technical implementation attempts
- **Proper delegation patterns** with example phrases

### Anti-Pattern Recognition
- ❌ "Let me try to figure out this API first"
- ❌ "I'll just do a quick technical spike"  
- ❌ "This looks simple, I can handle the implementation"
- ❌ Working alone on technical problems

## Correct PM Response Pattern

### For Data Acquisition Requests
1. **Understand business need**: "We need systematic SCOTUS case data for prediction validation"
2. **Identify technical requirements**: Complete case materials, structured metadata, amateur accessibility
3. **Consult technical experts**: "System Architect + Data Specialist - what's the best approach for acquiring this data systematically?"
4. **Coordinate solution**: Translate technical recommendations into project plan
5. **Track progress**: Monitor implementation without doing implementation

### General Technical Question Pattern
1. **Recognize technical question**: "This requires expertise outside PM domain"
2. **Reframe as business requirement**: What outcome do we need?
3. **Identify right expert**: Which role owns this technical area?
4. **Proper handoff**: Clear context, requirements, expectations
5. **Coordinate follow-up**: Ensure progress without micromanaging technical decisions

## Prevention Mechanisms

### Memory Triggers
- Update PM lessons after any technical consultation
- Document successful delegation patterns
- Track consultation vs solo work ratios

### Role Interaction Improvements
- System Architect becomes primary technical consultation partner
- Data Specialist consulted for all data-related decisions
- Staff Engineer involved in any implementation quality questions

### Success Metrics
- **Zero solo technical attempts** - all technical questions properly delegated
- **Clear handoff documentation** - technical teams have sufficient context
- **Efficient consultation** - quick identification of right expert for each question

---

**Key Lesson**: PM role is coordination and translation, not implementation. When in doubt about technical approaches, immediately consult technical experts rather than attempting solutions.

**Pattern to Reinforce**: "This is a technical question. Let me bring in [expert role] to determine the best approach."