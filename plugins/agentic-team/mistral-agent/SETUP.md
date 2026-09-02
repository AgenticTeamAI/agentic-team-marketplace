# Setup — Agentic Team in Mistral Le Chat

Vereist: Mistral Le Chat op de **webversie**, met toegang tot custom
MCP-connectors (abonnementsafhankelijk; op Team/Enterprise kan een beheerder
connectors eerst moeten toestaan).

1. **Voeg de connector toe**: open in Le Chat de **Connectors**-pagina →
   *Add Connector* → tab *Custom MCP Connector*. Naam: `Agentic Team`.
   Server-URL:
   `https://www.agentic-team.ai/api/mcp/k/PLAK-HIER-JE-SLEUTEL/mcp`
   (vervang het placeholder-segment door je licentiesleutel; de URL is
   daarmee geheim — deel hem niet).
2. **Kies géén OAuth**: laat de authenticatie leeg (je sleutel zit al in de
   URL). De OAuth-optie van Le Chat vereist dynamische clientregistratie en
   strandt bij onze server bewust vóór het inlogscherm — dat is geen
   storing, dus niet blijven proberen.
3. **Per gesprek activeren**: zet de Agentic Team-connector aan in het
   gesprek (tools-/connectormenu bij het invoerveld) en plak de inhoud van
   `AGENT-INSTRUCTIE.md` als eerste bericht.
4. Test met *"Start mijn dag"* — Le Chat hoort het orchestrator-playbook
   per fase op te halen.

Let op: of Le Chat vóór schrijfacties (les indienen, bronprofiel opslaan) om
jouw bevestiging vraagt, bepaalt Le Chat zelf — reken er niet op en lees het
resultaat na. Zelfde licentie als je Claude-plugin: één team, meerdere
omgevingen.
