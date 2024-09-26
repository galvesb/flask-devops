from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        return {'users': ['user1', 'user2', 'user3']}

class User(Resource):
    def get(self, cpf):
        return {'user': cpf}   

    def post(self):
        return {'user': 'created'}

api.add_resource(Users, '/users')
api.add_resource(User, '/users/<string:name>')


if __name__ == '__main__':
    app.run(debug=True)