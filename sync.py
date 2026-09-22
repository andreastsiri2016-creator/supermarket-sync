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

# Πλήρης Κατάλογος Προϊόντων
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
    {"id": "1", "product_id": "520101000001", "supermarket": "Σκλαβενίτης", "price": 11.45},
    {"id": "2", "product_id": "520101000001", "supermarket": "ΑΒ Βασιλόπουλος", "price": 11.80},
    {"id": "3", "product_id": "520101000001", "supermarket": "Lidl", "price": 10.90},
    {"id": "4", "product_id": "520101000001", "supermarket": "MyMarket", "price": 11.20},
    {"id": "5", "product_id": "520101000001", "supermarket": "Γαλαξίας", "price": 11.30},
    {"id": "6", "product_id": "520101000001", "supermarket": "Κρητικός", "price": 11.40},

    # Φέτα
    {"id": "7", "product_id": "520101000002", "supermarket": "Σκλαβενίτης", "price": 5.25},
    {"id": "8", "product_id": "520101000002", "supermarket": "ΑΒ Βασιλόπουλος", "price": 5.48},
    {"id": "9", "product_id": "520101000002", "supermarket": "Lidl", "price": 4.95},
    {"id": "10", "product_id": "520101000002", "supermarket": "MyMarket", "price": 5.15},
    {"id": "11", "product_id": "520101000002", "supermarket": "Γαλαξίας", "price": 5.10},
    {"id": "12", "product_id": "520101000002", "supermarket": "Κρητικός", "price": 5.30},

    # Γάλα
    {"id": "13", "product_id": "520101000003", "supermarket": "Σκλαβενίτης", "price": 1.62},
    {"id": "14", "product_id": "520101000003", "supermarket": "ΑΒ Βασιλόπουλος", "price": 1.68},
    {"id": "15", "product_id": "520101000003", "supermarket": "Lidl", "price": 1.55},
    {"id": "16", "product_id": "520101000003", "supermarket": "MyMarket", "price": 1.60},
    {"id": "17", "product_id": "520101000003", "supermarket": "Γαλαξίας", "price": 1.58},
    {"id": "18", "product_id": "520101000003", "supermarket": "Κρητικός", "price": 1.65},

    # Καφές
    {"id": "19", "product_id": "520101000004", "supermarket": "Σκλαβενίτης", "price": 4.80},
    {"id": "20", "product_id": "520101000004", "supermarket": "ΑΒ Βασιλόπουλος", "price": 4.95},
    {"id": "21", "product_id": "520101000004", "supermarket": "Lidl", "price": 4.50},
    {"id": "22", "product_id": "520101000004", "supermarket": "MyMarket", "price": 4.75},
    {"id": "23", "product_id": "520101000004", "supermarket": "Γαλαξίας", "price": 4.65},
    {"id": "24", "product_id": "520101000004", "supermarket": "Κρητικός", "price": 4.85},

    # Μακαρόνια
    {"id": "25", "product_id": "520101000005", "supermarket": "Σκλαβενίτης", "price": 0.92},
    {"id": "26", "product_id": "520101000005", "supermarket": "ΑΒ Βασιλόπουλος", "price": 0.98},
    {"id": "27", "product_id": "520101000005", "supermarket": "Lidl", "price": 0.85},
    {"id": "28", "product_id": "520101000005", "supermarket": "MyMarket", "price": 0.90},
    {"id": "29", "product_id": "520101000005", "supermarket": "Γαλαξίας", "price": 0.88},
    {"id": "30", "product_id": "520101000005", "supermarket": "Κρητικός", "price": 0.95},

    # Χαρτί Υγείας
    {"id": "31", "product_id": "520101000006", "supermarket": "Σκλαβενίτης", "price": 4.20},
    {"id": "32", "product_id": "520101000006", "supermarket": "ΑΒ Βασιλόπουλος", "price": 4.50},
    {"id": "33", "product_id": "520101000006", "supermarket": "Lidl", "price": 3.99},
    {"id": "34", "product_id": "520101000006", "supermarket": "MyMarket", "price": 4.15},
    {"id": "35", "product_id": "520101000006", "supermarket": "Γαλαξίας", "price": 4.10},
    {"id": "36", "product_id": "520101000006", "supermarket": "Κρητικός", "price": 4.30}
]

for p in products:
    supabase.table("products").upsert(p, on_conflict="barcode").execute()

for pr in prices:
    supabase.table("prices").upsert(pr).execute()

print("🎉 Επιτυχής ενημέρωση όλων των αλυσίδων!")
