from Logs.logger import Logger


class LearningEngine:
    """
    PROJECT PHOENIX AI
    Learning Engine
    E76.98

    Approva e memorizza strategie già validate,
    conservando strategia, validazione e cronologia.
    Espone le strategie apprese senza permettere
    modifiche dirette allo stato interno.
    Nessuna modifica autonoma dei parametri.
    Nessuna esecuzione ordini.
    """

    def __init__(self):
        self.learned_strategies = []
        self.learning_history = []

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
            result = {
                "learned": False,
                "decision": "REJECTED",
                "reasons": approval["reasons"]
            }

            self.learning_history.append({
                "strategy": (
                    strategy.copy()
                    if isinstance(strategy, dict)
                    else strategy
                ),
                "validation": (
                    validation.copy()
                    if isinstance(validation, dict)
                    else validation
                ),
                "decision": "REJECTED"
            })

            return result

        entry = {
            "strategy": strategy.copy(),
            "validation": validation.copy()
        }

        if not any(
            item["strategy"] == strategy
            for item in self.learned_strategies
        ):
            self.learned_strategies.append(entry)

        result = {
            "learned": True,
            "decision": "LEARNED",
            "reasons": []
        }

        self.learning_history.append({
            "strategy": strategy.copy(),
            "validation": validation.copy(),
            "decision": "LEARNED"
        })

        return result

    def get_learned_strategies(self):
        return [
            {
                "strategy": item["strategy"].copy(),
                "validation": item["validation"].copy()
            }
            for item in self.learned_strategies
        ]

    def get_learning_history(self):
        return [
            {
                "strategy": (
                    item["strategy"].copy()
                    if isinstance(item["strategy"], dict)
                    else item["strategy"]
                ),
                "validation": (
                    item["validation"].copy()
                    if isinstance(item["validation"], dict)
                    else item["validation"]
                ),
                "decision": item["decision"]
            }
            for item in self.learning_history
        ]

    def reset(self):
        self.learned_strategies.clear()
        self.learning_history.clear()
