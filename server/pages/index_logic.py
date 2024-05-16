import os


def teams() -> list:

    converter = {
        "76ers": "Philadelphia 76ers",
        "blazers": "Portland Trail Blazers",
        "bucks": "Milwaukee Bucks",
        "bulls": "Chicago Bulls",
        "cavaliers": "Cleveland Cavaliers",
        "celtics": "Boston Celtics",
        "clippers": "Los Angeles Clippers",
        "grizzlies": "Memphis Grizzlies",
        "hawks": "Atlanta Hawks",
        "heat": "Miami Heat",
        "hornets": "Charlotte Hornets",
        "jazz": "Utah Jazz",
        "kings": "Sacramento Kings",
        "knicks": "New York Knicks",
        "lakers": "Los Angeles Lakers",
        "magic": "Orlando Magic",
        "mavericks": "Dallas Mavericks",
        "nets": "Brooklyn Nets",
        "nuggets": "Denver Nuggets",
        "pacers": "Indiana Pacers",
        "pelicans": "New Orleans Pelicans",
        "pistons": "Detroit Pistons",
        "raptors": "Toronto Raptors",
        "rockets": "Houston Rockets",
        "suns": "Phoenix Suns",
        "spurs": "San Antonio Spurs",
        "thunder": "Oklahoma City Thunder",
        "timberwolves": "Minnesota Timberwolves",
        "warriors": "Golden State Warriors",
        "wizards": "Washington Wizards",
    }
    search_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "static", "images")
    result = []
    temp = []
    for file in os.listdir(search_path):
        if len(temp) == 3:
            result.append(temp)
            temp = []
        temp.append([converter[file[:-4]], os.path.join(search_path, file)])

    return sorted(result, key=lambda x: x[0])
