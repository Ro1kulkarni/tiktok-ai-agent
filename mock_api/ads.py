# mock_api/ads.py

def submit_ad(ad, token):
    if token != "mock_access_token":
        return {"error": "INVALID_TOKEN"}

    if ad["creative"]["music_id"] == "geo_blocked":
        return {"error": "GEO_RESTRICTION"}

    return {"status": "SUCCESS", "ad_id": "ad_12345"}
