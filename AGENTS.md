# Repository instructions

Use structured CPH as the default for agent-to-agent handoffs. Follow AGENT-INSTRUCTIONS.md, adapting fields to the task. User-facing replies remain clear and appropriately detailed.

Preserve permissions, uncertainty, stop conditions, test outcomes and provenance. Do not add restrictions or make conditions exclusive to save tokens.

Benchmark prompts and locked grade payloads are frozen. Version new experiments separately. Use only synthetic tasks and public primary-source references; exclude private corpora, private paths, credentials and runtime session/message identifiers.

For numerical benchmark changes, run the local reproduction scripts and link checks. Do not rerun models or change grades merely to validate documentation.
