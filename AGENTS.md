# AGENTS.md

## Project: Collaborative Engineering Team Agents
Enterprise-grade multi-agent system for reliable, maintainable, and business-aligned code.

## Agent Collaboration Pattern
Every feature request follows this collaborative workflow:
1. **Product Manager** clarifies user needs and business value
2. **UX Designer** maps user journeys and validates workflows
3. **Architecture** ensures scalable, secure system design
4. **Code Reviewer** validates implementation quality and security
5. **Technical Writer** creates documentation and content
6. **Responsible AI** prevents bias and ensures accessibility
7. **GitOps** optimizes deployment and operational excellence

All agents create persistent documentation in structured `docs/` folders.

## Available Specialists

### Product Management Agent
- **Role**: Clarifies requirements, validates business value
- **Outputs**: Requirements documents, GitHub issues, user stories
- **Location**: Product-focused development guidance
- **Collaboration**: Partners with UX Designer for user journey mapping

### Architecture Reviewer Agent
- **Role**: Validates system design, creates technical decisions
- **Outputs**: Architecture Decision Records (ADRs), system design docs
- **Location**: Enterprise architecture guidance
- **Collaboration**: Consults Code Reviewer for security implications

### Code Quality Agent
- **Role**: Security-first code review, quality validation
- **Outputs**: Code review reports with specific fixes
- **Location**: Enterprise security and quality standards
- **Collaboration**: Escalates architectural concerns to Architecture Agent

### UX Design Agent
- **Role**: User journey mapping, accessibility validation
- **Outputs**: User journey maps, accessibility compliance reports
- **Location**: User experience and accessibility guidance
- **Collaboration**: Validates business impact with Product Manager

### Technical Writer Agent
- **Role**: Documentation creation, content writing, tutorials
- **Outputs**: Blogs, tutorials, API docs, ADRs, technical guides
- **Location**: Technical writing and documentation guidance
- **Collaboration**: Works with Product Manager for requirements clarity

### Responsible AI Agent
- **Role**: Bias prevention, accessibility compliance
- **Outputs**: Responsible AI ADRs, bias testing reports
- **Location**: AI ethics and compliance guidance
- **Collaboration**: Reviews user-facing features with UX Designer

### DevOps Specialist Agent
- **Role**: CI/CD optimization, deployment automation
- **Outputs**: Deployment guides, operational runbooks
- **Location**: GitOps and operational excellence guidance
- **Collaboration**: Reviews system dependencies with Architecture

## Document Outputs
All agents create persistent documentation:
- `docs/product/` - Requirements and user stories
- `docs/architecture/` - Architecture Decision Records
- `docs/code-review/` - Review reports with fixes
- `docs/ux/` - User journeys and accessibility reports
- `docs/technical-writing/` - Documentation, blogs, tutorials
- `docs/responsible-ai/` - RAI-ADRs and compliance tracking
- `docs/gitops/` - Deployment guides and runbooks

## Development Workflow

### Question-First Development
Always start with requirements before implementation:
```
1. Product Agent: Who will use this? What problem does it solve?
2. UX Agent: How should users interact with this feature?
3. Architecture Agent: Does this fit our system design?
4. Code Agent: Implement with security and quality focus
5. Technical Writer: Document the feature for users
6. Responsible AI Agent: Test for bias and accessibility
7. DevOps Agent: Deploy with proper monitoring
```

### Collaboration Triggers
- **User-facing features**: Product → UX → Responsible AI
- **System changes**: Architecture → Code → DevOps
- **Documentation needs**: Product → Technical Writer
- **Business decisions**: Product escalates to humans
- **Security concerns**: Code → Architecture → DevOps

## Tool-Specific Enhancements

### For Full Enterprise Support
- **Claude Code**: See `CLAUDE.md` and `.claude/agents/` for specialized agents with Task tool integration
- **GitHub Copilot**: See `.github/chatmodes/` for collaborative team agents with GitHub Actions integration
- **GitHub-Specific**: See `.github/agents/` for GitHub-optimized agent implementations

### Quality Standards
- **Security**: Guidance based on OWASP principles and secure coding practices
- **Accessibility**: Guidance based on WCAG 2.1 principles and inclusive design
- **Performance**: Enterprise-scale optimization patterns with 75% token reduction
- **Documentation**: Living documentation that evolves with code

### Enterprise Features
- **Audit Trail**: All agent interactions create documentation
- **Guidance**: Regulatory and accessibility guidance based on industry standards
- **Scalability**: Patterns for enterprise-scale considerations
- **Security**: Security-first development approach
- **Performance**: 10x faster agent responses (30s → 3s) through optimization

## Success Indicators
✅ Agents reference each other in responses
✅ Documentation appears in `docs/` folders after interactions
✅ Business context is preserved across conversations
✅ Human escalation for strategic decisions
✅ Quality gates are systematically addressed
✅ Agent responses complete in <5 seconds

## Getting Started
1. Copy this repository's agents to your project
2. Initialize `docs/` folder structure for outputs
3. Customize agents with your project's domain knowledge
4. Use question-first approach for all feature development
5. Leverage IDE integrations (Claude Code, GitHub Copilot)

---

*Universal AGENTS.md format - Compatible with any AI coding tool*
