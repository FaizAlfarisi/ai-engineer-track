# Visualization Doctrine

Use the cheapest visual that answers fastest. 

## Response ladder
`one-line answer → table → ASCII → Mermaid → generated chart → API docs → screenshot/GIF`

## When to use
| Question | Visual | Notes |
|---------|--------|-------|
| Parts and connections | Mermaid `flowchart` / C4-lite subgraphs | Keep ≤12 nodes; split if larger |
| Time/order | Mermaid `sequenceDiagram` | Show actors and messages clearly |
| Entities/relations | Mermaid `erDiagram` | For data models |
| States/transitions | Mermaid `stateDiagram-v2` | For lifecycles |
| File layout | ASCII tree | In chat/notebooks |
| Tradeoffs | table | Always prefer for comparisons |
| Data insights | chart (matplotlib/Plotly/Vega-Lite) | Only when insight matters, not decoration |
| API contract | Swagger `/docs` + OpenAPI | For FastAPI projects |
| Bug story | 7-row chain table | Use `notes/DEBUGGING.md` format |
| Changes | diff snippet + before/after | Show minimal diff |

## Anti-overuse rules
- One visual per concept, max 2 per response
- Labels ≤6 words
- Chat/notebooks = ASCII/tables; files/GitHub/VS Code = Mermaid
- GitHub-safe Mermaid only (avoid experimental features)
- C4-lite via `flowchart` subgraphs
- D2/PlantUML only local/deep diagrams if needed
- No decoration
