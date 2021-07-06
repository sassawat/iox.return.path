from flask import Flask, url_for
from flask_restful import Api
from resources.routes import initialize_routes
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from config.config import Development
from flasgger import Swagger
from flask.logging import create_logger
from flask_cors import CORS

app = Flask(__name__)
LOG = create_logger(app)
CORS(app)
api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
app.config.from_object(Development)
swagger = Swagger(app)

@app.route("/")
def hello():
    """ This is just a test route for the first TTD test"""
    return {"hello": "world"}

initialize_routes(api)

# use the flask run approach
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5113, debug=True)