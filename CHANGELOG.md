# Changelog

## 1.21.0 — 2026-08-19

- Interne verankering van de agent↔datadomein-koppeling in de registry. Geen functionele wijziging voor jou — updaten is optioneel.

## 1.20.0 — 2026-08-19

- **Werkgeheugen (Logboek)**: je team houdt nu één gedeeld logboek bij — sessielogs en lopende werkstukken (zoals conceptdocumenten) blijven vindbaar over sessies heen. Agents lezen bij de start van een sessie hun lopende werk terug en sluiten sessies met een wezenlijke uitkomst af met een logboek-entry. Bij de Notion-route komt de Logboek-database automatisch mee met de kernstructuur; de Coördinator of Gids richt hem éénmalig met je in.
- De bron-intake legt nu ook vast wáár je logboek leeft (nieuw veld `werkgeheugen` in het databronnen-profiel); een profiel-update overschrijft voortaan alleen nog de velden die je wijzigt.
- Plugin-metadata uitgebreid (licentie- en repository-veld) en de installatie-instructies volgen de actuele Claude-app.

## 1.17.1 — 2026-08-09

- **Connector-URL vereenvoudigd**: de plugin verbindt nu rechtstreeks met het beveiligde connector-endpoint; je licentiesleutel gaat via de `license_key`-config (zoals altijd). De oude URL met een `PLAK-HIER-JE-SLEUTEL`-placeholder is weg — die kon een verwarrende foutmelding geven als de sleutel nog niet was ingevuld.

## 1.17.0 — 2026-08-07

- **Teamoverzicht altijd actueel**: vraag je "welke agents heb ik?" of "wat kan mijn team?", dan haalt de `team`-skill de agentlijst nu live op bij je licentie in plaats van een vaste lijst te tonen. Een nieuwe agent in jouw modules zie je dus meteen, zonder dat je de plugin hoeft te updaten.
- Vraag je expliciet wat je nog niet hebt ("wat mis ik nog?"), dan noemt het teamoverzicht nu ook de agents buiten je huidige modules, met de module die ze ontgrendelt — neutraal vermeld, geen verkooptaal.
- Interne opschoning: plugin-versienummer staat nu op één plek.

## 1.16.0 — 2026-08-07

- **Nieuwe agent: 💚 Customer Success Manager** (Complete-pakket, nu **19 agents**): bewaakt de klantrelatie na de deal — onboarding, gezondheidschecks, risicosignalen vóór een verlenging, groeisignalen terug naar de Dealmaker. Activeer met "Klantgezondheid check [klant]" of "Onboarding [klant]".
- **Nieuwe keten: klantsucces-keten** — Dealmaker → Delivery Architect → Customer Success Manager, van getekende deal naar werkende klant en groeisignaal. Samen met de bestaande commerciële en content-ketens zijn dat nu **drie ketens** in de `ketens`-skill.
- **Content-keten uitgebreid** met de SEO/GEO Specialist: Marktmaker → SEO/GEO Specialist → De Stem → Content Strateeg — de contentbriefing (welke vragen je doelgroep stelt) is er nu vóórdat er geschreven wordt.
- **Nieuw commando `/chief`**: expliciete ingang naast de activatiezin "Start mijn dag" om je Coördinator te starten.
- **Minder ruis in je lessen**: agents loggen een les nu alleen als de sessie een patroon opleverde dat hun aanpak had veranderd — geen les is een normale uitkomst. Elke les vermeldt voortaan ook waar hij vandaan komt (eigen redenering, geverifieerde bron of herhaalde waarneming).

## 1.10.4 — 2026-07-17

- **Plugin hernoemd naar `agentic-team`** (was agentic-team-complete) — er is één plugin, dus de toevoeging vervalt. Had je agentic-team-complete geïnstalleerd? Verwijder die en installeer **agentic-team**; je connector en licentiesleutel blijven gewoon werken.

## 1.10.3 — 2026-07-17

- **agentic-team-essentials verwijderd.** Er is nog één plugin: **agentic-team-complete** — je licentie bepaalt welke modules actief zijn. Had je essentials geïnstalleerd? Verwijder die en installeer agentic-team-complete; je connector en licentiesleutel blijven gewoon werken.

## 1.10.2 — 2026-07-17

- Beschrijvingen en installatie-instructies vernieuwd naar de module-opzet: installeer altijd **agentic-team-complete**; je licentie bepaalt welke modules actief zijn.
- **agentic-team-essentials** is gemarkeerd als legacy en wordt niet meer verkocht.

## 1.10.1 — 2026-07-16

- **Definitieve naam: Coördinator.** De hernoemde agent uit 1.10.0 heet definitief Coördinator (niet Regisseur). Zelfde agent — activatiezinnen zoals "Start mijn dag" en je connector blijven ongewijzigd.
- Update binnenhalen: `/plugin update agentic-team-complete` (of `agentic-team-essentials`).

## 1.10.0 — 2026-07-16

- **De Orchestrator heet voortaan Regisseur** — zelfde agent, duidelijker naam. Activatiezinnen ("Start mijn dag") en je connector blijven ongewijzigd; alleen de naam in skills en teamoverzichten is bijgewerkt.
- Update binnenhalen: `/plugin update agentic-team-complete` (of `agentic-team-essentials`).

## 1.9.0 — 2026-07-16

- Niet apart uitgebracht: de wijzigingen van 1.9.0 zijn dezelfde dag meegegaan in 1.9.1 hieronder. (Entry achteraf toegevoegd 19-08-2026 om het versiegat in deze changelog te dichten.)

## 1.9.1 — 2026-07-16

- **Modulair abonnement**: het team is opgebouwd uit een vaste Core met stapelbare modules (Growth, Visibility, Sales, Delivery, Strategy, Backoffice) en drie bundels Start / Scale / Complete. Je licentie bepaalt welke modules actief zijn; een agent buiten je modules vertelt precies welke module hem ontgrendelt.
- **Teamgeheugen in de bron-intake**: de intake richt nu ook je eigen "Lessen & Inzichten" in — als vijfde database (Notion), als `lessen.json` (werkbestanden) of als vijfde kopje (document). Zo leest elke agent zijn eerdere lessen terug.
- Update binnenhalen: `/plugin update agentic-team-complete` (of `agentic-team-essentials`).

## 1.8.0 — 2026-07-16

- **Fiscale normen actueel**: de Controller en Administratie rekenen met de actuele fiscale normbedragen. (Entry achteraf toegevoegd 19-08-2026; de release zelf was er wel, alleen de changelog-regel ontbrak.)

## 1.7.0 — 2026-07-16

- Interne opruiming: platform-tiers samengevoegd tot de twee pakketten (essentials/complete). Geen functionele wijziging voor jou — bestaande licenties en connector-URLs blijven gewoon werken; updaten is optioneel.

## 1.6.1 — 2026-07-16

- **Twee nieuwe platforms: ChatGPT en Microsoft 365 Copilot** — per plugin vind je `chatgpt-agent/` en `copilot-agent/` met een agent-instructie en stap-voor-stap setup. Zelfde licentie en connector-URL als je Claude-plugin; playbooks blijven server-side.
- **Outreach Specialist: ingebouwde spelregels** — concepten-only, opt-in-check voor koude e-mail (NL-recht), verplichte afmeldmogelijkheid, altijd gepersonaliseerd, geen scraping, menselijke review verplicht. Bescherming voor jouw account en compliance.
- Update binnenhalen: `/plugin update agentic-team-complete` (of `agentic-team-essentials`).

## 1.6.0 — 2026-07-16

- **Notion-werkwijzer — je team in de gratis Notion AI**: vraag de Orchestrator om een "Notion-werkwijzer" en je krijgt een pagina in je eigen Notion met de werkregels van jouw team. Stel die in via Settings → Notion AI → Add Instructions en de standaard Notion AI werkt voortaan volgens die regels — geen Custom Agents of credits nodig. De bron-intake wijst je op deze optie.
- `notion-agent/SETUP.md` benoemt nu de plan-eisen en credit-kosten van Notion Custom Agents, met de gratis werkwijzer-route als alternatief.
- Update binnenhalen: `/plugin update agentic-team-complete` (of `agentic-team-essentials`).

## 1.5.2 — 2026-07-15

- **Nieuw platform: Notion Custom Agents** — je Agentic Team draait nu ook ín Notion (Business/Enterprise). Per plugin vind je `notion-agent/AGENT-INSTRUCTIE.md` + `SETUP.md`: connectie toevoegen, instructie plakken, klaar. Zelfde licentie, zelfde playbooks, twee omgevingen.
- **Slimmere databronnen**: de bron-intake kent nu exacte Notion-database-schema's, en alle agents volgen strikte Notion-werkregels (nooit select-opties of structuren toevoegen zonder voorstel). Werkt ook met je bestáánde CRM/todo-databases — benoem ze in je bronprofiel.
- Playbooks: lokale JSON-werkbestanden als aanbevolen route zonder CRM (v1.4.x–1.5.x-reeks).

## 1.4.0 — 2026-07-15

- **Playbooks zijn nu pure methodiek**: vaste database- en bestandsverwijzingen zijn verwijderd. Je agents werken met wat jíj aanreikt (gesprek, projectkennis of je eigen gekoppelde bronnen) en verzinnen nooit data. Een adaptieve databronnen-laag volgt in een latere release.
- **Makkelijker verbinden**: de vooringevulde connector-URL bevat nu een placeholder — vervang alleen `PLAK-HIER-JE-SLEUTEL` door je licentiesleutel in het connector-dialoog.
- Update binnenhalen: `/plugin update agentic-team-complete` (of `agentic-team-essentials`).

## 1.3.1 — 2026-07-15

- **Vindbaarheid**: elke agent-skill vermeldt nu de letterlijke activatiezin (bv. "Start mijn dag") zodat Claude hem automatisch herkent — slash-commando's zijn niet nodig.
- **Nieuwe skill `team`**: vraag "welke agents heb ik?" of "wat kan mijn team?" en je krijgt het volledige teamoverzicht met activatiezinnen en ketens.
- Update binnenhalen: `/plugin update agentic-team-complete` (of `agentic-team-essentials`).

## 1.3.0 — 2026-07-15

- **🔗 Agent-ketens** (Complete): nieuwe skill `ketens` — de Orchestrator draait de commerciële keten (lead-to-cash) of de content-keten in één sessie via subagents, met gestructureerde overdrachten en één samengevat eindresultaat. Alle 18 agents zijn nu ook als subagent beschikbaar.
- Update binnenhalen: `/plugin update agentic-team-complete`.

## 1.2.0 — 2026-07-15

- **Nieuwe agent: 🧲 SEO/GEO Specialist** (Complete-pakket, nu 18 agents): vindbaarheid in Google én AI-assistenten (ChatGPT, Claude, Perplexity) — audits, zoekwoord-/vraagstrategie en GEO-rapporten.
- **Orchestrator**: instructie voor automatisch geplande dagstart (werkdagen 07:00) via Claude geplande taken.
- Update binnenhalen: `/plugin update agentic-team-complete` (of `agentic-team-essentials`).

## 1.1.0 — 2026-07-15

Eerste publieke release: marketplace met `agentic-team-essentials` (6 agents) en `agentic-team-complete` (17 agents). Playbooks worden per fase geserveerd via de Agentic Team-connector; de plugin bevat uitsluitend de menukaart.
