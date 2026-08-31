# Agentic Team

*Your AI business team as a Claude plugin (Dutch-language product). Requires an [Agentic Team](https://www.agentic-team.ai) license.*

Jouw AI-team als Claude-plugin: 21 agents in zeven teams (Core, Groei, Zichtbaarheid, Sales, Delivery, Strategie, Backoffice). De plugin bevat de menukaart van je team; de playbooks zelf worden per werkfase en altijd actueel opgehaald via de beveiligde Agentic Team-connector. Je licentie bepaalt welke modules actief zijn.

## Installatie

1. Voeg de marketplace toe — **claude.ai/desktop/Cowork:** Settings → Plugins → Add → *Add marketplace* → *Add from a repository*: `AgenticTeamAI/agentic-team-marketplace` (zorg dat *Sync automatically* aanstaat) · **Claude Code:** `/plugin marketplace add AgenticTeamAI/agentic-team-marketplace`.
2. Installeer **agentic-team**. Ga daarna in de plugin naar **Connectors** en klik op *Install* bij `agentic-team` — Claude opent de connector-dialoog met het adres al ingevuld. Handmatig kan ook: Settings → Connectors → Add custom connector, met `https://connector.agentic-team.ai/mcp`.
3. Bevestig de connector en log in op het e-mailadres waarop je bent uitgenodigd: je vraagt een inloglink aan, of je logt in met Google of Microsoft op datzelfde adres. Er is geen sleutel om te bewaren. Nog geen uitnodiging? Start op [agentic-team.ai](https://www.agentic-team.ai) — de wizard nodigt je uit op je aankoopadres.

## Gebruik

- Zeg **"Start mijn dag"** (of `/chief`) — de Coördinator maakt je dagplan.
- **"Welke agents heb ik?"** (`team`-skill) toont live je agentlijst op basis van je licentie.
- Elke agent heeft zijn eigen activatiezin; agents buiten je modules vertellen zelf welke module hen ontgrendelt.
- Eerste keer? Je Gids 🧭 maakt je startklaar: *"Hoe gebruik ik mijn team?"*
- Ketens ("draai de commerciële keten") laat je door de Coördinator draaien; welke ketens jouw team kent, vertelt `check_license`.
- Even geen verbinding? De plugin bevat geen playbooks; zonder connector werkt alleen de Gids-hulp om je connector te koppelen. Bij een storing in de connector melden je agents dat eerlijk, werken ze hooguit 14 dagen door op de laatst opgehaalde playbook-versie en verzinnen ze nooit playbook-inhoud of data; blijft het misgaan, mail support@agentic-team.ai.

## Licentie & data

De plugin-bestanden zijn openbaar in te zien; gebruik vereist een actieve licentie — playbooks en teamconfiguratie worden server-side geserveerd via de connector op `connector.agentic-team.ai`. De connector-URL is voor iedereen dezelfde en bevat geen geheim; toegang hangt aan het e-mailadres waarmee je inlogt.

Support: [support@agentic-team.ai](mailto:support@agentic-team.ai) · Changelog: [CHANGELOG.md](../../CHANGELOG.md)
