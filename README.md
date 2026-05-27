# Breathe ESG Assignment

A full-stack ESG data management platform built using Django and React.

---

# Features

## Backend Features

- CSV ingestion pipeline
- ESG data normalization
- Unit conversion support
- Scope mapping
- Suspicious data detection
- Review workflow
- Audit locking system
- Audit trail logging
- REST APIs using Django REST Framework

---

## Frontend Features

- React dashboard
- CSV upload UI
- Review management
- Approve records
- Lock records for audit
- Live status updates
- Professional UI dashboard

---

# Tech Stack

## Backend
- Django
- Django REST Framework
- SQLite

## Frontend
- React.js
- Axios
- CSS

---

# API Endpoints

## Upload CSV

POST

/api/upload/sap/

---

## Review Records

GET

/api/review/

---

## Approve Record

POST

/api/review/<id>/approve/

---

## Lock Record

POST

/api/review/<id>/lock/

---

# ESG Workflow

1. Upload CSV file
2. Data ingestion
3. Normalization engine processes records
4. Suspicious records flagged
5. Reviewer approves records
6. Records locked for audit
7. Audit logs generated

---

# Sample Suspicious Detection

Negative quantities are automatically flagged as suspicious.

Example:

-100 liters → suspicious_flag = True

---

# Project Setup

## Backend Setup

```bash
cd backend

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm start
```

---

# URLs

Frontend:

http://localhost:3000

Backend:

http://127.0.0.1:8000

---

# Future Improvements

- Authentication system
- Multi-tenant support
- Charts & analytics
- Cloud deployment
- AI anomaly detection

---

# Author

Adarsh Deshmukh