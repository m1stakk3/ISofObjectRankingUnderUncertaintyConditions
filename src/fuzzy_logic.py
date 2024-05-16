import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np


class FuzzyLogic(object):

    def __init__(self):
        # Определение нечетких переменных и их значения
        self.age = ctrl.Antecedent(np.arange(18, 41, 1), "age")
        self.games_played = ctrl.Antecedent(np.arange(0, 83, 1), "games_played")
        self.games_as_starter = ctrl.Antecedent(np.arange(0, 83, 1), "games_as_starter")
        self.minutes_played = ctrl.Antecedent(np.arange(0, 48.1, 0.1), "minutes_played")
        self.field_goals = ctrl.Antecedent(np.arange(0, 15, 0.1), "field_goals")
        self.field_goals_attempts = ctrl.Antecedent(
            np.arange(0, 15, 0.1), "field_goals_attempts"
        )
        self.field_goals_percentage = ctrl.Antecedent(
            np.arange(0, 100, 0.1), "field_goals_percentage"
        )
        self.three_field_goals = ctrl.Antecedent(
            np.arange(0, 15, 0.1), "three_field_goals"
        )
        self.three_field_goals_attempts = ctrl.Antecedent(
            np.arange(0, 15, 0.1), "three_field_goals_attempts"
        )
        self.three_field_goals_percentage = ctrl.Antecedent(
            np.arange(0, 100, 0.1), "three_field_goals_percentage"
        )
        self.two_field_goals = ctrl.Antecedent(np.arange(0, 15, 0.1), "two_field_goals")
        self.two_field_goals_attempts = ctrl.Antecedent(
            np.arange(0, 15, 0.1), "two_field_goals_attempts"
        )
        self.two_field_goals_percentage = ctrl.Antecedent(
            np.arange(0, 100, 0.1), "two_field_goals_percentage"
        )
        self.effective_field_goals = ctrl.Consequent(
            np.arange(0, 100, 0.1), "effective_field_goals"
        )
        self.free_throws = ctrl.Antecedent(np.arange(0, 15, 0.1), "free_throws")
        self.free_throws_attempts = ctrl.Antecedent(
            np.arange(0, 15, 0.1), "free_throws_attempts"
        )
        self.free_throws_percentage = ctrl.Antecedent(
            np.arange(0, 100, 0.1), "free_throws_percentage"
        )
        self.offensive_rebounds = ctrl.Antecedent(
            np.arange(0, 9, 0.1), "offensive_rebounds"
        )
        self.defensive_rebounds = ctrl.Antecedent(
            np.arange(0, 9, 0.1), "defensive_rebounds"
        )
        self.total_rebounds = ctrl.Antecedent(np.arange(0, 18, 0.1), "total_rebounds")
        self.assists = ctrl.Antecedent(np.arange(0, 15, 0.1), "assists")
        self.steals = ctrl.Antecedent(np.arange(0, 5, 0.1), "steals")
        self.blocks = ctrl.Antecedent(np.arange(0, 5, 0.1), "blocks")
        self.turnovers = ctrl.Antecedent(np.arange(0, 7, 0.1), "turnovers")
        self.fouls = ctrl.Antecedent(np.arange(0, 7, 0.1), "fouls")
        self.ppg = ctrl.Antecedent(np.arange(0, 41, 0.1), "ppg")
        self.rating = ctrl.Consequent(np.arange(0, 30, 1), "rating")

    def _set_age_universe(self):
        self.age["high"] = fuzz.trimf(self.age.universe, [18, 19, 23])
        self.age["medium"] = fuzz.trimf(self.age.universe, [22, 26, 32])
        self.age["low"] = fuzz.trimf(self.age.universe, [30, 33, 40])

    def _set_games_played_universe(self):
        self.games_played["low"] = fuzz.trimf(self.games_played.universe, [0, 15, 45])
        self.games_played["medium"] = fuzz.trimf(
            self.games_played.universe, [40, 50, 75]
        )
        self.games_played["high"] = fuzz.trimf(self.games_played.universe, [70, 79, 82])

    def _set_games_as_starter_universe(self):
        self.games_as_starter["low"] = fuzz.trimf(
            self.games_as_starter.universe, [0, 15, 45]
        )
        self.games_as_starter["medium"] = fuzz.trimf(
            self.games_as_starter.universe, [40, 50, 75]
        )
        self.games_as_starter["high"] = fuzz.trimf(
            self.games_as_starter.universe, [70, 79, 82]
        )

    def _set_minutes_played_universe(self):
        self.minutes_played["low"] = fuzz.trimf(
            self.minutes_played.universe, [0, 11, 20]
        )
        self.minutes_played["medium"] = fuzz.trimf(
            self.minutes_played.universe, [15, 26, 35]
        )
        self.minutes_played["high"] = fuzz.trimf(
            self.minutes_played.universe, [30, 40, 48]
        )

    def _set_field_goals_universe(self):
        self.field_goals["low"] = fuzz.trimf(self.field_goals.universe, [0, 2, 4])
        self.field_goals["medium"] = fuzz.trimf(self.field_goals.universe, [3, 4, 6])
        self.field_goals["high"] = fuzz.trimf(self.field_goals.universe, [5, 8, 12])

    def _set_field_goals_attempts_universe(self):
        self.field_goals_attempts["low"] = fuzz.trimf(
            self.field_goals_attempts.universe, [0, 3, 9]
        )
        self.field_goals_attempts["medium"] = fuzz.trimf(
            self.field_goals_attempts.universe, [8, 10, 12]
        )
        self.field_goals_attempts["high"] = fuzz.trimf(
            self.field_goals_attempts.universe, [10, 20, 25]
        )

    def _set_field_goals_percentage_universe(self):
        self.field_goals_percentage["low"] = fuzz.trimf(
            self.field_goals_percentage.universe, [0.0, 0.1, 0.25]
        )
        self.field_goals_percentage["medium"] = fuzz.trimf(
            self.field_goals_percentage.universe, [0.25, 0.3, 0.35]
        )
        self.field_goals_percentage["high"] = fuzz.trimf(
            self.field_goals_percentage.universe, [0.35, 0.45, 1.0]
        )

    def _set_three_field_goals_universe(self):
        self.three_field_goals["low"] = fuzz.trimf(
            self.three_field_goals.universe, [0, 2, 3]
        )
        self.three_field_goals["medium"] = fuzz.trimf(
            self.three_field_goals.universe, [1, 3, 3.1]
        )
        self.three_field_goals["high"] = fuzz.trimf(
            self.three_field_goals.universe, [3, 3.5, 5]
        )

    def _set_three_field_goals_attempts_universe(self):
        self.three_field_goals_attempts["low"] = fuzz.trimf(
            self.three_field_goals_attempts.universe, [0, 2, 4]
        )
        self.three_field_goals_attempts["medium"] = fuzz.trimf(
            self.three_field_goals_attempts.universe, [3, 6, 10]
        )
        self.three_field_goals_attempts["high"] = fuzz.trimf(
            self.three_field_goals_attempts.universe, [9, 12, 15]
        )

    def _set_three_field_goals_percentage_universe(self):
        self.three_field_goals_percentage["low"] = fuzz.trimf(
            self.three_field_goals_percentage.universe, [0.0, 0.1, 0.25]
        )
        self.three_field_goals_percentage["medium"] = fuzz.trimf(
            self.three_field_goals_percentage.universe, [0.25, 0.3, 0.35]
        )
        self.three_field_goals_percentage["high"] = fuzz.trimf(
            self.three_field_goals_percentage.universe, [0.35, 0.45, 1.0]
        )

    def _set_two_field_goals_universe(self):
        self.two_field_goals["low"] = fuzz.trimf(
            self.two_field_goals.universe, [0, 2, 3]
        )
        self.two_field_goals["medium"] = fuzz.trimf(
            self.two_field_goals.universe, [1, 3, 3.1]
        )
        self.two_field_goals["high"] = fuzz.trimf(
            self.two_field_goals.universe, [3, 3.5, 5]
        )

    def _set_two_field_goals_attempts_universe(self):
        self.two_field_goals_attempts["low"] = fuzz.trimf(
            self.two_field_goals_attempts.universe, [0, 2, 4]
        )
        self.two_field_goals_attempts["medium"] = fuzz.trimf(
            self.two_field_goals_attempts.universe, [3, 5, 7]
        )
        self.two_field_goals_attempts["high"] = fuzz.trimf(
            self.two_field_goals_attempts.universe, [6, 8, 20]
        )

    def _set_two_field_goals_percentage_universe(self):
        self.two_field_goals_percentage["low"] = fuzz.trimf(
            self.two_field_goals_percentage.universe, [0.0, 0.1, 0.25]
        )
        self.two_field_goals_percentage["medium"] = fuzz.trimf(
            self.two_field_goals_percentage.universe, [0.25, 0.3, 0.35]
        )
        self.two_field_goals_percentage["high"] = fuzz.trimf(
            self.two_field_goals_percentage.universe, [0.35, 0.45, 1.0]
        )

    def _set_effective_field_goals_universe(self):
        self.effective_field_goals["low"] = fuzz.trimf(
            self.effective_field_goals.universe, [0.0, 0.1, 0.28]
        )
        self.effective_field_goals["medium"] = fuzz.trimf(
            self.effective_field_goals.universe, [0.25, 0.3, 0.43]
        )
        self.effective_field_goals["high"] = fuzz.trimf(
            self.effective_field_goals.universe, [0.42, 0.52, 1.0]
        )

    def _set_free_throws_universe(self):
        self.free_throws["low"] = fuzz.trimf(self.free_throws.universe, [0, 1, 2])
        self.free_throws["medium"] = fuzz.trimf(self.free_throws.universe, [1, 2, 5])
        self.free_throws["high"] = fuzz.trimf(self.free_throws.universe, [4, 6, 10])

    def _set_free_throws_attempts_universe(self):
        self.free_throws_attempts["low"] = fuzz.trimf(
            self.free_throws_attempts.universe, [0, 1, 2]
        )
        self.free_throws_attempts["medium"] = fuzz.trimf(
            self.free_throws_attempts.universe, [1, 2, 5]
        )
        self.free_throws_attempts["high"] = fuzz.trimf(
            self.free_throws_attempts.universe, [4, 6, 10]
        )

    def _set_free_throws_percentage_universe(self):
        self.free_throws_percentage["low"] = fuzz.trimf(
            self.free_throws_percentage.universe, [0.0, 0.3, 0.45]
        )
        self.free_throws_percentage["medium"] = fuzz.trimf(
            self.free_throws_percentage.universe, [0.41, 0.7, 0.78]
        )
        self.free_throws_percentage["high"] = fuzz.trimf(
            self.free_throws_percentage.universe, [0.75, 0.9, 1.0]
        )

    def _set_offensive_rebounds_universe(self):
        self.offensive_rebounds["low"] = fuzz.trimf(
            self.offensive_rebounds.universe, [0, 0.5, 1]
        )
        self.offensive_rebounds["medium"] = fuzz.trimf(
            self.offensive_rebounds.universe, [0.7, 1.2, 1.9]
        )
        self.offensive_rebounds["high"] = fuzz.trimf(
            self.offensive_rebounds.universe, [1.8, 2.6, 5]
        )

    def _set_defensive_rebounds_universe(self):
        self.defensive_rebounds["low"] = fuzz.trimf(
            self.defensive_rebounds.universe, [0, 1.8, 2]
        )
        self.defensive_rebounds["medium"] = fuzz.trimf(
            self.defensive_rebounds.universe, [1.9, 3.6, 4]
        )
        self.defensive_rebounds["high"] = fuzz.trimf(
            self.defensive_rebounds.universe, [3.8, 5, 8]
        )

    def _set_total_rebounds_universe(self):
        self.total_rebounds["low"] = fuzz.trimf(self.total_rebounds.universe, [0, 2, 4])
        self.total_rebounds["medium"] = fuzz.trimf(
            self.total_rebounds.universe, [3, 5, 7]
        )
        self.total_rebounds["high"] = fuzz.trimf(
            self.total_rebounds.universe, [6, 8, 15]
        )

    def _set_assists_universe(self):
        self.assists["low"] = fuzz.trimf(self.assists.universe, [0, 2.5, 4])
        self.assists["medium"] = fuzz.trimf(self.assists.universe, [3, 5, 8])
        self.assists["high"] = fuzz.trimf(self.assists.universe, [7, 12, 15])

    def _set_steals_universe(self):
        self.steals["low"] = fuzz.trimf(self.steals.universe, [0, 0.5, 1.2])
        self.steals["medium"] = fuzz.trimf(self.steals.universe, [1.1, 1.3, 1.6])
        self.steals["high"] = fuzz.trimf(self.steals.universe, [1.5, 1.8, 3])

    def _set_blocks_universe(self):
        self.blocks["low"] = fuzz.trimf(self.blocks.universe, [0, 0.5, 1])
        self.blocks["medium"] = fuzz.trimf(self.blocks.universe, [0.9, 1.2, 1.9])
        self.blocks["high"] = fuzz.trimf(self.blocks.universe, [1.8, 2.6, 3.5])

    def _set_turnovers_universe(self):
        self.turnovers["high"] = fuzz.trimf(self.turnovers.universe, [0, 1, 1.2])
        self.turnovers["medium"] = fuzz.trimf(self.turnovers.universe, [1.1, 2, 3])
        self.turnovers["low"] = fuzz.trimf(self.turnovers.universe, [2.5, 4, 12])

    def _set_fouls_universe(self):
        self.fouls["high"] = fuzz.trimf(self.fouls.universe, [0, 0.8, 1.3])
        self.fouls["medium"] = fuzz.trimf(self.fouls.universe, [1.1, 1.5, 2.1])
        self.fouls["low"] = fuzz.trimf(self.fouls.universe, [2, 2.5, 6])

    def _set_ppg_universe(self):
        self.ppg["low"] = fuzz.trimf(self.ppg.universe, [0, 5, 10])
        self.ppg["medium"] = fuzz.trimf(self.ppg.universe, [8, 15, 22])
        self.ppg["high"] = fuzz.trimf(self.ppg.universe, [20, 30, 40])

    def _set_rating_universe(self):
        self.rating["low"] = fuzz.trimf(self.rating.universe, [0, 0, 5])
        self.rating["medium"] = fuzz.trimf(self.rating.universe, [3, 5, 7])
        self.rating["high"] = fuzz.trimf(self.rating.universe, [5, 10, 30])

    def create_parametrized_universes(self):
        self._set_age_universe()
        self._set_games_played_universe()
        self._set_games_as_starter_universe()
        self._set_minutes_played_universe()
        self._set_field_goals_universe()
        self._set_field_goals_attempts_universe()
        self._set_field_goals_percentage_universe()
        self._set_three_field_goals_universe()
        self._set_three_field_goals_attempts_universe()
        self._set_three_field_goals_percentage_universe()
        self._set_two_field_goals_universe()
        self._set_two_field_goals_attempts_universe()
        self._set_two_field_goals_percentage_universe()
        self._set_effective_field_goals_universe()
        self._set_free_throws_universe()
        self._set_free_throws_attempts_universe()
        self._set_free_throws_percentage_universe()
        self._set_offensive_rebounds_universe()
        self._set_defensive_rebounds_universe()
        self._set_total_rebounds_universe()
        self._set_assists_universe()
        self._set_steals_universe()
        self._set_blocks_universe()
        self._set_turnovers_universe()
        self._set_fouls_universe()
        self._set_ppg_universe()
        self._set_rating_universe()

    def create_rules(self) -> list:
        rules = []

        for _ in range(3):
            priority = {
                0: "low",
                1: "medium",
                2: "high",
            }
            rule = ctrl.Rule(
                self.ppg[priority[_]]
                & (
                    self.games_played[priority[_]]
                    & self.games_as_starter[priority[_]]
                    & self.minutes_played[priority[_]]
                )
                & self.field_goals[priority[_]]
                & self.assists[priority[_]]
                & self.steals[priority[_]]
                & self.blocks[priority[_]]
                & self.three_field_goals[priority[_]]
                & self.total_rebounds[priority[_]]
                & self.two_field_goals[priority[_]]
                & self.free_throws[priority[_]]
                | (
                    self.field_goals_attempts[priority[_]]
                    | self.three_field_goals_attempts[priority[_]]
                    & self.field_goals_percentage[priority[_]]
                    | self.offensive_rebounds[priority[_]]
                    | self.defensive_rebounds[priority[_]]
                    | self.free_throws_attempts[priority[_]]
                    | self.turnovers[priority[_]]
                    | self.two_field_goals_attempts[priority[_]]
                    | self.two_field_goals_percentage[priority[_]]
                    | self.three_field_goals_percentage[priority[_]]
                    | self.fouls[priority[_]]
                ),
                self.rating[priority[_]],
            )
            rules.append(rule)
        return rules
