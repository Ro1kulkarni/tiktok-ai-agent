from agent.schemas import AD_SCHEMA
from agent.conversation import ask_llm
from agent.validator import validate_ad, ValidationError
from mock_api.oauth import get_access_token
from mock_api.music import validate_music, upload_custom_music
from mock_api.ads import submit_ad

state = {
    "campaign_name": None,
    "objective": None,
    "creative": {"text": None, "cta": None, "music_id": None}
}

# Keep track of which field the agent is waiting for
current_field = None

# OAuth
oauth = get_access_token("valid_client", "valid_secret")
if "error" in oauth:
    print("OAuth failed:", oauth["error"])
    exit()
token = oauth["access_token"]
print("OAuth successful\n")

while True:
    user_input = input("User: ").strip()

    if user_input.lower() in ["exit", "quit"]:
        print("Exiting agent.")
        break

    # Intent trigger
    if user_input.lower() in ["create a tiktok ad", "create ad", "start"]:
        current_field = "campaign_name"
        print("Agent: What is the campaign name?")
        continue

    # Process the input depending on current field
    if current_field == "campaign_name":
        state["campaign_name"] = user_input
        current_field = "objective"
        print("Agent: What is the objective? (Traffic or Conversions)")
        continue

    if current_field == "objective":
        state["objective"] = user_input
        current_field = "text"
        print("Agent: Enter ad text (max 100 chars)")
        continue

    if current_field == "text":
        state["creative"]["text"] = user_input
        current_field = "cta"
        print("Agent: Enter CTA")
        continue

    if current_field == "cta":
        state["creative"]["cta"] = user_input
        current_field = "music_id"
        print("Agent: Choose music (existing ID / upload / none)")
        continue

    if current_field == "music_id":
        state["creative"]["music_id"] = user_input
        current_field = None
        print("Agent: All fields collected")
        break  # or continue to validation

# ---------------- Music Handling ----------------
music_id = state["creative"]["music_id"]

if music_id == "upload":
    # upload_custom_music() should return a string (music ID)
    upload_resp = upload_custom_music()
    if isinstance(upload_resp, str):
        state["creative"]["music_id"] = upload_resp
    else:
        # fallback if you later return dict from the function
        state["creative"]["music_id"] = upload_resp.get("music_id")

# ---------------- Submit Ad ----------------
result = submit_ad(state, token)

if "error" in result:
    print("Submission failed:", result["error"])
else:
    print("\n✅ Ad created successfully!")
    print("Final Payload:")
    print(state)
