# Course Web App 🎓 (Django)

A *Course Management Web Application* built using *Django*.  
The application allows users to view course details, while authenticated users can *add, edit, and delete courses/projects* with full *login and logout functionality*.

---

## ✨ Features

- User Authentication
  - Login
  - Logout

- Course / Project Management (CRUD)
  - Add course
  - Edit course
  - Delete course

- Course Detail View
  - Users can see detailed information about each course
- Secure access using Django Authentication
- Simple and clean UI



---

## 🛠 Tech Stack

- *Backend:* Django (Python)
- *Frontend:* HTML, CSS (Django Templates)
- *Database:* SQLite
- *Authentication:* Django built-in auth system

---

---

## ⚙️ How to Run the Project Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/courseweb.git
cd courseweb

---

2️⃣ Create Virtual Environment
Copy code
Bash
python -m venv venv
Activate the virtual environment:


Windows
Copy code

Bash
venv\Scripts\activate

Linux / Mac
Copy code

Bash
source venv/bin/activate

3️⃣ Install Required Dependencies
Copy code

Bash
pip install django
4️⃣ Apply Migrations
Copy code
Bash
python manage.py makemigrations
python manage.py migrate
5️⃣ Create Superuser (Optional but Recommended)
Copy code
Bash
python manage.py createsuperuser
Use this account to access admin and manage courses.

6️⃣ Run the Development Server
Copy code
Bash
python manage.py runserver
Open your browser and go to:
Copy code

http://127.0.0.1:8000/

