# Agentic Team — Plugin Marketplace

Officiële plugin-marketplace van [Agentic Team](https://www.agentic-team.ai) (Obeya Insights): jouw AI-team als Claude-plugin.

## Installatie (2 minuten)

1. Open Claude (chat, Cowork of Claude Code) → **Customize → Plugins** → voeg deze marketplace toe: `Obeya-Insights/agentic-team-marketplace` — of in Claude Code: `/plugin marketplace add Obeya-Insights/agentic-team-marketplace`
2. Installeer de plugin die bij je licentie hoort: **agentic-team-essentials** (6 agents) of **agentic-team-complete** (18 agents) — die geeft je de agents als skills.
3. **Verbind je persoonlijke connector** (werkt op claude.ai, desktop-app én Cowork): ga naar Instellingen → Connectors → *Add custom connector* en plak jouw persoonlijke connector-URL uit de wizard of welkomstmail (`https://www.agentic-team.ai/api/mcp/k/<jouw-sleutel>/mcp`). Behandel die URL als een wachtwoord. *Alternatief in Claude Code:* installeer de plugin met `--config license_key=<jouw sleutel>` — dan is de connector meteen mee geconfigureerd.
4. Klaar. Zeg bijvoorbeeld *"Start mijn dag"* en de Orchestrator gaat aan de slag.

**Tip:** plan *"Start mijn dag"* in als terugkerende taak in Claude (werkdagen, bv. 07:00) — dan ligt je dagplan elke ochtend klaar zonder dat je erom hoeft te vragen.

## Hoe het werkt

De plugin bevat alleen de menukaart van je team. De playbooks zelf worden per werkfase en volledig actueel opgehaald via de beveiligde Agentic Team-connector — updates zijn dus direct live, zonder dat je iets hoeft te installeren.

Na een release van nieuwe menukaart-versies: `/plugin update agentic-team-essentials` of `agentic-team-complete` (zie [CHANGELOG](CHANGELOG.md)).

## Support

support@agentic-team.ai · [agentic-team.ai](https://www.agentic-team.ai)
