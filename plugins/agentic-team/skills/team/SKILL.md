---
name: "team"
description: "Toont welke agents jouw Agentic Team bevat en hoe je ze activeert. Gebruik bij \"welke agents heb ik\", \"wat kan mijn team\", \"toon mijn team\", \"help met mijn agents\" of als de gebruiker niet weet welke agent hij nodig heeft."
---

# Agentic Team — jouw team

Welke agents je hebt hangt af van je licentie, niet van deze plugin. Toon
daarom altijd de actuele lijst — nooit een lijst uit je geheugen of een
eerdere sessie.

## Eerste keer? Eerst de Gids

Gaf `check_license` `onboarding_voltooid: false` terug, of ontbreekt die vlag?
Dan is de gebruiker nieuw. Wijs hem dan **eerst naar de Gids** ("typ: *hoe
gebruik ik mijn team?*"): die maakt hem startklaar (verbinding, context,
werkdata) — pas daarna heeft dit teamoverzicht echt nut. Is `onboarding_voltooid`
al `true`, toon dan gewoon het team hieronder.

## Zo toon je het team

1. Haal de agentlijst op via de `check_license`-tool van de Agentic
   Team-connector.
2. Bouw daaruit een tabel met drie kolommen — **Agent**, **Inzetbaar voor**,
   **Activatiezin** — met per agent zijn `naam` (met emoji), zijn
   `inzetbaar_voor` (of bij ontbreken zijn `beschrijving`) en zijn
   `activatiezin`. Die velden staan in de `check_license`-respons; verzin
   nooit een activatiezin die er niet in staat.
3. Help de gebruiker kiezen welke agent bij zijn vraag past. Agents
   activeren vanzelf op hun activatiezin — de gebruiker hoeft geen
   commando's of namen te kennen.

## Agents buiten het pakket

`check_license` geeft ook `beschikbaar_in_andere_modules` terug: de agents
die de gebruiker nog niet heeft. Noem die **alleen als de gebruiker er zelf
naar vraagt** (bv. "wat mis ik nog?", "wat zit er niet in mijn pakket?").
Antwoord dan per agent in **één neutrale zin** met zijn naam en de module die
hem ontgrendelt — dit is een menukaart, geen advertentie: geen verkooptaal,
geen aansporing om te upgraden.

## Ketens

Je team kan ook als keten samenwerken (één opdracht, meerdere agents, één eindresultaat):

- **Commerciële keten (lead-to-cash)** — Van marktonderzoek tot getekende deal en delivery-aanpak: Researcher vindt prospects, Pipeline Manager kwalificeert, Outreach Specialist benadert, Dealmaker sluit, Delivery Architect ontwerpt de uitvoering.
- **Content-keten (thought leadership)** — Van positionering naar publicatieklare content: Marktmaker bepaalt thema's en segmenten, SEO/GEO Specialist onderzoekt welke vragen je doelgroep aan Google en aan AI-assistenten stelt en levert de contentbriefing, De Stem kiest de thought-leadership-hoeken, Content Strateeg schrijft en plant.
- **Klantsucces-keten (van deal naar groeiende klant)** — Van getekende deal naar werkende klant en groeisignaal: Dealmaker sluit de deal, Delivery Architect ontwerpt de uitvoeraanpak, Customer Success Manager begeleidt onboarding, bewaakt retentie en signaleert groeikansen terug naar de Dealmaker voor upsell.

Tip voor elke werkdag: plan "Start mijn dag" als terugkerende geplande taak
(werkdagen, bv. 07:00) — dan ligt het dagplan klaar vóór de dag begint.
