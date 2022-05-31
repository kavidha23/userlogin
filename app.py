from flask import Flask, jsonify, request
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/new1')
db = client['new1']

app = Flask(__name__)

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
           
            "password" : password,
            
        })
        return jsonify({
            'status': '200. Data is posted to MongoDB',
            'Name': Name,
            
            'emailId': emailId,
            "password" : password,
           
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
                "password" : password,
               
            }
            
            dataJson.append(dataDict)
        print(dataJson)
        return jsonify(dataJson)
if __name__ == '__main__':
    app.run()




