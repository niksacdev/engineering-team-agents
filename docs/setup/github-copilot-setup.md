# GitHub Copilot Setup Guide

This guide will help you set up the engineering team agents for GitHub Copilot.

## Quick Setup

1. **Copy files to your repository:**
   ```bash
   cp -r engineering-team-agents/.github ./
   ```

2. **Bootstrap the agents with your project context:**
   
   **⚠️ Important**: Ensure you're in **agent/chat mode** for file modifications
   
   Open GitHub Copilot chat and paste this prompt:
   
   ```
   I've just installed engineering team agents in my repository. Please analyze my codebase and customize these agents to become domain experts for my project.
   
   **You have permission to modify the agent instruction files** - please update them with my project's domain knowledge, technology stack, and business context.
   
   **What to do:**
   1. **Discover**: Check what agent files I have (.github/instructions/ and .github/chatmodes/ directories)
   2. **Analyze**: Understand my project's domain, tech stack, architecture, and business logic  
   3. **Customize**: Update the agent files with my specific project context
   4. **Test**: Try one chatmode on a real file from my codebase to confirm it works
   
   **My project**: [Describe your project briefly - e.g., "E-commerce platform with React frontend and Node.js backend for small businesses"]
   
   Replace generic template content with my project-specific knowledge so the agents understand my domain and can give relevant advice.
   ```

3. **Start using your customized agents:**
   
   After the bootstrap process, use **chatmode commands** in GitHub Copilot Chat:
   
   ```
   /code-quality Review this authentication function for security issues
   
   /architecture-review I'm adding a caching layer, what should I consider?
   
   /pm-requirements Help me create a GitHub issue for user profile management
   
   /ui-validation Our checkout flow is confusing users, can you redesign it?
   
   /cicd-help My deployment pipeline is failing, help me debug it
   ```
   
   **GitHub Copilot automatically loads** your chatmodes from `.github/chatmodes/` and applies instructions from `.github/instructions/copilot-instructions.md`.

## Available Chatmode Commands

### /code-quality
**Purpose**: Reviews code for quality, patterns, security, and best practices  
**When to use**: After writing or modifying significant code  
**Example**: `/code-quality` followed by pasting your code or describing the changes  

### /architecture-review
**Purpose**: Validates architectural decisions and analyzes system impacts  
**When to use**: Before implementing new features or making architectural decisions  
**Example**: `/architecture-review I'm planning to add a caching layer to improve performance`  

### /pm-requirements
**Purpose**: Creates requirements, user stories, and validates business value  
**When to use**: When defining features or creating GitHub issues  
**Example**: `/pm-requirements Help me create a GitHub issue for user authentication`  

### /ui-validation
**Purpose**: Reviews UI/UX for usability, accessibility, and design best practices  
**When to use**: For user-facing components or UX validation  
**Example**: `/ui-validation Users find our dashboard confusing, can you help redesign it?`  

### /cicd-help
**Purpose**: Optimizes CI/CD workflows and deployment processes  
**When to use**: When setting up or troubleshooting CI/CD pipelines  
**Example**: `/cicd-help My GitHub Actions are failing, can you help debug this?`  

## File Structure

After setup, your repository will have:

```
.github/
├── chatmodes/
│   ├── code-reviewer.chatmode.md
│   ├── architecture-reviewer.chatmode.md
│   ├── product-manager.chatmode.md
│   ├── ux-designer.chatmode.md
│   └── gitops-ci-specialist.chatmode.md
└── instructions/
    └── copilot-instructions.md
```

## Best Practices

1. **Use agents proactively**: Don't wait for problems - engage agents during planning and development
2. **Provide specific context**: The more details you provide, the better the agent guidance
3. **Combine agents**: Use multiple agents for complex decisions (e.g., architecture + product + UX)
4. **Iterate**: Re-run the bootstrap process as your project evolves
5. **Test recommendations**: Validate agent suggestions with your specific codebase
6. **Update instructions**: Keep the instruction files current as your project evolves

## Integration with Development Workflow

### Planning Phase
1. Use `/pm-requirements` to clarify user needs and business value
2. Use `/architecture-review` to validate system design decisions
3. Use `/ui-validation` for user-facing component planning

### Development Phase
1. Write code following established patterns
2. Use `/code-quality` for ongoing code review and improvement
3. Use `/architecture-review` to validate integration with existing system

### Deployment Phase
1. Use `/cicd-help` to optimize deployment pipelines
2. Ensure all quality gates are met
3. Update documentation and requirements as needed

## Troubleshooting

**Chatmodes not working**: Ensure the `.github/chatmodes/` directory and files are properly copied

**Generic responses**: Re-run the bootstrap process with more specific project context

**Conflicting advice between agents**: Ask agents to collaborate or provide your specific constraints

**Need different agents**: You can create custom chatmodes by following the existing patterns