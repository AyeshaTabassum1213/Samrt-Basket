import random
from typing import List, Dict

def get_grocery_items() -> List[Dict]:
    """Generate mock grocery data with 500+ items"""
    
    categories = [
        'Fruits & Vegetables',
        'Meat & Seafood',
        'Dairy & Eggs',
        'Pantry Staples',
        'Grains & Bread',
        'Beverages',
        'Snacks',
        'Frozen Foods',
        'Health & Wellness',
        'Condiments & Sauces'
    ]
    
    category_items = {
        'Fruits & Vegetables': [
            'Organic Bananas', 'Fresh Spinach', 'Red Bell Peppers', 'Avocados', 'Broccoli Crowns',
            'Sweet Potatoes', 'Organic Carrots', 'Fresh Strawberries', 'Blueberries', 'Romaine Lettuce',
            'Cucumber', 'Tomatoes', 'Red Onions', 'Garlic', 'Fresh Ginger', 'Lemons', 'Limes',
            'Green Beans', 'Zucchini', 'Yellow Squash', 'Cauliflower', 'Brussels Sprouts',
            'Asparagus', 'Celery', 'Mushrooms', 'Apple', 'Oranges', 'Grapes', 'Pineapple',
            'Mango', 'Kiwi', 'Peaches', 'Pears', 'Watermelon', 'Cantaloupe', 'Honeydew',
            'Cherries', 'Plums', 'Apricots', 'Fresh Herbs Mix', 'Organic Kale', 'Cabbage',
            'Radishes', 'Turnips', 'Beets', 'Sweet Corn', 'Fresh Basil', 'Cilantro', 'Parsley',
            'Green Onions', 'Jalapenos'
        ],
        'Meat & Seafood': [
            'Organic Chicken Breast', 'Ground Turkey', 'Salmon Fillet', 'Grass-Fed Ground Beef',
            'Pork Tenderloin', 'Shrimp', 'Cod Fillet', 'Turkey Breast Slices', 'Bacon',
            'Italian Sausage', 'Chicken Thighs', 'Tuna Steaks', 'Crab Meat', 'Lobster Tails',
            'Scallops', 'Mussels', 'Clams', 'Sardines', 'Anchovies', 'Tilapia', 'Halibut',
            'Mahi Mahi', 'Sea Bass', 'Lamb Chops', 'Beef Sirloin', 'Ribeye Steak', 'T-Bone Steak',
            'Ground Pork', 'Ham Slices', 'Chorizo', 'Chicken Wings', 'Duck Breast',
            'Venison', 'Bison Burger', 'Turkey Sausage', 'Chicken Drumsticks', 'Pork Ribs',
            'Beef Brisket', 'Corned Beef', 'Prosciutto', 'Smoked Salmon', 'Fish Sticks',
            'Canned Tuna', 'Canned Salmon', 'Frozen Shrimp', 'Fish & Chips', 'Crab Cakes',
            'Fish Tacos', 'Seafood Mix', 'Calamari', 'Octopus'
        ],
        'Dairy & Eggs': [
            'Organic Whole Milk', 'Greek Yogurt', 'Free-Range Eggs', 'Sharp Cheddar Cheese',
            'Mozzarella Cheese', 'Cream Cheese', 'Butter', 'Heavy Cream', 'Sour Cream',
            'Cottage Cheese', 'Ricotta Cheese', 'Parmesan Cheese', 'Swiss Cheese', 'Goat Cheese',
            'Brie Cheese', 'Blue Cheese', 'Feta Cheese', 'Almond Milk', 'Coconut Milk',
            'Oat Milk', 'Soy Milk', 'Lactose-Free Milk', 'Buttermilk', 'Half & Half',
            'Whipped Cream', 'Ice Cream', 'Frozen Yogurt', 'Cheese Sticks', 'Yogurt Drinks',
            'Kefir', 'Chocolate Milk', 'Strawberry Milk', 'Vanilla Ice Cream', 'Sherbet',
            'Gelato', 'Cream Cheese Spread', 'String Cheese', 'Babybel Cheese', 'Cheese Slices',
            'Vegan Cheese', 'Cashew Milk', 'Rice Milk', 'Protein Milk', 'Organic Butter',
            'Ghee', 'Margarine', 'Vegan Butter', 'Egg Whites', 'Quail Eggs'
        ],
        'Pantry Staples': [
            'Extra Virgin Olive Oil', 'Coconut Oil', 'Sea Salt', 'Black Pepper', 'Garlic Powder',
            'Onion Powder', 'Paprika', 'Cumin', 'Oregano', 'Basil', 'Thyme', 'Rosemary',
            'Bay Leaves', 'Cinnamon', 'Vanilla Extract', 'Baking Soda', 'Baking Powder',
            'All-Purpose Flour', 'Whole Wheat Flour', 'Sugar', 'Brown Sugar', 'Honey',
            'Maple Syrup', 'Apple Cider Vinegar', 'White Vinegar', 'Balsamic Vinegar',
            'Soy Sauce', 'Hot Sauce', 'Worcestershire Sauce', 'Dijon Mustard', 'Yellow Mustard',
            'Ketchup', 'Mayonnaise', 'Ranch Dressing', 'Italian Dressing', 'Caesar Dressing',
            'Salsa', 'Pesto', 'Tomato Sauce', 'Marinara Sauce', 'Alfredo Sauce', 'BBQ Sauce',
            'Teriyaki Sauce', 'Fish Sauce', 'Sesame Oil', 'Vegetable Oil', 'Canola Oil',
            'Avocado Oil', 'Coconut Flour', 'Almond Flour'
        ],
        'Grains & Bread': [
            'Whole Wheat Bread', 'Sourdough Bread', 'Multigrain Bread', 'Bagels', 'English Muffins',
            'Tortillas', 'Pita Bread', 'Naan Bread', 'Dinner Rolls', 'Croissants', 'Brown Rice',
            'White Rice', 'Jasmine Rice', 'Basmati Rice', 'Wild Rice', 'Quinoa', 'Oats',
            'Steel Cut Oats', 'Granola', 'Cereal', 'Pasta', 'Whole Wheat Pasta', 'Rice Noodles',
            'Ramen Noodles', 'Spaghetti', 'Penne', 'Fusilli', 'Linguine', 'Lasagna Sheets',
            'Couscous', 'Bulgur', 'Barley', 'Millet', 'Buckwheat', 'Farro', 'Spelt',
            'Amaranth', 'Teff', 'Crackers', 'Rice Cakes', 'Breadcrumbs', 'Panko',
            'Pizza Dough', 'Pie Crust', 'Muffin Mix', 'Pancake Mix', 'Waffle Mix',
            'Cornbread Mix', 'Biscuit Mix', 'Cake Mix'
        ],
        'Beverages': [
            'Filtered Water', 'Sparkling Water', 'Green Tea', 'Black Tea', 'Coffee Beans',
            'Ground Coffee', 'Orange Juice', 'Apple Juice', 'Cranberry Juice', 'Grape Juice',
            'Tomato Juice', 'V8 Juice', 'Coconut Water', 'Sports Drinks', 'Energy Drinks',
            'Soda', 'Diet Soda', 'Kombucha', 'Herbal Tea', 'Chamomile Tea', 'Peppermint Tea',
            'Iced Tea', 'Lemonade', 'Fruit Punch', 'Smoothie Mix', 'Protein Shakes',
            'Meal Replacement Drinks', 'Electrolyte Water', 'Alkaline Water', 'Vitamin Water',
            'Flavored Water', 'Coconut Milk Drink', 'Almond Milk Drink', 'Cold Brew Coffee',
            'Espresso', 'Matcha Powder', 'Hot Chocolate', 'Chai Latte Mix', 'Instant Coffee',
            'Decaf Coffee', 'French Roast', 'Medium Roast', 'Light Roast', 'Espresso Beans',
            'Turkish Coffee', 'Vietnamese Coffee', 'Bubble Tea', 'Wine', 'Beer'
        ],
        'Snacks': [
            'Mixed Nuts', 'Almonds', 'Walnuts', 'Cashews', 'Pistachios', 'Peanuts',
            'Trail Mix', 'Granola Bars', 'Protein Bars', 'Energy Bars', 'Fruit Bars',
            'Dried Fruit', 'Beef Jerky', 'Turkey Jerky', 'Veggie Chips', 'Potato Chips',
            'Tortilla Chips', 'Pretzels', 'Popcorn', 'Rice Crackers', 'Cheese Crackers',
            'Goldfish Crackers', 'Animal Crackers', 'Graham Crackers', 'Cookies',
            'Chocolate Chip Cookies', 'Oreos', 'Candy', 'Chocolate', 'Dark Chocolate',
            'Milk Chocolate', 'White Chocolate', 'Gummy Bears', 'Sour Candy',
            'Hard Candy', 'Mints', 'Gum', 'Fruit Snacks', 'Fruit Leather',
            'Pudding Cups', 'Jello Cups', 'Apple Sauce', 'Fruit Cups', 'Nut Butter',
            'Peanut Butter', 'Almond Butter', 'Sunflower Seed Butter', 'Tahini',
            'Hummus', 'Guacamole', 'Salsa', 'Cheese Dip', 'Spinach Dip'
        ],
        'Frozen Foods': [
            'Frozen Berries', 'Frozen Mango', 'Frozen Pineapple', 'Frozen Vegetables',
            'Frozen Broccoli', 'Frozen Corn', 'Frozen Peas', 'Frozen Spinach',
            'Frozen Mixed Vegetables', 'Frozen Stir Fry Mix', 'Frozen Pizza',
            'Frozen Burritos', 'Frozen Dinners', 'Frozen Chicken Nuggets',
            'Frozen Fish Sticks', 'Frozen French Fries', 'Frozen Onion Rings',
            'Frozen Mozzarella Sticks', 'Frozen Waffles', 'Frozen Pancakes',
            'Ice Cream', 'Frozen Yogurt', 'Popsicles', 'Ice Cream Sandwiches',
            'Frozen Fruit Bars', 'Sorbet', 'Sherbet', 'Frozen Smoothie Packs',
            'Frozen Acai Bowls', 'Frozen Hash Browns', 'Frozen Tater Tots',
            'Frozen Garlic Bread', 'Frozen Pie', 'Frozen Cake', 'Frozen Cookies',
            'Frozen Dough', 'Frozen Pastries', 'Frozen Breakfast Sandwiches',
            'Frozen Breakfast Burritos', 'Frozen Egg Rolls', 'Frozen Dumplings',
            'Frozen Pot Pies', 'Frozen Lasagna', 'Frozen Mac and Cheese',
            'Frozen Soup', 'Frozen Appetizers', 'Frozen Seafood Mix'
        ],
        'Health & Wellness': [
            'Protein Powder', 'Multivitamins', 'Vitamin C', 'Vitamin D', 'Omega-3',
            'Probiotics', 'Calcium', 'Iron Supplements', 'Magnesium', 'Zinc',
            'B-Complex', 'Biotin', 'Collagen', 'Turmeric', 'Ginger Supplements',
            'Green Tea Extract', 'Garcinia Cambogia', 'Apple Cider Vinegar Pills',
            'Fiber Supplements', 'Digestive Enzymes', 'Melatonin', 'Ashwagandha',
            'Echinacea', 'Elderberry', 'CoQ10', 'Glucosamine', 'Chondroitin',
            'Fish Oil', 'Flaxseed Oil', 'Evening Primrose Oil', 'Spirulina',
            'Chlorella', 'Wheatgrass', 'Moringa', 'Maca Root', 'Ginseng',
            'Rhodiola', 'Valerian Root', 'Milk Thistle', 'Saw Palmetto',
            'Cranberry Extract', 'Garlic Extract', 'Grape Seed Extract',
            'Green Coffee Bean', 'Raspberry Ketones', 'Forskolin', 'CLA',
            'L-Carnitine', 'BCAA', 'Creatine', 'Glutamine'
        ],
        'Condiments & Sauces': [
            'Ketchup', 'Mustard', 'Mayonnaise', 'BBQ Sauce', 'Hot Sauce', 'Salsa',
            'Guacamole', 'Hummus', 'Ranch Dressing', 'Italian Dressing',
            'Caesar Dressing', 'Balsamic Glaze', 'Teriyaki Sauce', 'Soy Sauce',
            'Sriracha', 'Buffalo Sauce', 'Honey Mustard', 'Thousand Island',
            'Blue Cheese Dressing', 'French Dressing', 'Catalina Dressing',
            'Vinaigrette', 'Oil & Vinegar', 'Pesto', 'Marinara Sauce',
            'Alfredo Sauce', 'Cheese Sauce', 'Hollandaise Sauce', 'Tartar Sauce',
            'Cocktail Sauce', 'Remoulade', 'Aioli', 'Chipotle Mayo',
            'Garlic Sauce', 'Sweet & Sour Sauce', 'Duck Sauce', 'Plum Sauce',
            'Fish Sauce', 'Oyster Sauce', 'Hoisin Sauce', 'Black Bean Sauce',
            'Curry Paste', 'Chili Paste', 'Tomato Paste', 'Tahini',
            'Miso Paste', 'Harissa', 'Chimichurri', 'Tzatziki', 'Salsa Verde',
            'Enchilada Sauce', 'Mole Sauce', 'Worcestershire Sauce'
        ]
    }
    
    base_prices = {
        'Fruits & Vegetables': [0.5, 4.0],
        'Meat & Seafood': [3.0, 25.0],
        'Dairy & Eggs': [1.0, 8.0],
        'Pantry Staples': [1.0, 12.0],
        'Grains & Bread': [1.5, 8.0],
        'Beverages': [1.0, 6.0],
        'Snacks': [2.0, 10.0],
        'Frozen Foods': [2.0, 15.0],
        'Health & Wellness': [5.0, 50.0],
        'Condiments & Sauces': [1.5, 8.0]
    }
    
    items = []
    item_id = 1
    
    for category in categories:
        category_item_names = category_items[category]
        min_price, max_price = base_prices[category]
        
        # Generate 50+ items per category
        items_per_category = 50 + random.randint(0, 10)
        
        for i in range(items_per_category):
            name = random.choice(category_item_names)
            # Add variation to avoid exact duplicates
            if random.random() > 0.7:
                name += f" ({random.choice(['Premium', 'Organic', 'Fresh', 'Natural', 'Select'])})"
            
            price = round(random.uniform(min_price, max_price), 2)
            health_score = round(random.uniform(1, 10), 1)
            calories = random.randint(50, 500)
            
            item = {
                'id': f'item-{item_id}',
                'name': name,
                'category': category,
                'price': price,
                'health_score': health_score,
                'calories': calories,
                'protein': round(random.uniform(0, 30), 1),
                'carbs': round(random.uniform(0, 50), 1),
                'fat': round(random.uniform(0, 20), 1),
                'fiber': round(random.uniform(0, 15), 1),
                'sugar': round(random.uniform(0, 25), 1),
                'sodium': round(random.uniform(0, 1000), 0),
                'image_url': 'https://images.pexels.com/photos/1028599/pexels-photo-1028599.jpeg?auto=compress&cs=tinysrgb&w=400',
                'unit': random.choice(['lb', 'each', 'dozen', 'oz', 'bag', 'bottle', 'box', 'pack']),
                'brand': random.choice(['Organic Valley', 'Nature\'s Best', 'Fresh Market', 'Premium Select', None]),
                'organic': random.random() > 0.7
            }
            
            items.append(item)
            item_id += 1
    
    return items