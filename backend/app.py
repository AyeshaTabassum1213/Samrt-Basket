from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import json
import os
from algorithms.greedy import GreedyOptimizer
from algorithms.knapsack import KnapsackOptimizer
from data.mock_data import get_grocery_items
from utils.scoring import calculate_item_score

app = FastAPI(title="SmartBasket API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class OptimizationRequest(BaseModel):
    budget: float
    optimize_for: str  # 'health', 'calories', 'cost'
    excluded_items: Optional[List[str]] = []

class GroceryItem(BaseModel):
    id: str
    name: str
    category: str
    price: float
    health_score: float
    calories: int
    protein: float
    carbs: float
    fat: float
    fiber: float
    sugar: float
    sodium: float
    image_url: str
    unit: str
    brand: Optional[str] = None
    organic: Optional[bool] = False

class OptimizationResponse(BaseModel):
    recommended_items: List[GroceryItem]
    total_price: float
    total_score: float
    algorithm_used: str
    suggestions: List[str]
    category_breakdown: List[dict]
    nutritional_info: dict

@app.get("/")
async def root():
    return {"message": "SmartBasket API is running!"}

@app.get("/items", response_model=List[GroceryItem])
async def get_all_items():
    """Get all grocery items"""
    try:
        items = get_grocery_items()
        return items
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/optimize", response_model=OptimizationResponse)
async def optimize_basket(request: OptimizationRequest):
    """Optimize grocery basket based on budget and preferences"""
    try:
        # Get all items and filter out excluded ones
        all_items = get_grocery_items()
        available_items = [item for item in all_items if item['id'] not in request.excluded_items]
        
        if not available_items:
            raise HTTPException(status_code=400, detail="No items available for optimization")
        
        # Choose algorithm based on problem size and budget
        if len(available_items) > 100 or request.budget > 200:
            optimizer = GreedyOptimizer()
            algorithm_used = "Greedy Algorithm"
        else:
            optimizer = KnapsackOptimizer()
            algorithm_used = "Dynamic Programming (Knapsack)"
        
        # Optimize basket
        result = optimizer.optimize(available_items, request.budget, request.optimize_for)
        
        # Generate suggestions
        suggestions = generate_suggestions(result, request.budget, request.optimize_for)
        
        # Calculate category breakdown
        category_breakdown = calculate_category_breakdown(result['items'])
        
        # Calculate nutritional info
        nutritional_info = calculate_nutritional_info(result['items'])
        
        return OptimizationResponse(
            recommended_items=result['items'],
            total_price=result['total_price'],
            total_score=result['total_score'],
            algorithm_used=algorithm_used,
            suggestions=suggestions,
            category_breakdown=category_breakdown,
            nutritional_info=nutritional_info
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/basket/item/{item_id}")
async def remove_item_from_basket(item_id: str):
    """Remove item from current basket (for frontend state management)"""
    return {"message": f"Item {item_id} removed from basket", "item_id": item_id}

def generate_suggestions(result: dict, budget: float, optimize_for: str) -> List[str]:
    """Generate helpful suggestions based on optimization results"""
    suggestions = []
    
    savings = budget - result['total_price']
    if savings > 5:
        suggestions.append(f"You saved ${savings:.2f}! Consider adding more nutritious items.")
    
    if optimize_for == 'health':
        avg_health = result['total_score'] / len(result['items']) if result['items'] else 0
        if avg_health < 6:
            suggestions.append("Try adding more fruits and vegetables to improve health score.")
        else:
            suggestions.append("Great job choosing healthy options!")
    
    if optimize_for == 'calories':
        total_calories = sum(item['calories'] for item in result['items'])
        if total_calories < 2000:
            suggestions.append("Consider adding more calorie-dense foods for better energy.")
    
    categories = set(item['category'] for item in result['items'])
    if len(categories) < 4:
        suggestions.append("Try diversifying across more food categories for balanced nutrition.")
    
    return suggestions

def calculate_category_breakdown(items: List[dict]) -> List[dict]:
    """Calculate spending breakdown by category"""
    category_totals = {}
    total_price = sum(item['price'] for item in items)
    
    for item in items:
        category = item['category']
        if category not in category_totals:
            category_totals[category] = {'count': 0, 'total_price': 0}
        category_totals[category]['count'] += 1
        category_totals[category]['total_price'] += item['price']
    
    breakdown = []
    colors = {
        'Fruits & Vegetables': '#10B981',
        'Meat & Seafood': '#EF4444',
        'Dairy & Eggs': '#F59E0B',
        'Pantry Staples': '#8B5CF6',
        'Grains & Bread': '#F97316',
        'Beverages': '#06B6D4',
        'Snacks': '#EC4899',
        'Frozen Foods': '#3B82F6',
        'Health & Wellness': '#84CC16',
        'Condiments & Sauces': '#6B7280'
    }
    
    for category, data in category_totals.items():
        breakdown.append({
            'category': category,
            'count': data['count'],
            'total_price': round(data['total_price'], 2),
            'percentage': round((data['total_price'] / total_price) * 100, 1) if total_price > 0 else 0,
            'color': colors.get(category, '#6B7280')
        })
    
    return breakdown

def calculate_nutritional_info(items: List[dict]) -> dict:
    """Calculate total nutritional information"""
    return {
        'total_protein': round(sum(item['protein'] for item in items), 1),
        'total_carbs': round(sum(item['carbs'] for item in items), 1),
        'total_fat': round(sum(item['fat'] for item in items), 1),
        'total_fiber': round(sum(item['fiber'] for item in items), 1),
        'total_sugar': round(sum(item['sugar'] for item in items), 1),
        'total_sodium': round(sum(item['sodium'] for item in items), 0)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)