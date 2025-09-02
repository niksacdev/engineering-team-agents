# Universal AGENTS.md Setup Guide

This guide helps you set up collaborative engineering agents using the universal AGENTS.md format, compatible with any AI tool that supports the specification.

## ✅ Basic Support Level

**Support Level**: Universal compatibility via AGENTS.md standard
- **Broad Compatibility**: Works with Cursor, Windsurf, Aider, Continue, and 10+ other AI tools
- **Industry Standard**: Based on OpenAI's AGENTS.md specification (20,000+ repositories)
- **Simple Setup**: Single file provides collaborative patterns and agent guidance
- **Community Maintained**: Basic support with community contributions welcome

## 🚀 Quick Setup

### 1. Copy Universal Agent Configuration

```bash
# Clone the collaborative engineering template
git clone https://github.com/niksacdev/engineering-team-agents.git

# Navigate to YOUR project repository  
cd /path/to/your-project

# Install universal agent configuration
cp ../engineering-team-agents/AGENTS.md ./
```

### 2. Customize for Your Project

Edit the `AGENTS.md` file to include your project-specific context:

```markdown
## Project: [Your Project Name]
[Brief description of your domain and business goals]

## Domain-Specific Context
- **Industry**: [Healthcare, Finance, E-commerce, etc.]
- **Users**: [Who uses your product]
- **Tech Stack**: [Your primary technologies]
- **Business Model**: [SaaS, Enterprise, Consumer, etc.]
- **Compliance**: [GDPR, HIPAA, SOX, etc.]
```

### 3. Set Up Documentation Structure

The agents expect a structured documentation system:

```bash
# Create documentation folders (auto-populated by agent interactions)
mkdir -p docs/{product,architecture,code-review,ux,responsible-ai,gitops,templates}

# Copy documentation templates
cp -r ../engineering-team-agents/docs/templates/* docs/templates/
```

### 4. Test Agent Collaboration

Start with a simple request to test collaborative patterns:

```
I want to add a user registration feature. Please use the collaborative engineering approach described in AGENTS.md to help me think through this properly.

Expected: The AI should follow the question-first approach, asking about users, business value, and collaborating between different specialist roles.
```

## 🔧 Compatible AI Tools

The AGENTS.md format works with these tools (and more):

| Tool | Status | Notes |
|------|--------|-------|
| **Cursor** | ✅ Supported | Reads AGENTS.md automatically |
| **Windsurf** | ✅ Supported | Uses AGENTS.md for context |
| **Aider** | ✅ Supported | Loads AGENTS.md on startup |
| **Continue** | ✅ Supported | Integrates with VSCode/JetBrains |
| **Other Tools** | ✅ Likely | Any tool supporting AGENTS.md spec |

*Note: Specific tool integration may vary. Check your tool's documentation for AGENTS.md support.*

## 📖 How It Works

### Agent Collaboration Pattern

The AGENTS.md file guides AI tools to follow this workflow:

1. **Product Manager**: Question user needs and business value
2. **UX Designer**: Map user journeys and accessibility 
3. **Architecture**: Ensure scalable system design
4. **Code Reviewer**: Validate security and quality
5. **Responsible AI**: Check for bias and compliance
6. **DevOps**: Optimize deployment and operations

### Documentation Creation

All agent interactions should create persistent documentation:

```
docs/
├── product/           # Requirements, user stories, GitHub issues
├── architecture/      # ADRs, system design decisions
├── code-review/       # Review reports with specific fixes
├── ux/               # User journeys, accessibility reports
├── responsible-ai/    # Bias testing, compliance documentation
└── gitops/           # Deployment guides, operational runbooks
```

### Question-First Development

Always start feature requests with requirements clarification:

```
❌ Bad: "Add authentication to the app"
✅ Good: "I want to add authentication. Let's use the product-manager role to understand who needs this and why."
```

## 🎯 Usage Examples

### Example 1: New Feature Planning
```
Request: "Add shopping cart functionality"

Expected AI Response:
"I'll take on the Product Manager role first. Before we design a shopping cart, let me ask:

1. Who are your users? (B2B buyers, consumers, marketplace vendors?)
2. What's their current workflow for purchasing?
3. What specific problems does the current process create?
4. How will we measure cart success? (conversion rate, cart abandonment?)

Based on your answers, I'll collaborate with the UX Designer role to map the user journey..."
```

### Example 2: Architecture Decision
```
Request: "Should we use GraphQL or REST for our API?"

Expected AI Response:
"Let me approach this from the Architecture Reviewer perspective, collaborating with other specialists:

**Architecture Analysis:**
- What are your data access patterns?
- How complex are your queries?
- Do you have mobile clients with bandwidth constraints?

**Code Reviewer Input:** What are the security implications of each approach?
**Product Manager Input:** Which approach better serves your user workflows?

I'll create an ADR documenting this decision in docs/architecture/..."
```

### Example 3: Code Quality Review
```
Request: "Review this payment processing function"

Expected AI Response:
"Taking on the Code Reviewer role, with collaboration from other specialists:

**Security Analysis:** (Reviewing payment security based on secure coding principles)
**Responsible AI Input:** Any bias in payment processing logic?
**Architecture Input:** Does this fit our overall system design?

I'll create a detailed review report in docs/code-review/ with specific fixes..."
```

## 🔄 Upgrade Path to Full Support

If you need more comprehensive features, consider upgrading to full support platforms:

### For Enterprise Teams
- **Claude Code**: Advanced multi-agent workflows, Task tool integration
- **GitHub Copilot**: Team chatmodes, GitHub Actions integration, issue creation

### Migration Process
1. Keep your `AGENTS.md` file as universal fallback
2. Add platform-specific agents (`.claude/agents/` or `.github/chatmodes/`)
3. Gradually migrate to platform-native features
4. Maintain universal compatibility for team members using different tools

## 🐛 Troubleshooting

### Common Issues

**AI not following collaborative patterns:**
- Ensure your AI tool supports AGENTS.md (check tool documentation)
- Be explicit: "Use the collaborative approach described in AGENTS.md"
- Test with simpler requests first

**No documentation being created:**
- Explicitly request document creation: "Please create the appropriate documentation in docs/"
- Ensure docs/ folders exist
- Some tools may need explicit file creation requests

**Generic responses instead of role-based thinking:**
- Reference specific roles: "Take on the Product Manager role from AGENTS.md"
- Provide project context in your AGENTS.md customization
- Ask follow-up questions to guide role-specific thinking

### Getting Help

1. **Check Tool Documentation**: Verify AGENTS.md support for your specific AI tool
2. **Community Support**: Open issues in this repository for universal format questions
3. **Upgrade Consideration**: For complex workflows, consider full support platforms

## 📈 Success Indicators

You'll know the setup is working when:

✅ **AI asks clarifying questions** before providing solutions  
✅ **Multiple perspectives** are considered (PM, UX, Architecture, etc.)  
✅ **Documentation requests** are made for decisions  
✅ **Collaboration language** appears ("Let me consult the Architecture role...")  
✅ **Business context** is consistently considered  

## 🌟 Best Practices

1. **Customize AGENTS.md**: Add your domain-specific context and business goals
2. **Start Simple**: Begin with basic feature requests to test collaborative patterns
3. **Provide Context**: The more business context you provide, the better the collaboration
4. **Request Documentation**: Explicitly ask for documentation creation when needed
5. **Iterate and Improve**: Refine your AGENTS.md file based on what works for your team

---

**Universal AGENTS.md Format** - Compatible with any AI coding tool that supports the specification. For enterprise features and guaranteed support, consider [Claude Code](docs/setup/claude-setup.md) or [GitHub Copilot](docs/setup/github-copilot-setup.md) setups.