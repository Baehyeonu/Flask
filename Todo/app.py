# app.py
from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from flask_smorest import Api

from db import db
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db" # local db => 파일 형애틔 간단한 데이터 베이스
app.config["JWT_SECRET_KEY"] = "super-secret-key"


db.init_app(app)
migrate = Migrate(app, db)


jwt = JWTManager(app)
api = Api(app)

if __name__ == "__main__":
    app.run(debug=True)