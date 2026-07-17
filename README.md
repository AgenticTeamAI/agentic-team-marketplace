# Agentic Team — Plugin Marketplace

Officiële plugin-marketplace van [Agentic Team](https://www.agentic-team.ai): jouw AI-team als Claude-plugin.

## Installatie (2 minuten)

1. Open Claude (chat, Cowork of Claude Code) → **Customize → Plugins** → voeg deze marketplace toe: `AgenticTeamAI/agentic-team-marketplace` — of in Claude Code: `/plugin marketplace add AgenticTeamAI/agentic-team-marketplace`
2. Installeer **agentic-team-complete** — die geeft je alle agents als skills, bij élk abonnement. Je licentie bepaalt welke modules (Core, Groei, Zichtbaarheid, Sales, Delivery, Strategie, Backoffice) actief zijn; een agent buiten je modules vertelt zelf welke module hem ontgrendelt. *(agentic-team-essentials is legacy en wordt niet meer verkocht.)*
3. **Verbind je persoonlijke connector** (werkt op claude.ai, desktop-app én Cowork): ga naar Instellingen → Connectors → *Add custom connector* en plak jouw persoonlijke connector-URL uit de wizard of welkomstmail (`https://www.agentic-team.ai/api/mcp/k/<jouw-sleutel>/mcp`). Behandel die URL als een wachtwoord. *Alternatief in Claude Code:* installeer de plugin met `--config license_key=<jouw sleutel>` — dan is de connector meteen mee geconfigureerd.
4. Klaar. Zeg bijvoorbeeld *"Start mijn dag"* en de Coördinator gaat aan de slag.

**Tip:** plan *"Start mijn dag"* in als terugkerende taak in Claude (werkdagen, bv. 07:00) — dan ligt je dagplan elke ochtend klaar zonder dat je erom hoeft te vragen.

## Hoe het werkt

De plugin bevat alleen de menukaart van je team. De playbooks zelf worden per werkfase en volledig actueel opgehaald via de beveiligde Agentic Team-connector — updates zijn dus direct live, zonder dat je iets hoeft te installeren.

Na een release van nieuwe menukaart-versies: `/plugin update agentic-team-complete` (zie [CHANGELOG](CHANGELOG.md)).

Naast de agent-skills bevat elke plugin je agents ook als **subagents** (voor ketens die de Coördinator in één sessie draait), een `team`-skill ("welke agents heb ik?") en — in Complete — de `ketens`-skill.

## Ook buiten Claude

Je team draait met dezelfde licentie en connector-URL ook op andere platforms. In elke plugin-map vind je per platform een agent-instructie + stap-voor-stap setup:

| Platform | Map | Let op |
|---|---|---|
| Notion (Custom Agent) | `notion-agent/` | Business/Enterprise + Custom Agents-credits |
| ChatGPT | `chatgpt-agent/` | Developer mode, alleen web, activeren per gesprek |
| Microsoft 365 Copilot | `copilot-agent/` | Bouwen via Copilot Studio |

**Gratis Notion-route:** vraag de Coördinator om de **Notion-werkwijzer** — een pagina die je instelt via Settings → Notion AI → Add Instructions, waarna de standaard Notion AI (zonder add-on) volgens de werkregels van jouw team werkt.

## Bekende eigenaardigheden (desktop-app)

- **Update pakt oude versie?** De desktop-app cachet de marketplace-catalogus. Verwijder de *marketplace* (niet de plugin) en voeg hem opnieuw toe — dan is de catalogus vers en installeert de nieuwste versie. In Claude Code werkt `/plugin update` direct.
- **Geen sleutelvraag bij installatie?** Klopt — gebruik je persoonlijke connector-URL (stap 3 hierboven). Zodra de desktop-app plugin-configuratie ondersteunt, vervalt die stap vanzelf.
- Een oudere pluginversie is nooit blokkerend: playbooks komen altijd actueel van de server; alleen nieuwe *skills* vragen een plugin-update.

## Support

support@agentic-team.ai · [agentic-team.ai](https://www.agentic-team.ai)
