# Universal AI Agent Guide for Engineering Teams

## Quick Start
This repository contains 8 production-ready AI agents that work across Claude, GitHub Copilot, and other AI platforms. Each agent is optimized for <5 second response times through token optimization (300-500 lines per agent).

## Available Agents

| Agent | Purpose | Key Capabilities |
|-------|---------|-----------------|
| **product-manager-advisor** | Requirements & Planning | GitHub issues, user stories, prioritization |
| **system-architecture-reviewer** | Technical Design | ADRs, system design, impact analysis |
| **code-reviewer** | Quality & Security | OWASP compliance, best practices, performance |
| **ux-ui-designer** | User Experience | Journey mapping, accessibility, usability |
| **technical-writer** | Documentation | Blogs, tutorials, API docs, ADRs |
| **gitops-ci-specialist** | DevOps & Deployment | CI/CD, monitoring, troubleshooting |
| **responsible-ai-code** | Ethics & Compliance | Bias detection, privacy, accessibility |
| **sync-coordinator** | Cross-Platform Sync | Maintains consistency across AI tools |

## Integration Patterns

### Load Agent (Any Framework)
```python
# Example for Claude, Copilot, or custom frameworks
with open('agents/product-manager.md') as f:
    agent = Agent(name="PM", instructions=f.read())
```

### Sequential Workflow
```python
# Agents collaborate in sequence
requirements = pm_agent.analyze(request)
design = architect_agent.design(requirements)
review = code_reviewer.validate(implementation)
```

## Critical Performance Optimization

**Problem**: Large agent files (2000+ lines) cause 30+ second delays
**Solution**: Optimize to 300-500 lines focusing on directives
**Result**: 75% token reduction, 10x speed improvement (3 second responses)

## GitHub Issue Management (MANDATORY)

### Core Rule
**NO CODE WITHOUT AN ISSUE. NO PR WITHOUT A LINKED ISSUE.**

### Issue Requirements
- **Size Labels**: `size: small` (1-3d), `size: medium` (4-7d), `size: large/epic` (8+d)
- **3 Labels Minimum**: component + size + phase
- **Epic Rule**: If >1 week, create Epic with sub-issues

### PR Format
```markdown
[#123] Brief description

Closes #123
```

## Quality Gates (Pre-Commit)

```bash
# Must pass before ANY commit
ruff check . --fix      # Linting
ruff format .          # Formatting
pytest tests/          # Tests (≥85% coverage)
```

## Best Practices

1. **Token Optimization**: Keep agents 300-500 lines
2. **Async Execution**: Run agents in parallel when possible
3. **Error Handling**: Graceful degradation for failures
4. **Documentation**: Update with code changes
5. **Testing**: Maintain ≥85% coverage

## File Locations

```
.claude/agents/          # Claude agent implementations
.github/chatmodes/       # GitHub Copilot versions
.github/agents/          # GitHub-specific formats
AGENTS.md               # This universal guide
```

## Success Metrics

✅ All agents respond in <5 seconds
✅ Token usage reduced by >70%
✅ All PRs linked to issues
✅ Code coverage ≥85%
✅ Agents are 300-600 lines each

## Getting Started

1. Copy agents to your project
2. Load agent personas into your AI framework
3. Configure tools/APIs for your domain
4. Follow GitHub issue workflow
5. Use quality gates before commits

See individual agent files for detailed capabilities and usage patterns.