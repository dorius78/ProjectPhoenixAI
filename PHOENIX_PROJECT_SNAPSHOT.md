# ============================================================
# PROJECT PHOENIX AI
# MASTER PROJECT SNAPSHOT
# ============================================================

Snapshot generato: 2026-08-29T12:10:28.328194

## CARTELLA PRINCIPALE

C:\ProjectPhoenixAI

## STRUTTURA COMPLETA

```text
├── AI
│   ├── __init__.py
│   └── main.py
├── Archive
│   └── E27_E40_HISTORICAL_20260826_223518
│       ├── e27_10_10_single_demo_order.py
│       ├── e27_10_2_symbol_audit.py
│       ├── e27_10_5_patch.py
│       ├── e27_10_6_dry_run_test.py
│       ├── e27_10_7_full_dry_run.py
│       ├── e27_10_9_phoenix_mt5_pre_live.py
│       ├── e27_11_2_close_dry_run.py
│       ├── e27_11_3_real_demo_close.py
│       ├── e27_11_position_lifecycle_audit.py
│       ├── e27_12_10_patch.py
│       ├── e27_12_11_live_sync_integration_audit.py
│       ├── e27_12_12_live_loop_flow_audit.py
│       ├── e27_12_13_open_position_lifecycle_audit.py
│       ├── e27_12_14_full_integration_connection_audit.py
│       ├── e27_12_14_open_position_builder_audit.py
│       ├── e27_12_15_execution_result_contract_audit.py
│       ├── e27_12_16_execution_return_contract.py
│       ├── e27_12_17_mt5_result_payload_audit.py
│       ├── e27_12_18_mt5_result_field_audit.py
│       ├── e27_12_19_mt5_result_contract_deep_audit.py
│       ├── e27_12_1_lifecycle_orchestration_audit.py
│       ├── e27_12_20_position_id_propagation_audit.py
│       ├── e27_12_21_mt5_bridge_result_audit.py
│       ├── e27_12_22_mt5_position_ticket_audit.py
│       ├── e27_12_23_mt5_result_object_audit.py
│       ├── e27_12_24_patch.py
│       ├── e27_12_25_execution_position_contract_audit.py
│       ├── e27_12_26_patch.py
│       ├── e27_12_28_simulated_mt5_contract_test.py
│       ├── e27_12_29_failed_execution_safety_test.py
│       ├── e27_12_2_mt5_phoenix_sync_audit.py
│       ├── e27_12_30_simulated_mt5_sync_test.py
│       ├── e27_12_31_mt5_close_disappearance_sync_test.py
│       ├── e27_12_32_position_close_lifecycle_audit.py
│       ├── e27_12_33_mt5_close_sync_design_audit.py
│       ├── e27_12_34_execution_close_contract_audit.py
│       ├── e27_12_35_closed_position_flow_audit.py
│       ├── e27_12_36_external_mt5_close_contract_audit.py
│       ├── e27_12_37_patch.py
│       ├── e27_12_38_external_mt5_close_full_simulation.py
│       ├── e27_12_39_closed_position_process_audit.py
│       ├── e27_12_40_close_routing_audit.py
│       ├── e27_12_41_close_routing_patch.py
│       ├── e27_12_42_external_close_full_pipeline_test.py
│       ├── e27_12_43_external_close_complete_services_test.py
│       ├── e27_12_44_closed_trade_builder_audit.py
│       ├── e27_12_45_closed_trade_mt5_metadata_patch.py
│       ├── e27_12_46_external_close_mt5_metadata_full_test.py
│       ├── e27_12_47_normal_close_result_contract_audit.py
│       ├── e27_12_48_normal_close_mt5_contract_audit.py
│       ├── e27_12_49_mt5_close_result_contract_audit.py
│       ├── e27_12_50_close_result_contract_patch.py
│       ├── e27_12_50b_close_contract_state.py
│       ├── e27_12_50c_close_result_tail.py
│       ├── e27_12_52_normal_close_full_pipeline_test.py
│       ├── e27_12_53_normal_close_failure_safety_test.py
│       ├── e27_12_54_close_contract_integration_audit.py
│       ├── e27_12_55_close_ticket_propagation_test.py
│       ├── e27_12_55_test_fix.py
│       ├── e27_12_56_mt5_lifecycle_final_audit.py
│       ├── e27_12_57_execution_engine_contract_audit.py
│       ├── e27_12_58_mt5_open_result_propagation_audit.py
│       ├── e27_12_59_execution_open_return_audit.py
│       ├── e27_12_60_mt5_open_execute_contract_audit.py
│       ├── e27_12_61_open_result_propagation_test.py
│       ├── e27_12_62_open_position_controller_propagation_test.py
│       ├── e27_12_62a_open_position_method_audit.py
│       ├── e27_12_62b_open_position_mt5_metadata_test.py
│       ├── e27_12_63_position_controller_failure_safety_test.py
│       ├── e27_12_64_mt5_open_recovery_no_duplicate_test.py
│       ├── e27_12_64a_magic_recovery_audit.py
│       ├── e27_12_64b_test_fix.py
│       ├── e27_12_65_double_sync_safety_test.py
│       ├── e27_12_66_external_close_no_reopen_safety_test.py
│       ├── e27_12_66a_test_fix.py
│       ├── e27_12_67_position_lifecycle_integration_test.py
│       ├── e27_12_68_normal_close_result_lifecycle_test.py
│       ├── e27_12_68a_test_fix.py
│       ├── e27_12_69_normal_close_position_reset_audit.py
│       ├── e27_12_69a_normal_close_position_reset_patch.py
│       ├── e27_12_69b_reset_location_audit.py
│       ├── e27_12_69c_normal_close_position_reset_patch.py
│       ├── e27_12_70_duplicate_close_idempotency_audit.py
│       ├── e27_12_71_duplicate_trade_database_audit.py
│       ├── e27_12_72_database_implementation_search.py
│       ├── e27_12_73_database_trade_schema_audit.py
│       ├── e27_12_74_closed_position_idempotency_audit.py
│       ├── e27_12_75_trade_idempotency_key_audit.py
│       ├── e27_12_76_database_idempotency_api_audit.py
│       ├── e27_12_77_database_has_trade_patch.py
│       ├── e27_12_78_idempotency_insertion_point_audit.py
│       ├── e27_12_79_trade_idempotency_patch.py
│       ├── e27_12_7_patch.py
│       ├── e27_12_80a_test_fix.py
│       ├── e27_12_8_2_mt5_state_audit.py
│       ├── e27_12_8_3_historical_ticket_audit.py
│       ├── e27_12_8_sync_test.py
│       ├── e27_12_9_live_loop_audit.py
│       ├── e27_12_position_lifecycle_audit.py
│       ├── e27_13_full_system_roadmap_audit.py
│       ├── e27_15_analysis_engine_pipeline_audit.py
│       ├── e27_16_decision_layer_audit.py
│       ├── e27_17_decision_logic_audit.py
│       ├── e27_18_market_analysis_data_audit.py
│       ├── e27_19_indicator_data_source_audit.py
│       ├── e27_20_indicator_data_quality_audit.py
│       ├── e27_21_decision_score_stress_audit.py
│       ├── e27_22_brain_logic_weight_audit.py
│       ├── e27_23_decision_weight_matrix_audit.py
│       ├── e27_24_risk_ai_decision_interface_audit.py
│       ├── e27_25_risk_limits_logic_audit.py
│       ├── e27_26_risk_architecture_audit.py
│       ├── e27_27_risk_trade_integration_audit.py
│       ├── e27_28_trade_manager_integration_audit.py
│       ├── e27_29_trade_builder_audit.py
│       ├── e27_30_execution_trade_contract_audit.py
│       ├── e27_31_mt5_bridge_execution_contract_audit.py
│       ├── e27_31a_mt5_bridge_class_audit.py
│       ├── e27_32_mt5_ticket_propagation_audit.py
│       ├── e27_33_sync_mt5_duplicate_code_audit.py
│       ├── e27_34_remove_duplicate_sync_block.py
│       ├── e27_35_sync_structure_verification.py
│       ├── e27_37_decision_core_deep_audit.py
│       ├── e27_38_decision_engine_behavioral_test.py
│       ├── e27_39_contradictory_signals_audit.py
│       ├── e27_40_decision_contradiction_fix_precheck.py
│       ├── e27_40b_decision_contradiction_patch.py
│       ├── e27_40c_exact_patch_target_audit.py
│       ├── e27_40d_decision_contradiction_patch.py
│       ├── e27_40e_exact_decision_contradiction_patch.py
│       ├── e27_40f_exact_decision_core_source_audit.py
│       ├── e27_40g_decision_contradiction_patch.py
│       ├── e27_41_decision_risk_trade_end_to_end_audit.py
│       ├── e27_42_end_to_end_behavioral_test.py
│       ├── e27_43_signal_manager_gate_audit.py
│       ├── e27_44_signal_threshold_behavioral_test.py
│       ├── e27_45_min_confidence_source_audit.py
│       ├── e27_46_strong_signal_gate_target_audit.py
│       ├── e27_47_strong_signal_confidence_gate_patch.py
│       ├── e27_50_decision_signal_trade_builder_audit.py
│       ├── e27_51_trade_manager_trade_builder_audit.py
│       ├── e27_52_risk_ai_trade_builder_contract_audit.py
│       ├── e27_53_risk_gate_trade_contract_test.py
│       ├── e27_54_execution_engine_audit.py
│       ├── e27_57_execution_validator_contract_patch.py
│       ├── e27_57b_execution_validator_contract_patch.py
│       ├── e27_57c_execution_validator_contract_patch.py
│       ├── e27_58_execution_validator_behavioral_test.py
│       ├── e27_59_position_controller_execution_report_test.py
│       ├── e27_8_5_end_to_end_test.py
│       └── e27_8_7_risk_gate_test.py
├── Config
│   ├── __init__.py
│   ├── mt5_credentials.example.py
│   ├── mt5_credentials.py
│   └── settings.py
├── Core
│   ├── Tests
│   ├── analysis_engine.py
│   ├── backtest_engine.py
│   ├── calmar_ratio.py
│   ├── core_system.py
│   ├── core_system.py.d44.bak
│   ├── core_system.py.d44_ohclink.bak
│   ├── core_system.py.phase_d3.bak
│   ├── equity_curve.py
│   ├── exit_manager.py
│   ├── exit_manager.py.bak
│   ├── exit_manager.py.d411_before_fix.bak
│   ├── exit_manager.py.d44.bak
│   ├── exit_manager.py.d44.final.bak
│   ├── exit_manager.py.d46.bak
│   ├── exit_manager.py.d46_priority.bak
│   ├── kelly_criterion.py
│   ├── live_trading_engine.py
│   ├── live_trading_engine.py.c121_backup
│   ├── live_trading_engine.py.c132_backup
│   ├── live_trading_engine.py.E27.12.10.backup
│   ├── live_trading_engine.py.E27.12.26.backup
│   ├── live_trading_engine.py.E27.12.37.backup
│   ├── live_trading_engine.py.E27.12.41.backup
│   ├── live_trading_engine.py.E27.12.45.backup
│   ├── live_trading_engine.py.E27.12.69.backup
│   ├── live_trading_engine.py.E27.12.69C.backup
│   ├── live_trading_engine.py.E27.12.7.backup
│   ├── live_trading_engine.py.E27.12.79.backup
│   ├── live_trading_engine.py.E27.34.backup
│   ├── market_analyzer.py
│   ├── market_regime_detector.py
│   ├── market_scanner.py
│   ├── monthly_statistics.py
│   ├── omega_ratio.py
│   ├── paper_decision_bridge.py
│   ├── paper_trading_engine.py
│   ├── payoff_ratio.py
│   ├── performance_analytics.py
│   ├── performance_analytics_calculator.py
│   ├── performance_analytics_report.py
│   ├── performance_report.py
│   ├── phoenix_brain.py
│   ├── phoenix_brain_logic.py
│   ├── phoenix_brain_logic.py.E27.40.backup
│   ├── phoenix_brain_logic.py.E27.40D.backup
│   ├── phoenix_brain_logic.py.E27.40G.backup
│   ├── portfolio_manager.py
│   ├── position_controller.py
│   ├── position_controller.py.d44.bak
│   ├── position_controller.py.d44.final.bak
│   ├── position_manager.py
│   ├── position_monitor.py
│   ├── profit_to_drawdown.py
│   ├── recovery_factor.py
│   ├── report_csv.py
│   ├── report_exporter.py
│   ├── report_factory.py
│   ├── report_formats.py
│   ├── report_html.py
│   ├── report_json.py
│   ├── report_pdf.py
│   ├── report_service.py
│   ├── report_statistics.py
│   ├── risk_drawdown.py
│   ├── risk_limits.py
│   ├── risk_manager.py
│   ├── risk_position_size.py
│   ├── risk_statistics.py
│   ├── sharpe_ratio.py
│   ├── signal_manager.py
│   ├── signal_manager.py.E27.47.backup
│   ├── smart_money.py
│   ├── smart_money_fvg.py
│   ├── smart_money_liquidity.py
│   ├── smart_money_orderblocks.py
│   ├── smart_money_structure.py
│   ├── sortino_ratio.py
│   ├── strategy_discovery.py
│   ├── supervisor.py
│   ├── symbol_statistics.py
│   ├── timeframe_statistics.py
│   ├── trade_builder.py
│   ├── trade_journal.py
│   ├── trade_manager.py
│   ├── trade_report.py
│   ├── trade_statistics.py
│   ├── trading_guard.py
│   ├── trading_guard.py.phase_d3.bak
│   ├── ulcer_index.py
│   └── win_loss_ratio.py
├── Data
│   ├── Indicators
│   │   ├── Documentation
│   │   │   ├── BRAIN_INTERFACE.md
│   │   │   └── PHOENIX_BRAIN.md
│   │   ├── __init__.py
│   │   ├── adx.py
│   │   ├── atr.py
│   │   ├── bollinger.py
│   │   ├── ema.py
│   │   ├── indicator_manager.py
│   │   ├── macd.py
│   │   ├── PHOENIX_MASTER.md
│   │   ├── rsi.py
│   │   ├── sma.py
│   │   ├── stochastic.py
│   │   └── volume.py
│   ├── __init__.py
│   ├── candle_manager.py
│   ├── market_data.py
│   ├── market_provider.py
│   ├── mt5_provider.py
│   ├── price_manager.py
│   ├── PROJECT_STATUS.md
│   ├── symbols.py
│   └── yfinance_provider.py
├── Database
│   ├── __init__.py
│   ├── database_manager.py
│   ├── database_manager.py.c121_backup
│   └── database_manager.py.E27.12.77.backup
├── Docs
│   ├── Docs
│   │   ├── Docs
│   │   │   ├── Docs
│   │   │   │   ├── Docs
│   │   │   │   │   ├── 05_CHANGELOG.md
│   │   │   │   │   └── 06_TODO.md
│   │   │   │   └── 04_ARCHITETTURA.md
│   │   │   └── 03_ROADMAP.md
│   │   └── 02_DECISIONI_PROGETTUALI.md
│   ├── 001_Project_Vision.md
│   ├── 002_System_Architecture.md
│   ├── 003_Decision_Engine.md
│   ├── 00_PROJECT_BOOK.md
│   ├── 01_SPRINTS.md
│   └── TRADE_LIFECYCLE.md
├── Execution
│   ├── execution_builder.py
│   ├── execution_engine.py
│   ├── execution_engine.py.bak
│   ├── execution_report.py
│   ├── execution_report.py.E27.66.backup
│   ├── execution_validator.py
│   ├── mt5_broker.py
│   ├── mt5_broker.py.c121_backup
│   └── mt5_broker.py.E27.10.5.backup
├── Logs
│   ├── logger.py
│   └── phoenix_autonomous_20260826_133349.jsonl
├── MT5_Bridge
│   ├── INSTALLA_MT5_BRIDGE.txt
│   ├── mt5_bridge.py
│   ├── mt5_execution.py
│   ├── mt5_execution_backup.txt
│   ├── mt5_execution_before_risk_fix.py
│   ├── mt5_execution_recovered.py
│   ├── mt5_execution_recovered.py.E27.12.24.backup
│   ├── mt5_execution_recovered.py.E27.12.50.backup
│   ├── mt5_execution_recovered_before_protect.py
│   └── run_mt5_phoenix.py
├── PHOENIX_SNAPSHOTS
│   └── 20260820_000111
│       ├── git_diff.txt
│       ├── git_diff_stat.txt
│       ├── git_log.txt
│       ├── git_status.txt
│       ├── PHOENIX_MASTER_STATE.md
│       ├── project_files.txt
│       └── SNAPSHOT_INFO.txt
├── Position_Manager
│   ├── position_manager.py
│   ├── position_manager_before_protect_bridge.py
│   └── position_manager_before_protect_bridge_v2.py
├── Tests
│   ├── find_symbol.py
│   ├── run_all_tests.py
│   ├── test_analysis.py
│   ├── test_backtest.py
│   ├── test_core.py
│   ├── test_end_to_end.py
│   ├── test_execution.py
│   ├── test_exit_manager.py
│   ├── test_exit_manager.py.d410_before_cleanup.bak
│   ├── test_exit_manager.py.d411_before_fix.bak
│   ├── test_exit_manager.py.d49.bak
│   ├── test_exit_manager.py.d49_failed.bak
│   ├── test_indicators.py
│   ├── test_market.py
│   ├── test_mt5_connection.py
│   ├── test_position_controller.py
│   ├── test_position_cycle.py
│   ├── test_position_manager.py
│   ├── test_position_monitor.py
│   ├── test_risk.py
│   ├── test_signal.py
│   ├── test_signal.py.E27.49.backup
│   ├── test_trade_builder.py
│   ├── test_trade_manager.py
│   ├── test_trading_guard.py
│   └── test_trading_guard.py.phase_d3.bak
├── .gitignore
├── audit_dependencies.py
├── audit_modules.py
├── create_phoenix_snapshot.py
├── E38_1_SAFE_MASTER_AUTOFIX_REPORT.txt
├── find_symbol.py
├── performance_report.csv
├── performance_report.html
├── performance_report.json
├── performance_report.pdf
├── performance_report.txt
├── phoenix_ai.db
├── PHOENIX_AUTO_AUDIT_REPORT.txt
├── phoenix_backtest.db
├── phoenix_backtest_h4.db
├── phoenix_c110_duplicates.py
├── phoenix_c111_idempotency.py
├── PHOENIX_COMPLETE_AUDIT.txt
├── phoenix_db_test.db
├── PHOENIX_DEMO_LIVE_ROUTING_AUDIT.txt
├── phoenix_e70_lifecycle_test.db
├── PHOENIX_FINAL_COMPLETION_AUDIT.txt
├── PHOENIX_FULL_PROJECT_DUMP.txt
├── phoenix_live.db
├── PHOENIX_MASTER_AUDIT_REPORT.txt
├── PHOENIX_MASTER_FINAL_STATUS.txt
├── PHOENIX_MASTER_INSPECTION.txt
├── PHOENIX_MASTER_STATE.md
├── phoenix_v6_test.db
├── README.md
├── run.py
└── run_phoenix_live_demo.py
```

## FILE PYTHON

- `AI\__init__.py`
- `AI\main.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_10_10_single_demo_order.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_10_2_symbol_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_10_5_patch.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_10_6_dry_run_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_10_7_full_dry_run.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_10_9_phoenix_mt5_pre_live.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_11_2_close_dry_run.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_11_3_real_demo_close.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_11_position_lifecycle_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_10_patch.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_11_live_sync_integration_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_12_live_loop_flow_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_13_open_position_lifecycle_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_14_full_integration_connection_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_14_open_position_builder_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_15_execution_result_contract_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_16_execution_return_contract.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_17_mt5_result_payload_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_18_mt5_result_field_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_19_mt5_result_contract_deep_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_1_lifecycle_orchestration_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_20_position_id_propagation_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_21_mt5_bridge_result_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_22_mt5_position_ticket_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_23_mt5_result_object_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_24_patch.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_25_execution_position_contract_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_26_patch.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_28_simulated_mt5_contract_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_29_failed_execution_safety_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_2_mt5_phoenix_sync_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_30_simulated_mt5_sync_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_31_mt5_close_disappearance_sync_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_32_position_close_lifecycle_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_33_mt5_close_sync_design_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_34_execution_close_contract_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_35_closed_position_flow_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_36_external_mt5_close_contract_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_37_patch.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_38_external_mt5_close_full_simulation.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_39_closed_position_process_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_40_close_routing_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_41_close_routing_patch.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_42_external_close_full_pipeline_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_43_external_close_complete_services_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_44_closed_trade_builder_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_45_closed_trade_mt5_metadata_patch.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_46_external_close_mt5_metadata_full_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_47_normal_close_result_contract_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_48_normal_close_mt5_contract_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_49_mt5_close_result_contract_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_50_close_result_contract_patch.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_50b_close_contract_state.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_50c_close_result_tail.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_52_normal_close_full_pipeline_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_53_normal_close_failure_safety_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_54_close_contract_integration_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_55_close_ticket_propagation_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_55_test_fix.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_56_mt5_lifecycle_final_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_57_execution_engine_contract_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_58_mt5_open_result_propagation_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_59_execution_open_return_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_60_mt5_open_execute_contract_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_61_open_result_propagation_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_62_open_position_controller_propagation_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_62a_open_position_method_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_62b_open_position_mt5_metadata_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_63_position_controller_failure_safety_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_64_mt5_open_recovery_no_duplicate_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_64a_magic_recovery_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_64b_test_fix.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_65_double_sync_safety_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_66_external_close_no_reopen_safety_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_66a_test_fix.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_67_position_lifecycle_integration_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_68_normal_close_result_lifecycle_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_68a_test_fix.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_69_normal_close_position_reset_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_69a_normal_close_position_reset_patch.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_69b_reset_location_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_69c_normal_close_position_reset_patch.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_70_duplicate_close_idempotency_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_71_duplicate_trade_database_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_72_database_implementation_search.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_73_database_trade_schema_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_74_closed_position_idempotency_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_75_trade_idempotency_key_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_76_database_idempotency_api_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_77_database_has_trade_patch.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_78_idempotency_insertion_point_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_79_trade_idempotency_patch.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_7_patch.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_80a_test_fix.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_8_2_mt5_state_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_8_3_historical_ticket_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_8_sync_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_9_live_loop_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_12_position_lifecycle_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_13_full_system_roadmap_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_15_analysis_engine_pipeline_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_16_decision_layer_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_17_decision_logic_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_18_market_analysis_data_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_19_indicator_data_source_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_20_indicator_data_quality_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_21_decision_score_stress_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_22_brain_logic_weight_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_23_decision_weight_matrix_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_24_risk_ai_decision_interface_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_25_risk_limits_logic_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_26_risk_architecture_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_27_risk_trade_integration_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_28_trade_manager_integration_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_29_trade_builder_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_30_execution_trade_contract_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_31_mt5_bridge_execution_contract_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_31a_mt5_bridge_class_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_32_mt5_ticket_propagation_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_33_sync_mt5_duplicate_code_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_34_remove_duplicate_sync_block.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_35_sync_structure_verification.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_37_decision_core_deep_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_38_decision_engine_behavioral_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_39_contradictory_signals_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_40_decision_contradiction_fix_precheck.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_40b_decision_contradiction_patch.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_40c_exact_patch_target_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_40d_decision_contradiction_patch.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_40e_exact_decision_contradiction_patch.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_40f_exact_decision_core_source_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_40g_decision_contradiction_patch.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_41_decision_risk_trade_end_to_end_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_42_end_to_end_behavioral_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_43_signal_manager_gate_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_44_signal_threshold_behavioral_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_45_min_confidence_source_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_46_strong_signal_gate_target_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_47_strong_signal_confidence_gate_patch.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_50_decision_signal_trade_builder_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_51_trade_manager_trade_builder_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_52_risk_ai_trade_builder_contract_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_53_risk_gate_trade_contract_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_54_execution_engine_audit.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_57_execution_validator_contract_patch.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_57b_execution_validator_contract_patch.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_57c_execution_validator_contract_patch.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_58_execution_validator_behavioral_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_59_position_controller_execution_report_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_8_5_end_to_end_test.py`
- `Archive\E27_E40_HISTORICAL_20260826_223518\e27_8_7_risk_gate_test.py`
- `audit_dependencies.py`
- `audit_modules.py`
- `Config\__init__.py`
- `Config\mt5_credentials.example.py`
- `Config\mt5_credentials.py`
- `Config\settings.py`
- `Core\analysis_engine.py`
- `Core\backtest_engine.py`
- `Core\calmar_ratio.py`
- `Core\core_system.py`
- `Core\equity_curve.py`
- `Core\exit_manager.py`
- `Core\kelly_criterion.py`
- `Core\live_trading_engine.py`
- `Core\market_analyzer.py`
- `Core\market_regime_detector.py`
- `Core\market_scanner.py`
- `Core\monthly_statistics.py`
- `Core\omega_ratio.py`
- `Core\paper_decision_bridge.py`
- `Core\paper_trading_engine.py`
- `Core\payoff_ratio.py`
- `Core\performance_analytics.py`
- `Core\performance_analytics_calculator.py`
- `Core\performance_analytics_report.py`
- `Core\performance_report.py`
- `Core\phoenix_brain.py`
- `Core\phoenix_brain_logic.py`
- `Core\portfolio_manager.py`
- `Core\position_controller.py`
- `Core\position_manager.py`
- `Core\position_monitor.py`
- `Core\profit_to_drawdown.py`
- `Core\recovery_factor.py`
- `Core\report_csv.py`
- `Core\report_exporter.py`
- `Core\report_factory.py`
- `Core\report_formats.py`
- `Core\report_html.py`
- `Core\report_json.py`
- `Core\report_pdf.py`
- `Core\report_service.py`
- `Core\report_statistics.py`
- `Core\risk_drawdown.py`
- `Core\risk_limits.py`
- `Core\risk_manager.py`
- `Core\risk_position_size.py`
- `Core\risk_statistics.py`
- `Core\sharpe_ratio.py`
- `Core\signal_manager.py`
- `Core\smart_money.py`
- `Core\smart_money_fvg.py`
- `Core\smart_money_liquidity.py`
- `Core\smart_money_orderblocks.py`
- `Core\smart_money_structure.py`
- `Core\sortino_ratio.py`
- `Core\strategy_discovery.py`
- `Core\supervisor.py`
- `Core\symbol_statistics.py`
- `Core\timeframe_statistics.py`
- `Core\trade_builder.py`
- `Core\trade_journal.py`
- `Core\trade_manager.py`
- `Core\trade_report.py`
- `Core\trade_statistics.py`
- `Core\trading_guard.py`
- `Core\ulcer_index.py`
- `Core\win_loss_ratio.py`
- `create_phoenix_snapshot.py`
- `Data\__init__.py`
- `Data\candle_manager.py`
- `Data\Indicators\__init__.py`
- `Data\Indicators\adx.py`
- `Data\Indicators\atr.py`
- `Data\Indicators\bollinger.py`
- `Data\Indicators\ema.py`
- `Data\Indicators\indicator_manager.py`
- `Data\Indicators\macd.py`
- `Data\Indicators\rsi.py`
- `Data\Indicators\sma.py`
- `Data\Indicators\stochastic.py`
- `Data\Indicators\volume.py`
- `Data\market_data.py`
- `Data\market_provider.py`
- `Data\mt5_provider.py`
- `Data\price_manager.py`
- `Data\symbols.py`
- `Data\yfinance_provider.py`
- `Database\__init__.py`
- `Database\database_manager.py`
- `Execution\execution_builder.py`
- `Execution\execution_engine.py`
- `Execution\execution_report.py`
- `Execution\execution_validator.py`
- `Execution\mt5_broker.py`
- `find_symbol.py`
- `Logs\logger.py`
- `MT5_Bridge\mt5_bridge.py`
- `MT5_Bridge\mt5_execution.py`
- `MT5_Bridge\mt5_execution_before_risk_fix.py`
- `MT5_Bridge\mt5_execution_recovered.py`
- `MT5_Bridge\mt5_execution_recovered_before_protect.py`
- `MT5_Bridge\run_mt5_phoenix.py`
- `phoenix_c110_duplicates.py`
- `phoenix_c111_idempotency.py`
- `Position_Manager\position_manager.py`
- `Position_Manager\position_manager_before_protect_bridge.py`
- `Position_Manager\position_manager_before_protect_bridge_v2.py`
- `run.py`
- `run_phoenix_live_demo.py`
- `Tests\find_symbol.py`
- `Tests\run_all_tests.py`
- `Tests\test_analysis.py`
- `Tests\test_backtest.py`
- `Tests\test_core.py`
- `Tests\test_end_to_end.py`
- `Tests\test_execution.py`
- `Tests\test_exit_manager.py`
- `Tests\test_indicators.py`
- `Tests\test_market.py`
- `Tests\test_mt5_connection.py`
- `Tests\test_position_controller.py`
- `Tests\test_position_cycle.py`
- `Tests\test_position_manager.py`
- `Tests\test_position_monitor.py`
- `Tests\test_risk.py`
- `Tests\test_signal.py`
- `Tests\test_trade_builder.py`
- `Tests\test_trade_manager.py`
- `Tests\test_trading_guard.py`

## DOCUMENTAZIONE MARKDOWN

- `Data\Indicators\Documentation\BRAIN_INTERFACE.md`
- `Data\Indicators\Documentation\PHOENIX_BRAIN.md`
- `Data\Indicators\PHOENIX_MASTER.md`
- `Data\PROJECT_STATUS.md`
- `Docs\001_Project_Vision.md`
- `Docs\002_System_Architecture.md`
- `Docs\003_Decision_Engine.md`
- `Docs\00_PROJECT_BOOK.md`
- `Docs\01_SPRINTS.md`
- `Docs\Docs\02_DECISIONI_PROGETTUALI.md`
- `Docs\Docs\Docs\03_ROADMAP.md`
- `Docs\Docs\Docs\Docs\04_ARCHITETTURA.md`
- `Docs\Docs\Docs\Docs\Docs\05_CHANGELOG.md`
- `Docs\Docs\Docs\Docs\Docs\06_TODO.md`
- `Docs\TRADE_LIFECYCLE.md`
- `PHOENIX_MASTER_STATE.md`
- `PHOENIX_SNAPSHOTS\20260820_000111\PHOENIX_MASTER_STATE.md`
- `README.md`

## GIT

Il repository Git è la fonte dello storico/versionamento.

## REGOLE

- Non cancellare file senza verifica.
- Non creare moduli duplicati.
- Conservare lo storico Git.
- Verificare prima di ogni commit.
- Nessun LIVE reale senza validazione completa.

## SNAPSHOT

File totali rilevati: 374
File Python rilevati: 283
File Markdown rilevati: 18

Questo file serve come indice centrale del progetto.
