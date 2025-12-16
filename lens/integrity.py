class IntegrityLens:
    """
    Layer 3: The Lens
    Ensures the AI has provided the mandatory explanation before the text.
    """
    
    def check_integrity(self, components: dict):
        """
        Returns (is_valid: bool, error: str)
        """
        analysis = components.get("analysis")
        result = components.get("result")

        # RULE 1: Completeness
        if not analysis or not result:
            return False, "STRUCTURAL FAILURE: Missing Analysis or Result block."

        # RULE 2: Length Ratio (Heuristic)
        # If the explanation is tiny compared to a huge document, it's suspicious.
        if len(result) > 500 and len(analysis) < 50:
            return False, "AUDIT FAILURE: Explanation too brief for the generated text length."

        # RULE 3: Citation consistency (Simple Keyword Check)
        # If Result has '[Source]', Analysis should mention 'Source'.
        if "[Source]" in result and "Source" not in analysis:
            return False, "CITATION ERROR: Result cites a source not discussed in Analysis."

        return True, "INTEGRITY_PASS"
      
