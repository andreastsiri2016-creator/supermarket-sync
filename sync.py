import os
import requests
from supabase import create_client

# Διαβάζουμε τα μυστικά κλειδιά από τις ρυθμίσεις του GitHub
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print("🚀 Το ρομπότ ξύπνησε και ξεκινάει το γέμισμα τιμών...")

# Ενδεικτική λίστα προϊόντων
products = [
    {"barcode": "520101000001", "name": "Ελαιόλαδο Έξτρα Παρθένο 1L", "category": "Ελαιόλαδα", "brand": "Χωριό", "unit": "1L", "image_url": "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=300"},
    {"barcode": "520101000002", "name": "Φέτα Π.Ο.Π. 400g", "category": "Γαλακτοκομικά", "brand": "Δωδώνη", "unit": "400g", "image_url": "https://images.unsplash.com/photo-1559561853-08451507cbe7?w=300"}
]

for p in products:
    res = supabase.table("products").upsert(p, on_conflict="barcode").execute()
    if res.data:
        print(f"✅ Ενημερώθηκε το προϊόν: {p['name']}")

print("🎉 Το ρομπότ ολοκλήρωσε τη δουλειά και ξανακοιμάται!")
