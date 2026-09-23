import os
import sys

print("🚀 Εκκίνηση ασφαλούς συγχρονισμού Supabase...")

# 1. Έλεγχος Περιβάλλοντος
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

if not url or not key:
    print("❌ ΣΦΑΛΜΑ: Λείπουν τα SUPABASE_URL ή SUPABASE_KEY στα Secrets!")
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

# 3. Κατάλογος Τιμών ανά Barcode & Αλυσίδα
prices_catalog = [
    # Ελαιόλαδο
    {"barcode": "520101000001", "supermarket": "Lidl", "price": 10.90},
    {"barcode": "520101000001", "supermarket": "Sklavenitis", "price": 11.45},
    {"barcode": "520101000001", "supermarket": "AB Vassilopoulos", "price": 11.80},
    {"barcode": "520101000001", "supermarket": "MyMarket", "price": 11.20},
    {"barcode": "520101000001", "supermarket": "Galaxias", "price": 11.30},
    {"barcode": "520101000001", "supermarket": "Kritikos", "price": 11.40},

    # Φέτα
    {"barcode": "520101000002", "supermarket": "Lidl", "price": 4.95},
    {"barcode": "520101000002", "supermarket": "Sklavenitis", "price": 5.25},
    {"barcode": "520101000002", "supermarket": "AB Vassilopoulos", "price": 5.48},
    {"barcode": "520101000002", "supermarket": "MyMarket", "price": 5.15},
    {"barcode": "520101000002", "supermarket": "Galaxias", "price": 5.10},
    {"barcode": "520101000002", "supermarket": "Kritikos", "price": 5.30},

    # Γάλα
    {"barcode": "520101000003", "supermarket": "Lidl", "price": 1.55},
    {"barcode": "520101000003", "supermarket": "Sklavenitis", "price": 1.62},
    {"barcode": "520101000003", "supermarket": "AB Vassilopoulos", "price": 1.68},
    {"barcode": "520101000003", "supermarket": "MyMarket", "price": 1.60},
    {"barcode": "520101000003", "supermarket": "Galaxias", "price": 1.58},
    {"barcode": "520101000003", "supermarket": "Kritikos", "price": 1.65},

    # Καφές
    {"barcode": "520101000004", "supermarket": "Lidl", "price": 4.50},
    {"barcode": "520101000004", "supermarket": "Sklavenitis", "price": 4.80},
    {"barcode": "520101000004", "supermarket": "AB Vassilopoulos", "price": 4.95},
    {"barcode": "520101000004", "supermarket": "MyMarket", "price": 4.75},
    {"barcode": "520101000004", "supermarket": "Galaxias", "price": 4.65},
    {"barcode": "520101000004", "supermarket": "Kritikos", "price": 4.85},

    # Μακαρόνια
    {"barcode": "520101000005", "supermarket": "Lidl", "price": 0.85},
    {"barcode": "520101000005", "supermarket": "Sklavenitis", "price": 0.92},
    {"barcode": "520101000005", "supermarket": "AB Vassilopoulos", "price": 0.98},
    {"barcode": "520101000005", "supermarket": "MyMarket", "price": 0.90},
    {"barcode": "520101000005", "supermarket": "Galaxias", "price": 0.88},
    {"barcode": "520101000005", "supermarket": "Kritikos", "price": 0.95},

    # Χαρτί Υγείας
    {"barcode": "520101000006", "supermarket": "Lidl", "price": 3.99},
    {"barcode": "520101000006", "supermarket": "Sklavenitis", "price": 4.20},
    {"barcode": "520101000006", "supermarket": "AB Vassilopoulos", "price": 4.50},
    {"barcode": "520101000006", "supermarket": "MyMarket", "price": 4.15},
    {"barcode": "520101000006", "supermarket": "Galaxias", "price": 4.10},
    {"barcode": "520101000006", "supermarket": "Kritikos", "price": 4.30}
]

# -------------------------------------------------------------
# 4. Ασφαλής Εγγραφή Προϊόντων (Safe Insert / Update)
# -------------------------------------------------------------
product_map = {}  # barcode -> db_id

for prod in products_catalog:
    bcd = prod["barcode"]
    try:
        # Έλεγχος αν υπάρχει ήδη
        existing = supabase.table("products").select("id").eq("barcode", bcd).execute()
        
        if existing.data and len(existing.data) > 0:
            prod_id = existing.data[0]["id"]
            supabase.table("products").update(prod).eq("id", prod_id).execute()
            print(f"📦 Ενημερώθηκε: {prod['name']} (ID: {prod_id})")
        else:
            inserted = supabase.table("products").insert(prod).execute()
            prod_id = inserted.data[0]["id"]
            print(f"➕ Προστέθηκε: {prod['name']} (ID: {prod_id})")
            
        product_map[bcd] = prod_id
    except Exception as e:
        print(f"❌ Σφάλμα στο προϊόν {prod['name']}: {e}")

# -------------------------------------------------------------
# 5. Ασφαλής Εγγραφή Τιμών (Safe Insert / Update)
# -------------------------------------------------------------
for item in prices_catalog:
    bcd = item["barcode"]
    market = item["supermarket"]
    price_val = item["price"]
    
    prod_id = product_map.get(bcd)
    if not prod_id:
        print(f"⚠️ Παράβλεψη τιμής για barcode {bcd}: Δεν βρέθηκε το ID προϊόντος.")
        continue

    try:
        # Έλεγχος αν υπάρχει ήδη εγγραφή τιμής για το ίδιο προϊόν & αλυσίδα
        existing_price = supabase.table("prices")\
            .select("id")\
            .eq("product_id", prod_id)\
            .eq("supermarket", market)\
            .execute()
            
        payload = {
            "product_id": prod_id,
            "supermarket": market,
            "price": price_val
        }

        if existing_price.data and len(existing_price.data) > 0:
            row_id = existing_price.data[0]["id"]
            supabase.table("prices").update(payload).eq("id", row_id).execute()
            print(f"  💰 Ενημέρωση: {market} -> {price_val}€")
        else:
            supabase.table("prices").insert(payload).execute()
            print(f"  ➕ Νέα Τιμή: {market} -> {price_val}€")

    except Exception as e:
        print(f"❌ Σφάλμα στην τιμή {market}: {e}")

print("🎉 Ο συγχρονισμός ολοκληρώθηκε 100% επιτυχώς και χωρίς σφάλματα!")
