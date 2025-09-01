# Claude Code Instructions - Engineering Team Agents

## Collaborative Multi-Agent Development System

This project provides a specialized team of engineering agents that work together to ensure **reliable, maintainable, and business-aligned code**. Each agent creates persistent documentation and collaborates with team members to deliver enterprise-grade solutions.

## 🎯 Core Mission: Build the Right Thing, Build It Right

**Every feature request follows this collaborative workflow:**
1. **Product Manager** clarifies user needs and business value
2. **UX Designer** maps user journeys and validates workflows  
3. **Architecture** ensures scalable, secure system design
4. **Code Reviewer** validates implementation quality and security
5. **Responsible AI** prevents bias and ensures accessibility
6. **GitOps** optimizes deployment and operational excellence

**All agents create persistent documentation** in a structured `docs/` folder system for knowledge continuity.

## ⚡ Agent-First Development Workflow

### 🔍 ALWAYS Start Here (Question-First Approach)
**Before writing any code, use these agents to clarify requirements:**

```
Use product-manager-advisor to ask:
- Who exactly will use this feature?
- What specific problem does it solve?  
- How will we measure success?
```

**Why**: Prevents building features nobody needs or uses.

### 🏗️ Design Phase (Architecture & UX)
**For any new feature or system change:**

```
1. Use system-architecture-reviewer to validate:
   - Does this fit our current architecture?
   - Any security or scalability risks?
   - Should we create an ADR for this decision?

2. Use ux-ui-designer for user-facing changes:
   - Map current vs future user journey
   - Identify accessibility requirements
   - Validate workflow with real user scenarios
```

**Output**: Architecture Decision Records (ADRs) and User Journey Maps saved to `docs/`

### 💻 Implementation Phase (Quality-First Development)
**Write code following project patterns, then immediately validate:**

```
1. Use responsible-ai-code for any user-facing or AI features:
   - Test with diverse user inputs (names, ages, contexts)
   - Ensure keyboard accessibility and screen reader support
   - Validate privacy and data collection practices

2. Use code-reviewer after writing significant code:
   - Security vulnerabilities (SQL injection, XSS, auth)
   - Reliability issues (timeouts, error handling)
   - Performance bottlenecks (for >1000 user systems)
```

**Output**: Code Review Reports with specific fixes and implementation recommendations

### 🚀 Deployment Phase (Operational Excellence)
**Before deploying to production:**

```
Use gitops-ci-specialist to optimize:
- CI/CD pipeline efficiency and reliability
- Deployment automation and rollback strategies  
- Monitoring and observability implementation
```

**Result**: Reliable deployments with proper monitoring and quick recovery capabilities

## 🤝 Available Engineering Team Agents

### Core Development Team
- **`product-manager-advisor`** 📊
  - Creates product requirements and GitHub issues
  - Validates business value and user alignment
  - Partners with UX for user journey mapping
  - **Documents**: Requirements, user stories, business context

- **`ux-ui-designer`** 🎨  
  - Maps user journeys and validates workflows
  - Ensures accessibility and inclusive design
  - Reviews interfaces for usability issues
  - **Documents**: User journey maps, UX design reports

- **`system-architecture-reviewer`** 🏛️
  - Validates architectural decisions and system design
  - Creates Architecture Decision Records (ADRs)
  - Ensures scalability and security compliance
  - **Documents**: ADRs, system design decisions

- **`code-reviewer`** 🔍
  - Reviews code for security, reliability, performance
  - Provides specific code fixes and improvements
  - Validates implementation against best practices
  - **Documents**: Code review reports with actionable fixes

- **`responsible-ai-code`** 🌍
  - Prevents bias and ensures accessibility compliance
  - Creates Responsible AI ADRs for ethical decisions
  - Tests with diverse user scenarios and edge cases
  - **Documents**: RAI-ADRs, evolution logs, compliance reports

- **`gitops-ci-specialist`** 🚀
  - Optimizes CI/CD workflows and deployment processes
  - Implements monitoring and operational excellence
  - Automates deployment and rollback strategies
  - **Documents**: Deployment guides, operational runbooks

### Coordination Agent
- **`sync-coordinator`**: Synchronizes instruction files across IDE platforms (optional)

## 🔄 Team Collaboration Patterns

### Agent-to-Agent Handoffs
Agents actively collaborate and delegate to specialists:

```
Product Manager → UX Designer: "Can you map the user journey for this workflow?"
UX Designer → Responsible AI: "Any accessibility barriers with this interface?"
Architecture → Code Reviewer: "Security implications of this design decision?"
Code Reviewer → GitOps: "Any deployment concerns with this implementation?"
```

### Human Escalation Triggers
Agents escalate to humans when:
- **Business vs technical tradeoffs** require strategic decisions
- **Budget/timeline implications** need stakeholder input  
- **Legal/compliance clarity** requires domain expertise
- **Complex user research** needs direct user validation

## 📁 Documentation System

### Structured Knowledge Preservation
All agents create persistent documentation in organized folders:

```
docs/
├── architecture/          # ADRs and system design decisions
├── product/              # Requirements and user stories  
├── ux/                   # User journeys and design reports
├── code-review/          # Code review reports and fixes
├── responsible-ai/       # RAI-ADRs and compliance tracking
├── gitops/              # Deployment and operational guides
└── templates/           # Consistent documentation templates
```

### Living Documentation
- **Updates automatically** when business requirements change
- **Maintains decision context** for future team members
- **Tracks evolution** of practices and patterns over time
- **Enables knowledge continuity** across team changes

## 🚦 Quality Gates & Deployment Readiness

### Pre-Deployment Checklist
Before any production deployment, ensure:

- [ ] **Product Manager**: Requirements validated with clear success metrics
- [ ] **UX Designer**: User journey tested and accessible to all users
- [ ] **Architecture**: System design documented in ADRs, scalability validated
- [ ] **Code Reviewer**: Security vulnerabilities resolved, reliability confirmed
- [ ] **Responsible AI**: Bias testing completed, accessibility compliance verified
- [ ] **GitOps**: Deployment pipeline tested, monitoring implemented

### Continuous Quality Improvement
- Agents learn from each project iteration
- Documentation patterns evolve based on team needs
- Collaboration workflows optimize over time
- Enterprise patterns automatically adapt to project complexity

## ⚙️ Setup Requirements

### Documentation Folder Structure
**Important**: Each agent assumes a `docs/` folder structure exists in your project root. 

**To customize document locations:**
1. Edit the relevant agent files in `.claude/agents/` 
2. Update the `docs/[folder]/` paths to your preferred locations
3. Ensure templates exist in your specified template folder

**Default folder structure will be created automatically** when agents first run.

### Getting Started
1. **Ask questions first**: Use `product-manager-advisor` before writing code
2. **Design before building**: Validate with `ux-ui-designer` and `system-architecture-reviewer`
3. **Review everything**: Use `code-reviewer` and `responsible-ai-code` for quality
4. **Deploy confidently**: Use `gitops-ci-specialist` for operational excellence

**Remember**: These agents work as a team to ensure every feature is user-focused, well-architected, secure, accessible, and reliably deployed. Use them proactively throughout your development process.