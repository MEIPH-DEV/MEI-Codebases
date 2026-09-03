"""
Godrej HIT Codebase Module
Auto-generated for programmatic access to Godrej HIT pest control data.
"""

import json

class GodrejHitKnowledgeBase:
    """Class to manage and retrieve information on Godrej HIT products."""
    
    def __init__(self):
        self.metadata = {
            "title": "Godrej HIT Codebase",
            "description": "Comprehensive reference document for the Godrej HIT product line."
        }
        
        self.brand_overview = {
        "brand_name": "Godrej HIT",
        "category": "Household Insecticide & Pest Control",
        "parent_company": "Godrej Consumer Products"
}
        self.products = [
        {
                "name": "Kala HIT",
                "description": "Aerosol spray designed to eliminate mosquitoes and flying insects.",
                "variants": [
                        "Regular",
                        "Lime Fragrance"
                ],
                "features": "Reaches deep corners to kill hidden mosquitoes, providing protection against Dengue and Malaria vectors."
        },
        {
                "name": "Lal HIT",
                "description": "Aerosol spray designed to eradicate cockroaches and other crawling insects.",
                "variants": [
                        "Lal HIT Aerosol"
                ],
                "features": "Features a deep reach nozzle for cracks and crevices to kill cockroaches hiding in corners."
        },
        {
                "name": "HIT Anti Roach Gel",
                "description": "Hassle-free, long-lasting pest control gel for cockroaches.",
                "variants": [
                        "HIT Anti Roach Gel"
                ],
                "features": "Odorless application, kills the entire nest of cockroaches, providing long-lasting control without fumes."
        },
        {
                "name": "HIT Chalk",
                "description": "Chalk line repellent to keep homes free of ants, cockroaches, and other crawling insects.",
                "variants": [
                        "HIT Chalk 1N"
                ],
                "features": "Simply draw a line across floors or surfaces; crawling insects are killed upon crossing the toxic chalk line."
        },
        {
                "name": "HIT Rat Solutions",
                "description": "Traps and baits for rodents.",
                "variants": [
                        "HIT Rat Glue Pad",
                        "HIT Rat Cube"
                ],
                "features": "Glue pads offer a non-toxic solution to capture rats indoors safely. Rat Cubes serve as effective baits for rodent management."
        },
        {
                "name": "HIT Mosquito Racquet",
                "description": "Electric mosquito and bug zapper.",
                "variants": [
                        "Rechargeable Racquet"
                ],
                "features": "Intelligently designed unique shape to reach corners, larger coverage area, offering active protection from disease-carrying mosquitoes."
        }
]
        
    def get_product(self, product_name: str) -> dict:
        """Retrieve a specific product by name."""
        for prod in self.products:
            if product_name.lower() in prod['name'].lower():
                return prod
        return None

if __name__ == "__main__":
    kb = GodrejHitKnowledgeBase()
    print(f"Loaded: {kb.brand_overview['brand_name']} ({len(kb.products)} products)")
