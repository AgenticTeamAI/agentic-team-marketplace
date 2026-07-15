---
name: ketens
description: Draait een complete agent-keten in één sessie — bv. de commerciële keten (lead-to-cash) of de content-keten. Gebruik bij "draai de commerciële keten", "run de content-keten" of "laat het team dit samen oppakken".
---

# 🔗 Agent-ketens

Jij orkestreert als Orchestrator een keten van agents in één sessie, in plaats
van losse chats met handmatige overdrachten.

### Commerciële keten (lead-to-cash)

Van marktonderzoek tot getekende deal en delivery-aanpak: Researcher vindt prospects, Pipeline Manager kwalificeert, Outreach Specialist benadert, Dealmaker sluit, Delivery Architect ontwerpt de uitvoering.

`researcher → pipeline-manager → outreach-specialist → dealmaker → delivery-architect`

### Content-keten (thought leadership)

Van positionering naar publicatieklare content: Marktmaker bepaalt thema's en segmenten, De Stem kiest de thought-leadership-hoeken, Content Strateeg schrijft en plant.

`marktmaker → de-stem → content-strateeg`

## Zo draai je een keten

1. Haal via `check_license` je agentlijst op en bevestig kort met de gebruiker
   wat de input is (bv. het segment of het thema).
2. Zet per ketenstap een **subagent** in (de agents van deze plugin zijn als
   subagent beschikbaar): geef hem de opdracht plus de gestructureerde
   overdracht van de vorige stap. Onafhankelijke stappen mogen parallel.
3. Bewaak de rode draad: controleer elke overdracht op volledigheid voordat de
   volgende stap start.
4. Sluit af met **één samengevat eindresultaat** voor de gebruiker: wat er per
   stap is opgeleverd, welke beslissingen zijn genomen en wat de vervolgacties
   zijn — plus een geanonimiseerde les via `log_lesson`.

**Fallback:** ondersteunt jouw omgeving geen subagents (of kan een subagent
niet bij de connector)? Draai de keten dan zelf sequentieel in deze sessie:
haal per stap het playbook van die agent op via `get_playbook` en voer de rol
uit, met dezelfde overdrachtsstructuur tussen de stappen.
