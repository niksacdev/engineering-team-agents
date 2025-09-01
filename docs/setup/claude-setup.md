# Claude Code Setup Guide

This guide will help you set up the engineering team agents for Claude Code IDE.

## Quick Setup

1. **Copy agent files to your repository:**
   ```bash
   cp -r engineering-team-agents/.claude ./
   cp engineering-team-agents/claude.md ./
   ```
   
   This creates:
   - `.claude/agents/` directory with individual agent files
   - `claude.md` as your main project instructions file

2. **Bootstrap the agents with your project context:**
   
   **⚠️ Important**: Ensure you're in **edit mode** (not just conversation mode)
   
   Copy and paste this prompt into Claude Code:
   
   ```
   I've just installed engineering team agents in my repository. Please analyze my codebase and customize these agents to become domain experts for my project.
   
   **You have permission to modify the agent instruction files** - please update them with my project's domain knowledge, technology stack, and business context.
   
   **What to do:**
   1. **Discover**: Check what agent files I have (.claude/agents/ directory and claude.md)
   2. **Analyze**: Understand my project's domain, tech stack, architecture, and business logic  
   3. **Customize**: Update the agent files with my specific project context
   4. **Test**: Try one agent on a real file from my codebase to confirm it works
   
   **My project**: [Describe your project briefly - e.g., "E-commerce platform with React frontend and Node.js backend for small businesses"]
   
   Replace generic template content with my project-specific knowledge so the agents understand my domain and can give relevant advice.
   ```

3. **Start using your customized agents:**
   
   After the bootstrap process, you can use the **Task tool** to invoke specific agents:
   
   ```
   # Code review
   Use code-reviewer to analyze this authentication module
   
   # Architecture review  
   Use system-architecture-reviewer to validate this new microservice design
   
   # Product management guidance
   Use product-manager-advisor to create GitHub issues for this feature
   
   # UX/UI design guidance
   Use ux-ui-designer to improve this dashboard user experience
   
   # GitOps and CI/CD guidance
   Use gitops-ci-specialist to optimize my deployment pipeline
   ```
   
   **Claude automatically loads** agents from your `.claude/agents/` directory and uses the `claude.md` file as your main project instructions.

## Available Agents

### code-reviewer
**When to use**: After writing or modifying significant code
**What it does**: Reviews code quality, patterns, security, and best practices
**Example**: "I just implemented user authentication. Can you review it?"

### system-architecture-reviewer
**When to use**: Before implementing new features or making architectural decisions
**What it does**: Validates architectural decisions and analyzes system impacts
**Example**: "I'm planning to add a caching layer. What should I consider?"

### product-manager-advisor
**When to use**: When defining requirements or making product decisions
**What it does**: Aligns business value with technical decisions, creates GitHub issues
**Example**: "Help me create proper GitHub issues for this new feature."

### ux-ui-designer
**When to use**: For user-facing components or UX validation
**What it does**: Validates user experience and interface design decisions
**Example**: "Users find our dashboard confusing. Can you help redesign it?"

### gitops-ci-specialist
**When to use**: Before committing code or when troubleshooting CI/CD issues
**What it does**: Ensures proper Git workflows and CI/CD pipeline success
**Example**: "My GitHub Actions are failing. Can you help debug this?"

### responsible-ai-code
**When to use**: For AI/ML features, accessibility validation, or ethical code review
**What it does**: Ensures responsible AI practices, accessibility compliance, and inclusive design
**Example**: "Can you check if our ML recommendation system has bias issues?" or "Does our form meet accessibility standards?"

## Best Practices

1. **Use agents proactively**: Don't wait for problems - use agents during planning and development
2. **Provide context**: The more specific context you provide, the better the agent guidance
3. **Iterate**: Re-run the bootstrap process as your project evolves
4. **Validate**: Test agent recommendations with real examples from your codebase
5. **Combine agents**: Use multiple agents for complex decisions (e.g., architecture + product + UX)

## Troubleshooting

**Agent not found error**: Make sure you copied the agents to `.claude/agents/` directory

**Generic responses**: Re-run the bootstrap process with more specific project context

**Conflicting advice**: Ask agents to collaborate or provide context about your specific constraints

**Need more agents**: You can create custom agents by following the existing agent patterns

## Advanced Usage

### Custom Agents
You can create additional domain-specific agents by:
1. Copying an existing agent file
2. Modifying the name, description, and instructions
3. Adding domain-specific expertise

### Agent Collaboration
For complex decisions, you can have agents work together:
```
Use the system-architecture-reviewer to evaluate this design, then use the product-manager-advisor to validate business alignment, and finally use the ux-ui-designer to ensure good user experience.
```