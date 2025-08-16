from typing import List, Dict
from utils.scoring import calculate_item_score

class KnapsackOptimizer:
    def optimize(self, items: List[Dict], budget: float, optimize_for: str) -> Dict:
        """
        0/1 Knapsack Dynamic Programming optimization
        Finds optimal subset of items within budget
        """
        # Convert budget to cents for integer DP
        budget_cents = int(budget * 100)
        
        # Prepare items with integer weights and values
        dp_items = []
        for item in items:
            weight = int(item['price'] * 100)  # Price in cents
            value = int(calculate_item_score(item, optimize_for) * 100)  # Scaled score
            dp_items.append({
                **item,
                'weight': weight,
                'value': value
            })
        
        n = len(dp_items)
        if n == 0 or budget_cents <= 0:
            return {'items': [], 'total_price': 0, 'total_score': 0}
        
        # DP table: dp[i][w] = maximum value using first i items with weight limit w
        dp = [[0 for _ in range(budget_cents + 1)] for _ in range(n + 1)]
        
        # Fill DP table
        for i in range(1, n + 1):
            for w in range(budget_cents + 1):
                item = dp_items[i - 1]
                if item['weight'] <= w:
                    # Max of including or excluding current item
                    dp[i][w] = max(
                        dp[i - 1][w],  # Exclude item
                        dp[i - 1][w - item['weight']] + item['value']  # Include item
                    )
                else:
                    dp[i][w] = dp[i - 1][w]
        
        # Backtrack to find selected items
        selected_items = []
        w = budget_cents
        total_price = 0
        total_score = 0
        
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                item = dp_items[i - 1]
                selected_items.append(item)
                w -= item['weight']
                total_price += item['price']
                total_score += calculate_item_score(item, optimize_for)
        
        return {
            'items': selected_items,
            'total_price': round(total_price, 2),
            'total_score': round(total_score, 2)
        }