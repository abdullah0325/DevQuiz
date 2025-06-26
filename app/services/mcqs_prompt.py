from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from app.schemas.mcq_schema import MCQList

parser = PydanticOutputParser(pydantic_object=MCQList)

mcq_prompt = PromptTemplate(
    template="""
    Generate 10 multiple-choice questions (MCQs) on the programming language {language}.
    Each question should have four options (A, B, C, D), with one correct answer clearly indicated.

    {format_instructions}

    Ensure questions cover syntax, best practices, and key concepts.
    """,
    input_variables=["language"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)


