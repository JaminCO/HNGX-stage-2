```markdown
# HNGx Stage 2 Backend Task

This is a basic RESTful API created with Flask that performs simple CRUD operations. It allows you to create, read, update, and delete user records in a SQLite database.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3 (python.org)
- Flask (pip install Flask)
- Flask-SQLAlchemy (pip install Flask-SQLAlchemy)

## Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/JaminCO/HNGx.git
   ```

2. Change to the project directory:

   ```bash
   cd Hngx
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

5. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

6. Initialize the SQLite database:

   ```bash
   python
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

## Running the API

To start the Flask API, run the following command from the project directory:

```bash
python app.py
```

By default, the API will be accessible at http://localhost:5000.

## Usage

### Create a User

- **Endpoint:** POST /api
- **Request Body:**

  ```json
  {
    "name": "John Doe"
  }
  ```

- **Response:**

  ```json
  {
    "success": true,
    "message": "User created",
    "id": 1
  }
  ```

### Get a User

- **Endpoint:** GET /api/{user_id}

- **Response:**

  ```json
  {
    "id": 1,
    "name": "John Doe"
  }
  ```

### Update a User

- **Endpoint:** PUT /api/{user_id}
- **Request Body:**

  ```json
  {
    "name": "Updated Name"
  }
  ```

- **Response:**

  ```json
  {
    "success": true,
    "message": "User updated",
    "id": 1
  }
  ```

### Delete a User

- **Endpoint:** DELETE /api/{user_id}

- **Response:**

  ```json
  {
    "success": true
  }
  ```
Please note that the `{user_id}` in the endpoint should be replaced with the actual user ID you want to interact with.

## Closing Remarks

This Flask API provides basic CRUD functionality for managing user records in a SQLite database. You can use it as a starting point for more complex projects or as a learning resource for Flask and RESTful API development.
