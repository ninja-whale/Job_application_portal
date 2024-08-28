# Job Application Portal

Welcome to the Job Application Portal! This Flask-based web application allows users to log in, fill out a job application form for a Software Engineer position, and upload their resume. Once the form is submitted, users can view their submission but cannot modify it.

## Features

- **User Authentication**: Users can sign up, log in, and log out.
- **Job Application Form**: Users fill out a form with their experience, skills, cover letter, and upload their resume.
- **View Submission**: After submission, users can view their job application details but cannot edit them.
- **Responsive Design**: The application is styled using Bootstrap for a clean and responsive interface.

## Installation

Follow these steps to set up and run the application locally:

### Prerequisites

- Python 3.7+
- Flask
- SQLAlchemy
- Werkzeug

### Clone the Repository

```bash
git clone https://github.com/ninja-whale/Job_application_portal.git
cd job-application-portal
```

### Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python backend/app.py
```

The application should now be running on [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Usage

1. **Sign Up**: Create an account by signing up with your name, email, and password.
2. **Log In**: Log in using your credentials.
3. **Fill Out Job Application**: Complete the form with your experience, skills, cover letter, and upload your resume.
4. **View Submission**: After submitting, you can view your application details, but you won’t be able to modify them.

## File Structure

```plaintext
Job_applicatiob_portal/
│
├── Website/
│   ├── app.py
│   ├── config.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── signup.html
│   │   ├── login.html
│   │   ├── job_details.html
│   │   ├── view_submission.html
│   │   └── layout.html
│   ├── uploads/            # Uploaded resumes will be stored here
│   └── requirements.txt             
└── README.md          # This file
```

## Contributing

If you'd like to contribute to this project, please feel free to fork the repository and submit a pull request.

---

Developed by [ninja-whale](https://github.com/ninja-whale)

