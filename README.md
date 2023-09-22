# task_management

# Task List RESTful API

This is a simple RESTful API built with Flask that allows users to manage a task list.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- Python 3.x
- Pip (Python package manager)
- SQLite (or any other database of your choice)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/task-list-api.git
   cd task-list-api


### Create and activate a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

### Install project dependencies:
pip install -r requirements.txt

### Set up the database:
flask db init
flask db migrate
flask db upgrade


## Usage
### Start the Flask application:
flask run
The API will be available at http://localhost:5000.

### You can use a tool like curl or a REST client like Postman or Insomnia to interact with the API. Here are some example API endpoints:
POST /tasks: Create a new task.
GET /tasks: Retrieve a list of all tasks.
GET /tasks/{id}: Retrieve a specific task by ID.
PUT /tasks/{id}: Update an existing task by ID.
DELETE /tasks/{id}: Delete a task by ID.
