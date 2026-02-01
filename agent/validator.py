# agent/validator.py

class ValidationError(Exception):
    pass


def validate_ad(ad):
    if not ad["campaign_name"] or len(ad["campaign_name"]) < 3:
        raise ValidationError("Campaign name must be at least 3 characters")

    if ad["objective"] not in ["Traffic", "Conversions"]:
        raise ValidationError("Objective must be Traffic or Conversions")

    creative = ad["creative"]

    if not creative["text"] or len(creative["text"]) > 100:
        raise ValidationError("Ad text is required and max 100 characters")

    if not creative["cta"]:
        raise ValidationError("CTA is required")

    # 🚨 KEY RULE: music enforcement
    if ad["objective"] == "Conversions" and not creative["music_id"]:
        raise ValidationError("Music is required for Conversion ads")

    return True
