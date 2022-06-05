from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask_cors import CORS
client = MongoClient('mongodb://localhost:27017/kavidha')
db = client['kavidha']

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/login', methods=['POST', 'GET'])
def data():

    if request.method == 'POST':
        body = request.json
        Name = body['Name']

        emailId = body['emailId']
        password = body['password']

        db['Users'].insert_one({
            "Name": Name,

            "emailId": emailId,

            "password": password,

        })
        return jsonify({
            'status': '200. Data is posted to MongoDB',
            'Name': Name,

            'emailId': emailId,
            "password": password,

        })

    if request.method == 'GET':
        allData = db['Users'].find()
        dataJson = []
        for data in allData:
            id = data['_id']
            Name = data['Name']

            emailId = data['emailId'],

            password = data['password']

            dataDict = {
                'id': str(id),
                'Name': Name,

                'emailId': emailId,
                "password": password,

            }

            dataJson.append(dataDict)
        print(dataJson)
        return jsonify(dataJson)


@app.route('/register', methods=['POST'])
def register():
    collist = db.list_collection_names()
    if "registerUser" in collist:
        print("The collection exists.")
    else:
        collection = db['registerUser']

    if request.method == 'POST':
        body = request.json
        print("Body", request.json)
        username = body['username']
        password = body['password']
        emailId = body['emailId']
        role = body['role']

        db['registerUser'].insert_one({
            "username": username,
            "emailId": emailId,
            "password": password,
            "role": role
        })
        return jsonify({
            'status': '200. Data is posted to MongoDB',
            "username": username,
            "emailId": emailId,
            "password": password,
            "role": role
        })


if __name__ == '__main__':
    app.run()
