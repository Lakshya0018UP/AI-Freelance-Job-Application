""" from flask_jwt_extended import create_access_token
from models import User,db
from flask import jsonify,request,Blueprint
from app import db
auth_bp=Blueprint("auth",__name__)

@auth_bp.route('/signup',methods=['POST'])
def signup():
    data=request.get_json()
    username=data.get('username')
    name=data.get('name')
    email=data.get('email')
    password_hash=data.get('password_hash')
    role=data.get('role')

    new_user=User(username=username,name=name,email=email,role=role)
    new_user.set_password(password_hash)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg":"The User has been added"}) """
