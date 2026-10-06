from Logs.logger import Logger


class LearningEngine:
    """
    PROJECT PHOENIX AI
    Learning Engine
    E76.95

    Approva e memorizza strategie già validate.
    Nessuna modifica autonoma dei parametri.
    Nessuna esecuzione ordini.
    """

    def __init__(self):
        self.learned_strategies = []

        Logger.success("Learning Engine V1 inizializzato.")

    def approve(self, strategy, validation):
        if not isinstance(strategy, dict):
            return {
                "approved": False,
                "decision": "REJECTED",
                "reasons": ["Strategia non valida."]
            }

        if not isinstance(validation, dict):
            return {
                "approved": False,
                "decision": "REJECTED",
                "reasons": ["Validazione strategia mancante."]
            }

        if validation.get("valid") is not True:
            return {
                "approved": False,
                "decision": "REJECTED",
                "reasons": validation.get(
                    "reasons",
                    ["Strategia non validata."]
                )
            }

        return {
            "approved": True,
            "decision": "APPROVED",
            "reasons": []
        }

    def learn(self, strategy, validation):
        approval = self.approve(strategy, validation)

        if not approval["approved"]:
            return {
                "learned": False,
                "decision": "REJECTED",
                "reasons": approval["reasons"]
            }

        if strategy not in self.learned_strategies:
            self.learned_strategies.append(strategy.copy())

        return {
            "learned": True,
            "decision": "LEARNED",
            "reasons": []
        }

    def reset(self):
        self.learned_strategies.clear()
