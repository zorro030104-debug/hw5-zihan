---
name: support-ticket-triage
description: Classifies customer support tickets into categories (e.g., billing, bug, account issue, feature request) and assigns priority and escalation level. Use when analyzing customer complaints, support requests, or service issues.
---

## When to use
Use this skill when:
- A user provides a customer support ticket, complaint, or feedback
- You need to classify the issue into a category
- You need to assess urgency or priority
- You need to determine whether the issue should be escalated

## When NOT to use
Do not use this skill when:
- The input is not a customer support request
- The task is general conversation or brainstorming
- The user is asking for subjective opinions unrelated to support issues

## Expected Inputs
- A text description of a customer issue, complaint, or request

Example:
"I was charged twice for my subscription and need a refund."

## Steps
1. Read and understand the ticket content
2. Identify key signals (keywords, tone, intent)
3. Call the script to:
   - Classify the ticket category
   - Assign a priority level (low, medium, high)
   - Determine whether escalation is needed
4. Summarize the result clearly

## Output Format
Return a structured result:

- Category: (billing / bug / account issue / feature request / other)
- Priority: (low / medium / high)
- Escalation: (yes / no)
- Reason: brief explanation

## Limitations
- Keyword-based classification may not fully capture complex intent
- Very short or vague tickets may lead to uncertain classification
- Does not replace human judgment in critical situations