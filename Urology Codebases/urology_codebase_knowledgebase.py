"""
Urology Codebase Knowledge Base Module
Auto-generated for programmatic access to brand information.
"""

import json

class UrologyKnowledgeBase:
    """Class to manage and retrieve information on Urology Codebase brands."""
    
    def __init__(self):
        self.metadata = {
            "title": "Urology Codebase Knowledge Base",
            "description": "Comprehensive reference document for brands under the Urology Codebase portfolio."
        }
        
        self.brands = [
        {
                "brand_name": "Aizerone",
                "generic_name": "Azithromycin",
                "category": "Macrolide Antibiotic",
                "mechanism": "Binds to the 50S ribosomal subunit of susceptible microorganisms, thereby interfering with microbial protein synthesis.",
                "indications": "Treatment of urogenital infections, uncomplicated genital ulcer disease, chlamydia, gonorrhea, and various other bacterial infections."
        },
        {
                "brand_name": "Enzastik",
                "generic_name": "Digestive Enzymes",
                "category": "Digestive Aid",
                "mechanism": "Supplements endogenous digestive enzymes (amylase, protease, lipase) to facilitate the breakdown of proteins, fats, and carbohydrates.",
                "indications": "Management of digestive disorders, dyspepsia, and pancreatic exocrine insufficiency."
        },
        {
                "brand_name": "Medrozole",
                "generic_name": "Metronidazole",
                "category": "Nitroimidazole Antimicrobial",
                "mechanism": "Interacts with microbial DNA to cause a loss of helical DNA structure and strand breakage, inhibiting protein synthesis and causing cell death in susceptible organisms.",
                "indications": "Treatment of trichomoniasis, bacterial vaginosis, amebiasis, and anaerobic bacterial infections."
        },
        {
                "brand_name": "Pubergen",
                "generic_name": "Human Chorionic Gonadotropin (hCG)",
                "category": "Gonadotropin / Hormonal Therapy",
                "mechanism": "Mimics the action of luteinizing hormone (LH), stimulating the Leydig cells of the testes to produce testosterone in males, and inducing ovulation in females.",
                "indications": "Treatment of prepubertal cryptorchidism, hypogonadotropic hypogonadism in males, and induction of ovulation in infertility."
        },
        {
                "brand_name": "Thafil",
                "generic_name": "Tadalafil",
                "category": "PDE5 Inhibitor",
                "mechanism": "Selectively inhibits phosphodiesterase type 5 (PDE5), enhancing the effect of nitric oxide by increasing cGMP levels, which results in smooth muscle relaxation and increased blood flow.",
                "indications": "Treatment of erectile dysfunction (ED), signs and symptoms of benign prostatic hyperplasia (BPH), and pulmonary arterial hypertension."
        },
        {
                "brand_name": "Endmet 11.25",
                "generic_name": "Leuprorelin Acetate",
                "category": "GnRH Agonist",
                "mechanism": "Continuous administration produces an initial stimulation followed by prolonged suppression of pituitary gonadotropins, resulting in suppression of ovarian and testicular steroidogenesis. Formulated as a 3-month depot.",
                "indications": "Palliative treatment of advanced prostate cancer, endometriosis, and uterine leiomyomata (fibroids)."
        },
        {
                "brand_name": "Endmet 3.75",
                "generic_name": "Leuprorelin Acetate",
                "category": "GnRH Agonist",
                "mechanism": "Down-regulates GnRH receptors in the pituitary gland, suppressing gonadotropin secretion and resulting in a hypogonadal state. Formulated as a 1-month depot.",
                "indications": "Management of advanced prostate cancer, endometriosis, central precocious puberty, and pre-operative treatment of uterine fibroids."
        },
        {
                "brand_name": "Dustam",
                "generic_name": "Dutasteride",
                "category": "5-alpha Reductase Inhibitor",
                "mechanism": "Inhibits both type 1 and type 2 isoforms of steroid 5-alpha reductase, an intracellular enzyme that converts testosterone to dihydrotestosterone (DHT), thereby reducing prostate size.",
                "indications": "Treatment of symptomatic benign prostatic hyperplasia (BPH) in men with an enlarged prostate to improve symptoms and reduce the risk of acute urinary retention."
        },
        {
                "brand_name": "Citrix Soda",
                "generic_name": "Disodium Hydrogen Citrate",
                "category": "Urinary Alkalinizer",
                "mechanism": "Metabolized to bicarbonate in the body, which increases plasma bicarbonate concentration, buffers excess hydrogen ion concentration, and raises blood and urinary pH.",
                "indications": "Symptomatic relief of dysuria associated with mild urinary tract infections, and to prevent crystallization of uric acid and cystine calculi."
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
    kb = UrologyKnowledgeBase()
    print(f"Loaded {len(kb.brands)} brands from {kb.metadata['title']}.")
