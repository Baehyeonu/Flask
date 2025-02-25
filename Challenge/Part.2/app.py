from flask import Flask
from flask_smorest import Api
from api import blp

app = Flask(__name__)
# Flask-Smorest 설정 추가...


app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
# API와 블루프린트 등록...

api = Api(app)
api.register_blueprint(blp)

if __name__ == "__main__":
    app.run(debug=True)
