---
name: "chief"
description: "Start een sessie met je Coördinator — dagplan, ad hoc een agent inzetten of een keten draaien. Gebruik bij \"/chief\" of als expliciete ingang naast \"Start mijn dag\"."
---

# 🔮 /chief — start de Coördinator

Expliciete ingang naast de bestaande activatiezin "Start mijn dag" — zelfde rol,
alleen als los commando aan te roepen.

1. **Haal het playbook op** via de `get_playbook`-tool van de Agentic
   Team-connector: eerst zonder fase-parameter (oriëntatiefase + fase-index),
   daarna per fase zodra je die nodig hebt.
2. **Volg het playbook** voor de rol van Coördinator:
   dagplan, ad hoc een specifieke agent inzetten, of een keten draaien — laat
   de gebruiker sturen wat er vandaag nodig is.
3. **Bij storing**: gebruik de laatst opgehaalde versie uit deze sessie of je
   projectkennis (maximaal 14 dagen oud) en meld dat je op een gecachte versie
   draait.
