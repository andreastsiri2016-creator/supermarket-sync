import os
import sys

print("🚀 Εκκίνηση συγχρονισμού για ΟΛΑ τα προϊόντα (1-15)...")

# 1. Έλεγχος Περιβάλλοντος
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

if not url or not key:
    print("❌ ΣΦΑΛΜΑ: Λείπουν τα Secrets!")
    sys.exit(1)

try:
    from supabase import create_client
    supabase = create_client(url, key)
    print("✅ Επιτυχής σύνδεση με το Supabase!")
except Exception as e:
    print(f"❌ Σφάλμα σύνδεσης: {e}")
    sys.exit(1)

# 2. Πλήρης Κατάλογος Προϊόντων (15 Προϊόντα)
products_catalog = [
    {"barcode": "520101000001", "name": "Ελαιόλαδο Έξτρα Παρθένο 1L", "category": "Ελαιόλαδα", "brand": "Χωριό", "unit": "1L", "image_url": "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=400"},
    {"barcode": "520101000002", "name": "Φέτα Π.Ο.Π. 400g", "category": "Γαλακτοκομικά", "brand": "Δωδώνη", "unit": "400g", "image_url": "https://images.unsplash.com/photo-1559561853-08451507cbe7?w=400"},
    {"barcode": "520101000003", "name": "Γάλα Φρέσκο Πλήρες 1L", "category": "Γαλακτοκομικά", "brand": "ΟΛΥΜΠΟΣ", "unit": "1L", "image_url": "https://images.unsplash.com/photo-1550583724-b2692b85b150?w=400"},
    {"barcode": "520101000004", "name": "Εσπρέσο Αλεσμένος 250g", "category": "Καφέδες", "brand": "Jacobs", "unit": "250g", "image_url": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=400"},
    {"barcode": "520101000005", "name": "Μακαρόνια No 6 500g", "category": "Ζυμαρικά", "brand": "MISKO", "unit": "500g", "image_url": "https://images.unsplash.com/photo-1621996346565-e3d5d6281318?w=400"},
    {"barcode": "520101000006", "name": "Χαρτί Υγείας 3-ply 10 ρολά", "category": "Χαρτικά & Καθαριστικά", "brand": "Endless", "unit": "10 τμχ", "image_url": "https://images.unsplash.com/photo-1584556812952-905ffd0c611a?w=400"},
    {"barcode": "520101000007", "name": "Γιαούρτι Στραγγιστό 2% 3x200g", "category": "Γαλακτοκομικά", "brand": "ΦΑΓΕ", "unit": "600g", "image_url": "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=400"},
    {"barcode": "520101000008", "name": "Δημητριακά Ολικής 375g", "category": "Πρωινό", "brand": "Nestle Fitness", "unit": "375g", "image_url": "https://images.unsplash.com/photo-1521483451569-e33803c0330c?w=400"},
    {"barcode": "520101000009", "name": "Χυμός Πορτοκάλι 100% 1L", "category": "Αναψυκτικά & Χυμοί", "brand": "Amita", "unit": "1L", "image_url": "https://images.unsplash.com/photo-1600271886742-f049cd451bba?w=400"},
    {"barcode": "520101000010", "name": "Τόνος σε Νερό 3x80g", "category": "Κονσέρβες", "brand": "Rio Mare", "unit": "240g", "image_url": "https://images.unsplash.com/photo-1534483509719-3feaee7c30da?w=400"},
    {"barcode": "520101000011", "name": "Ρύζι Καρολίνα 1kg", "category": "Όσπρια & Ρύζια", "brand": "Agrino", "unit": "1kg", "image_url": "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400"},
    {"barcode": "520101000012", "name": "Μπισκότα Γεμιστά 200g", "category": "Σνακ & Γλυκά", "brand": "Παπαδοπούλου", "unit": "200g", "image_url": "https://images.unsplash.com/photo-1558961363-fa8fdf82db35?w=400"},
    {"barcode": "520101000013", "name": "Υγρό Πιάτων 500ml", "category": "Χαρτικά & Καθαριστικά", "brand": "Fairy", "unit": "500ml", "image_url": "https://images.unsplash.com/photo-1585842378054-ee2e52f94ba2?w=400"},
    {"barcode": "520101000014", "name": "Οδοντόκρεμα Total 75ml", "category": "Προσωπική Φροντίδα", "brand": "Colgate", "unit": "75ml", "image_url": "https://images.unsplash.com/photo-1559598467-f8b76c8155d0?w=400"},
    {"barcode": "520101000015", "name": "Εμφιαλωμένο Νερό 6x1.5L", "category": "Αναψυκτικά & Χυμοί", "brand": "Ζαγόρι", "unit": "9L", "image_url": "https://images.unsplash.com/photo-1548839140-29a749e1bc4e?w=400"}
]

# 3. Τιμές για Όλα τα 15 Προϊόντα & Όλες τις 6 Αλυσίδες
chains = ["Lidl", "Σκλαβενίτης", "ΑΒ Βασιλόπουλος", "MyMarket", "Γαλαξίας", "Κρητικός"]

# Βασικές τιμές αναφοράς για κάθε προϊόν
base_prices = {
    "520101000001": 11.20,
    "520101000002": 5.20,
    "520101000003": 1.60,
    "520101000004": 4.70,
    "520101000005": 0.90,
    "520101000006": 4.10,
    "520101000007": 3.40,
    "520101000008": 2.80,
    "520101000009": 1.50,
    "520101000010": 4.90,
    "520101000011": 2.10,
    "520101000012": 1.20,
    "520101000013": 2.30,
    "520101000014": 2.90,
    "520101000015": 1.80
}

prices_catalog = []

# Δημιουργία τιμών με μικρές διακυμάνσεις ανά αλυσίδα
for bcd, price in base_prices.items():
    prices_catalog.append({"barcode": bcd, "chain_name": "Lidl", "price": round(price * 0.95, 2)})            # Lidl η φθηνότερη
    prices_catalog.append({"barcode": bcd, "chain_name": "Σκλαβενίτης", "price": round(price * 1.00, 2)})
    prices_catalog.append({"barcode": bcd, "chain_name": "MyMarket", "price": round(price * 1.01, 2)})
    prices_catalog.append({"barcode": bcd, "chain_name": "Γαλαξίας", "price": round(price * 1.02, 2)})
    prices_catalog.append({"barcode": bcd, "chain_name": "Κρητικός", "price": round(price * 1.03, 2)})
    prices_catalog.append({"barcode": bcd, "chain_name": "ΑΒ Βασιλόπουλος", "price": round(price * 1.05, 2)})

# 4. Εγγραφή Προϊόντων στο Supabase
product_map = {}

for prod in products_catalog:
    bcd = prod["barcode"]
    try:
        existing = supabase.table("products").select("id").eq("barcode", bcd).execute()
        
        if existing.data and len(existing.data) > 0:
            prod_id = existing.data[0]["id"]
            supabase.table("products").update(prod).eq("id", prod_id).execute()
        else:
            inserted = supabase.table("products").insert(prod).execute()
            prod_id = inserted.data[0]["id"]
            
        product_map[bcd] = prod_id
        print(f"📦 Προϊόν {prod['name']} -> ID: {prod_id}")
    except Exception as e:
        print(f"❌ Σφάλμα στο προϊόν {prod['name']}: {e}")

# 5. Εγγραφή Τιμών στη στήλη chain_name
for item in prices_catalog:
    bcd = item["barcode"]
    chain = item["chain_name"]
    price_val = item["price"]
    
    prod_id = product_map.get(bcd)
    if not prod_id:
        continue

    try:
        existing_price = supabase.table("prices")\
            .select("id")\
            .eq("product_id", prod_id)\
            .eq("chain_name", chain)\
            .execute()
            
        payload = {
            "product_id": prod_id,
            "chain_name": chain,
            "price": price_val
        }

        if existing_price.data and len(existing_price.data) > 0:
            row_id = existing_price.data[0]["id"]
            supabase.table("prices").update(payload).eq("id", row_id).execute()
        else:
            supabase.table("prices").insert(payload).execute()

    except Exception as e:
        print(f"❌ Σφάλμα στην τιμή {chain}: {e}")

print("🎉 Ο συγχρονισμός ολοκληρώθηκε επιτυχώς για ΟΛΑ τα 15 προϊόντα!")
