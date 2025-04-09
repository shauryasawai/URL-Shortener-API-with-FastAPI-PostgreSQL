# 🔗 URL Shortener API using Django & PostgreSQL

---

## 📌 Overview

This is a basic URL shortener API built using **Django**, **Django REST Framework**, and **PostgreSQL**.

It allows users to:
- **Shorten a long URL** (e.g., https://openai.com/blog/chatgpt)
- **Get a short URL** (e.g., http://localhost:8000/aB9d2K)
- **Redirect** to the original URL when the short one is accessed

---

## ⚙️ Tech Stack

- **Backend**: Django + Django REST Framework
- **Database**: PostgreSQL
- **Language**: Python 3.x
- **Tools**: curl/Postman for testing

---

## 🧠 Functionality

### 1. Shorten URL
- **Endpoint**: `POST /shorten/`
- **Input**: A JSON object with `"original_url"`
- **Output**: A shortened URL containing a unique 6-character code

### 2. Redirect to Original URL
- **Endpoint**: `GET /<short_code>/`
- **Action**: Redirects the user to the original long URL

---


---

