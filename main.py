from server.server import app
from server.config import Config


if __name__ == '__main__':
    app.run(debug=True, host=Config.ip, port=Config.port)
