from constants import DATA_FOLDER
import os
import csv


class DataProcessing(object):

    def __init__(self, team_name: str) -> None:
        self._data = []
        self.path = (os.path.join(DATA_FOLDER, f"{team_name}.csv"))

    def load_data(self) -> None:
        with open(self.path, "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Пропускаем заголовки
            for row in csv_reader:
                if not all([True if len(i) > 0 else False for i in row]):
                    continue
                self._data.append(
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

    @property
    def data(self) -> list:
        return self._data
