config = statsig.get_config(StatsigUser("user-id"), "thomas")
statsig.check_gate(StatsigUser("user-id"), "thomas")

config_json = config.get_value()
