# Setup — Agentic Team in ChatGPT

Vereist: ChatGPT Plus, Pro, Business, Enterprise of Edu, op de **webversie**
(custom connectors werken niet in de mobiele apps). Op Business/Enterprise/Edu
moet een workspace-admin eerst developer mode toestaan (Workspace settings →
Permissions & roles → Connected data).

1. **Zet developer mode aan**: Settings → Apps → Advanced settings →
   *Developer mode*.
2. **Voeg de connector toe**: Settings → Apps → *Create*. Naam: `Agentic
   Team`. MCP Server URL: `https://connector.agentic-team.ai/mcp`
   (voor iedereen dezelfde, bevat geen geheim). Authenticatie: **OAuth**.
3. **Log in** op het e-mailadres waarop je bent uitgenodigd: je vraagt een
   inloglink aan, of je logt in met Google of Microsoft op datzelfde adres.
   Er is geen sleutel om te bewaren, en je eigen werkruimte werkt gewoon mee.
4. **Per gesprek activeren**: open in een nieuwe chat het **+**-menu bij het
   invoerveld → kies de Agentic Team-app. Plak daarna de inhoud van
   `AGENT-INSTRUCTIE.md` als eerste bericht.
5. Test met *"Start mijn dag"* — ChatGPT hoort het orchestrator-playbook per
   fase op te halen. Schrijfacties (les indienen, bronprofiel opslaan) vragen
   telkens om jouw bevestiging.

Let op: ChatGPT onthoudt de connector-activering niet tussen gesprekken —
stap 4 hoort bij elk nieuw team-gesprek. Lukt inloggen in jouw omgeving
niet, dan werkt de sleutelroute ook: MCP Server URL
`https://www.agentic-team.ai/api/mcp/k/PLAK-HIER-JE-SLEUTEL/mcp`
   (vervang het placeholder-segment door je licentiesleutel; de URL is
   daarmee geheim — deel hem niet). Authenticatie: **No authentication**.
Zelfde licentie als je Claude-plugin: één team, meerdere omgevingen.
