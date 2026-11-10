
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


class MODEL:
    def __init__(self, API_KEY):
        self.api = API_KEY

    def CHAIN_RETURN(self):
        llm_model = ChatGroq(
            model="qwen/qwen3.8-27b",
            api_key=self.api,
            temperature=0
        )

        template = """
        Convert the user's question into a SQLite SELECT query.

        Table: employee
        Columns:
        - employee_name
        - employee_role
        - employee_salary

        Question: How many employees are there?
        SQL: SELECT COUNT(*) FROM employee

        Question: What is the average salary by role?
        SQL: SELECT employee_role, AVG(employee_salary)
             FROM employee GROUP BY employee_role

        User question: {query}

        Return only one SELECT query.
        Do not return Markdown, explanations, or semicolons.
        """

        prompt = PromptTemplate(
            input_variables=["query"],
            template=template
        )

        return prompt | llm_model | StrOutputParser()
