# AI Database Query System using Groq and LangChain

## Project Overview
This project converts natural language questions into SQL queries using a Groq LLM integrated with LangChain. It executes the generated SQL queries on an SQLite database and displays the results.

## Technologies Used
- Python
- Groq LLM
- LangChain
- SQLite
- SQL
- python-dotenv

## Project Structure
```text
AI_Database/
├── app.py
├── employee_db.py
├── llm.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Features
- Converts English questions into SQL queries.
- Uses Groq LLM through LangChain.
- Executes SQL queries using SQLite.
- Restricts execution to SELECT queries.
- Displays database query results.

## Installation

1. Clone the repository:
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Navigate to the project:
```bash
cd AI_Database
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file and add your Groq API key:
```env
API_KEY=your_groq_api_key
```

5. Run the application:
```bash
python app.py
```

## Example Query

**Input:**
What is the average salary based on department?

**Output:**
The application generates an SQL query and executes it against the employee database.

## Security
API keys are stored in environment variables and are not committed to GitHub.
