# mock_api/oauth.py

def get_access_token(client_id, client_secret):
    if client_id != "valid_client":
        return {"error": "invalid_client"}

    return {
        "access_token": "mock_access_token",
        "scope": "ads_management",
        "expires_in": 3600
    }
