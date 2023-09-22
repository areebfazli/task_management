from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/tasks/*": {"origins": "http://127.0.0.1:5000"}})  # Allow requests from your frontend


# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Task model structure
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

# Create the database tables within the app context
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
def create_task_page():
    return render_template('index.html')

# POST: Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if 'title' not in data or 'description' not in data:
        return jsonify({'message': 'Title and description are required'}), 400

    new_task = Task(title=data['title'], description=data['description'])
    db.session.add(new_task)
    db.session.commit()

    return jsonify({'message': 'Task created successfully', 'id': new_task.id}), 201

# GET: Retrieve all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    task_list = [{'id': task.id, 'title': task.title, 'description': task.description} for task in tasks]
    return jsonify(task_list)

# GET: Retrieve a specific task by ID
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get(id)
    if task:
        return jsonify({'id': task.id, 'title': task.title, 'description': task.description})
    return jsonify({'message': 'Task not found'}), 404

# PUT: Update an existing task by ID
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    task = Task.query.get(id)
    if task:
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        db.session.commit()
        return jsonify({'message': 'Task updated successfully'})
    return jsonify({'message': 'Task not found'}), 404

# DELETE: Delete a task by ID
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted successfully'})
    return jsonify({'message': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
