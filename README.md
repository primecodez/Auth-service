````markdown
# Auth Service

My first attempt at building an authentication service from scratch using **FastAPI**, **PostgreSQL**, and **JWT**.

The goal of this project isn't just to make authentication work—it's to understand *how* it works. Instead of relying on third-party authentication services or copying a tutorial, I'm building each feature step by step while learning the concepts behind it.

This repository will continue to evolve as I learn more about backend development, security, and writing cleaner code.

If you're learning FastAPI too, I hope this project can be a useful reference.

---

## Features

- User Registration
- User Login
- Password Hashing (bcrypt)
- JWT Authentication
- Access & Refresh Tokens
- Role-Based Access Control (RBAC)
- Email Verification
- Password Reset
- Protected Routes
- Database Migrations

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.12+ |
| Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| Authentication | JWT |
| Password Hashing | bcrypt |
| Migrations | Alembic |
| Server | Uvicorn |

---

## Project Structure

```text
auth-service/
│
├── app/
│   ├── api/
│   ├── database/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── tests/
├── requirements.txt
├── .env.example
├── README.md
└── LICENSE
```

---

## What I'm Learning

This project is helping me explore and understand:

- Designing REST APIs with FastAPI
- Authentication & Authorization
- JWT Access & Refresh Tokens
- Password Hashing
- PostgreSQL & SQLAlchemy
- Database Migrations
- Writing maintainable backend code
- Building projects with a clean structure
- Backend security fundamentals

---

## API Endpoints

| Method | Endpoint |
|---------|----------|
| POST | `/register` |
| POST | `/login` |
| POST | `/refresh` |
| POST | `/logout` |
| POST | `/verify-email` |
| POST | `/forgot-password` |
| POST | `/reset-password` |
| GET | `/me` |

---

## Running Locally

Clone the repository:

```bash
git clone https://github.com/<your-username>/auth-service.git
cd auth-service
```

Create a virtual environment:

```bash
python -m venv .venv
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file using `.env.example`, run the migrations, and start the server:

```bash
alembic upgrade head

uvicorn app.main:app --reload
```

Visit:

```
http://localhost:8000/docs
```

to explore the API.

---

## Roadmap

- [ ] User Registration
- [ ] Login
- [ ] JWT Authentication
- [ ] Refresh Tokens
- [ ] Role-Based Access Control
- [ ] Email Verification
- [ ] Password Reset
- [ ] Unit & Integration Tests
- [ ] Docker Support
- [ ] GitHub Actions
- [ ] OAuth Login (Google & GitHub)

---

## Why this project?

Authentication is something almost every application needs, but it often feels like a "black box."

I wanted to understand what actually happens when a user signs up, logs in, receives a token, or resets a password. Instead of treating those features as magic, this project is my attempt to build them myself, understand the trade-offs, and improve the implementation as I learn.

---

## Contributing

Suggestions, feedback, and improvements are always welcome. If you spot a bug or have an idea that could make the project better, feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License.
````
