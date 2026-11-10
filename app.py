
import os
import sqlite3
from dotenv import load_dotenv
from employee_db import SQLDB
from llm import MODEL

load_dotenv()

api = os.getenv("API_KEY")

if not api:
    raise ValueError("API_KEY is missing from your .env file.")

# Initialize the database
db = SQLDB()
db.DATABASE()

# Create the chain
chain = MODEL(api).CHAIN_RETURN()

query = "What is the average salary based on department"

sql_query = chain.invoke({"query": query}).strip()
sql_query = sql_query.removeprefix("```sql").removesuffix("```").strip()
sql_query = sql_query.removesuffix(";").strip()

print("\nGenerated SQL:")
print(sql_query)

# Only allow SELECT queries
if not sql_query.upper().startswith("SELECT"):
    raise ValueError("Only SELECT queries are allowed.")

conn = sqlite3.connect("employee.db")

try:
    cursor = conn.cursor()
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    print("\nQuery Results:")
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print("SQL execution error:", e)

finally:
    conn.close()
