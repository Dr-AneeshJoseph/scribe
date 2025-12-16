import re

class ParchmentIsolator:
    """
    Layer 2: The Parchment
    Quarantines input and extracts BOTH Analysis and Result for the user.
    """
    
    @staticmethod
    def quarantine_input(user_query: str) -> str:
        safe_query = user_query.replace('"""', "'")
        return f'"""\n{safe_query}\n"""'

    @staticmethod
    def extract_components(llm_response: str):
        """
        Extracts Analysis AND Result for human review.
        """
        analysis_match = re.search(r"__ANALYSIS__\s*(.*?)\s*(__RESULT__|$)", llm_response, re.DOTALL)
        result_match = re.search(r"__RESULT__\s*(.*?)\s*(__STATE__|$)", llm_response, re.DOTALL)
        
        return {
            "analysis": analysis_match.group(1).strip() if analysis_match else None,
            "result": result_match.group(1).strip() if result_match else None
        }
      
