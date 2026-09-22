import os
import sys

print("🚀 Εκκίνηση script...")

# 1. Έλεγχος Secrets
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

if not url or not key:
    print("❌ ΣΦΑΛΜΑ: Λείπουν τα Secrets!")
    sys.exit(1)

# 2. Σύνδεση με Supabase
try:
    from supabase import create_client
    supabase = create_client(url, key)
    print("✅ Επιτυχής σύνδεση με το Supabase!")
except Exception as e:
    print(f"❌ Σφάλμα σύνδεσης: {e}")
    sys.exit(1)

# 3. Λίστα Προϊόντων
products = [
    {
        "id": "520101000001",
        "barcode": "520101000001", 
        "name": "Ελαιόλαδο Έξτρα Παρθένο 1L", 
        "category": "Ελαιόλαδα", 
        "brand": "Χωριό", 
        "unit": "1L", 
        "image_url": "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=300"
    },
    {
        "id": "520101000002",
        "barcode": "520101000002", 
        "name": "Φέτα Π.Ο.Π. 400g", 
        "category": "Γαλακτοκομικά", 
        "brand": "Δωδώνη", 
        "unit": "400g", 
        "image_url": "https://images.unsplash.com/photo-1559561853-08451507cbe7?w=300"
    }
]

# 4. Λίστα Τιμών ανά Σούπερ Μάρκετ
prices = [
    # Τιμές για το Ελαιόλαδο
    {"product_id": "520101000001", "supermarket": "Σκλαβενίτης", "price": 11.50},
    {"product_id": "520101000001", "supermarket": "ΑΒ Βασιλόπουλος", "price": 11.80},
    {"product_id": "520101000001", "supermarket": "Lidl", "price": 10.90},
    
    # Τιμές για τη Φέτα
    {"product_id": "520101000002", "supermarket": "Σκλαβενίτης", "price": 5.20},
    {"product_id": "520101000002", "supermarket": "ΑΒ Βασιλόπουλος", "price": 5.40},
    {"product_id": "520101000002", "supermarket": "Lidl", "price": 4.95}
]

# Ενημέρωση Πίνακα Products
for p in products:
    try:
        supabase.table("products").upsert(p, on_conflict="barcode").execute()
        print(f"✅ Ενημερώθηκε το προϊόν: {p['name']}")
    except Exception as e:
        print(f"❌ Σφάλμα στο προϊόν {p['name']}: {e}")

# Ενημέρωση Πίνακα Prices
for pr in prices:
    try:
        supabase.table("prices").upsert(pr).execute()
        print(f"💰 Ενημερώθηκε η τιμή: {pr['supermarket']} -> {pr['price']}€")
    except Exception as e:
        print(f"❌ Σφάλμα στην τιμή: {e}")

print("🎉 Ολοκληρώθηκε με επιτυχία!")
