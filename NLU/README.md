# NLU

This is the main NLU and primary bot that runs when the robot is idling (i.e. not in proactive mode).

Intents are determined via a trained RASA NLU neural network, with intents forwarded to the correct secondary bot so that they can respond appropriately.

Secondary bots may 'lock' te conversation so that subsequent responses from the user are handled by the correct bot, and not subject to the intent prediction of the primary bot.