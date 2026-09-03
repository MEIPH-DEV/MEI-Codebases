"""
Pedia Codebase Knowledge Base Module
Auto-generated for programmatic access to brand information.
"""

class PediaKnowledgeBase:
    """Class to manage and retrieve information on Pedia Codebase brands."""
    
    def __init__(self):
        self.metadata = {
            "title": "Pedia Codebase Knowledge Base",
            "description": "Comprehensive reference document for brands under the Pedia Codebase portfolio."
        }
        
        self.brands = [
        {
                "brand_name": "Clavaxie",
                "generic_name": "Amoxicillin and Clavulanate Potassium",
                "category": "Antibiotic (Penicillin-class)",
                "mechanism": "Amoxicillin inhibits bacterial cell wall synthesis. Clavulanate acts as a beta-lactamase inhibitor to extend the spectrum of activity against resistant strains.",
                "indications": "Used to treat a variety of bacterial infections, including respiratory tract infections, ear infections, sinus infections, and skin structure infections."
        },
        {
                "brand_name": "Lactoteri",
                "generic_name": "Lactobacillus",
                "category": "Probiotic",
                "mechanism": "Supplements the natural flora of the gastrointestinal tract, creating an unfavorable environment for pathogenic bacteria through lactic acid production and competitive inhibition.",
                "indications": "Prevention and treatment of acute diarrhea, antibiotic-associated diarrhea, and maintenance of a healthy gut microbiome."
        },
        {
                "brand_name": "Levomol",
                "generic_name": "Levocetirizine",
                "category": "Antihistamine (H1 receptor antagonist)",
                "mechanism": "An active enantiomer of cetirizine, acting as a potent and selective antagonist of peripheral H1-receptors with low sedative potential.",
                "indications": "Symptomatic treatment of allergic rhinitis (including persistent allergic rhinitis) and chronic idiopathic urticaria."
        },
        {
                "brand_name": "Levotussive 120",
                "generic_name": "Levodropropizine",
                "category": "Antitussive",
                "mechanism": "Acts peripherally by inhibiting the afferent pathways that mediate the generation of the cough reflex within the respiratory tract.",
                "indications": "Symptomatic relief of dry, non-productive cough. Specifically formulated in a 120mg concentration for targeted dosing."
        },
        {
                "brand_name": "Levotussive 60",
                "generic_name": "Levodropropizine",
                "category": "Antitussive",
                "mechanism": "Acts peripherally by inhibiting the afferent pathways that mediate the generation of the cough reflex. (Lower dosage variant)",
                "indications": "Symptomatic relief of dry, non-productive cough, specifically formulated for lower dosing requirements (60mg)."
        },
        {
                "brand_name": "Probio",
                "generic_name": "Probiotics",
                "category": "Dietary Supplement / Gut Health",
                "mechanism": "Introduces beneficial live microorganisms into the gut, competing with pathogens for adhesion sites, nutrients, and modulating local immunity.",
                "indications": "General digestive health, immune system support, and restoration of intestinal microflora balance."
        },
        {
                "brand_name": "Mist Dress",
                "generic_name": "Wound Dressing",
                "category": "Medical Device / Wound Care",
                "mechanism": "Creates a moist wound healing environment, facilitating autolytic debridement and protecting against external contamination and fluid loss.",
                "indications": "Management of minor acute wounds, abrasions, lacerations, burns, and post-operative surgical incisions."
        },
        {
                "brand_name": "Endmet 3.75",
                "generic_name": "Leuprorelin Acetate",
                "category": "GnRH Agonist / Hormonal Therapy",
                "mechanism": "Continuous administration leads to down-regulation of GnRH receptors in the pituitary gland, suppressing gonadotropin secretion and resulting in a hypogonadal state.",
                "indications": "Treatment of endometriosis, uterine fibroids, advanced prostate cancer, and central precocious puberty."
        }
]
        
    def get_brand(self, brand_name: str) -> dict:
        """Retrieve brand details by exact or partial name."""
        for brand in self.brands:
            if brand_name.lower() in brand['brand_name'].lower():
                return brand
        return None
        
    def list_all_brands(self) -> list:
        """Return a list of all brand names."""
        return [b['brand_name'] for b in self.brands]

if __name__ == "__main__":
    kb = PediaKnowledgeBase()
    print(f"Loaded {len(kb.brands)} brands from {kb.metadata['title']}.")
