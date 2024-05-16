from skfuzzy import control as ctrl


class ProcessingSystem(object):

    def __init__(self, data: list, rules: list):
        self.data = data
        self.rating_simulation = ctrl.ControlSystemSimulation(ctrl.ControlSystem(rules))

    def get_ranked_players(self) -> list:
        # Ранжированный список игроков
        ranked_players = []

        # Оценка рейтинга для каждого игрока и добавление в ранжированный список
        for player in self.data:
            self.rating_simulation.input["games_played"] = player[3]
            self.rating_simulation.input["games_as_starter"] = player[4]
            self.rating_simulation.input["minutes_played"] = player[5]
            self.rating_simulation.input["field_goals"] = player[6]
            self.rating_simulation.input["field_goals_attempts"] = player[7]
            self.rating_simulation.input["field_goals_percentage"] = player[8]
            self.rating_simulation.input["three_field_goals"] = player[9]
            self.rating_simulation.input["three_field_goals_attempts"] = player[10]
            self.rating_simulation.input["three_field_goals_percentage"] = player[11]
            self.rating_simulation.input["two_field_goals"] = player[12]
            self.rating_simulation.input["two_field_goals_attempts"] = player[13]
            self.rating_simulation.input["two_field_goals_percentage"] = player[14]
            self.rating_simulation.input["free_throws"] = player[16]
            self.rating_simulation.input["free_throws_attempts"] = player[17]
            self.rating_simulation.input["offensive_rebounds"] = player[19]
            self.rating_simulation.input["defensive_rebounds"] = player[20]
            self.rating_simulation.input["total_rebounds"] = player[21]
            self.rating_simulation.input["assists"] = player[22]
            self.rating_simulation.input["steals"] = player[23]
            self.rating_simulation.input["blocks"] = player[24]
            self.rating_simulation.input["turnovers"] = player[25]
            self.rating_simulation.input["fouls"] = player[26]
            self.rating_simulation.input["ppg"] = player[27]

            self.rating_simulation.compute()

            rating_value = self.rating_simulation.output["rating"]
            ranked_players.append(
                {
                    "name": player[1].encode("utf-8").decode("utf-8"),
                    "age": player[2],
                    "ppg": player[27],
                    "assists": player[22],
                    "rebounds": player[21],
                    "steals": player[23],
                    "blocks": player[24],
                    "fg_percentage": player[8],
                    "three_field_goals_percentage": player[11],
                    "free_throws_percentage": player[18],
                    "rating": rating_value,
                }
            )

        # Сортировка игроков по рейтингу в порядке убывания
        ranked_players = sorted(ranked_players, key=lambda x: x["rating"], reverse=True)
        return ranked_players
