from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

client = MongoClient("mongodb+srv://riVFerd:test_mongodb@cluster0.rq9u845.mongodb.net/?retryWrites=true&w=majority")
db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/homework', methods=['POST'])
def homework_post():
    db.fanmessages.insert_one({
        'name': request.form['name_give'],
        'comment': request.form['comment_give']
    })
    return jsonify({
        'msg': 'POST messages!'
    })

@app.route('/homework')
def homework_get():
    return jsonify({
        'messages': list(db.fanmessages.find({}, {'_id': False}))
    })
    

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)