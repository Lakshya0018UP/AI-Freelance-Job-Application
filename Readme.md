# Job Portal Application

This is a full-stack job portal application built with Flask (backend) and React (frontend). It allows users to sign up, log in, create jobs, apply for jobs, and manage applications.

## Features
- User authentication (signup/login) with JWT
- Create, view, update, and delete jobs
- Apply for jobs
- Role-based access control (Admin/Professional can create jobs)
- View applied jobs and update job status

## Technologies Used
### Backend (Flask)
- Flask
- Flask-JWT-Extended
- SQLAlchemy
- SQLite/PostgreSQL (configurable)

### Frontend (React)
- React.js
- React Router
- Axios
- Tailwind CSS

## Installation

### Prerequisites
- Python 3.8+
- Node.js & npm

### Backend Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo.git
   cd your-repo/backend
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Set environment variables:
   **For Windows:**
   ```sh
   set FLASK_APP=app.py
   set FLASK_ENV=development
   ```
   **For macOS/Linux:**
   ```sh
   export FLASK_APP=app.py
   export FLASK_ENV=development
   ```

5. Initialize the database:
   ```sh
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

6. Run the backend server:
   ```sh
   flask run
   ```

### Frontend Setup
1. Navigate to the frontend folder:
   ```sh
   cd ../frontend
   ```

2. Install dependencies:
   ```sh
   npm install
   ```

3. Start the React development server:
   ```sh
   npm start
   ```

## API Endpoints

### Authentication
- `POST /api/signup` - User registration
- `POST /api/login` - User login

### Jobs
- `GET /api/jobs` - Get all jobs
- `POST /api/jobs` - Create a new job (Admin/Professional only)
- `DELETE /api/delete_job/<id>` - Delete a job
- `PATCH /api/update_jobs/<id>` - Update a job

### Applications
- `POST /api/apply/<id>` - Apply for a job
- `GET /api/applied_jobs/<id>` - View applicants (Admin/Professional only)
- `PATCH /api/update_status/<id>` - Update application status

