import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scribe.editor import ScribeEditor

# 1. Context (e.g., Client Requirements)
CONTEXT = "Client needs a Non-Disclosure Agreement (NDA). Jurisdiction: New York. Duration: 5 years."

editor = ScribeEditor(CONTEXT)

print("✍️ S.C.R.I.B.E. Legal Drafting System Online\n")

# --- SCENARIO: DRAFTING A CLAUSE ---
print("--- SCENARIO: Drafting Confidentiality Clause ---")
instruction = "Draft the confidentiality obligations clause."

# Mocking LLM Response
mock_response = """
__ANALYSIS__
Intent: Define obligations.
Precedents: NY Standard NDA.
Strategy: Included 'reasonable care' standard and 5-year sunset clause per context.
__RESULT__
The Recipient agrees to hold all Confidential Information in strict confidence and shall use at least a reasonable degree of care... for a period of five (5) years.
__STATE__
{"draft_status": "DRAFT"}
"""

review_packet = editor.review_draft(mock_response)

if review_packet["valid"]:
    print(f"✅ INTEGRITY CHECK PASSED")
    print(f"--- [LEFT PANEL: AI REASONING] ---\n{review_packet['review_panel']}")
    print(f"\n--- [RIGHT PANEL: DRAFT TEXT] ---\n{review_packet['final_text']}")
else:
    print(f"❌ REJECTED: {review_packet['error']}")
  
