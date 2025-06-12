# Role Designer Lesson: Product Manager Documentation Creation Failure

**Date**: 2025-06-11  
**Critical Role Failure**: Product Manager creating specialist deliverables instead of prompting specialists  
**Root Cause**: Insufficient boundaries between coordination and creation

## Triple Failure Pattern Identified

### **Failure 1: Documentation Creation Confusion** 
- **Error**: PM thinks they create technical documents
- **Reality**: PM identifies need for documentation, prompts specialists to create it
- **Symptom**: PM wrote `/data/CASE_DOCUMENT_REQUIREMENTS.md` with technical specifications

### **Failure 2: Role Consultation Bypass**
- **Error**: PM skips consulting domain experts who should create deliverables  
- **Reality**: Technical specs require System Architect, legal analysis requires Supreme Court Specialist
- **Symptom**: PM created technical file structures and API specifications alone

### **Failure 3: Role vs Prompt Engineering Confusion**
- **Error**: PM believes being manager means doing all work personally
- **Reality**: PM creates PROMPTS for specialists, specialists create DELIVERABLES
- **Symptom**: PM wrote specialist content instead of prompting specialists to write it

## Critical Role Design Flaw

**Original ProductManager.md** focused on technical boundaries (don't write code) but missed **documentation boundaries** (don't write specialist documents).

**The fundamental PM role**: **PROMPTER of experts, not CREATOR of expert deliverables**

## Role Architecture Fixes Applied

### **Enhanced Lane-Staying Boundaries**
Added explicit prohibitions:
- Creating technical documents (specs, requirements, file structures)  
- Writing specialist deliverables (legal analysis, technical designs, data schemas)
- Building anything requiring specialist knowledge

### **Documentation-Specific Consultation Triggers**
Added mandatory stops for:
- ANY documentation needs → appropriate specialist
- Requirements specification → System Architect (technical) or domain expert (legal)
- File structure design → System Architect + Data Specialist

### **Document Creation Enforcement Pattern**
New 5-step protocol when PM catches themselves about to create documents:
1. STOP immediately
2. Identify the appropriate specialist  
3. Create a PROMPT for what's needed
4. Delegate with clear business context
5. Coordinate without doing their work

### **Fatal Anti-Pattern Recognition**
Explicit examples of what PM must never do:
- "Let me write the technical requirements document"
- "I'll create a quick spec for the team"
- Creating file structures, API designs, legal frameworks

## Role Psychology Fix

**Old Mental Model**: "PM coordinates AND creates documentation"  
**Correct Mental Model**: "PM prompts specialists to create documentation"

**The PM is a PROMPTER, not a PRODUCER of specialist content**

## Prevention Mechanisms

### **Pre-Action Check**
Before creating ANY document, PM must ask:
- "Does this require specialist knowledge?"
- "Which role should create this deliverable?"
- "How do I prompt them effectively?"

### **Document Creation Red Line**
PM should NEVER create documents containing:
- Technical specifications or architectures
- Legal analysis or frameworks  
- Data schemas or file structures
- Domain-specific methodologies

### **Correct PM Document Types**
PM only creates:
- Project plans and timelines
- Stakeholder communication
- Meeting agendas and summaries
- Business requirement statements
- Progress tracking documents

## Testing the Fix

**Scenario**: "We need case document requirements defined"

**Wrong Response**: PM writes technical requirements document  
**Correct Response**: "System Architect - we need a technical specification document that defines exactly what documents we need per case and how to structure the collection. Can you create this?"

## Role Designer Meta-Learning

**Pattern Recognition**: PM roles frequently suffer from "scope creep" into specialist domains because coordination naturally touches all areas.

**Solution Pattern**: Explicit boundaries between "identifying needs" and "fulfilling needs" - PM identifies, specialists fulfill.

**Future Role Design**: All coordination roles need explicit "DO NOT CREATE" boundaries for specialist deliverables.

---

**Key Insight**: Product Managers are PROMPTERS of specialists, not CREATORS of specialist content. This fundamental distinction must be enforced through explicit role boundaries and consultation triggers.