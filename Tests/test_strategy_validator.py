from Core.strategy_validator import StrategyValidator


def valid_result():
    return {
        "net_profit": 500,
        "roi": 5.0,
        "win_rate": 60.0,
        "profit_factor": 1.5,
        "max_drawdown": 200,
        "total_trades": 50
    }


def test_strategy_validator_accepts_valid_result():

    validator = StrategyValidator()

    result = validator.validate(
        valid_result(),
        {
            "min_net_profit": 100,
            "min_win_rate": 50,
            "min_profit_factor": 1.2,
            "max_drawdown": 500,
            "min_trades": 30
        }
    )

    assert result["valid"] is True
    assert result["decision"] == "VALID"
    assert result["reasons"] == []


def test_strategy_validator_rejects_low_profit():

    validator = StrategyValidator()

    result = validator.validate(
        valid_result(),
        {
            "min_net_profit": 1000
        }
    )

    assert result["valid"] is False
    assert result["decision"] == "INVALID"
    assert len(result["reasons"]) == 1


def test_strategy_validator_ignores_missing_criteria():

    validator = StrategyValidator()

    result = validator.validate(
        valid_result(),
        {
            "min_net_profit": 100
        }
    )

    assert result["valid"] is True


def test_strategy_validator_rejects_invalid_result():

    validator = StrategyValidator()

    result = validator.validate(
        None,
        {
            "min_net_profit": 100
        }
    )

    assert result["valid"] is False
    assert result["decision"] == "INVALID"
    assert result["reasons"]
