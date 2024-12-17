# Django Quiz Application 🎯

A simple quiz application built using Django. This project allows users to take a quiz, submit answers, and view results at the end. It includes a clean UI, random question fetching, and real-time answer submission without using sessions.

---

## Features 🛠️

- **Home Page**: Users type `start` to begin the quiz.  
- **Random Questions**: Questions are fetched dynamically from the database.  
- **Timer**: A 45-second timer with a progress bar to complete the quiz.  
- **Answer Submission**: User answers are submitted and evaluated in real-time.  
- **Results Page**: Displays total questions, correct answers, and incorrect answers.  

---

## Technologies Used 🚀

- **Backend**: Django 4.2.5  
- **Frontend**: HTML, CSS (Bootstrap 5.3), JavaScript  
- **Database**: SQLite3 (default Django DB)  

---

## Setup Instructions 🖥️

Follow these steps to get the project up and running locally:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/quiz-app.git
cd quiz-app
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
```

### 3. Activate it

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Server
```bash
python manage.py runserver
```

---

## Contact ✉️
For questions or support, reach out to:

Shawn T

LinkedIn: www.linkedin.com/in/shawnthomas02
