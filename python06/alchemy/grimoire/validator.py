from .spellbook import record_spell


def validate_ingredients(ingredients: str) -> str:
    if ("fire" in ingredients or "earth" in ingredients or "water" in ingredients or "air" in ingredients):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
