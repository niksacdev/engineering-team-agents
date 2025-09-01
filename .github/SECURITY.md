# Security Policy - Claude Agent Access Control

## 🔒 Owner-Only Claude Agent Access

This repository implements strict access controls for Claude AI agents to protect private code and maintain security.

### Security Controls

**✅ Authorized Access:**
- Repository owner's PRs automatically get Claude review
- Repository owner can add `claude-approved` label to any PR to enable Claude review
- Repository owner can comment `/claude-review` on any PR to trigger manual review
- Repository owner can use `@claude` mentions in issues and comments

**❌ Blocked Access:**
- External contributors cannot trigger Claude agents directly
- Forks cannot inherit Claude agent access
- No automatic Claude review for external PRs without explicit approval

### How It Works

#### 1. Automatic Review (Owner PRs)
```yaml
# claude-secure-review.yml triggers on:
- pull_request from repository owner
- Automatic security check passes
- Claude review runs with full collaborative agent access
```

#### 2. Manual Approval (External PRs)
```yaml
# Repository owner can enable review by:
- Adding "claude-approved" label to PR
- Security check validates label and owner approval
- Claude review runs with security notice
```

#### 3. Manual Trigger
```yaml
# Repository owner can trigger by:
- Commenting "/claude-review" on any PR
- Security check validates owner identity
- Claude review runs immediately
```

### Workflow Files

1. **`claude-secure-review.yml`** - Main secure workflow with owner-only access
2. **`claude.yml`** - Updated to owner-only for @claude mentions  
3. **`claude-code-review.yml`** - Disabled (manual trigger only)

### Security Features

- **Identity Verification**: `github.actor == github.repository_owner`
- **Event Validation**: Checks PR author and approval labels
- **Security Notifications**: Clear messages about access restrictions
- **Audit Trail**: All Claude agent access logged in workflow runs

### For Repository Owner

**Enable Claude Review:**
```bash
# For your own PRs - automatic

# For external PRs - add label
gh pr edit <PR_NUMBER> --add-label "claude-approved"

# Manual trigger - comment on PR
/claude-review
```

**Monitor Access:**
- Check Actions tab for security notifications
- Review workflow logs for unauthorized attempts
- Remove `claude-approved` label to revoke access

### For External Contributors

Claude agent access is restricted for security. The repository owner can enable review by:
1. Adding the `claude-approved` label to your PR
2. Using the `/claude-review` comment trigger
3. Your PR will receive collaborative agent review once approved

This ensures private code remains secure while maintaining the benefits of AI-assisted code review for approved contributions.