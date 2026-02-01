# mock_api/music.py
import uuid

def validate_music(music_id):
    if music_id.startswith("invalid"):
        return {"error": "MUSIC_NOT_FOUND"}
    return {"status": "valid"}


def upload_custom_music():
    return f"custom_{uuid.uuid4()}"
