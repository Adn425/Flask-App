from flask import Flask,jsonify, request

app = Flask(__name__)

tasks = [
    {
        'contact': '9987644456',
        'name':'Raju',
        'done': False,
        'id': 1
    },
    {
        'contact': 9876543222,
        'name': 'Rahul',
        'done': False,
        'id': 2
    }
]

@app.route("/")
def add_contact():
    return "Contact added"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': tasks[-1]['id'] + 1,
        'contact': request.json.get('contact', ""),
        'name': request.json['name'],
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)