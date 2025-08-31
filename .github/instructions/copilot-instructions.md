---
applyTo: '**'
---

Provide project context and coding guidelines that AI should follow when generating code, answering questions, or reviewing changes.

# GitHub Copilot Instructions - Engineering Team Agents

## Self-Adaptive Agent System
**IMPORTANT**: These agents automatically adapt to your project. When first used, analyze the codebase to understand domain, technology stack, architecture patterns, and business requirements. Customize all guidance accordingly.

This project uses enterprise-grade engineering team agents that provide domain-specific expertise on code quality, architecture, product decisions, UX design, and DevOps practices.

## Critical Development Principles

### Token Optimization
- **Problem**: Large instruction files cause excessive token consumption
- **Solution**: Keep instructions focused and reference external documentation
- **Best Practice**: Use file references instead of inline code examples

### Context Management
- **Problem**: Context loss during long development sessions leads to conflicting changes
- **Solution**: Use regular checkpoints, explicit context anchoring, focused work sessions
- **Recommendation**: Keep development sessions to 2-3 hours with clear context breaks

### Circular Debugging Prevention
- **Problem**: AI repeats failed solutions in endless loops
- **Solution**: Track attempted fixes, detect patterns, request human intervention when needed
- **Human Role**: Provide strategic direction and pragmatic guidance when loops are detected

## Architecture Principles (Self-Adaptive)

**Key Design Principles** (Customize based on project analysis):
- **Domain-Driven**: Architecture reflects discovered business domain and user workflows
- **Separation of Concerns**: Clear boundaries aligned with existing system responsibilities
- **Testability**: Code designed to support project's current testing strategies
- **Maintainability**: Optimize for long-term maintenance and discovered team productivity patterns
- **Security-First**: Build security considerations appropriate to domain requirements
- **Performance-Aware**: Consider performance implications based on project scale and usage patterns

## Development Standards (Auto-Discover from Project)

### Quality Standards Discovery
**Auto-analyze project to determine**:
- **Type Safety**: Identify and follow project's typing patterns and strictness level
- **Error Handling**: Match project's error handling patterns and user experience standards
- **Code Organization**: Follow discovered patterns for framework/language in existing codebase
- **Testing**: Match project's current test coverage standards and testing approaches
- **Documentation**: Align with project's existing documentation patterns and requirements

### Pre-Commit Quality Checks (Project-Specific)
**Auto-detect and use project's validation tools**:
- **Linting**: Identify and use project's linting configuration (eslint, ruff, etc.)
- **Formatting**: Follow project's formatting standards (prettier, black, etc.)
- **Testing**: Use project's test runners and coverage requirements
- **Security**: Apply project's security scanning tools and standards
- **Dependencies**: Follow project's dependency management patterns

**⚠️ Always run project-specific quality checks before committing**

### Engineering Team Agent Integration

This project includes specialized engineering team agents accessible via chatmodes:

#### Available Agents
- **`/code-quality`**: Reviews code for quality, patterns, security, and best practices
- **`/architecture-review`**: Validates architectural decisions and system design
- **`/pm-requirements`**: Helps create requirements and align business value
- **`/ui-validation`**: Reviews user experience and interface design
- **`/cicd-help`**: Optimizes CI/CD workflows and deployment processes

#### When to Use Agents
- **Before Implementation**: Use `/architecture-review` and `/pm-requirements` for planning
- **During Development**: Use `/code-quality` for ongoing code review
- **For User-Facing Features**: Use `/ui-validation` for UX validation
- **For Deployment**: Use `/cicd-help` for pipeline optimization
- **Combine Agents**: Use multiple agents for complex decisions

## Development Workflow

### Planning Phase
1. **Requirements Definition**: Use `/pm-requirements` to clarify user needs and business value
2. **Architecture Design**: Use `/architecture-review` to validate system design
3. **UX Planning**: Use `/ui-validation` for user-facing components

### Implementation Phase
1. **Write Code**: Follow established project patterns and conventions
2. **Quality Validation**: Run local quality checks (linting, formatting, tests)
3. **Code Review**: Use `/code-quality` for expert feedback
4. **Integration**: Ensure changes integrate well with existing codebase

### Deployment Phase
1. **Pipeline Validation**: Use `/cicd-help` to optimize deployment process
2. **Quality Gates**: Ensure all automated checks pass
3. **Documentation**: Update relevant documentation
4. **Monitoring**: Implement appropriate observability for changes

## Auto-Discovery Process

**When first activated, agents will**:

### Domain Knowledge Discovery
- **Business Context**: Analyze README, documentation, code comments to understand domain
- **User Personas**: Identify target users from UI patterns, API endpoints, user flows
- **Key Workflows**: Map business processes from service architectures and data flows
- **Success Metrics**: Discover KPIs from analytics code, monitoring, and business logic

### Technical Stack Analysis
- **Languages**: Scan project files to identify primary and secondary languages
- **Frameworks**: Detect frameworks from package.json, requirements.txt, dependencies
- **Infrastructure**: Identify deployment patterns from config files, Docker, CI/CD
- **Tools**: Discover development tools from config files, scripts, and workflow files

### Quality Standards Detection
- **Test Coverage**: Analyze existing test patterns and coverage configuration
- **Performance**: Identify performance standards from monitoring, SLA definitions
- **Security**: Discover security requirements from existing security implementations
- **Compliance**: Detect regulatory needs from code patterns and documentation

## Agent Activation
**Agents automatically activate** when chatmodes are used:
1. **Analyze Project**: Understand current codebase, patterns, and requirements
2. **Adapt Guidance**: Customize recommendations to discovered project context
3. **Apply Expertise**: Provide domain-specific, technology-appropriate guidance
4. **Learn Continuously**: Improve recommendations based on project evolution

## Best Practices

1. **Agent-First Development**: Proactively use agents for guidance and validation
2. **Iterative Improvement**: Regularly update instructions based on project evolution
3. **Context Preservation**: Maintain clear context during development sessions
4. **Quality Focus**: Never compromise on code quality for speed
5. **Collaborative Decision-Making**: Use agents to facilitate technical discussions
6. **Documentation Hygiene**: Keep documentation current with code changes

Remember: These agents are designed to enhance your development process. Use them actively to improve code quality, architectural decisions, and user experience outcomes.