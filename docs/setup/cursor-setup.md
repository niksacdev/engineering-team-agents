# Cursor IDE Setup Guide

This guide will help you set up the engineering team agent-enhanced rules for Cursor IDE.

## Quick Setup

1. **Copy rule files to your repository:**
   ```bash
   cp -r engineering-team-agents/.cursor ./
   ```

2. **Bootstrap the rules with your project context:**
   
   **⚠️ Important**: Ensure you're in **edit mode** for file modifications
   
   Open Cursor IDE and paste this prompt in the chat:
   
   ```
   I've just installed engineering team agent rules in my repository. Please analyze my codebase and customize these rules to become domain experts for my project.
   
   **You have permission to modify the rule files** - please update them with my project's domain knowledge, technology stack, and business context.
   
   **What to do:**
   1. **Discover**: Check what rule files I have (.cursor/rules/ directory)
   2. **Analyze**: Understand my project's domain, tech stack, architecture, and business logic  
   3. **Customize**: Update the rule files with my specific project context and file patterns
   4. **Test**: Open different file types to confirm rules activate properly
   
   **My project**: [Describe your project briefly - e.g., "E-commerce platform with React frontend and Node.js backend for small businesses"]
   
   Replace generic template content with my project-specific knowledge so the rules understand my domain and can give relevant guidance.
   ```

3. **Verify automatic rule activation:**
   
   **Cursor automatically applies rules** based on the files you open:
   
   ```
   # Open any source code file (.js, .py, .go, etc.)
   # → project-rules.mdc activates (always active)
   # → Security rules activate for service/API files
   
   # Open test files (test_*.py, *.test.js, etc.) 
   # → testing.mdc rules activate automatically
   
   # No manual commands needed - rules work in the background
   ```
   
   **How it works**: Cursor reads the `globs` patterns in each `.mdc` file and automatically applies relevant rules when you open matching files. No explicit commands required!

## How Cursor Rules Work

### Automatic Context Attachment
Cursor automatically applies rules based on file patterns:
- **alwaysApply: true** rules are active for all files
- **globs** patterns determine when specific rules activate
- Rules provide contextual guidance without explicit invocation

### Rule File Structure
```
.cursor/rules/
├── project-rules.mdc          # Always applied (alwaysApply: true)
└── testing.mdc               # Applied to test files
```

### Metadata Format
Each rule file includes YAML frontmatter:
```yaml
---
description: "Brief description of the rule"
globs:
  - "**/*.py"      # Python files
  - "tests/**/*"   # Test files
alwaysApply: true  # Apply to all files (optional)
---
```

## Available Rules

### project-rules.mdc
**When active**: Always (alwaysApply: true)  
**Purpose**: Core project guidelines, architecture principles, development workflow  
**Contains**: Project context, key principles, quality standards, agent integration guidance  

### testing.mdc
**When active**: Test files and validation scripts  
**Purpose**: Testing standards, patterns, and validation requirements  
**Contains**: Test requirements, patterns, commands, quality gates  

## File Pattern Matching

### Common Glob Patterns (Customize for Your Stack)

**Python Projects:**
```yaml
globs:
  - "**/*.py"
  - "tests/**/*.py"
  - "**/test_*.py"
```

**JavaScript/TypeScript Projects:**
```yaml
globs:
  - "**/*.js"
  - "**/*.ts"
  - "**/*.jsx"
  - "**/*.tsx"
  - "**/*.test.js"
  - "**/*.spec.ts"
```

**Go Projects:**
```yaml
globs:
  - "**/*.go"
  - "**/*_test.go"
```

**Java Projects:**
```yaml
globs:
  - "**/*.java"
  - "**/src/test/**/*.java"
```

## Best Practices

1. **Keep Rules Focused**: Each rule file should have a clear, specific purpose
2. **Use Descriptive Globs**: Make file patterns specific enough to be relevant
3. **Regular Updates**: Keep rules current as your project evolves
4. **Test Rule Activation**: Verify rules activate on appropriate files
5. **Team Alignment**: Ensure all team members benefit from consistent rules

## Troubleshooting

**Rules not activating**: Check that `.cursor/rules/` directory is in project root

**Wrong context**: Verify glob patterns match your file structure and naming conventions

**Too much context**: Make glob patterns more specific to avoid irrelevant rule activation

**Rules conflict**: Ensure rules complement rather than contradict each other

**Performance issues**: Avoid overly broad glob patterns that activate unnecessarily

## Advanced Usage

### Custom Rules
Create domain-specific rules by adding new `.mdc` files:

```yaml
# .cursor/rules/api-development.mdc
---
description: "API development patterns and standards"
globs:
  - "**/api/**/*"
  - "**/controllers/**/*"
  - "**/routes/**/*"
---

# API Development Rules
- RESTful design principles
- OpenAPI documentation requirements
- Error handling standards
- Rate limiting considerations
```

### Conditional Rules
Use specific glob patterns for conditional rule application:
```yaml
# Only for TypeScript React components
globs:
  - "**/*.component.tsx"
  - "**/components/**/*.tsx"
```

## Integration with Development Workflow

### Code Review Integration
Rules automatically provide context during code review and development, helping maintain consistency.

### CI/CD Alignment
Ensure rule recommendations align with your CI/CD quality gates and automated checks.

### Documentation Sync
Keep rules synchronized with your project documentation and coding standards.