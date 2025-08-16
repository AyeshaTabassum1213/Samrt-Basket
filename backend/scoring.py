def calculate_item_score(item: dict, optimize_for: str) -> float:
    """
    Calculate item score based on optimization preference
    """
    if optimize_for == 'health':
        return item['health_score']
    elif optimize_for == 'calories':
        return item['calories'] / 100  # Scale calories to reasonable range
    elif optimize_for == 'cost':
        return 10 / item['price']  # Inverse of price (higher score for cheaper items)
    else:
        return item['health_score']  # Default to health