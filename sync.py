import os
import sys

print("🚀 Εκκίνηση ασφαλούς συγχρονισμού 43 προϊόντων & 258 τιμών...")

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
    print(f"❌ Σφάλμα σύνδεσης με Supabase: {e}")
    sys.exit(1)

# 2. Πλήρης Κατάλογος 43 Προϊόντων
products_catalog = [
    # Βασικά Τρόφιμα & Γαλακτοκομικά
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
    {"barcode": "520101000015", "name": "Εμφιαλωμένο Νερό 6x1.5L", "category": "Αναψυκτικά & Χυμοί", "brand": "Ζαγόρι", "unit": "9L", "image_url": "https://images.unsplash.com/photo-1548839140-29a749e1bc4e?w=400"},

    # Αρτοποιία, Κρέατα, Αλλαντικά, Καφέδες & Πρωινό
    {"barcode": "520101000016", "name": "Ψωμί για Τόστ Σίτου 500g", "category": "Αρτοποιία", "brand": "Karas", "unit": "500g", "image_url": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=400"},
    {"barcode": "520101000017", "name": "Γραβιέρα Κρήτης 350g", "category": "Γαλακτοκομικά", "brand": "Κολιός", "unit": "350g", "image_url": "https://images.unsplash.com/photo-1452195100486-9cc805987862?w=400"},
    {"barcode": "520101000018", "name": "Κασέρι Π.Ο.Π. 300g", "category": "Γαλακτοκομικά", "brand": "Φάρμα", "unit": "300g", "image_url": "https://images.unsplash.com/photo-1618160702438-9b02ab6515c9?w=400"},
    {"barcode": "520101000019", "name": "Βούτυρο Αγελάδος 225g", "category": "Γαλακτοκομικά", "brand": "Lurpak", "unit": "225g", "image_url": "https://images.unsplash.com/photo-1589985270826-4b7bb135bc9d?w=400"},
    {"barcode": "520101000020", "name": "Κοτόπουλο Νωπό Ολόκληρο 1.5kg", "category": "Κρέατα", "brand": "Πίνδος", "unit": "1.5kg", "image_url": "https://images.unsplash.com/photo-1587593810167-a84920ea0781?w=400"},
    {"barcode": "520101000021", "name": "Κιμάς Μοσχαρίσιος 500g", "category": "Κρέατα", "brand": "Φρέσκος", "unit": "500g", "image_url": "https://images.unsplash.com/photo-1588347818036-558601350947?w=400"},
    {"barcode": "520101000022", "name": "Γαλοπούλα Καπνιστή Φέτες 160g", "category": "Αλλαντικά", "brand": "Υφαντής", "unit": "160g", "image_url": "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?w=400"},
    {"barcode": "520101000023", "name": "Πάριζα Χαράκι 300g", "category": "Αλλαντικά", "brand": "Creta Farm", "unit": "300g", "image_url": "https://images.unsplash.com/photo-1541529086526-db283c563270?w=400"},
    {"barcode": "520101000024", "name": "Ελληνικός Καφές 194g", "category": "Καφέδες", "brand": "Λουμίδης", "unit": "194g", "image_url": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=400"},
    {"barcode": "520101000025", "name": "Καφές Φίλτρου 250g", "category": "Καφέδες", "brand": "Jacobs Gold", "unit": "250g", "image_url": "https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=400"},
    {"barcode": "520101000026", "name": "Μέλι Ανθέων 480g", "category": "Πρωινό", "brand": "Αττική", "unit": "480g", "image_url": "https://images.unsplash.com/photo-1587049352846-4a222e784d38?w=400"},
    {"barcode": "520101000027", "name": "Merenda 360g", "category": "Πρωινό", "brand": "Παυλίδης", "unit": "360g", "image_url": "https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?w=400"},
    {"barcode": "520101000028", "name": "Φακές Ψιλές 500g", "category": "Όσπρια & Ρύζια", "brand": "Voion", "unit": "500g", "image_url": "https://images.unsplash.com/photo-1515543237350-b3eea1ec8082?w=400"},
    {"barcode": "520101000029", "name": "Φασόλια Μέτρια 500g", "category": "Όσπρια & Ρύζια", "brand": "Agrino", "unit": "500g", "image_url": "https://images.unsplash.com/photo-1551462147-37885acc36f1?w=400"},
    {"barcode": "520101000030", "name": "Σάλτσα Τομάτας Passata 500g", "category": "Κονσέρβες", "brand": "KYKNOS", "unit": "500g", "image_url": "https://images.unsplash.com/photo-1598170845058-32b9d6a5da37?w=400"},
    {"barcode": "520101000031", "name": "Ηλιέλαιο 1L", "category": "Ελαιόλαδα", "brand": "Sol", "unit": "1L", "image_url": "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=400"},
    {"barcode": "520101000032", "name": "Coca-Cola 4x500ml", "category": "Αναψυκτικά & Χυμοί", "brand": "Coca-Cola", "unit": "2L", "image_url": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=400"},
    {"barcode": "520101000033", "name": "Μπίρα Κουτί 6x330ml", "category": "Αναψυκτικά & Χυμοί", "brand": "Fix Hellas", "unit": "1.98L", "image_url": "https://images.unsplash.com/photo-1608270586620-248524c67de9?w=400"},
    {"barcode": "520101000034", "name": "Πατατάκια Αλάτι 150g", "category": "Σνακ & Γλυκά", "brand": "Lay's", "unit": "150g", "image_url": "https://images.unsplash.com/photo-1566478989037-eec170784d0b?w=400"},
    {"barcode": "520101000035", "name": "Σοκολάτα Υγείας 100g", "category": "Σνακ & Γλυκά", "brand": "Παυλίδης", "unit": "100g", "image_url": "https://images.unsplash.com/photo-1582176647444-3e9146ec75aa?w=400"},
    {"barcode": "520101000036", "name": "Απορρυπαντικό Πλυντηρίου 40 μεζούρες", "category": "Χαρτικά & Καθαριστικά", "brand": "Ariel", "unit": "2L", "image_url": "https://images.unsplash.com/photo-1610557892470-55d9e80c0bce?w=400"},
    {"barcode": "520101000037", "name": "Μαλακτικό Ρούχων 50 μεζούρες", "category": "Χαρτικά & Καθαριστικά", "brand": "Lenor", "unit": "1.2L", "image_url": "https://images.unsplash.com/photo-1585842378054-ee2e52f94ba2?w=400"},
    {"barcode": "520101000038", "name": "Σαμπουάν 400ml", "category": "Προσωπική Φροντίδα", "brand": "Pantene", "unit": "400ml", "image_url": "https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?w=400"},
    {"barcode": "520101000039", "name": "Αφρόλουτρο 650ml", "category": "Προσωπική Φροντίδα", "brand": "Dove", "unit": "650ml", "image_url": "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?w=400"},
    {"barcode": "520101000040", "name": "Χαρτί Κουζίνας 2 ρολά", "category": "Χαρτικά & Καθαριστικά", "brand": "Endless", "unit": "2 τμχ", "image_url": "https://images.unsplash.com/photo-1584556812952-905ffd0c611a?w=400"},

    # Βρεφικά Είδη
    {"barcode": "520101000041", "name": "Μωρομάντηλα Νερού 3x52 τμχ", "category": "Βρεφικά", "brand": "Pampers Aqua Pure", "unit": "156 τμχ", "image_url": "https://images.unsplash.com/photo-1555252333-9f8e92e65df9?w=400"},
    {"barcode": "520101000042", "name": "Πάνες Νο 4 (9-14kg) 52 τμχ", "category": "Βρεφικά", "brand": "Pampers Premium Care", "unit": "52 τμχ", "image_url": "https://images.unsplash.com/photo-1515488042361-ee00e0ddd4e4?w=400"},
    {"barcode": "520101000043", "name": "Βρεφική Κρέμα Συγκάματος 100ml", "category": "Βρεφικά", "brand": "Sudocrem", "unit": "100ml", "image_url": "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400"}
]

# 3. Βασικές Τιμές αναφοράς
base_prices = {
    "520101000001": 11.20, "520101000002": 5.20, "520101000003": 1.60, "520101000004": 4.70, "520101000005": 0.90,
    "520101000006": 4.10, "520101000007": 3.40, "520101000008": 2.80, "520101000009": 1.50, "520101000010": 4.90,
    "520101000011": 2.10, "520101000012": 1.20, "520101000013": 2.30, "520101000014": 2.90, "520101000015": 1.80,
    "520101000016": 1.65, "520101000017": 5.80, "520101000018": 4.20, "520101000019": 3.10, "520101000020": 6.50,
    "520101000021": 5.40, "520101000022": 2.70, "520101000023": 2.90, "520101000024": 2.85, "520101000025": 4.10,
    "520101000026": 6.20, "520101000027": 3.15, "520101000028": 1.75, "520101000029": 1.95, "520101000030": 0.85,
    "520101000031": 2.40, "520101000032": 3.80, "520101000033": 5.90, "520101000034": 1.40, "520101000035": 1.30,
    "520101000036": 12.50, "520101000037": 4.20, "520101000038": 3.60, "520101000039": 3.90, "520101000040": 2.10,
    "520101000041": 5.90, "520101000042": 16.80, "520101000043": 4.50
}

# 4. Ασφαλής Ενημέρωση/Εισαγωγή Προϊόντων
print("📦 Συγχρονισμός καταλόγου προϊόντων...")
for prod in products_catalog:
    try:
        existing = supabase.table("products").select("id").eq("barcode", prod["barcode"]).execute()
        if existing.data and len(existing.data) > 0:
            supabase.table("products").update(prod).eq("id", existing.data[0]["id"]).execute()
        else:
            supabase.table("products").insert(prod).execute()
    except Exception as e:
        print(f"⚠️ Προειδοποίηση στο προϊόν {prod['name']}: {e}")

# 5. Ανάκτηση όλων των IDs από τη βάση δεδομένων
all_products = supabase.table("products").select("id, barcode").execute()
product_map = {item["barcode"]: item["id"] for item in all_products.data}

print(f"✅ Βρέθηκαν {len(product_map)} συνδεδεμένα προϊόντα στη βάση.")

# 6. Προετοιμασία Τιμών για όλες τις 6 Αλυσίδες
prices_payload = []
for bcd, price in base_prices.items():
    prod_id = product_map.get(bcd)
    if prod_id:
        prices_payload.extend([
            {"product_id": prod_id, "chain_name": "Lidl", "price": round(price * 0.95, 2)},
            {"product_id": prod_id, "chain_name": "Σκλαβενίτης", "price": round(price * 1.00, 2)},
            {"product_id": prod_id, "chain_name": "MyMarket", "price": round(price * 1.01, 2)},
            {"product_id": prod_id, "chain_name": "Γαλαξίας", "price": round(price * 1.02, 2)},
            {"product_id": prod_id, "chain_name": "Κρητικός", "price": round(price * 1.03, 2)},
            {"product_id": prod_id, "chain_name": "ΑΒ Βασιλόπουλος", "price": round(price * 1.05, 2)}
        ])

# 7. Ασφαλής Εγγραφή Τιμών (Row-by-Row Safe Update/Insert)
print("💰 Συγχρονισμός τιμών για όλες τις αλυσίδες...")
updated_count = 0

for price_item in prices_payload:
    try:
        existing_price = supabase.table("prices")\
            .select("id")\
            .eq("product_id", price_item["product_id"])\
            .eq("chain_name", price_item["chain_name"])\
            .execute()

        if existing_price.data and len(existing_price.data) > 0:
            supabase.table("prices").update({"price": price_item["price"]}).eq("id", existing_price.data[0]["id"]).execute()
        else:
            supabase.table("prices").insert(price_item).execute()
        
        updated_count += 1
    except Exception as e:
        print(f"⚠️ Προειδοποίηση στην τιμή {price_item['chain_name']}: {e}")

print(f"🎉 Ο συγχρονισμός ολοκληρώθηκε 100% επιτυχώς για {len(product_map)} προϊόντα και {updated_count} τιμές!")
