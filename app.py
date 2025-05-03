from flask import Flask, jsonify, request, abort, render_template
## Importing the necessary modules from the flask package
## The Flask class is used to create a new Flask application instance
##pip install Flask, pip install Flask-RESTful
## The jsonify function is used to convert a Python dictionary to a JSON response
## The request module is used to access the incoming request data
## The abort function is used to return an error response with a specific status code
app = Flask(__name__)

# Static student data
st_data = {
    "st_1": "swapna",
    "st_2": "sai",
    "st_3": "sri"
}

@app.route('/hello', methods=['GET'])
def hellolabs():
    data = {"data": "AVJ Labs"}
    return jsonify(data)

@app.route('/students', methods=['GET'])
def hellomvj():
    return jsonify(st_data)

# New route to handle individual student lookup
@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    if student_id in st_data.keys():
        return jsonify({student_id: st_data[student_id]})
    else:
        abort(404, description="Student not found")

@app.route('/mywebsite')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
