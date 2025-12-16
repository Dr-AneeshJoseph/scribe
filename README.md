# ✍️ S.C.R.I.B.E. (Secure Content Review & Integrity-Based Engine)

> **The Human-in-the-Loop Architecture for High-Stakes Drafting.**

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


---

## ⚠️ The Problem
In Legal and Medical AI, "Black Box" generation is unacceptable.
* You cannot sign a contract if you don't know *why* the AI added a specific clause.
* You cannot approve a medical summary if you don't see the source data linkage.

## 🛡️ The Solution
**S.C.R.I.B.E.** forces the AI to "Show its Work." It decouples the **Reasoning** (`__ANALYSIS__`) from the **Output** (`__RESULT__`) and mechanically validates that both exist before presenting them to the human reviewer.

### The Architecture
1.  **Layer 1: The Quill (Prompt)**
    * Mandates a "Meta-Commentary" block before any text generation.
2.  **Layer 2: The Parchment (Sanitizer)**
    * Quarantines input to prevent prompt injection.
3.  **Layer 3: The Lens (Validator)**
    * **Integrity Check:** Ensures the Explanation is proportional to the Draft.
    * **Format Check:** Blocks generation if the AI skips the reasoning step.

## 🚀 Quick Start
```python
from scribe.editor import ScribeEditor

editor = ScribeEditor("Context: Client wants a strict NDA.")

# Get the packet
packet = editor.review_draft(llm_response)

# Display to User
if packet["valid"]:
    show_split_screen(packet["review_panel"], packet["final_text"])
