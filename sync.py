import os
import sys

print("🚀 Εκκίνηση συγχρονισμού με τη σωστή στήλη (chain_name)...")

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

# 2. Κατάλογος Προϊόντων
products_catalog = [
    {"barcode": "520101000001", "name": "Ελαιόλαδο Έξτρα Παρθένο 1L", "category": "Ελαιόλαδα", "brand": "Χωριό", "unit": "1L", "image_url": "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=400"},
    {"barcode": "520101000002", "name": "Φέτα Π.Ο.Π. 400g", "category": "Γαλακτοκομικά", "brand": "Δωδώνη", "unit": "400g", "image_url": "https://images.unsplash.com/photo-1559561853-08451507cbe7?w=400"},
    {"barcode": "520101000003", "name": "Γάλα Φρέσκο Πλήρες 1L", "category": "Γαλακτοκομικά", "brand": "ΟΛΥΜΠΟΣ", "unit": "1L", "image_url": "https://images.unsplash.com/photo-1550583724-b2692b85b150?w=400"},
    {"barcode": "520101000004", "name": "Εσπρέσο Αλεσμένος 250g", "category": "Καφέδες", "brand": "Jacobs", "unit": "250g", "image_url": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=400"},
    {"barcode": "520101000005", "name": "Μακαρόνια No 6 500g", "category": "Ζυμαρικά", "brand": "MISKO", "unit": "500g", "image_url": "https://images.unsplash.com/photo-1621996346565-e3d5d6281318?w=400"},
    {"barcode": "520101000006", "name": "Χαρτί Υγείας 3-ply 10 ρολά", "category": "Χαρτικά & Καθαριστικά", "brand": "Endless", "unit": "10 τμχ", "image_url": "https://images.unsplash.com/photo-1584556812952-905ffd0c611a?w=400"}
]

# 3. Κατάλογος Τιμών (Χρήση chain_name)
prices_catalog = [
    # Ελαιόλαδο
    {"barcode": "520101000001", "chain_name": "Lidl", "price": 10.90},
    {"barcode": "520101000001", "chain_name": "Σκλαβενίτης", "price": 11.45},
    {"barcode": "520101000001", "chain_name": "ΑΒ Βασιλόπουλος", "price": 11.80},
    {"barcode": "520101000001", "chain_name": "MyMarket", "price": 11.20},
    {"barcode": "520101000001", "chain_name": "Γαλαξίας", "price": 11.30},
    {"barcode": "520101000001", "chain_name": "Κρητικός", "price": 11.40},

    # Φέτα
    {"barcode": "520101000002", "chain_name": "Lidl", "price": 4.95},
    {"barcode": "520101000002", "chain_name": "Σκλαβενίτης", "price": 5.25},
    {"barcode": "520101000002", "chain_name": "ΑΒ Βασιλόπουλος", "price": 5.48},
    {"barcode": "520101000002", "chain_name": "MyMarket", "price": 5.15},
    {"barcode": "520101000002", "chain_name": "Γαλαξίας", "price": 5.10},
    {"barcode": "520101000002", "chain_name": "Κρητικός", "price": 5.30},

    # Γάλα
    {"barcode": "520101000003", "chain_name": "Lidl", "price": 1.55},
    {"barcode": "520101000003", "chain_name": "Σκλαβενίτης", "price": 1.62},
    {"barcode": "520101000003", "chain_name": "ΑΒ Βασιλόπουλος", "price": 1.68},
    {"barcode": "520101000003", "chain_name": "MyMarket", "price": 1.60},
    {"barcode": "520101000003", "chain_name": "Γαλαξίας", "price": 1.58},
    {"barcode": "520101000003", "chain_name": "Κρητικός", "price": 1.65},

    # Καφές
    {"barcode": "520101000004", "chain_name": "Lidl", "price": 4.50},
    {"barcode": "520101000004", "chain_name": "Σκλαβενίτης", "price": 4.80},
    {"barcode": "520101000004", "chain_name": "ΑΒ Βασιλόπουλος", "price": 4.95},
    {"barcode": "520101000004", "chain_name": "MyMarket", "price": 4.75},
    {"barcode": "520101000004", "chain_name": "Γαλαξίας", "price": 4.65},
    {"barcode": "520101000004", "chain_name": "Κρητικός", "price": 4.85},

    # Μακαρόνια
    {"barcode": "520101000005", "chain_name": "Lidl", "price": 0.85},
    {"barcode": "520101000005", "chain_name": "Σκλαβενίτης", "price": 0.92},
    {"barcode": "520101000005", "chain_name": "ΑΒ Βασιλόπουλος", "price": 0.98},
    {"barcode": "520101000005", "chain_name": "MyMarket", "price": 0.90},
    {"barcode": "520101000005", "chain_name": "Γαλαξίας", "price": 0.88},
    {"barcode": "520101000005", "chain_name": "Κρητικός", "price": 0.95},

    # Χαρτί Υγείας
    {"barcode": "520101000006", "chain_name": "Lidl", "price": 3.99},
    {"barcode": "520101000006", "chain_name": "Σκλαβενίτης", "price": 4.20},
    {"barcode": "520101000006", "chain_name": "ΑΒ Βασιλόπουλος", "price": 4.50},
    {"barcode": "520101000006", "chain_name": "MyMarket", "price": 4.15},
    {"barcode": "520101000006", "chain_name": "Γαλαξίας", "price": 4.10},
    {"barcode": "520101000006", "chain_name": "Κρητικός", "price": 4.30}
]

# 4. Εγγραφή Προϊόντων
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
            print(f"  💰 Ενημέρωση: {chain} -> {price_val}€")
        else:
            supabase.table("prices").insert(payload).execute()
            print(f"  ➕ Νέα Εγγραφή: {chain} -> {price_val}€")

    except Exception as e:
        print(f"❌ Σφάλμα στην τιμή {chain}: {e}")

print("🎉 Ο συγχρονισμός ολοκληρώθηκε επιτυχώς με τη στήλη chain_name!")

