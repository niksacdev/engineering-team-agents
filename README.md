# 🚀 Engineering Team Agents

> **Disclaimer**: This is an experimental repository. The content, methodologies, and opinions expressed herein are solely those of the individual contributors and do not represent the views, policies, or practices of any employer, client, or affiliated organization.

## Background

This templates was developed based on learnings from experimental multi-agent system documented in: [Beyond Vibe Coding: A Multi-Agent Approach to Software Engineering](https://www.appliedcontext.ai/p/beyond-vibe-coding-a-multi-agent), The complete multi-agent system with code is available at: [https://github.com/niksacdev/multi-agent-system](https://github.com/niksacdev/multi-agent-system)

## Your AI Engineering Team

Get an **engineering agent team** working on your project - not just a single AI assistant.

Works with [Claude Code](https://claude.ai/code), [GitHub Copilot](https://github.com/features/copilot), or [Cursor](https://www.cursor.com/).

**5 Engineering Team Agents** that understand YOUR codebase:
- **Senior Code Reviewer** - Security, architecture patterns, your tech stack
- **Product Advisor** - Your users, business logic, domain workflows
- **Principal System Architect** - Your scale, constraints, infrastructure  
- **Lead UX Designer** - Your design system, user journeys, accessibility
- **DevOps Engineer** - Your CI/CD, deployment, compliance requirements

**Multi-Agent Collaboration**: Agents work together on complex decisions, just like a real team. Architecture review → Product validation → Code review → UX feedback → DevOps deployment.

**Domain Expertise**: They learn your business rules, terminology, patterns, and constraints - becoming true team members, not generic helpers.


## Available Agents

| Agent | Purpose | Enterprise Capabilities |
|-------|---------|------------------------|
| **Code Reviewer** | Enterprise-grade code quality, security, compliance | SOLID principles, security assessment, performance analysis, regulatory compliance |
| **System Architecture Reviewer** | Enterprise architecture, ADR creation, system design | ADR templates, enterprise patterns, scalability design, security architecture |
| **Product Manager Advisor** | Business strategy, requirements, stakeholder management | Enterprise GitHub issues, compliance frameworks, ROI analysis, market research |
| **UX/UI Designer** | Accessibility, design systems, user research | WCAG compliance, enterprise design patterns, user journey mapping |
| **GitOps CI Specialist** | Enterprise DevOps, security, deployment strategies | Security scanning, compliance automation, enterprise deployment patterns |


## Getting Started (5 Minutes)

### 1. Install Agent Files

```bash
# 1. Clone this template repository
git clone https://github.com/niksacdev/engineering-team-agents.git

# 2. Go to YOUR project repository  
cd /path/to/your-project

# 3. Copy agent files to your project:
cp -r ../engineering-team-agents/.claude ./           # Claude Code
cp -r ../engineering-team-agents/.github ./          # GitHub Copilot  
cp -r ../engineering-team-agents/.cursor ./          # Cursor IDE
cp ../engineering-team-agents/claude.md ./           # Claude main instructions
```

**Windows:** Use `xcopy /E /I` instead of `cp -r` and `copy` instead of `cp`

### 2. Bootstrap Your Agents

Run the bootstrap process in your IDE to customize agents for your specific project. 

**Follow your platform-specific guide:**
- [Claude Code Setup](docs/setup/claude-setup.md)
- [GitHub Copilot Setup](docs/setup/github-copilot-setup.md)  
- [Cursor IDE Setup](docs/setup/cursor-setup.md)

### 3. Start Using Your Agents

- **Claude Code:** `Use code-reviewer to analyze this file`  
- **GitHub Copilot:** `/code-quality`, `/architecture-review`, `/pm-requirements`, `/ui-validation`, `/cicd-help`
- **Cursor IDE:** Automatic activation based on file types

**Detailed usage:** See [setup guides](docs/setup/)

## 🤝 Contributing

We welcome contributions from the community! Whether you want to:
- Improve existing agents or create new specialized agents
- Add support for additional IDE platforms
- Enhance documentation and examples
- Report issues or suggest improvements

Please see our [Contributing Guide](CONTRIBUTING.md) for detailed information on how to get started.

---