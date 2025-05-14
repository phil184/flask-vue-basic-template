# 🚀 Flask + Vue 3 + Tailwind CSS Template

A simple starter template to quickly get up and running with **Flask** and **Vue 3** + **Tailwind CSS**.

This project includes:
- A minimal base configuration
- A simple authentication system (login)
- A connected frontend and backend with a working dashboard after login

---

## 📦 Dependencies

### Backend
- Flask
- Flask-Login
- SQLAlchemy
- Flask-CORS

### Frontend
- Vue 3
- Tailwind CSS
- Axios

---

## 🧱 Tech Stack

- [Flask](https://flask.palletsprojects.com/)
- [Vue.js](https://vuejs.org/)
- [Tailwind CSS](https://tailwindcss.com/)

---

## 📁 Project Structure
```
template/
│
├── api/ # Flask application
│ ├── init # App initialization, database, blueprints
│ ├── config # Basic configuration classes
│ ├── models # SQLAlchemy models / Flask-Login User class
│ └── views # API routes
│
├── frontend/ # Vue 3 + Tailwind app
│ ├── src/ # Assets, components, views
│ ├── router/ # Routing configuration
│ ├── App/ # Main entry point
│ └── ... # Tailwind and Vite config files
│
├── run # Flask entry point
├── Makefile # Setup script (venv, install dependencies, etc.)
├── requirements.txt # Python dependencies
└── setup # Optional: Windows/Linux setup scripts
```

---

## 🛠️ Setup Instructions

### Option 1: Quick Setup

Use the provided setup scripts:

- On Windows:  
```bash
  ./setup.bat
```
With Makefile (Linux/macOS):
```bash
    make setup
```

## Manual Setup
### Backend
```bash
    python3 -m venv venv
    source venv/Scripts/activate  # Or 'source venv/bin/activate' on Linux/macOS
    pip install -r requirements.txt
    python run
```
# Create a user with a password when prompted

### Frontend
```bash
    cd frontend
    npm install
    npm run dev
```

Flask runs on port 5000 and Vue on port 5174

Visit: http://localhost:5174

You should see a message displaying "API response", this confirms the connection is working.

Then navigate to /login to access the login page. Use your created credentials to log in and access the dashboard.

🤝 Contributing

Suggestions, improvements, and pull requests are always welcome!

❤️ Happy coding!
