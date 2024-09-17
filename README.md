# redback-cms
Content management system (software) for the management of:
- shared information and media for public-facing websites (such as "About Redback" and product overviews)
- static information within the apps for Redback's wearable technology, smartbike, and related projects (such as how-to guides).


# Redback Fit Backend

This is the backend API for the Redback Fit application, built with Flask.

## Project Structure

redback_cms/
│
├── app/
│ ├── init .py
│ ├── models.py
│ ├── routes/
│ │ ├── init .py
│ │ ├── auth.py
│ │ 
│ └── utils.py
│
├── config.py
├── requirements.txt
└── run.py


## Setup and Installation

1. Clone the repository:
git clone https://github.com/Redback-Operations/redback-cms.git
cd redback_cms





2. Activate the virtual environment:
- On Windows: `env\Scripts\activate`
- On macOS and Linux: `source env/bin/activate`

3. Install the required packages:
pip install -r requirements.txt


4. Set up environment variables:
Create a `.env` file in the project root with the following content:


FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///redback_fit.db # in developmenthttps://github.com/Redback-Operations/redback-cms.git





## Running the Application

To run the application, use the following command:


python run.py


The API will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### Authentication

- Register a new user:
  - POST `/auth/register`
  - Body: `{"username": "string", "email": "string", "password": "string"}`

- Login:
  - POST `/auth/login`
  - Body: `{"username": "string", "password": "string"}`



## Database Models

### User
- id: Integer, primary key
- username: String, unique
- email: String, unique
- password_hash: String



