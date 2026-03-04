def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    val = validate_ingredients(ingredients)
    if val == f"{ingredients} - VALID":
        return f"Spell recorded: {spell_name} ({val})"
    else:
        return f"Spell rejected: {spell_name} ({val})"
