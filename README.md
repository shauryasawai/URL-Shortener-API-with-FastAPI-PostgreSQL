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

## Installation Steps:-


### 1️⃣ Setting Up the Django Backend

### Step 1: Clone the Repository

Clone the Django application repository to your local machine using the following command:

```bash
git clone https://github.com/shauryasawai/URL-Shortener-API-with-FastAPI-PostgreSQL
```

### Step 2: Navigate to the Project Directory

Change into the directory of the cloned repository:

```bash
cd LOOB_aasign
```

### Step 3: Create a Virtual Environment

Create a virtual environment using `virtualenv`:

```bash
python -m venv my_env
```
```bash
pip install virtualenv
```
This will create a virtual environment named `my_env`.

### Step 4: Activate the Virtual Environment

Activate the virtual environment using the following command:

- On Windows:
  ```bash
  my_env\Scripts\activate
  ```
- On macOS and Linux:
  ```bash
  source venv/bin/activate
  ```

### Step 5: Install Dependencies

With the virtual environment activated, install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

This will install all the dependencies listed in the `full-requirements.txt` file.

### Step 6: Run Migrations

Apply the database migrations:

```bash
python manage.py migrate
```

### Step 7: Start the Development Server

Run the development server to start the application:

```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/` in your web browser.

## Deactivating the Virtual Environment

To deactivate the virtual environment, simply run:

```bash
deactivate
```
---

