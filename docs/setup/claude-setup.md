# Claude Code Setup Guide

This guide will help you set up the engineering team agents for Claude Code IDE.

## ⭐ Full Enterprise Support

**Support Level**: Fully tested and actively maintained
- **Native Integration**: Uses Claude's Task tool for seamless agent switching
- **Comprehensive Testing**: All agents tested across multiple project types
- **Enterprise Features**: Complete ADR creation, cross-agent consultation, document management
- **Active Development**: Regular updates and improvements based on user feedback

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
   I've just installed engineering team agents in my repository. Please help me set them up to work with my specific project context.
   
   **Setup Approach**:
   1. **Discover**: Check what agent files I have (.claude/agents/ directory and claude.md)
   2. **Analyze Repository Context**: Read my README.md, package.json, docs/, and any existing architecture documentation to understand:
      - Project domain and business context
      - Technology stack and frameworks
      - Existing documentation structure
      - User types and business goals
   3. **Use Repository Links**: When agents need domain knowledge, provide **file paths and links** to repository documentation instead of copying content:
      - "See README.md for project overview"
      - "Business context in docs/business*.md"
      - "Architecture decisions in docs/architecture/"
      - "User personas in docs/product/user-personas.md"
   4. **Fill Documentation Gaps**: If business context is missing, use the product-manager-advisor agent to help me create:
      - docs/product/business-context.md
      - docs/architecture/tech-stack-overview.md  
      - User personas and success metrics
   5. **Test**: Try one agent on a real file from my codebase to confirm it works with the discovered context
   
   **My project**: [Brief description - e.g., "E-commerce platform with React frontend and Node.js backend for small businesses"]
   
   **🎯 Token Optimization Goal**: Agents understand my domain through **repository links and file references**, not duplicated content in agent files. This keeps agent instructions lean while providing access to comprehensive project knowledge.
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

### technical-writer
**When to use**: When creating documentation, blogs, tutorials, or API docs
**What it does**: Creates clear, concise technical documentation and content
**Example**: "Help me write API documentation for our authentication endpoints."

### responsible-ai-code
**When to use**: For AI/ML features, accessibility validation, or ethical code review
**What it does**: Ensures responsible AI practices, accessibility compliance, and inclusive design
**Example**: "Can you check if our ML recommendation system has bias issues?" or "Does our form meet accessibility standards?"

### gitops-ci-specialist
**When to use**: Before committing code or when troubleshooting CI/CD issues
**What it does**: Ensures proper Git workflows and CI/CD pipeline success
**Example**: "My GitHub Actions are failing. Can you help debug this?"

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