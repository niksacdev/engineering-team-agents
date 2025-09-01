# Cursor IDE Enterprise Engineering Rules

Transform Cursor IDE into an **enterprise-grade development environment** with collaborative engineering practices that ensure reliable, maintainable, and business-aligned code.

## 🎯 What You Get: Context-Aware Enterprise Guidance

Cursor automatically applies **specialized engineering rules** based on the files you're editing:
- **Business-first development**: Always ask "what user need does this serve?"
- **Quality gates**: Security, accessibility, performance validation at every step
- **Documentation-first**: Create persistent knowledge that lives with your code
- **Enterprise patterns**: SOLID principles, domain-driven design, microservices best practices
- **Collaboration workflows**: Multi-agent patterns for complex decisions

## 🚀 Quick Setup

1. **Install enterprise engineering rules:**
   ```bash
   cp -r engineering-team-agents/.cursor ./
   ```

2. **Initialize context-aware engineering system:**
   
   **⚠️ Important**: Use **Composer mode** or enable file editing permissions
   
   Open Cursor IDE chat and run this enterprise initialization:
   
   ```
   🏗️ INITIALIZE ENTERPRISE ENGINEERING ENVIRONMENT
   
   I've installed context-aware engineering rules that automatically guide development based on enterprise best practices. Please customize these rules to become domain experts for my specific project.
   
   **Enterprise Mission**: Ensure every line of code serves user needs, follows security best practices, maintains high quality, and integrates seamlessly with business objectives.
   
   **Customization Tasks:**
   1. **Domain Analysis**: Understand my business domain, user personas, and success metrics
   2. **Tech Stack Integration**: Customize rules for my specific frameworks and tools
   3. **Quality Standards**: Align rules with my team's definition of done and quality gates
   4. **Documentation Setup**: Create `docs/` folder structure for persistent knowledge
   5. **Enterprise Patterns**: Apply appropriate patterns based on project complexity
   
   **My Project Context**: [Provide detailed context]
   Example: "Healthcare appointment scheduling SaaS serving 500+ medical practices. React/TypeScript frontend, Node.js/PostgreSQL backend, HIPAA compliance required, focus on accessibility and offline capabilities."
   
   **Expected Outcome**: Context-aware rules that automatically enforce enterprise standards and collaborative workflows while I code.
   ```

3. **Experience context-aware enterprise guidance:**
   
   **Cursor automatically applies specialized rules** as you work:
   
   ```
   # Open any source file → Enterprise standards active
   → Business-first questions: "What user need does this solve?"
   → Quality gates: Security, performance, accessibility checks
   → Documentation prompts: "Create ADR for this architecture decision"
   
   # Open API/service files → Enhanced security rules
   → Input validation, authentication, rate limiting guidance
   → Microservices patterns and distributed system best practices
   
   # Open UI component files → UX/accessibility rules  
   → WCAG compliance, responsive design, user journey validation
   → Accessibility testing with diverse user scenarios
   
   # Open test files → Enterprise testing standards
   → Test pyramid guidance, quality gates, business validation
   ```

## 🏗️ Enterprise Engineering Rules System

### Context-Aware Rule Activation
**Cursor intelligently applies rules** based on what you're working on:

- **Business Context Rules** (always active): User-first development, business value validation
- **Security Rules** (API/service files): Authentication, input validation, compliance
- **UX Rules** (component files): Accessibility, user experience, inclusive design  
- **Architecture Rules** (system files): Scalability, maintainability, enterprise patterns
- **Quality Rules** (all files): Code review standards, testing requirements, documentation

### Enterprise Rule Structure
```
.cursor/rules/
├── enterprise-standards.mdc    # Always active: business-first development
├── security-compliance.mdc     # API/service files: security standards
├── ux-accessibility.mdc        # UI components: inclusive design  
├── architecture-patterns.mdc   # System design: enterprise patterns
└── quality-gates.mdc          # Testing/review: quality standards
```

### Intelligent File Pattern Matching
Rules activate based on **semantic file patterns**:
```yaml
---
description: "Enterprise security standards for API development"
globs:
  - "**/api/**/*"         # API routes and handlers
  - "**/services/**/*"    # Business logic services
  - "**/auth/**/*"        # Authentication systems
  - "**/middleware/**/*"  # Request processing
---
```

## 🎯 Enterprise Rule Specializations

### enterprise-standards.mdc 🏢
**Active**: Always (all files)
**Focus**: Business-first development, user value validation  
**Enforces**: 
- "What user need does this code serve?" questioning
- Business value before technical implementation
- Documentation-first development practices
- Cross-functional collaboration patterns

### security-compliance.mdc 🔒  
**Active**: API routes, services, authentication, middleware
**Focus**: Enterprise security standards and compliance
**Enforces**:
- Input validation and sanitization
- Authentication and authorization patterns  
- Rate limiting and DOS protection
- Secrets management and compliance (GDPR, HIPAA, SOC2)

### ux-accessibility.mdc 🌍
**Active**: UI components, forms, user interfaces  
**Focus**: Inclusive design and accessibility compliance
**Enforces**:
- WCAG 2.1 AA compliance standards
- Keyboard navigation and screen reader support
- Responsive design and mobile-first approach
- User journey validation and usability testing

### architecture-patterns.mdc 🏗️
**Active**: System design files, configuration, infrastructure
**Focus**: Scalable, maintainable enterprise architecture
**Enforces**:
- Domain-driven design patterns
- Microservices best practices
- SOLID principles and clean architecture
- Performance optimization and monitoring

### quality-gates.mdc ✅
**Active**: All code files, especially tests and reviews
**Focus**: Quality assurance and continuous improvement  
**Enforces**:
- Test-driven development practices
- Code review standards and security checks
- Performance benchmarking and optimization
- Documentation and knowledge sharing

## 📁 Semantic File Pattern Recognition

### Enterprise Stack Patterns

**Full-Stack TypeScript/React:**
```yaml
# UI Components & User Experience  
- "**/components/**/*.{tsx,jsx}"
- "**/pages/**/*.{tsx,jsx}"
- "**/ui/**/*.{tsx,jsx}"

# API & Business Logic
- "**/api/**/*.{ts,js}"
- "**/services/**/*.{ts,js}"  
- "**/controllers/**/*.{ts,js}"

# Testing & Quality
- "**/*.test.{ts,tsx,js,jsx}"
- "**/*.spec.{ts,tsx,js,jsx}"
- "**/tests/**/*"
```

**Enterprise Java/Spring:**
```yaml
# Domain & Business Logic
- "**/domain/**/*.java"
- "**/service/**/*.java"
- "**/repository/**/*.java"

# Web Layer & APIs
- "**/controller/**/*.java"
- "**/rest/**/*.java"
- "**/web/**/*.java"

# Security & Configuration
- "**/security/**/*.java"
- "**/config/**/*.java"
```

**Python/Django Enterprise:**
```yaml
# Models & Business Logic  
- "**/models/**/*.py"
- "**/services/**/*.py"
- "**/business/**/*.py"

# Views & APIs
- "**/views/**/*.py"
- "**/api/**/*.py"
- "**/serializers/**/*.py"

# Testing & Quality
- "**/tests/**/*.py"
- "**/test_*.py"
```

## 🎯 Enterprise Development Best Practices

### Business-First Development
1. **Question Everything**: Each feature must answer "What user need does this solve?"
2. **Document Decisions**: Create ADRs for architecture choices, user journeys for UX decisions
3. **Collaborate Early**: Engage stakeholders before writing code, not after
4. **Measure Impact**: Define success metrics upfront, track business outcomes

### Quality-First Engineering  
1. **Security by Design**: Security rules activate automatically for sensitive code paths
2. **Accessibility by Default**: UX rules enforce WCAG compliance from the start
3. **Performance Awareness**: Architecture rules guide scalable system design
4. **Test Everything**: Quality rules ensure comprehensive testing coverage

### Documentation as Code
- **Persistent Knowledge**: Rules prompt you to create lasting documentation
- **Context Preservation**: Business decisions and technical rationale live with the code
- **Team Alignment**: Shared understanding through consistent documentation patterns

## 🔧 Troubleshooting & Optimization

### Common Issues & Solutions

**Rules not providing context**: 
- Verify `.cursor/rules/` is in project root with proper `.mdc` extension
- Check YAML frontmatter formatting in rule files

**Irrelevant rule activation**:
- Make glob patterns more specific to your file structure
- Use semantic patterns like `**/components/**/*` instead of broad `**/*.tsx`

**Missing enterprise guidance**: 
- Re-run initialization with more detailed project context
- Customize rule files with your specific domain knowledge

**Performance impact**:
- Avoid overly broad patterns that match too many files
- Focus rules on semantic file locations rather than file extensions

### Success Indicators
✅ **Business questions** appear automatically when writing new features  
✅ **Security prompts** activate when working on authentication or APIs  
✅ **Accessibility reminders** show up during UI development  
✅ **Documentation prompts** encourage ADR and user journey creation  
✅ **Quality gates** are consistently applied across all code changes

## 🚀 Advanced Enterprise Customization

### Domain-Specific Rules
Create specialized rules for your industry:

```yaml
# .cursor/rules/healthcare-compliance.mdc
---
description: "Healthcare-specific HIPAA compliance and patient data protection"
globs:
  - "**/patient/**/*"
  - "**/medical/**/*"  
  - "**/health/**/*"
---

# Healthcare Enterprise Rules
- HIPAA compliance for patient data handling
- Audit logging for all medical record access
- Encryption requirements for PHI data
- Access control patterns for healthcare systems
```

### Multi-Environment Rules
Different rules for different environments:

```yaml
# .cursor/rules/production-standards.mdc
---
description: "Production deployment standards and monitoring"
globs:
  - "**/prod/**/*"
  - "**/production/**/*"
  - "**/*.prod.*"
---

# Production Enterprise Standards
- Zero-downtime deployment patterns
- Comprehensive monitoring and alerting
- Performance optimization requirements
- Security hardening and compliance
```

### Integration Excellence

**CI/CD Pipeline Alignment**: Rules automatically align with your quality gates and automated checks

**Documentation Synchronization**: Rule guidance stays current with evolving project documentation

**Team Knowledge Sharing**: Consistent rule application ensures all team members follow enterprise patterns

**Business Stakeholder Communication**: Rules facilitate clear communication between technical and business teams

**Remember**: These rules transform Cursor IDE into an enterprise development environment that automatically guides you toward reliable, maintainable, and business-aligned code.