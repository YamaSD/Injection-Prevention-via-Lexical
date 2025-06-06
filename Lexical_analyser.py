import mysql.connector
import re


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="******",
    database="testdatabase"
)

cursor = connection.cursor()


ALLOWED_SQL_PATTERNS = [
    r"SELECT\s+\*\s+FROM\s+\w+\s+WHERE\s+\w+\s*=\s*\d+",     #  numeric comparison
    r"SELECT\s+\*\s+FROM\s+\w+\s+WHERE\s+\w+\s*=\s*'.*'",  # string comparison
]

DISALLOWED_PATTERNS = [
    r".*\s+OR\s+.*",  # detects 'OR' based SQL injection
    r".*\s+AND\s+.*",  # Detects 'AND' based SQL injection
    r".*;\s*--.*",  # detects semicolon, comment attacks
    r".*=\s*\d+\s*=\s*\d+.*",  # detects cases '1=1'
]

def escape_special_characters(query):
    query = query.replace("'", "\\'")
    query = query.replace('"', '\\"')
    query = query.replace('--', '')  # remove comments
    return query

def tokenize_query(query):
    tokens = re.findall(r"[\w']+|[.,;*()=<>]", query)
    return tokens

def contains_disallowed_patterns(query):
    """Check if the query contains any disallowed patterns like OR 1=1."""
    for pattern in DISALLOWED_PATTERNS:
        if re.search(pattern, query, re.IGNORECASE):
            return True
    return False

def is_valid_query(query):
    """Check if the query matches the allowed patterns and doesn't contain disallowed patterns."""
    if contains_disallowed_patterns(query):
        return False
    for pattern in ALLOWED_SQL_PATTERNS:
        if re.search(pattern, query, re.IGNORECASE):
            return True
    return False

def analyze_sql_query(query):
    safe_query = escape_special_characters(query)
    tokens = tokenize_query(safe_query)
    print("Tokens:", tokens)

    if is_valid_query(safe_query):
        print("Valid query.")
        return safe_query
    else:
        print("Invalid query: possible SQL injection detected!")
        return None


user_input = input("Enter user ID: ")


query = f"SELECT * FROM users WHERE id = {user_input};"


safe_query = analyze_sql_query(query)

if safe_query:
    cursor.execute(safe_query)
    results = cursor.fetchall()

    for row in results:
        print(row)
else:
    print("Query rejected due to potential SQL injection risk.")


cursor.close()
connection.close()
