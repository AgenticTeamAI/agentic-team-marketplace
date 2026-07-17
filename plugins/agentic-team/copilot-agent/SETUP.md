# Setup — Agentic Team in Microsoft 365 Copilot

Vereist: toegang tot **Copilot Studio** (maker-rechten in een Power
Platform-omgeving) om de agent te bouwen, en een **Microsoft 365
Copilot-licentie** voor wie hem gebruikt. De lichte "Agent Builder" in de
Copilot-app ondersteunt géén MCP — gebruik Copilot Studio.

1. **Maak een agent** in Copilot Studio (Create → New agent). Plak de inhoud
   van `AGENT-INSTRUCTIE.md` in de instructies van de agent.
2. **Koppel de connector**: Tools → *Add a tool* → *New tool* → *Model
   Context Protocol*. Servernaam: `Agentic Team`. Server-URL:
   `https://www.agentic-team.ai/api/mcp/k/PLAK-HIER-JE-SLEUTEL/mcp`
   (vervang het placeholder-segment door je licentiesleutel; de URL is
   daarmee geheim — deel hem niet). Authenticatie: **None** (je sleutel zit
   al in de URL). Maak de connection aan en kies *Add to agent*.
3. **Publiceer** de agent naar Microsoft 365 Copilot / Teams (Publish).
   Publicatie kan goedkeuring van je Microsoft 365-beheerder vergen.
4. Test met *"Start mijn dag"* — de agent hoort het orchestrator-playbook
   per fase op te halen.

Let op: Power Platform DLP-policies kunnen externe MCP-servers blokkeren —
vraag je beheerder de Agentic Team-server toe te staan als stap 2 faalt.
Zelfde licentie als je Claude-plugin: één team, meerdere omgevingen.
