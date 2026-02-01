## TikTok AI Agent (Assignment)

### Overview
This project demonstrates a production-style AI workflow for creating TikTok Ads via conversation.

### Key Design Decisions
- Gemini 1.5 Flash used (free tier)
- TikTok APIs are mocked to focus on reasoning
- Business rules enforced outside the LLM
- Structured JSON output enforced via prompts

### Music Rules
- Existing music ID validated via API
- Custom music upload simulated
- No-music blocked for Conversion campaigns

### How to Run
1. Add Groq API key
2. `pip install -r requirements.txt`
3. `python main.py`
