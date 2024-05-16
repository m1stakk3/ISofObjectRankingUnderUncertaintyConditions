import csv
import os
from constants import DATA_FOLDER
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Загрузка данных из CSV файла
data = []
with open(os.path.join(DATA_FOLDER, "mavericks.csv"), "r") as file:
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

# Преобразование данных в массивы
players = np.array([row[2] for row in data])
ages = np.array([row[3] for row in data])
games_played = np.array([row[4] for row in data])
games_as_starter = np.array([row[5] for row in data])
avg_minutes_played = np.array([row[6] for row in data])
avg_field_goals = np.array([row[7] for row in data])
avg_field_goals_attempts = np.array([row[8] for row in data])
avg_field_goals_percentage = np.array([row[9] for row in data])
avg_three_point_field_goals = np.array([row[10] for row in data])
avg_three_point_field_goals_attempts = np.array([row[11] for row in data])
avg_three_point_field_goals_percentage = np.array([row[12] for row in data])
avg_two_point_field_goals = np.array([row[13] for row in data])
avg_two_point_field_goals_attempts = np.array([row[14] for row in data])
avg_two_point_field_goals_percentage = np.array([row[15] for row in data])
avg_effective_field_goals_percentage = np.array([row[16] for row in data])
avg_free_field_goals = np.array([row[17] for row in data])
avg_free_field_goals_attempts = np.array([row[18] for row in data])
avg_free_field_goals_percentage = np.array([row[19] for row in data])
avg_offensive_rebounds = np.array([row[20] for row in data])
avg_defensive_rebounds = np.array([row[21] for row in data])
avg_rebounds = np.array([row[22] for row in data])
avg_assists = np.array([row[23] for row in data])
avg_blocks = np.array([row[24] for row in data])
avg_turnovers = np.array([row[25] for row in data])
avg_personal_fouls = np.array([row[26] for row in data])
avg_points_per_game = np.array([row[27] for row in data])


# Показатели для возраста
age_low = fuzz.trimf(ages, [18, 19, 23])
age_medium = fuzz.trimf(ages, [22, 26, 32])
age_high = fuzz.trimf(ages, [30, 33, 40])
#age_rule = ctrl.Rule(age_low | age_medium | age_high)

# Показатели количества игр
games_played_low = fuzz.trimf(games_played, [0, 15, 45])
games_played_medium = fuzz.trimf(games_played, [40, 50, 75])
games_played_high = fuzz.trimf(games_played, [70, 79, 82])
# games_played_rule = ctrl.Rule(
#     games_played_low | games_played_medium | games_played_high
# )

# Показатели сыгранных игр в стартовом составе
games_as_starter_low = fuzz.trimf(games_as_starter, [0, 15, 45])
games_as_starter_medium = fuzz.trimf(games_as_starter, [40, 50, 75])
games_as_starter_high = fuzz.trimf(games_as_starter, [70, 79, 82])
# games_as_starter_rule = ctrl.Rule(
#     games_as_starter_low | games_as_starter_medium | games_as_starter_high
# )

# Показатели средних минут за игру
avg_minutes_played_low = fuzz.trimf(avg_minutes_played, [0, 11, 20])
avg_minutes_played_medium = fuzz.trimf(avg_minutes_played, [15, 26, 35])
avg_minutes_played_high = fuzz.trimf(avg_minutes_played, [30, 40, 48])
# avg_minutes_rule = ctrl.Rule(
#     avg_minutes_played_low | avg_minutes_played_medium | avg_minutes_played_high
# )

# Показатели среднего количества успешных попыток за игру
avg_field_goals_low = fuzz.trimf(avg_field_goals, [0, 2, 4])
avg_field_goals_medium = fuzz.trimf(avg_field_goals, [3, 4, 6])
avg_field_goals_high = fuzz.trimf(avg_field_goals, [5, 8, 12])
# avg_field_goals_rule = ctrl.Rule(
#     avg_field_goals_low | avg_field_goals_medium | avg_field_goals_high
# )

# Показатели среднего количества попыток за игру
avg_field_goals_attempts_low = fuzz.trimf(avg_field_goals_attempts, [0, 3, 9])
avg_field_goals_attempts_medium = fuzz.trimf(avg_field_goals_attempts, [8, 10, 12])
avg_field_goals_attempts_high = fuzz.trimf(avg_field_goals_attempts, [10, 20, 25])
# avg_field_goals_attempts_rule = ctrl.Rule(
#     avg_field_goals_attempts_low
#     | avg_field_goals_attempts_medium
#     | avg_field_goals_attempts_high
# )

# Показатели среднего процента успешных попыток за игру
avg_field_goals_percentage_low = fuzz.trimf(
    avg_field_goals_percentage, [0.0, 0.1, 0.25]
)
avg_field_goals_percentage_medium = fuzz.trimf(
    avg_field_goals_percentage, [0.25, 0.3, 0.35]
)
avg_field_goals_percentage_high = fuzz.trimf(
    avg_field_goals_percentage, [0.35, 0.45, 1.0]
)
# avg_field_goals_percentage_rule = ctrl.Rule(
#     avg_field_goals_percentage_low
#     | avg_field_goals_percentage_medium
#     | avg_field_goals_percentage_high
# )

# Показатели среднего количества трехочковых за игру
avg_three_point_field_goals_low = fuzz.trimf(avg_three_point_field_goals, [0, 2, 3])
avg_three_point_field_goals_medium = fuzz.trimf(
    avg_three_point_field_goals, [1, 3, 3.1]
)
avg_three_point_field_goals_high = fuzz.trimf(avg_three_point_field_goals, [3, 3.5, 5])
# avg_three_point_field_goals_rule = ctrl.Rule(
#     avg_three_point_field_goals_low
#     | avg_three_point_field_goals_medium
#     | avg_three_point_field_goals_high
# )

# Показатели среднего количества попыток трехочковых за игру
avg_three_point_field_goals_attempts_low = fuzz.trimf(
    avg_three_point_field_goals_attempts, [0, 2, 4]
)
avg_three_point_field_goals_attempts_medium = fuzz.trimf(
    avg_three_point_field_goals_attempts, [3, 6, 10]
)
avg_three_point_field_goals_attempts_high = fuzz.trimf(
    avg_three_point_field_goals_attempts, [9, 12, 15]
)
# avg_three_point_field_goals_attempts_rule = ctrl.Rule(
#     avg_three_point_field_goals_attempts_low
#     | avg_three_point_field_goals_attempts_medium
#     | avg_three_point_field_goals_attempts_high
# )

# Показатели среднего процента трехочковых за игру
avg_three_point_field_goals_percentage_low = fuzz.trimf(
    avg_three_point_field_goals_percentage, [0.0, 0.1, 0.25]
)
avg_three_point_field_goals_percentage_medium = fuzz.trimf(
    avg_three_point_field_goals_percentage, [0.25, 0.3, 0.35]
)
avg_three_point_field_goals_percentage_high = fuzz.trimf(
    avg_three_point_field_goals_percentage, [0.35, 0.45, 1.0]
)
# avg_three_point_field_goals_percentage_rule = ctrl.Rule(
#     avg_three_point_field_goals_percentage_low
#     | avg_three_point_field_goals_percentage_medium
#     | avg_three_point_field_goals_percentage_high
# )

# Показатели среднего количества двухочковых за игру
avg_two_point_field_goals_low = fuzz.trimf(avg_two_point_field_goals, [0, 2, 3])
avg_two_point_field_goals_medium = fuzz.trimf(avg_two_point_field_goals, [1, 3, 3.1])
avg_two_point_field_goals_high = fuzz.trimf(avg_two_point_field_goals, [3, 3.5, 5])
# avg_two_point_field_goals_rule = ctrl.Rule(
#     avg_two_point_field_goals_low
#     | avg_two_point_field_goals_medium
#     | avg_two_point_field_goals_high
# )

# Показатели среднего количества попыток двухочковых за игру
avg_two_point_field_goals_attempts_low = fuzz.trimf(
    avg_two_point_field_goals_attempts, [0, 2, 4]
)
avg_two_point_field_goals_attempts_medium = fuzz.trimf(
    avg_two_point_field_goals_attempts, [3, 5, 7]
)
avg_two_point_field_goals_attempts_high = fuzz.trimf(
    avg_two_point_field_goals_attempts, [6, 8, 20]
)
# avg_two_point_field_goals_attempts_rule = ctrl.Rule(
#     avg_two_point_field_goals_attempts_low
#     | avg_two_point_field_goals_attempts_medium
#     | avg_two_point_field_goals_attempts_high
# )

# Показатели среднего процента двухочковых за игру
avg_two_point_field_goals_percentage_low = fuzz.trimf(
    avg_two_point_field_goals_percentage, [0.0, 0.1, 0.25]
)
avg_two_point_field_goals_percentage_medium = fuzz.trimf(
    avg_two_point_field_goals_percentage, [0.25, 0.3, 0.35]
)
avg_two_point_field_goals_percentage_high = fuzz.trimf(
    avg_two_point_field_goals_percentage, [0.35, 0.45, 1.0]
)
# avg_two_point_field_goals_percentage_rule = ctrl.Rule(
#     avg_two_point_field_goals_percentage_low
#     | avg_two_point_field_goals_percentage_medium
#     | avg_two_point_field_goals_percentage_high
# )

# Показатели эффективных бросков за игру
avg_effective_field_goals_percentage_low = fuzz.trimf(
    avg_effective_field_goals_percentage, [0.0, 0.1, 0.25]
)
avg_effective_field_goals_percentage_medium = fuzz.trimf(
    avg_effective_field_goals_percentage, [0.25, 0.3, 0.35]
)
avg_effective_field_goals_percentage_high = fuzz.trimf(
    avg_effective_field_goals_percentage, [0.35, 0.45, 1.0]
)
# avg_effective_field_goals_percentage_rule = ctrl.Rule(
#     avg_effective_field_goals_percentage_low
#     | avg_effective_field_goals_percentage_medium
#     | avg_effective_field_goals_percentage_high
# )

# Показатели среднего количества штрафных бросков за игру
avg_free_throws_low = fuzz.trimf(avg_free_field_goals, [0, 1, 2])
avg_free_throws_medium = fuzz.trimf(avg_free_field_goals, [1, 2, 5])
avg_free_throws_high = fuzz.trimf(avg_free_field_goals, [4, 6, 10])
# avg_free_throws_rule = ctrl.Rule(
#     avg_free_throws_low | avg_free_throws_medium | avg_free_throws_high
# )

# Показатели среднего количества попыток штрафных бросков за игру
avg_free_throws_attempts_low = fuzz.trimf(avg_free_field_goals, [0, 1, 2])
avg_free_throws_attempts_medium = fuzz.trimf(avg_free_field_goals, [1, 2, 5])
avg_free_throws_attempts_high = fuzz.trimf(avg_free_field_goals, [4, 6, 10])
# avg_free_throws_attempts_rule = ctrl.Rule(
#     avg_free_throws_attempts_low
#     | avg_free_throws_attempts_medium
#     | avg_free_throws_attempts_high
# )

# Показатели среднего процента попыток штрафных бросков за игру
avg_free_throws_percentage_low = fuzz.trimf(
    avg_free_field_goals_percentage, [0.0, 0.3, 0.45]
)
avg_free_throws_percentage_medium = fuzz.trimf(
    avg_free_field_goals_percentage, [0.41, 0.7, 0.78]
)
avg_free_throws_percentage_high = fuzz.trimf(
    avg_free_field_goals_percentage, [0.75, 0.9, 1.0]
)
# avg_free_throws_percentage_rule = ctrl.Rule(
#     avg_free_throws_percentage_low
#     | avg_free_throws_percentage_medium
#     | avg_free_throws_percentage_high
# )

# Показатели подборов в атаке за игру
offensive_rebounds_low = fuzz.trimf(avg_offensive_rebounds, [0, 0.5, 1])
offensive_rebounds_medium = fuzz.trimf(avg_offensive_rebounds, [0.7, 1.2, 1.9])
offensive_rebounds_high = fuzz.trimf(avg_offensive_rebounds, [1.8, 2.6, 5])
# offensive_rebounds_rule = ctrl.Rule(
#     offensive_rebounds_low | offensive_rebounds_medium | offensive_rebounds_high
# )

# Показатели подборов в защите за игру
defensive_rebounds_low = fuzz.trimf(avg_defensive_rebounds, [0, 1.8, 2])
defensive_rebounds_medium = fuzz.trimf(avg_defensive_rebounds, [1.9, 3.6, 4])
defensive_rebounds_high = fuzz.trimf(avg_defensive_rebounds, [3.8, 5, 8])
# defensive_rebounds_rule = ctrl.Rule(
#     defensive_rebounds_low | defensive_rebounds_medium | defensive_rebounds_high
# )

# Показатели подборов за игру
rebounds_low = fuzz.trimf(avg_rebounds, [0, 2, 4])
rebounds_medium = fuzz.trimf(avg_rebounds, [3, 5, 7])
rebounds_high = fuzz.trimf(avg_rebounds, [6, 8, 15])
# rebound_rule = ctrl.Rule(rebounds_low | rebounds_medium | rebounds_high)

# Показатели блокшотов за игру
blocks_low = fuzz.trimf(avg_rebounds, [0, 0.5, 1])
blocks_medium = fuzz.trimf(avg_rebounds, [0.9, 1.2, 1.9])
blocks_high = fuzz.trimf(avg_rebounds, [1.8, 2.6, 3.5])
# blocks_rule = ctrl.Rule(blocks_low | blocks_medium | blocks_high)

# Показатели потерь за игру
turnovers_low = fuzz.trimf(avg_turnovers, [0, 1, 1.7])
turnovers_medium = fuzz.trimf(avg_turnovers, [1.5, 2, 3])
turnovers_high = fuzz.trimf(avg_turnovers, [2.7, 4, 6])
# turnovers_rule = ctrl.Rule(turnovers_low | turnovers_medium | turnovers_high)

# Показатели фолов за игру
fouls_low = fuzz.trimf(avg_personal_fouls, [0, 1, 2])
fouls_medium = fuzz.trimf(avg_personal_fouls, [1.8, 2.6, 3.2])
fouls_high = fuzz.trimf(avg_personal_fouls, [3, 4, 6])
# foul_rule = ctrl.Rule(fouls_low | fouls_medium | fouls_high)

# Показатели очков за игру
ppg_low = fuzz.trimf(avg_points_per_game, [0, 5, 10])
ppg_medium = fuzz.trimf(avg_points_per_game, [8, 15, 22])
ppg_high = fuzz.trimf(avg_points_per_game, [20, 30, 40])
# ppg_rule = ctrl.Rule(ppg_low | ppg_medium | ppg_high)


# Ранжирование баскетболистов
# ranking_ctrl = ctrl.ControlSystem(
#     [
#         age_rule,
#         games_played_rule,
#         games_as_starter_rule,
#         avg_minutes_rule,
#         avg_field_goals_rule,
#         avg_field_goals_attempts_rule,
#         avg_field_goals_percentage_rule,
#         avg_three_point_field_goals_rule,
#         avg_three_point_field_goals_attempts_rule,
#         avg_three_point_field_goals_percentage_rule,
#         avg_two_point_field_goals_rule,
#         avg_two_point_field_goals_attempts_rule,
#         avg_two_point_field_goals_percentage_rule,
#         avg_effective_field_goals_percentage_rule,
#         avg_free_throws_rule,
#         avg_free_throws_attempts_rule,
#         avg_free_throws_percentage_rule,
#         offensive_rebounds_rule,
#         defensive_rebounds_rule,
#         rebound_rule,
#         blocks_rule,
#         turnovers_rule,
#         foul_rule,
#         ppg_rule
#     ]
# )
# ranking = ctrl.ControlSystemSimulation(ranking_ctrl)
# ranking.compute()

# # Вывод результатов
# print("Ранжирование баскетболистов:")
# for i, index in enumerate(ranking):
#     print(f"{i + 1}. {data[index][0]}")

print(age_high)
