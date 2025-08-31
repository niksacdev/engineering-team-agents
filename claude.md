# Claude Code Instructions - Engineering Team Agents

## Self-Adaptive Multi-Agent System
**IMPORTANT**: These agents automatically adapt to your project. When first activated, analyze the codebase to understand domain, technology stack, architecture patterns, and business requirements. Customize all agent guidance accordingly.

This project uses enterprise-grade engineering team agents accessible via the Task tool that provide domain-specific expertise on code quality, architecture, product decisions, UX design, and DevOps practices.

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

## Available Engineering Team Agents

Use the Task tool with these subagent_type values:

### Core Development Agents
- **`code-reviewer`**: Reviews code for quality, patterns, security, and best practices
- **`system-architecture-reviewer`**: Validates architectural decisions and system design
- **`product-manager-advisor`**: Helps create requirements and align business value
- **`ux-ui-designer`**: Reviews user experience and interface design
- **`gitops-ci-specialist`**: Optimizes CI/CD workflows and deployment processes

### Coordination Agent
- **`sync-coordinator`**: Synchronizes instruction files across multiple IDE platforms (optional)

## Agent Usage Patterns

### Before Implementation
1. **Requirements Planning**: Use `product-manager-advisor` to clarify user needs and business value
2. **Architecture Design**: Use `system-architecture-reviewer` to validate system design
3. **UX Planning**: Use `ux-ui-designer` for user-facing components

### During Development
1. **Write Code**: Follow discovered project patterns and conventions
2. **Quality Validation**: Run project-specific quality checks (auto-detected tools)
3. **Code Review**: Use `code-reviewer` for expert feedback
4. **Integration**: Ensure changes integrate well with existing codebase

### Before Deployment
1. **Pipeline Validation**: Use `gitops-ci-specialist` to optimize deployment process
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

## Multi-Agent Coordination

### Agent Orchestration Patterns
- **Sequential Processing**: Pass context between agents for complex decisions
- **Parallel Analysis**: Use multiple agents simultaneously for comprehensive review
- **Hybrid Workflows**: Combine sequential and parallel patterns as needed
- **Context Preservation**: Maintain context across multi-agent interactions

### Best Practices for Multi-Agent Usage
1. **Start with Planning Agents**: Use product-manager-advisor and system-architecture-reviewer first
2. **Implement with Quality Focus**: Use code-reviewer and ux-ui-designer during development
3. **Deploy with Confidence**: Use gitops-ci-specialist for deployment optimization
4. **Iterate and Improve**: Continuously refine agent guidance based on project evolution

## Agent Development Best Practices
- **Token Optimization**: Concise instructions, file references over inline content
- **Context Management**: Preserve context, avoid circular reasoning loops
- **Error Handling**: Graceful degradation with human escalation triggers
- **Feedback Integration**: Learn from interactions, continuous improvement
- **Structured Output**: Consistent response formats, actionable recommendations
- **Safety Guardrails**: Appropriate response boundaries, content filtering

## Enterprise Patterns Integration
All agents are trained on enterprise patterns including: SOLID principles, security-first development, operational excellence, compliance frameworks, and domain-driven design. They automatically apply appropriate patterns based on discovered project complexity and requirements.

Remember: These agents enhance your development process through intelligent, context-aware guidance. Use them proactively to improve code quality, architectural decisions, and user experience outcomes.