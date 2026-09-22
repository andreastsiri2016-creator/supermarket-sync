import os
import sys

print("🚀 Εκκίνηση ενημέρωσης τιμών για όλες τις αλυσίδες...")

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

# Πλήρης Κατάλογος Προϊόντων (σταθερά IDs)
products = [
    {"id": "520101000001", "barcode": "520101000001", "name": "Ελαιόλαδο Έξτρα Παρθένο 1L", "category": "Ελαιόλαδα", "brand": "Χωριό", "unit": "1L", "image_url": "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=400"},
    {"id": "520101000002", "barcode": "520101000002", "name": "Φέτα Π.Ο.Π. 400g", "category": "Γαλακτοκομικά", "brand": "Δωδώνη", "unit": "400g", "image_url": "https://images.unsplash.com/photo-1559561853-08451507cbe7?w=400"},
    {"id": "520101000003", "barcode": "520101000003", "name": "Γάλα Φρέσκο Πλήρες 1L", "category": "Γαλακτοκομικά", "brand": "ΟΛΥΜΠΟΣ", "unit": "1L", "image_url": "https://images.unsplash.com/photo-1550583724-b2692b85b150?w=400"},
    {"id": "520101000004", "barcode": "520101000004", "name": "Εσπρέσο Αλεσμένος 250g", "category": "Καφέδες", "brand": "Jacobs", "unit": "250g", "image_url": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=400"},
    {"id": "520101000005", "barcode": "520101000005", "name": "Μακαρόνια No 6 500g", "category": "Ζυμαρικά", "brand": "MISKO", "unit": "500g", "image_url": "https://images.unsplash.com/photo-1621996346565-e3d5d6281318?w=400"},
    {"id": "520101000006", "barcode": "520101000006", "name": "Χαρτί Υγείας 3-ply 10 ρολά", "category": "Χαρτικά & Καθαριστικά", "brand": "Endless", "unit": "10 τμχ", "image_url": "https://images.unsplash.com/photo-1584556812952-905ffd0c611a?w=400"}
]

# Τιμές για ΌΛΑ τα Σούπερ Μάρκετ (Σκλαβενίτης, ΑΒ, Lidl, MyMarket, Γαλαξίας, Κρητικός)
prices = [
    # Ελαιόλαδο
    {"product_id": "520101000001", "supermarket": "Σκλαβενίτης", "price": 11.45},
    {"product_id": "520101000001", "supermarket": "ΑΒ Βασιλόπουλος", "price": 11.80},
    {"product_id": "520101000001", "supermarket": "Lidl", "price": 10.90},
    {"product_id": "520101000001", "supermarket": "MyMarket", "price": 11.20},
    {"product_id": "520101000001", "supermarket": "Γαλαξίας", "price": 11.30},
    {"product_id": "520101000001", "supermarket": "Κρητικός", "price": 11.40},

    # Φέτα
    {"product_id": "520101000002", "supermarket": "Σκλαβενίτης", "price": 5.25},
    {"product_id": "520101000002", "supermarket": "ΑΒ Βασιλόπουλος", "price": 5.48},
    {"product_id": "520101000002", "supermarket": "Lidl", "price": 4.95},
    {"product_id": "520101000002", "supermarket": "MyMarket", "price": 5.15},
    {"product_id": "520101000002", "supermarket": "Γαλαξίας", "price": 5.10},
    {"product_id": "520101000002", "supermarket": "Κρητικός", "price": 5.30},

    # Γάλα
    {"product_id": "520101000003", "supermarket": "Σκλαβενίτης", "price": 1.62},
    {"product_id": "520101000003", "supermarket": "ΑΒ Βασιλόπουλος", "price": 1.68},
    {"product_id": "520101000003", "supermarket": "Lidl", "price": 1.55},
    {"product_id": "520101000003", "supermarket": "MyMarket", "price": 1.60},
    {"product_id": "520101000003", "supermarket": "Γαλαξίας", "price": 1.58},
    {"product_id": "520101000003", "supermarket": "Κρητικός", "price": 1.65},

    # Καφές
    {"product_id": "520101000004", "supermarket": "Σκλαβενίτης", "price": 4.80},
    {"product_id": "520101000004", "supermarket": "ΑΒ Βασιλόπουλος", "price": 4.95},
    {"product_id": "520101000004", "supermarket": "Lidl", "price": 4.50},
    {"product_id": "520101000004", "supermarket": "MyMarket", "price": 4.75},
    {"product_id": "520101000004", "supermarket": "Γαλαξίας", "price": 4.65},
    {"product_id": "520101000004", "supermarket": "Κρητικός", "price": 4.85},

    # Μακαρόνια
    {"product_id": "520101000005", "supermarket": "Σκλαβενίτης", "price": 0.92},
    {"product_id": "520101000005", "supermarket": "ΑΒ Βασιλόπουλος", "price": 0.98},
    {"product_id": "520101000005", "supermarket": "Lidl", "price": 0.85},
    {"product_id": "520101000005", "supermarket": "MyMarket", "price": 0.90},
    {"product_id": "520101000005", "supermarket": "Γαλαξίας", "price": 0.88},
    {"product_id": "520101000005", "supermarket": "Κρητικός", "price": 0.95},

    # Χαρτί Υγείας
    {"product_id": "520101000006", "supermarket": "Σκλαβενίτης", "price": 4.20},
    {"product_id": "520101000006", "supermarket": "ΑΒ Βασιλόπουλος", "price": 4.50},
    {"product_id": "520101000006", "supermarket": "Lidl", "price": 3.99},
    {"product_id": "520101000006", "supermarket": "MyMarket", "price": 4.15},
    {"product_id": "520101000006", "supermarket": "Γαλαξίας", "price": 4.10},
    {"product_id": "520101000006", "supermarket": "Κρητικός", "price": 4.30}
]

# 1. Πρώτα ενημερώνουμε τα προϊόντα
for p in products:
    try:
        supabase.table("products").upsert(p, on_conflict="id").execute()
        print(f"📦 Προϊόν: {p['name']}")
    except Exception as e:
        print(f"❌ Σφάλμα στο προϊόν {p['name']}: {e}")

# 2. Μετά ενημερώνουμε τις τιμές
for pr in prices:
    try:
        supabase.table("prices").upsert(pr).execute()
        print(f"  💰 {pr['supermarket']}: {pr['price']}€")
    except Exception as e:
        print(f"❌ Σφάλμα στην τιμή: {e}")

print("🎉 Επιτυχής ενημέρωση όλων των αλυσίδων!")
