from app.services.openai_service import llm
from app.services.mcqs_prompt import mcq_prompt, parser
from app.utils.logger import logger

def generate_mcqs(language: str):
    logger.info(f"Generating MCQs for {language}")
    try:
        chain = mcq_prompt | llm | parser
        result = chain.invoke({"language": language})
        logger.info(f"Generated {len(result.mcqs)} MCQs")
        return result.mcqs

    except Exception as e:
        logger.error(f"Error generating MCQs: {str(e)}", exc_info=True)
        raise Exception("Failed to generate MCQs")
