from typing import List, Dict
from utils.scoring import calculate_item_score

class GreedyOptimizer:
    def optimize(self, items: List[Dict], budget: float, optimize_for: str) -> Dict:
        """
        Greedy optimization algorithm
        Selects items with best value-to-price ratio within budget
        """
        # Calculate score per dollar for each item
        scored_items = []
        for item in items:
            score_per_dollar = calculate_item_score(item, optimize_for) / item['price']
            scored_items.append({
                **item,
                'score_per_dollar': score_per_dollar
            })
        
        # Sort by score per dollar (descending)
        scored_items.sort(key=lambda x: x['score_per_dollar'], reverse=True)
        
        # Greedy selection
        selected_items = []
        remaining_budget = budget
        total_score = 0
        
        for item in scored_items:
            if item['price'] <= remaining_budget:
                selected_items.append(item)
                remaining_budget -= item['price']
                total_score += calculate_item_score(item, optimize_for)
        
        return {
            'items': selected_items,
            'total_price': round(budget - remaining_budget, 2),
            'total_score': round(total_score, 2)
        }