from models.user import User
from flask import Blueprint,jsonify, request
from passlib.hash import pbkdf2_sha256
import jwt


user_api = Blueprint('user_api', __name__)

@user_api.route('/signup', methods=['POST'])
def signup():
    user = {
                "name": request.json.get('name'),
                "email": request.json.get('email'),
                "password": request.json.get('password'),
                "reset_token":"",
                "expire_token":""
                }

    user['password'] = pbkdf2_sha256.encrypt(user['password'])

    user_save=User(name=user["name"],email=user["email"],password=user["password"])

    check_user=User.objects(email=user["email"])

    if check_user:
        return jsonify({ "error": "Email address already in use" }), 400
    
    if user_save.save():
        return jsonify({ "message": "Saved successfully" }), 200
    
    return jsonify({ "error": "Signup failed" }), 400


@user_api.route('/login', methods=['POST'])
def login_service():
    
    user=User.objects(email=request.json.get('email'))

    if not(user):
        return jsonify({ "error": "Invalid email" }), 401  
    user=User.objects.get(email=request.json.get('email'))
    if not(pbkdf2_sha256.verify(request.json.get('password'), user.password)):
        return jsonify({ "error": "Invalid password" }), 401 

    
    token = jwt.encode({'user': str(user.id)},"shhhhh")      
    

    return jsonify({"token": token}), 200   