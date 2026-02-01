# agent/conversation.py

import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are a TikTok Ads assistant.

Ask ONLY ONE question at a time.
Do NOT explain.
Do NOT ask multiple questions.

Ask in this order:
1. Campaign name (min 3 chars)
2. Objective (Traffic or Conversions)
3. Ad text (max 100 chars)
4. CTA
5. Music choice (existing ID / upload / none)

Respond with only the next question.
"""

def ask_llm(user_input, state):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_input}
    ]

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.3
    )

    # Extract reply safely
    reply = response.choices[0].message.content.strip()

    # Update state based on which field is missing
    if state["campaign_name"] is None:
        state["campaign_name"] = user_input
        next_question = "What is the objective? (Traffic or Conversions)"
    elif state["objective"] is None:
        state["objective"] = user_input
        next_question = "Enter ad text (max 100 chars)"
    elif state["creative"]["text"] is None:
        state["creative"]["text"] = user_input
        next_question = "Enter CTA"
    elif state["creative"]["cta"] is None:
        state["creative"]["cta"] = user_input
        next_question = "Choose music (existing ID / upload / none)"
    elif state["creative"]["music_id"] is None:
        state["creative"]["music_id"] = user_input
        next_question = "All fields collected"
    else:
        next_question = ""

    print("Agent:", next_question)
    return state
