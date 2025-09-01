# Code Review Report: [COMPONENT/FEATURE NAME]

**Date**: [YYYY-MM-DD]  
**Reviewer**: Code Reviewer Agent  
**Files Reviewed**: [list of files or PR/commit reference]

## Executive Summary
**Overall Assessment**: [Pass | Pass with Minor Changes | Requires Major Changes | Reject]  
**Priority Issues**: [count of critical/high/medium/low issues]  
**Ready for Production**: [Yes/No with conditions]

## Security Review
### Critical Issues ⛔ (Fix Before Merge)
- [ ] **[Issue Type]**: [specific vulnerability found]
  - **Location**: [file:line]
  - **Risk**: [potential impact]
  - **Fix**: [specific code change needed]

### Security Recommendations
- [ ] **[Issue Type]**: [security improvement]
  - **Current**: [what code does now]
  - **Recommended**: [better approach]
  - **Rationale**: [why this is safer]

## Reliability Review
### Production Risk Issues 🚨
- [ ] **[Issue Type]**: [reliability concern]
  - **Location**: [file:line]
  - **Scenario**: [when this could fail]
  - **Fix**: [error handling/timeout/retry needed]

### Reliability Improvements
- [ ] **[Issue Type]**: [robustness enhancement]
  - **Current**: [current implementation]
  - **Recommended**: [more reliable approach]

## Performance Review
### Performance Issues (if >1000 users)
- [ ] **[Issue Type]**: [performance bottleneck]
  - **Location**: [file:line]
  - **Impact**: [expected performance degradation]
  - **Fix**: [optimization approach]

## Code Quality
### Maintainability Issues
- [ ] **[Issue Type]**: [maintainability concern]
  - **Location**: [file:line]
  - **Issue**: [why this is hard to maintain]
  - **Suggestion**: [cleaner approach]

## Positive Recognition ✅
### Excellent Practices Found
- **[Pattern/Practice]**: [what was done well]
  - **Location**: [file:line]
  - **Why Good**: [explanation of best practice]

## Collaboration Needed
### Hand-offs Required
- [ ] **Architecture Review**: [complex system design decisions]
- [ ] **UX Review**: [user-facing error messages or flows]
- [ ] **Responsible AI Review**: [AI/ML components or accessibility]
- [ ] **DevOps Review**: [deployment or infrastructure concerns]

## Implementation Recommendations
### Priority 1 (Must Fix) ⛔
- [ ] [specific actionable change]
- [ ] [specific actionable change]

### Priority 2 (Should Fix) ⚠️
- [ ] [specific actionable change]
- [ ] [specific actionable change]

### Priority 3 (Nice to Have) 💡
- [ ] [specific actionable change]
- [ ] [specific actionable change]

## Suggested Code Changes
```[language]
// Current problematic code
[show actual code that needs changing]

// Recommended replacement
[show specific improved code]
```

## Follow-up Actions
- [ ] Schedule architecture review for [specific concerns]
- [ ] Create technical debt ticket for [specific items]
- [ ] Add monitoring for [specific metrics]
- [ ] Update documentation for [specific areas]

## Sign-off
**Status**: [Ready for merge | Needs changes | Needs re-review]  
**Next Steps**: [what should happen next]