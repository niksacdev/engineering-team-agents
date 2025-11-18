# Claude Development Rules - Optimized

> **Size-Optimized Version**: Reduced from 600+ to ~200 lines while maintaining critical information

## Project Context
Multi-agent development system using 8 specialized AI agents for enterprise software development. Agents are domain-agnostic and reusable across any project.

## Critical Rules

### 1. GitHub Issue Management
**NO CODE WITHOUT AN ISSUE. NO PR WITHOUT A LINKED ISSUE.**
- Every change needs issue with 3+ labels (component, size, phase)
- PRs must use format: `[#123] Description` and include `Closes #123`
- Features >1 week become Epics with sub-issues

### 2. Quality Gates (MANDATORY)
Before ANY commit:
```bash
ruff check . --fix      # Auto-fix linting
ruff format .          # Auto-format
pytest tests/ -v       # Tests must pass
# Coverage must be ≥85%
```

### 3. Token Optimization
- **Problem**: 2000+ line agents = 30+ second responses
- **Solution**: 300-500 lines focusing on directives
- **Result**: 75% reduction, 10x speed (3 seconds)

## Development Support Agents

Use Task tool with `subagent_type` parameter:

| Agent | When to Use | Key Output |
|-------|------------|------------|
| **system-architecture-reviewer** | Design validation, impact analysis | ADRs, design review |
| **product-manager-advisor** | Requirements, GitHub issues | User stories, priorities |
| **code-reviewer** | After writing code | Security/quality feedback |
| **ux-ui-designer** | UI components, UX flows | Design validation |
| **technical-writer** | Documentation, blogs | Clear technical content |
| **gitops-ci-specialist** | CI/CD issues, deployments | Pipeline optimization |
| **responsible-ai-code** | AI ethics, accessibility | Bias reports, WCAG compliance |
| **sync-coordinator** | Before commits with agent changes | Cross-platform sync |

### Usage Pattern
```
1. Requirements → product-manager-advisor
2. Design → system-architecture-reviewer
3. Implementation → Write code
4. Review → code-reviewer
5. UI → ux-ui-designer
6. Deploy → gitops-ci-specialist
```

## Architecture Principles

1. **Agent Autonomy**: Agents decide tool usage, personas drive behavior
2. **Clean Orchestration**: Minimal orchestrator, logic in personas
3. **Token Efficiency**: <500 lines per agent for performance
4. **Sequential Workflow**: Context passed between agents

## Documentation Structure

**NEVER create ALL CAPS files in root**. Use:
- ADRs → `docs/architecture/decisions/adr-XXX-*.md`
- Troubleshooting → `docs/troubleshooting/*.md`
- Guides → `docs/getting-started/*.md`
- Product → `docs/product-guide/*.md`

## Commit Best Practices

### Branch Management
- Delete branches after PR merge
- Feature branches only (`feat/`, `fix/`)
- Never commit to main directly

### Commit Format
```bash
git commit -m "type: brief description"
# Types: feat, fix, docs, test, refactor, chore
```

### Frequency
- Commit after each logical change
- Small PRs (50-200 lines)
- Atomic commits

## Testing Standards

- Use `uv` package manager exclusively
- Tests required for all changes
- Coverage ≥85% on core modules
- Run validation: `python scripts/validate_ci_fix.py`

## Performance Targets

- Agent responses <5 seconds
- Token reduction >70%
- All PRs linked to issues
- Zero security vulnerabilities
- Full test coverage

## Common Patterns

### Multi-Agent Workflow
```python
# Sequential processing
result1 = agent1.run(input)
result2 = agent2.run(input, context=result1)
final = orchestrator.run(all_results)
```

### Error Handling
- Implement timeouts for agents
- Graceful degradation
- Retry logic for failures

## Quick Reference

### Commands
```bash
uv sync                    # Install deps
uv run pytest             # Run tests
uv run ruff check .       # Lint
git commit -m "type: msg" # Commit
```

### File Locations
- Agents: `.claude/agents/*.md`
- Chatmodes: `.github/chatmodes/*.md`
- GitHub agents: `.github/agents/*.md`
- Config: `config/agents.yaml`

## Success Checklist

- [ ] Issue created and linked
- [ ] Tests pass (≥85% coverage)
- [ ] Agents used for validation
- [ ] Documentation updated
- [ ] Quality gates passed
- [ ] PR reviewed

## Key Learnings

1. **Token optimization**: 300-500 lines = 10x faster
2. **Issue enforcement**: Every change tracked
3. **Agent collaboration**: Sequential validation
4. **Quality automation**: Pre-commit checks mandatory

---
*For complete details, see full documentation in `docs/` directory*