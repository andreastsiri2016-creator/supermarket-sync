import os
import sys

print("🚀 Εκκίνηση script...")

# 1. Έλεγχος αν υπάρχουν τα Secrets
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

if not url or not key:
    print("❌ ΣΦΑΛΜΑ: Λείπουν τα SUPABASE_URL ή SUPABASE_KEY από τα Secrets του GitHub!")
    sys.exit(1)

print("✅ Τα Secrets βρέθηκαν επιτυχώς!")

# 2. Σύνδεση με το Supabase
try:
    from supabase import create_client
    supabase = create_client(url, key)
    print("✅ Επιτυχής σύνδεση με το Supabase!")
except Exception as e:
    print(f"❌ Σφάλμα σύνδεσης με Supabase: {e}")
    sys.exit(1)

# 3. Ενημέρωση Δείγματος Προϊόντων
products = [
    {"barcode": "520101000001", "name": "Ελαιόλαδο Έξτρα Παρθένο 1L", "category": "Ελαιόλαδα", "brand": "Χωριό", "unit": "1L", "image_url": "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=300"},
    {"barcode": "520101000002", "name": "Φέτα Π.Ο.Π. 400g", "category": "Γαλακτοκομικά", "brand": "Δωδώνη", "unit": "400g", "image_url": "https://images.unsplash.com/photo-1559561853-08451507cbe7?w=300"}
]

for p in products:
    try:
        res = supabase.table("products").upsert(p, on_conflict="barcode").execute()
        print(f"✅ Ενημερώθηκε το προϊόν: {p['name']}")
    except Exception as e:
        print(f"❌ Σφάλμα στο προϊόν {p['name']}: {e}")

print("🎉 Ολοκληρώθηκε με επιτυχία!")
