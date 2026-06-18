# 💰 Microfinance Loan Management Website

A web-based Microfinance Loan Management System developed to simplify the management of loans, customers, and financial records. The application provides an easy-to-use platform for handling loan applications, approvals, repayments, and customer information.

## ✨ Features

- 👥 Customer registration and management
- 💵 Loan application and processing
- ✅ Loan approval and status tracking
- 📅 Repayment schedule management
- 📊 Dashboard for monitoring loan records
- 🔐 User authentication and authorization
- 📝 Manage customer and loan information
- 📱 Responsive user interface

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- Bootstrap

### Backend
- Django
- Python

### Database
- SQLite (Default Django Database)

---

## 📦 Installation

### 1. Clone the repository

### 2. Create a virtual environment

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install required packages

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file, install Django manually:

```bash
pip install django
```

---

## ⚙️ Configuration

Apply database migrations:

```bash
python manage.py migrate
```

Create an admin account:

```bash
python manage.py createsuperuser
```

---

## ▶️ Running the Project

Start the Django development server:

```bash
python manage.py runserver
```

Then open your browser and visit:

```
http://127.0.0.1:8000/
```

---

## 📁 Project Structure

```
microfinance-loan-system/
│
├── manage.py            # Django management file
├── app/                 # Main application
├── templates/           # HTML templates
├── static/              # CSS, JavaScript, images
├── db.sqlite3           # Database file
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

---

## 🔮 Future Improvements

- Add mobile money payment integration
- Generate loan reports and analytics
- Add email/SMS notifications
- Improve security and permissions
- Integrate advanced financial dashboards
- Deploy the system to a cloud server

---

## 👨‍💻 Author

**Mukasa Mohamedy**

Information Technology Developer passionate about Web Development, AI, and Software Engineering.

---

## 📄 License

This project is open-source and available under the MIT License.
