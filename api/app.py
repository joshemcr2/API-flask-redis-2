from flask import Flask, jsonify
from flask_redis import FlaskRedis

app = Flask(__name__)
app.config['REDIS_URL'] = 'redis://localhost:6379/0'

redis_store = FlaskRedis(app)


@app.route('/api/users', methods=['GET'])
def get_users():
    users = redis_store.get('users')
    if users is not None:
            return users
    users = [{'id': 1, 'name': 'Jose'}, {'id': 2, 'name': 'Angel'}]
    redis_store.set('users', users)
    return jsonify(users)

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = redis_store.get('user')
    if user is not None:
            return user
    user = {'id': user_id, 'name': 'Jose'}
    redis_store.set('user', user)
    return jsonify(user)

@app.route('/api/users', methods=['POST'])
def create_user():
    user = {'id': 3, 'name': 'Jose Angel'}
    return jsonify(user), 201

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = {'id': user_id, 'name': 'Updated'}
    return jsonify(user)

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return '', 204

if __name__ == '__main__':
     app.run(debug=True)
