# Support Ticket Triage Skill

## Overview
This project implements a reusable AI skill called support-ticket-triage, which classifies customer support tickets into structured categories and assigns priority and escalation levels.

The skill combines natural language understanding with a deterministic Python script to ensure consistent and reliable results.

## What this skill does
This skill analyzes customer support tickets and:

- Classifies the issue into categories:
  - billing
  - bug
  - account issue
  - feature request
  - other
- Assigns a priority level:
  - low
  - medium
  - high
- Determines whether escalation is needed
- Provides a brief explanation of the decision

## Why I chose this skill
Customer support automation is a critical use case for AI in business and product systems.

This skill reflects a real-world ToB scenario where incoming tickets must be triaged efficiently before being routed to the appropriate team.

It also demonstrates how combining AI reasoning with deterministic logic improves reliability.

## How to use

Run the script with a support ticket as input:

python .agents/skills/support-ticket-triage/scripts/triage_ticket.py "Your ticket text here"

Example:

python .agents/skills/support-ticket-triage/scripts/triage_ticket.py "I was charged twice for my subscription."

## Example Output

{
  "category": "billing",
  "priority": "medium",
  "escalation": "yes",
  "reason": "Detected category signals for billing.",
  "matched_categories": ["billing"],
  "matched_keywords": ["charged", "subscription"]
}

## Script Explanation
The Python script performs:

- Keyword-based classification
- Detection of urgency signals
- Multi-category identification (for complex tickets)
- Priority and escalation logic

This deterministic logic ensures consistent and reproducible results, which cannot be reliably achieved using prompts alone.

## Design Improvement (Iteration)
Initially, the system only supported single-category classification.

This caused issues in complex cases where a ticket contained multiple problems. For example, a ticket describing both a system crash and a login failure was classified as only one category with low priority.

The script was improved to:

- Detect multiple issue types
- Increase priority for multi-issue tickets
- Recommend escalation for more complex scenarios

## Test Cases

### 1. Normal Case
Billing issue with clear keywords  
Example: "I was charged twice for my subscription this month."

### 2. Edge Case
Multiple issues (bug + account issue)  
Example: "The app crashed after I updated it, and now I cannot log in to my account."

### 3. Limited Case
Vague complaint with emotional signals  
Example: "I hate this company. This is terrible."

## Limitations

- Relies on keyword matching rather than deep semantic understanding
- May not fully capture complex or nuanced intent
- Does not replace human judgment in critical cases

## Video Demo
https://vimeo.com/1187105750?share=copy&fl=sv&fe=cigit