# Agentic Team — Plugin Marketplace

Officiële plugin-marketplace van [Agentic Team](https://www.agentic-team.ai): jouw AI-team als Claude-plugin.

## Installatie (2 minuten)

1. **Voeg de marketplace toe** (claude.ai, desktop-app of Cowork): ga naar **Settings → Plugins → Add → Add marketplace → Add from a repository** en plak `AgenticTeamAI/agentic-team-marketplace`. Zorg dat **Sync automatically** aanstaat — dan blijft je team automatisch actueel.
2. **Installeer agentic-team**: klik op *Install*. De plugin geeft je alle agents als skills, bij élk abonnement. Je licentie bepaalt welke modules (Core, Groei, Zichtbaarheid, Sales, Delivery, Strategie, Backoffice) actief zijn; een agent buiten je modules vertelt zelf welke module hem ontgrendelt.
3. **Verbind de connector**: ga in de plugin naar **Connectors** en klik op *Install* bij `agentic-team` — Claude opent de connector-dialoog met het adres al ingevuld. Handmatig kan ook: Settings → Connectors → *Add custom connector*, en plak `https://connector.agentic-team.ai/mcp`. Die URL is voor iedereen dezelfde en bevat geen geheim.
4. **Log in**: bevestig de connector en log in op het e-mailadres waarop je bent uitgenodigd — met een inloglink, of met Google of Microsoft op datzelfde adres. Er is geen sleutel om te bewaren.
5. Klaar. Zeg bijvoorbeeld *"Start mijn dag"* (of gebruik `/chief`) en de Coördinator gaat aan de slag.

<details>
<summary>Claude Code (voor ontwikkelaars)</summary>

```shell
/plugin marketplace add AgenticTeamAI/agentic-team-marketplace
/plugin install agentic-team@agentic-team
```

De plugin brengt de connector zelf mee; bij het eerste gebruik opent Claude de inlogflow op je e-mailadres. Zet auto-update aan via `/plugin` → *Marketplaces* → *Enable auto-update*.

</details>

**Tip:** plan *"Start mijn dag"* in als terugkerende taak in Claude (werkdagen, bv. 07:00) — dan ligt je dagplan elke ochtend klaar zonder dat je erom hoeft te vragen.

## Hoe het werkt

De plugin bevat alleen de menukaart van je team. De playbooks zelf worden per werkfase en volledig actueel opgehaald via de beveiligde Agentic Team-connector — updates zijn dus direct live, zonder dat je iets hoeft te installeren.

Nieuwe menukaart-versies komen vanzelf binnen zolang *Sync automatically* aanstaat (zie [CHANGELOG](CHANGELOG.md)); in Claude Code: `/plugin update agentic-team`.

Naast de agent-skills bevat de plugin je agents ook als **subagents** (zodat de Coördinator ketens in één sessie kan draaien), een `team`-skill ("welke agents heb ik?" — toont je actuele agentlijst live, op basis van je licentie), een `ketens`-skill (de ketennamen; welke ketens jouw team kent en hoe ze lopen, komt van de server) en de commando's `/chief` en `/gids`.

**Wat hier bewust níet in staat (sinds 1.45):** de werkwijze van je agents, de ketenstappen, de cadans van de dagstart en de rekenlogica voor je dashboard. Dat wordt allemaal geserveerd via de connector of leeft in je werkruimte. Deze repo is de menukaart — niet meer. `plugin-manifest.json` somt op welke bestanden door de generator zijn gemaakt; de CI weigert alles wat daar niet in staat.

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

## Voor ontwikkelaars: hoe deze repo wordt bijgewerkt

Alles onder `plugins/` en `.claude-plugin/` is gegenereerd door `installer/build_plugin.py` uit de privé-repo `agent-architecture`, op de commit in `agent-architecture.lock.json`. Bijwerken: **altijd ná de merge in arch, op de main-SHA — nooit vanaf een feature-branch**: `python3 scripts/sync_plugin.py` (bouwt op een commit van arch-main, schrijft precies de manifest-bestanden en de lock), daarna `python3 scripts/check_zero_ip.py`. Volgorde bij een release: eerst de site deployen die de velden uit `serverContract` in `plugin-manifest.json` serveert (`check_license`: `ketens`, `volgende_stap`), dán syncen — anders verwijzen de stubs naar velden die de server nog niet kent. CI: de menukaart-check (allowlist via het manifest + patroonchecks) op elke PR, en de driftgate `plugin-drift` (verse build op de gepinde commit moet hetzelfde manifest opleveren; arch-main mag niet verder zijn dan de pin) op elke PR én dagelijks.

## Support

support@agentic-team.ai · [agentic-team.ai](https://www.agentic-team.ai)

## Licentie

Deze repository is **bron-inzage (source-available), niet open source**: lezen
en bestuderen mag iedereen, gebruiken mag met een geldige Agentic
Team-licentie, herpubliceren of doorverkopen niet. Zie [LICENSE](LICENSE)
(Nederlands, leidend), [LICENSE.en.md](LICENSE.en.md) (Engelse vertaling; bij
verschil gaat de Nederlandse tekst voor) en [NOTICE](NOTICE). De licentietekst
is een concept: de eerste juridische ronde is verwerkt (versie 0.2,
27-08-2026), een tweede volgt — het blokkerende punt is de tenaamstelling van
Licentiegever (gemarkeerd met `<<JURIST-REVIEW>>`).

> **This repository is source-available, not open source.** Anyone may read
> and study the code; only holders of a valid Agentic Team licence may use
> it. **No text and data mining for AI training.** The rightsholder expressly
> reserves the rights referred to in section 15o of the Dutch Copyright Act
> and article 4(3) of Directive (EU) 2019/790: this material may not be used
> for text and data mining for the development or training of artificial
> intelligence models without prior written permission. Reading and indexing
> by search engines and comparable automated tools is welcome.

**Tekst- en datamining (TDM).** Indexeren en lezen door zoekmachines mag —
daar is deze repo openbaar voor. Gebruik van de inhoud als trainingsdata voor
AI-modellen niet: dat recht is uitdrukkelijk voorbehouden (artikel 15o
Auteurswet, artikel 4 lid 3 Richtlijn (EU) 2019/790), zie artikel 2a van de
LICENSE.

**Bijdragen** zijn welkom onder de DCO 1.1 — onderteken je commits met
`git commit -s`. Zie [CONTRIBUTING.md](CONTRIBUTING.md); het meeste in deze
repo is gegenereerd, dus een issue is vaak nuttiger dan een pull request.
