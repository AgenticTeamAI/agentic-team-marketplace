---
name: "team"
description: "Toont welke agents jouw Agentic Team bevat en hoe je ze activeert. Gebruik bij \"welke agents heb ik\", \"wat kan mijn team\", \"toon mijn team\", \"help met mijn agents\" of als de gebruiker niet weet welke agent hij nodig heeft."
---

# Agentic Team — jouw team

Welke agents je hebt hangt af van je licentie, niet van deze plugin. Toon
daarom altijd de actuele lijst — nooit een lijst uit je geheugen of een
eerdere sessie.

## Zo toon je het team

1. Haal de agentlijst op via de `check_license`-tool van de Agentic
   Team-connector.
2. Bouw daaruit een tabel met drie kolommen — **Agent**, **Inzetbaar voor**,
   **Activatiezin** — met per agent zijn `naam` (met emoji), zijn
   `inzetbaar_voor` (of bij ontbreken zijn `beschrijving`) en zijn
   `activatiezin`. Die velden staan in de `check_license`-respons; verzin
   nooit een activatiezin die er niet in staat.
3. Staat er een `volgende_stap` in de respons (bv. bij een team dat nog niet
   is ingericht) of een lijst `ketens`? Geef die letterlijk door: de server
   bepaalt wat er eerst moet gebeuren en welke ketens dit team kent.
4. Help de gebruiker kiezen welke agent bij zijn vraag past. Agents
   activeren vanzelf op hun activatiezin — de gebruiker hoeft geen
   commando's of namen te kennen.

## Agents buiten het pakket

`check_license` geeft ook `beschikbaar_in_andere_modules` terug: de agents
die de gebruiker nog niet heeft. Noem die **alleen als de gebruiker er zelf
naar vraagt** (bv. "wat mis ik nog?", "wat zit er niet in mijn pakket?").
Antwoord dan per agent in **één neutrale zin** met zijn naam en de module die
hem ontgrendelt — dit is een menukaart, geen advertentie: geen verkooptaal,
geen aansporing om te upgraden.
