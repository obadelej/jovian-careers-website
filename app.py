from flask import Flask, render_template, jsonify

Persons = [
    {    
        'id': 1,
        'name': 'Taigon',
        'age': '19',
        'address': 'Willis'
    },
    
    {    
        'id': 2,
        'name': 'Ethan',
        'age': '17',
        'address': 'La Mode'
    },
    {    
        'id': 3,
        'name': 'Devonni',
        'age': '19',
        'address': 'Gouyave'
    }
        
]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html', persons=Persons)


@app.route("/api/persons")
def list_persons():
    return jsonify(Persons)
    
  

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)


