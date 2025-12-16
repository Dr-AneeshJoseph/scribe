import os
from .parchment.isolator import ParchmentIsolator
from .lens.integrity import IntegrityLens

class ScribeEditor:
    def __init__(self, context_str: str = ""):
        self.isolator = ParchmentIsolator()
        self.lens = IntegrityLens()
        self.context = context_str
        
        # Load Prompt
        prompt_path = os.path.join(os.path.dirname(__file__), 'quill', 'drafting_prompt.md')
        with open(prompt_path, 'r') as f:
            self.base_prompt = f.read()

    def draft(self, user_instruction: str) -> str:
        quarantined = self.isolator.quarantine_input(user_instruction)
        return f"{self.base_prompt}\n\nCONTEXT:\n{self.context}\n\nINSTRUCTION:\n{quarantined}"

    def review_draft(self, llm_raw_response: str):
        """
        Pipeline: Extract -> Check Integrity -> Return Split View
        """
        # 1. Extract
        parts = self.isolator.extract_components(llm_raw_response)
        
        # 2. Validate
        is_valid, msg = self.lens.check_integrity(parts)

        if is_valid:
            return {
                "valid": True,
                "review_panel": parts["analysis"],  # Show to human
                "final_text": parts["result"],      # The draft
                "status": "READY_FOR_HUMAN"
            }
        else:
            return {"valid": False, "error": msg}
          
