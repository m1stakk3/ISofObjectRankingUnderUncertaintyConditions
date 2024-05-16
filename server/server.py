import os
from server.config import Config
from flask import Flask, render_template, request, flash, redirect, Response
from werkzeug.exceptions import BadRequestKeyError
from src import *

from .pages.index_logic import teams

app = Flask(__name__)
app.config['SECRET_KEY'] = Config.secret_key


@app.route('/', methods=['GET'])
def index() -> Response:
    if request.method == 'GET':
        return render_template('index.html', teams=teams())


@app.route('/help', methods=['GET'])
def help() -> Response:
    return render_template('help.html')


@app.route('/team/<string:team_name>', methods=['GET'])
def team(team_name: str) -> Response:
    data_processing = DataProcessing(team_name)
    data_processing.load_data()
    fuzzy_logic = FuzzyLogic()
    fuzzy_logic.create_parametrized_universes()
    inf_system = ProcessingSystem(data=data_processing.data, rules=fuzzy_logic.create_rules())
    ranked_players = inf_system.get_ranked_players()
    return render_template('team.html', ranked_players=ranked_players, team_name=team_name)


@app.errorhandler(404)
def page_not_found(_):
    return redirect("/")
