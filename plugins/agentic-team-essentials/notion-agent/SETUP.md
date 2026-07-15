# Setup — Agentic Team Essentials als Notion Custom Agent

Vereist: Notion Business of Enterprise (custom MCP-connecties), een
workspace-admin, én het Custom Agents-add-on (credits, apart gefactureerd
door Notion — elke agent-run verbruikt credits).

**Gratis alternatief:** stuur het team aan vanuit Claude (de plugin) en laat
het zijn werkdata in jouw Notion bijhouden — de standaard Notion AI kan die
data vervolgens gewoon lezen, samenvatten en doorzoeken zonder add-on. Vraag
de Orchestrator bovendien om de **Notion-werkwijzer**: een pagina die je in
Notion instelt als Instructions-pagina (Settings → Notion AI → Add
Instructions → kies die pagina), waarna de standaard Notion AI automatisch
volgens de werkregels van jouw team werkt. De Custom Agent hieronder is
alleen nodig als je het team ook ín Notion wilt aansturen.

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
