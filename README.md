Readme · MD
Copy

# 📝 Todo App

A full-stack web application for managing your daily tasks, built with **Flask** and **SQLite**.

## ✨ Features

- 🔐 User authentication (Register / Login) with password hashing (SHA-256)
- ➕ Add, update, and delete tasks
- 🏷️ Tag system with 35+ categories (Work, Study, Health, Programming...)
- 📅 Due date and priority support
- 💾 Persistent storage with SQLite

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite
- **Frontend:** HTML, CSS (Jinja2 Templates)

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/v4nixxpy/todo-app.git
cd todo-app
```

### 2. Install dependencies
```bash
pip install flask
```

### 3. Run the app
```bash
python app.py
```

### 4. Open in browser
```
http://localhost:9090
```

## 📁 Project Structure

```
todo-app/
├── app.py          # Main application
├── sqlite3.py      # create the SqLlite database you can copy it's code to app.py and delete this file
├── todo.db         # SQLite database (auto-created)
└── templates/      # HTML templates
    ├── login.html
    ├── register.html
    ├── add.html
    └── update.html
```

## 📌 Usage

1. **Register** a new account
2. **Login** with your credentials
3. **Add tasks** with title, description, priority, tag, and due date
4. **Update or delete** tasks as needed
