# 💸 Expense Tracking System

A **full-stack Expense Tracking System** built as a bootcamp project to help users **track, manage, and analyze daily expenses**. This project demonstrates the practical use of **FastAPI** for backend APIs, **MySQL** for data storage, and **Streamlit** for building an interactive and user-friendly web interface.

---

## 🚀 Project Overview

This system allows users to:

- Add and update expenses for any selected date.
- View detailed analytics by category for a custom date range.
- Get a monthly breakdown of expenses with charts and tables.

It's an end-to-end data project that covers:

✅ Backend API development  
✅ Database design and interaction  
✅ Logging and error handling  
✅ Interactive frontend dashboard  
✅ Data visualization with charts  
✅ Clean project structure  

---

## 🏗️ Architecture & Components

### 🔧 Backend – FastAPI

- **FastAPI** serves as the RESTful API framework.
- Handles CRUD operations and analytics endpoints.
- Implements error handling with meaningful HTTP responses.
- Uses Python’s `logging` module to track key events.

### 🛢️ Database – MySQL

- Stores all expense records in a table `expenses`.
- Each record has: `id`, `expense_date`, `amount`, `category`, and `notes`.
- Accessed using `mysql.connector` with context managers for safe transactions.

### 📊 Frontend – Streamlit

- Allows users to:
  - Add or update up to 5 expenses per day.
  - View expense breakdown by category using bar charts and tables.
  - Get monthly summaries with visualizations.
- Communicates with the FastAPI backend using Python `requests`.

## 📚 What I Learned

- How to build APIs using **FastAPI** to send and receive data.
- How to connect Python with a **MySQL** database to store and retrieve data.
- How to create an interactive web app using **Streamlit**.
- How to make HTTP requests and handle responses between frontend and backend.
- How to visualize data with charts and tables.
- How to organize code into clean, modular files.
- How to add logging to track program actions.

---
