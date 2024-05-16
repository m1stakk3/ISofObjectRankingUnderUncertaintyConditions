import csv
import os

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

from constants import DATA_FOLDER

data = []
with open(os.path.join(DATA_FOLDER, "bulls.csv"), "r") as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)  # Пропускаем заголовки
    for row in csv_reader:
        data.append(
            [
                int(row[0]),
                str(row[1]),
                *[int(value) for value in row[2:5]],
                *[
                    (
                        float(value if len(value) > 0 else 0)
                        if not value.startswith(".")
                        else float(value.replace(".", "0."))
                    )
                    for value in row[5:]
                ],
            ]
        )

# Определение нечетких переменных и их значения
age = ctrl.Antecedent(np.arange(18, 41, 1), "age")
games_played = ctrl.Antecedent(np.arange(0, 83, 1), "games_played")
games_as_starter = ctrl.Antecedent(np.arange(0, 83, 1), "games_as_starter")
minutes_played = ctrl.Antecedent(np.arange(0, 48.1, 0.1), "minutes_played")
field_goals = ctrl.Antecedent(np.arange(0, 15, 0.1), "field_goals")
field_goals_attempts = ctrl.Antecedent(np.arange(0, 15, 0.1), "field_goals_attempts")
field_goals_percentage = ctrl.Antecedent(
    np.arange(0, 100, 0.1), "field_goals_percentage"
)
three_field_goals = ctrl.Antecedent(np.arange(0, 15, 0.1), "three_field_goals")
three_field_goals_attempts = ctrl.Antecedent(
    np.arange(0, 15, 0.1), "three_field_goals_attempts"
)
three_field_goals_percentage = ctrl.Antecedent(
    np.arange(0, 100, 0.1), "three_field_goals_percentage"
)
two_field_goals = ctrl.Antecedent(np.arange(0, 15, 0.1), "two_field_goals")
two_field_goals_attempts = ctrl.Antecedent(
    np.arange(0, 15, 0.1), "two_field_goals_attempts"
)
two_field_goals_percentage = ctrl.Antecedent(
    np.arange(0, 100, 0.1), "two_field_goals_percentage"
)
effective_field_goals = ctrl.Consequent(np.arange(0, 100, 0.1), "effective_field_goals")
free_throws = ctrl.Antecedent(np.arange(0, 15, 0.1), "free_throws")
free_throws_attempts = ctrl.Antecedent(np.arange(0, 15, 0.1), "free_throws_attempts")
free_throws_percentage = ctrl.Antecedent(
    np.arange(0, 100, 0.1), "free_throws_percentage"
)
offensive_rebounds = ctrl.Antecedent(np.arange(0, 9, 0.1), "offensive_rebounds")
defensive_rebounds = ctrl.Antecedent(np.arange(0, 9, 0.1), "defensive_rebounds")
total_rebounds = ctrl.Antecedent(np.arange(0, 18, 0.1), "total_rebounds")
assists = ctrl.Antecedent(np.arange(0, 15, 0.1), "assists")
steals = ctrl.Antecedent(np.arange(0, 5, 0.1), "steals")
blocks = ctrl.Antecedent(np.arange(0, 5, 0.1), "blocks")
turnovers = ctrl.Antecedent(np.arange(0, 7, 0.1), "turnovers")
fouls = ctrl.Antecedent(np.arange(0, 7, 0.1), "fouls")
ppg = ctrl.Antecedent(np.arange(0, 41, 0.1), "ppg")
rating = ctrl.Consequent(np.arange(0, 30, 1), "rating")


age["high"] = fuzz.trimf(age.universe, [18, 19, 23])
age["medium"] = fuzz.trimf(age.universe, [22, 26, 32])
age["low"] = fuzz.trimf(age.universe, [30, 33, 40])

games_played["low"] = fuzz.trimf(games_played.universe, [0, 15, 45])
games_played["medium"] = fuzz.trimf(games_played.universe, [40, 50, 75])
games_played["high"] = fuzz.trimf(games_played.universe, [70, 79, 82])

games_as_starter["low"] = fuzz.trimf(games_as_starter.universe, [0, 15, 45])
games_as_starter["medium"] = fuzz.trimf(games_as_starter.universe, [40, 50, 75])
games_as_starter["high"] = fuzz.trimf(games_as_starter.universe, [70, 79, 82])

minutes_played["low"] = fuzz.trimf(minutes_played.universe, [0, 11, 20])
minutes_played["medium"] = fuzz.trimf(minutes_played.universe, [15, 26, 35])
minutes_played["high"] = fuzz.trimf(minutes_played.universe, [30, 40, 48])

field_goals["low"] = fuzz.trimf(field_goals.universe, [0, 2, 4])
field_goals["medium"] = fuzz.trimf(field_goals.universe, [3, 4, 6])
field_goals["high"] = fuzz.trimf(field_goals.universe, [5, 8, 12])

field_goals_attempts["low"] = fuzz.trimf(field_goals_attempts.universe, [0, 3, 9])
field_goals_attempts["medium"] = fuzz.trimf(field_goals_attempts.universe, [8, 10, 12])
field_goals_attempts["high"] = fuzz.trimf(field_goals_attempts.universe, [10, 20, 25])

field_goals_percentage["low"] = fuzz.trimf(
    field_goals_percentage.universe, [0.0, 0.1, 0.25]
)
field_goals_percentage["medium"] = fuzz.trimf(
    field_goals_percentage.universe, [0.25, 0.3, 0.35]
)
field_goals_percentage["high"] = fuzz.trimf(
    field_goals_percentage.universe, [0.35, 0.45, 1.0]
)

three_field_goals["low"] = fuzz.trimf(three_field_goals.universe, [0, 2, 3])
three_field_goals["medium"] = fuzz.trimf(three_field_goals.universe, [1, 3, 3.1])
three_field_goals["high"] = fuzz.trimf(three_field_goals.universe, [3, 3.5, 5])

three_field_goals_attempts["low"] = fuzz.trimf(
    three_field_goals_attempts.universe, [0, 2, 4]
)
three_field_goals_attempts["medium"] = fuzz.trimf(
    three_field_goals_attempts.universe, [3, 6, 10]
)
three_field_goals_attempts["high"] = fuzz.trimf(
    three_field_goals_attempts.universe, [9, 12, 15]
)

three_field_goals_percentage["low"] = fuzz.trimf(
    three_field_goals_percentage.universe, [0.0, 0.1, 0.25]
)
three_field_goals_percentage["medium"] = fuzz.trimf(
    three_field_goals_percentage.universe, [0.25, 0.3, 0.35]
)
three_field_goals_percentage["high"] = fuzz.trimf(
    three_field_goals_percentage.universe, [0.35, 0.45, 1.0]
)

two_field_goals["low"] = fuzz.trimf(two_field_goals.universe, [0, 2, 3])
two_field_goals["medium"] = fuzz.trimf(two_field_goals.universe, [1, 3, 3.1])
two_field_goals["high"] = fuzz.trimf(two_field_goals.universe, [3, 3.5, 5])

two_field_goals_attempts["low"] = fuzz.trimf(
    two_field_goals_attempts.universe, [0, 2, 4]
)
two_field_goals_attempts["medium"] = fuzz.trimf(
    two_field_goals_attempts.universe, [3, 5, 7]
)
two_field_goals_attempts["high"] = fuzz.trimf(
    two_field_goals_attempts.universe, [6, 8, 20]
)

two_field_goals_percentage["low"] = fuzz.trimf(
    two_field_goals_percentage.universe, [0.0, 0.1, 0.25]
)
two_field_goals_percentage["medium"] = fuzz.trimf(
    two_field_goals_percentage.universe, [0.25, 0.3, 0.35]
)
two_field_goals_percentage["high"] = fuzz.trimf(
    two_field_goals_percentage.universe, [0.35, 0.45, 1.0]
)

effective_field_goals["low"] = fuzz.trimf(
    effective_field_goals.universe, [0.0, 0.1, 0.28]
)
effective_field_goals["medium"] = fuzz.trimf(
    effective_field_goals.universe, [0.25, 0.3, 0.43]
)
effective_field_goals["high"] = fuzz.trimf(
    effective_field_goals.universe, [0.42, 0.52, 1.0]
)

free_throws["low"] = fuzz.trimf(free_throws.universe, [0, 1, 2])
free_throws["medium"] = fuzz.trimf(free_throws.universe, [1, 2, 5])
free_throws["high"] = fuzz.trimf(free_throws.universe, [4, 6, 10])

free_throws_attempts["low"] = fuzz.trimf(free_throws_attempts.universe, [0, 1, 2])
free_throws_attempts["medium"] = fuzz.trimf(free_throws_attempts.universe, [1, 2, 5])
free_throws_attempts["high"] = fuzz.trimf(free_throws_attempts.universe, [4, 6, 10])

free_throws_percentage["low"] = fuzz.trimf(
    free_throws_percentage.universe, [0.0, 0.3, 0.45]
)
free_throws_percentage["medium"] = fuzz.trimf(
    free_throws_percentage.universe, [0.41, 0.7, 0.78]
)
free_throws_percentage["high"] = fuzz.trimf(
    free_throws_percentage.universe, [0.75, 0.9, 1.0]
)

offensive_rebounds["low"] = fuzz.trimf(offensive_rebounds.universe, [0, 0.5, 1])
offensive_rebounds["medium"] = fuzz.trimf(offensive_rebounds.universe, [0.7, 1.2, 1.9])
offensive_rebounds["high"] = fuzz.trimf(offensive_rebounds.universe, [1.8, 2.6, 5])

defensive_rebounds["low"] = fuzz.trimf(defensive_rebounds.universe, [0, 1.8, 2])
defensive_rebounds["medium"] = fuzz.trimf(defensive_rebounds.universe, [1.9, 3.6, 4])
defensive_rebounds["high"] = fuzz.trimf(defensive_rebounds.universe, [3.8, 5, 8])

total_rebounds["low"] = fuzz.trimf(total_rebounds.universe, [0, 2, 4])
total_rebounds["medium"] = fuzz.trimf(total_rebounds.universe, [3, 5, 7])
total_rebounds["high"] = fuzz.trimf(total_rebounds.universe, [6, 8, 15])

assists["low"] = fuzz.trimf(assists.universe, [0, 2.5, 4])
assists["medium"] = fuzz.trimf(assists.universe, [3, 5, 8])
assists["high"] = fuzz.trimf(assists.universe, [7, 12, 15])

steals["low"] = fuzz.trimf(steals.universe, [0, 0.5, 1.2])
steals["medium"] = fuzz.trimf(steals.universe, [1.1, 1.3, 1.6])
steals["high"] = fuzz.trimf(steals.universe, [1.5, 1.8, 3])

blocks["low"] = fuzz.trimf(blocks.universe, [0, 0.5, 1])
blocks["medium"] = fuzz.trimf(blocks.universe, [0.9, 1.2, 1.9])
blocks["high"] = fuzz.trimf(blocks.universe, [1.8, 2.6, 3.5])

turnovers["high"] = fuzz.trimf(turnovers.universe, [0, 1, 1.2])
turnovers["medium"] = fuzz.trimf(turnovers.universe, [1.1, 2, 3])
turnovers["low"] = fuzz.trimf(turnovers.universe, [2.5, 4, 12])

fouls["high"] = fuzz.trimf(fouls.universe, [0, 0.8, 1.3])
fouls["medium"] = fuzz.trimf(fouls.universe, [1.1, 1.5, 2.1])
fouls["low"] = fuzz.trimf(fouls.universe, [2, 2.5, 6])

ppg["low"] = fuzz.trimf(ppg.universe, [0, 5, 10])
ppg["medium"] = fuzz.trimf(ppg.universe, [8, 15, 22])
ppg["high"] = fuzz.trimf(ppg.universe, [20, 30, 40])

rating["low"] = fuzz.trimf(rating.universe, [0, 0, 5])
rating["medium"] = fuzz.trimf(rating.universe, [3, 5, 7])
rating["high"] = fuzz.trimf(rating.universe, [5, 10, 30])

# Определение нечетких правил
rules = []
for _ in range(3):

    priority = {
        0: "low",
        1: "medium",
        2: "high",
    }
    rule = ctrl.Rule(
        ppg[priority[_]]
        & (games_played[priority[_]] & games_as_starter[priority[_]] & minutes_played[priority[_]]) &
         field_goals[priority[_]]
        & assists[priority[_]]
        & steals[priority[_]]
        & blocks[priority[_]]
        & three_field_goals[priority[_]]
        & total_rebounds[priority[_]]
        & two_field_goals[priority[_]]
        & free_throws[priority[_]] |
        (field_goals_attempts[priority[_]]
        | three_field_goals_attempts[priority[_]] & field_goals_percentage[priority[_]]
        | offensive_rebounds[priority[_]]
        | defensive_rebounds[priority[_]]
        | free_throws_attempts[priority[_]]
        | turnovers[priority[_]]
        | two_field_goals_attempts[priority[_]]
        | two_field_goals_percentage[priority[_]]
        | three_field_goals_percentage[priority[_]]
        | fouls[priority[_]]),
        rating[priority[_]]
    )
    rules.append(rule)


# Создание нечеткой системы управления
rating_ctrl = ctrl.ControlSystem(rules)
rating_simulation = ctrl.ControlSystemSimulation(rating_ctrl)


# Ранжированный список игроков
ranked_players = []

# Оценка рейтинга для каждого игрока и добавление в ранжированный список
for player in data:
    rating_simulation.input["games_played"] = player[3]
    rating_simulation.input["games_as_starter"] = player[4]
    rating_simulation.input["minutes_played"] = player[5]
    rating_simulation.input["field_goals"] = player[6]
    rating_simulation.input["field_goals_attempts"] = player[7]
    rating_simulation.input["field_goals_percentage"] = player[8]
    rating_simulation.input["three_field_goals"] = player[9]
    rating_simulation.input["three_field_goals_attempts"] = player[10]
    rating_simulation.input["three_field_goals_percentage"] = player[11]
    rating_simulation.input["two_field_goals"] = player[12]
    rating_simulation.input["two_field_goals_attempts"] = player[13]
    rating_simulation.input["two_field_goals_percentage"] = player[14]
    rating_simulation.input["free_throws"] = player[16]
    rating_simulation.input["free_throws_attempts"] = player[17]
    rating_simulation.input["three_field_goals_attempts"] = player[18]
    rating_simulation.input["offensive_rebounds"] = player[19]
    rating_simulation.input["defensive_rebounds"] = player[20]
    rating_simulation.input["total_rebounds"] = player[21]
    rating_simulation.input["assists"] = player[22]
    rating_simulation.input["steals"] = player[23]
    rating_simulation.input["blocks"] = player[24]
    rating_simulation.input["turnovers"] = player[25]
    rating_simulation.input["fouls"] = player[26]
    rating_simulation.input["ppg"] = player[27]

    rating_simulation.compute()

    rating_value = rating_simulation.output["rating"]
    ranked_players.append({"name": player[1], "rating": rating_value})

# Сортировка игроков по рейтингу в порядке убывания
ranked_players = sorted(ranked_players, key=lambda x: x["rating"], reverse=True)

# print(data[1])
# Вывод ранжированного списка игроков
for i, player in enumerate(ranked_players):
    print(f"{i+1}. {player['name']} - Rating: {player['rating']:.2f}")
