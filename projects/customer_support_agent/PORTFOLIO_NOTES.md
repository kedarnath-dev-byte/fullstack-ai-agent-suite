# Portfolio Notes: Customer Support Agent

## My Role

I maintain this project in my `fullstack-ai-agent-suite` portfolio as a customer-support automation case study. My focus is on understanding the workflow, documenting the support-domain architecture, and explaining how routing, specialist agents, guardrails, and CSAT scoring work together.

## What This Project Demonstrates

- Customer intent classification
- Order, billing, technical, escalation, and resolution agents
- Simulated customer, order, billing, and knowledge-base data
- Guardrails for response safety and PII protection
- CSAT prediction and resolution summary generation
- FastAPI backend and React frontend for support workflows

## Architecture Summary

The pipeline models a support ticket lifecycle:

```text
Intake Router
  -> Order Support / Billing Support / Technical Support
  -> Escalation Agent
  -> Resolution and CSAT Agent
```

The intake agent routes the problem to the right specialist. Specialist agents use domain tools, and the final agent creates a clean resolution summary.

## Why The Design Matters

Customer support systems need accuracy, safety, and escalation. This architecture avoids forcing one agent to solve everything. It also includes response safety checks so the system is less likely to expose sensitive data or approve unsafe actions.

## Interview Talking Points

- I can explain how intent routing works in a support workflow.
- I can explain why billing and order tools are separated.
- I can explain how response guardrails protect customers and the business.
- I can explain how CSAT prediction can be used as an operational signal.

## Future Improvements

- Add ticket history persistence
- Add integration tests for each scenario
- Add sample UI screenshots
- Add human handoff status tracking
