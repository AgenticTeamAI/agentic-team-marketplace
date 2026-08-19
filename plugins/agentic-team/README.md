# Agentic Team

*Your AI business team as a Claude plugin (Dutch-language product). Requires an [Agentic Team](https://www.agentic-team.ai) license.*

Jouw AI-team als Claude-plugin: 20 agents in zeven teams (Core, Groei, Zichtbaarheid, Sales, Delivery, Strategie, Backoffice). De plugin bevat de menukaart van je team; de playbooks zelf worden per werkfase en altijd actueel opgehaald via de beveiligde Agentic Team-connector. Je licentie bepaalt welke modules actief zijn.

## Installatie

1. Voeg de marketplace toe — **claude.ai/desktop/Cowork:** Settings → Plugins → Add → *Add marketplace* → *Add from a repository*: `AgenticTeamAI/agentic-team-marketplace` (zorg dat *Sync automatically* aanstaat) · **Claude Code:** `/plugin marketplace add AgenticTeamAI/agentic-team-marketplace`.
2. Installeer **agentic-team**. In Claude Code kan dat direct mét je licentiesleutel: `--config license_key=<jouw sleutel>` — dan is de connector meteen geconfigureerd.
3. Nog geen sleutel? Start op [agentic-team.ai](https://www.agentic-team.ai) — de wizard geeft je je persoonlijke sleutel en connector-link ("Verbind met Claude").

## Gebruik

- Zeg **"Start mijn dag"** (of `/chief`) — de Coördinator maakt je dagplan.
- **"Welke agents heb ik?"** (`team`-skill) toont live je agentlijst op basis van je licentie.
- Elke agent heeft zijn eigen activatiezin; agents buiten je modules vertellen zelf welke module hen ontgrendelt.
- Eerste keer? Je Gids 🧭 maakt je startklaar: *"Hoe gebruik ik mijn team?"*

## Licentie & data

De plugin-bestanden zijn openbaar in te zien; gebruik vereist een geldige licentiesleutel — playbooks en teamconfiguratie worden server-side geserveerd via de connector op `www.agentic-team.ai`. Behandel je persoonlijke connector-URL als een wachtwoord.

Support: [support@agentic-team.ai](mailto:support@agentic-team.ai) · Changelog: [CHANGELOG.md](../../CHANGELOG.md)
