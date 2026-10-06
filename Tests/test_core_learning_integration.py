from Core.core_system import CoreSystem
from Core.learning_engine import LearningEngine
from Core.strategy_validator import StrategyValidator

def test_core_system_initializes_strategy_validator():
    core = CoreSystem()
    assert isinstance(core.strategy_validator, StrategyValidator)

def test_core_system_initializes_learning_engine():
    core = CoreSystem()
    assert isinstance(core.learning_engine, LearningEngine)
