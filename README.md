# 🛡️ Lexical SQL Injection Analyzer with Python and MySQL

This project demonstrates how to detect and prevent **SQL injection attacks** using a basic **lexical analyzer** built in Python, along with a MySQL database connection.

## 🚀 Project Overview

SQL injection is one of the most common web security vulnerabilities. This project shows how input validation and lexical analysis can help detect suspicious query patterns before they reach the database.

### 🔍 What the project includes:

- `file1.py`: Creates a `users` table and inserts sample data into a MySQL database.
- `Injection testing.py`: Demonstrates a **vulnerable query** where SQL injection can succeed (e.g., using `1 OR 1=1`).
- `Lexical_analyser.py`: Analyzes SQL queries using regex and tokenization to detect potentially malicious patterns **before execution**.

---

## ⚙️ Technologies Used

- **Python**
- **MySQL** (via `mysql-connector-python`)
- **Regex** for query pattern detection

---

## 📁 Files Description

| File                  | Description |
|-----------------------|-------------|
| `file1.py`            | Creates a `users` table and inserts dummy data securely |
| `Injection testing.py`| Demonstrates how SQL injection works when input is not validated |
| `Lexical_analyser.py` | Uses lexical analysis to check for dangerous input patterns |

---

## ✅ Features

- Detects common SQL injection patterns (e.g., `OR 1=1`, `--`, etc.)
- Tokenizes SQL queries for analysis
- Rejects unsafe queries before they are executed
- Adds a learning layer on **how not to write unsafe SQL code**

---

## 🖥️ How to Run the Project

### 1. Install dependencies:
```bash
pip install mysql-connector-python
```

### 2. Set up MySQL database:
-Make sure MySQL is running.
-Update the database credentials (host, user, passwd, etc.) in all files.

### 3. Run the files in order:
```bash
python file1.py
```
-This will create the table and insert sample users.

```bash
python Injection\ testing.py
```
-This shows a vulnerable query (try inputting: 1 OR 1=1).

```bash
python Lexical_analyser.py
```
-This protects the query using lexical pattern checks. It will reject suspicious inputs.

---

## ⚠️ Disclaimer
This project is for educational purposes only. Lexical analysis is helpful as a secondary detection method, but the most secure approach is to always use parameterized queries.
