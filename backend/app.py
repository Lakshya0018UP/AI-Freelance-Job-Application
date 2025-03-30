from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import create_access_token,JWTManager
from flask_migrate import Migrate

#Sfrom auth_routes import auth_bp
app=Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']="SUPER-SECRET-KEY"
#app.config['JWT_TOKEN_LOCATION'] = ['headers', 'query_string']
app.config["JWT_ALGORITHM"] = "HS256"  # Ensure consistency
app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies"]
#Sapp.register_blueprint(auth_bp, url_prefix="/api/auth")
app.config['JWT_VERIFY_SUB'] = False
db=SQLAlchemy(app)
jwt = JWTManager(app)
migrate = Migrate(app, db,render_as_batch=True)
import routes
import auth_routes

with app.app_context():
    db.create_all()

if __name__=="__main__":
    app.run(debug=True)