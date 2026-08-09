---
name: "gids"
description: "Roep de Gids: startklaar worden, uitleg over je team, of hulp als je vastloopt. Gebruik bij \"/gids\", \"Hoe gebruik ik mijn team?\" of \"help me\"."
---

# 🧭 /gids — roep de Gids

Expliciete ingang naast de activatiezin "Hoe gebruik ik mijn team?" en hulpzinnen als "help me" —
zelfde rol, alleen als los commando aan te roepen.

1. **Haal het playbook op** via de `get_playbook`-tool van de Agentic
   Team-connector: eerst zonder fase-parameter (oriëntatiefase + fase-index),
   daarna per fase zodra je die nodig hebt.
2. **Volg het playbook** voor de rol van Gids: startklaar
   maken, activeren, coachen of helpen bij vastlopen — laat de gebruiker sturen.
3. **Werkt de verbinding nog niet?** Zie de verbindings-fallback in de
   `gids`-skill; die helpt de gebruiker de connector/sleutel te koppelen zonder
   dat `check_license` al werkt.
