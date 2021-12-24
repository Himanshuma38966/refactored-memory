from flask import Flask,jsonify,request
#######object creation i.e app and class name is Flask passing argument __name__  i.e main
app=Flask(__name__)
@app.route("/")
def helloworld():
    return "Hi iam himanshu"


@app.route("/aboutme")
def helloworldi():
    return "Hi"


tasks=[
    
    
    {
        'id':1,
        'title':u'do your home work',
        'description':u'maths,kannada,',
        'done':False
        
    },
     {
        'id':1,
        'title':u'do your home work',
        'description':u'maths,kannada,',
        'done':False
        
    }
     
]


@app.route('/get-data')
def get_data():
    return jsonify({
        "data":tasks
            
    })
    
@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!",
        # added to show all tasks added by me
        "data":tasks
    })
    
    
    
#print(__name__)
if(__name__ =="__main__"):
    app.run(debug=True)
    
    
    