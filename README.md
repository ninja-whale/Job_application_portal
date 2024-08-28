# Job Application Portal

This is a simple Flask-based job application portal where users can sign up, log in, fill out a job application form, and upload their resumes for a Software Engineer position. The application is deployed on Vercel.

## Features

- **User Authentication**: Users can sign up and log in to the portal.
- **Job Application Form**: Users can fill out details about their experience, skills, and upload a resume.
- **View Submission**: Once the form is submitted, users can view their application details but cannot edit them.
- **File Uploads**: Uploaded resumes are securely stored in the `uploads/` directory.

## Project Structure

```
Job_application_portal/
│
├── Website/
│   ├── app.py                # Main entry point of the Flask application
│   ├── config.py             # Configuration settings
│   ├── templates/            # HTML templates for the application
│   │   ├── index.html
│   │   ├── signup.html
│   │   ├── login.html
│   │   ├── job_details.html
│   │   ├── view_submission.html
│   │   └── layout.html
│   ├── uploads/              # Directory for uploaded resumes
│   └── requirements.txt      # Python dependencies
├── vercel.json               # Configuration for deploying on Vercel
└── README.md                 # Project documentation
```

## Requirements

Ensure you have the following installed:

- Python 3.8 or higher
- Pip (Python package installer)
- Vercel CLI (optional, for local deployment testing)

## Installation

### Clone the Repository

```bash
git clone https://github.com/ninja-whale/Job_application_portal.git
cd your-repo-name/Website
```

### Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Run the Application Locally

Start the Flask application:

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your web browser to see the application running.

## Deployment

### Deploying on Vercel

This project is configured to deploy on Vercel. Follow these steps:

1. **Push to GitHub**: Ensure your code is pushed to GitHub.
2. **Import GitHub Repository**: Go to [Vercel](https://vercel.com/), log in, and import your GitHub repository.
3. **Deploy**: Vercel will automatically build and deploy the application based on the `vercel.json` file.
4. **Visit the Deployed URL**: Vercel will provide a URL where your application is hosted.

### Configuration

The application uses a `config.py` file for configuration. You can modify this file to set your Flask configuration settings, such as secret keys or database URIs.

### Environment Variables

If your application requires environment variables (e.g., for secret keys or API access), you can set them in the Vercel dashboard under **Settings** -> **Environment Variables**.

## Troubleshooting

- **500 Internal Server Error**: Check the Vercel logs for details on the error.
- **File Not Found**: Ensure that all paths are correctly referenced in your Flask application, especially when serving static files or accessing the `uploads/` directory.
- **Build Failures**: Double-check your `requirements.txt` and `vercel.json` configuration files.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments

- **Flask**: Micro web framework for Python.
- **Bootstrap**: CSS framework used for styling the application.
- **Vercel**: Platform for frontend frameworks and static sites, and deployment of full-stack applications.
