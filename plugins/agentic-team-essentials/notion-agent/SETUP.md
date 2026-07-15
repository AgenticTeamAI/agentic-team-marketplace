# Setup — Agentic Team Essentials als Notion Custom Agent

Vereist: Notion Business of Enterprise (custom MCP-connecties), en een
workspace-admin.

1. **Zet custom MCP aan**: Settings → Notion AI → AI connectors →
   *Enable Custom MCP servers*.
2. **Voeg de connectie toe**: Add connection → *Custom MCP server* →
   URL: `https://www.agentic-team.ai/api/mcp/k/PLAK-HIER-JE-SLEUTEL/mcp`
   (vervang het placeholder-segment door je licentiesleutel; de URL is
   daarmee geheim — deel hem niet). Naam: `Agentic Team`.
3. **Maak een Custom Agent** (Notion AI → Agents → New): plak de inhoud van
   `AGENT-INSTRUCTIE.md` als instructie en koppel de Agentic Team-connectie
   aan deze agent.
4. Test met *"Start mijn dag"* — de agent hoort het orchestrator-playbook
   per fase op te halen. Write-acties (les indienen, bronprofiel opslaan)
   vragen in Notion standaard om jouw bevestiging.

Zelfde licentie als je Claude-plugin: één team, twee omgevingen.
