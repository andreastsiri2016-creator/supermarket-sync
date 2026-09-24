import os
import sys

print("🚀 Έναρξη αναγκαστικού συγχρονισμού προϊόντων & εικόνων...")

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

if not url or not key:
    print("❌ Λείπουν τα secrets!")
    sys.exit(1)

from supabase import create_client
supabase = create_client(url, key)

products_catalog = [
    # --- Ελαιόλαδα & Λάδια ---
    {"barcode": "520101000001", "name": "Ελαιόλαδο Έξτρα Παρθένο 1L", "category": "Ελαιόλαδα", "brand": "Χωριό", "unit": "1L", "image_url": "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=600&auto=format&fit=crop"},
    {"barcode": "520101000031", "name": "Ηλιέλαιο Sol 1L", "category": "Ελαιόλαδα", "brand": "Sol", "unit": "1L", "image_url": "https://images.unsplash.com/photo-1620706857370-e1b993a58c35?w=600&auto=format&fit=crop"},

    # --- Γαλακτοκομικά, Τυριά & Εναλλακτικά ---
    {"barcode": "520101000002", "name": "Φέτα Π.Ο.Π. Δωδώνη 400g", "category": "Γαλακτοκομικά", "brand": "Δωδώνη", "unit": "400g", "image_url": "https://images.unsplash.com/photo-1559561853-08451507cbe7?w=600&auto=format&fit=crop"},
    {"barcode": "520101000003", "name": "Γάλα Φρέσκο Πλήρες 3.5% 1L", "category": "Γαλακτοκομικά", "brand": "ΟΛΥΜΠΟΣ", "unit": "1L", "image_url": "https://images.unsplash.com/photo-1563636619-e9143da7973b?w=600&auto=format&fit=crop"},
    {"barcode": "520101000007", "name": "Γιαούρτι Στραγγιστό Total 2% 3x200g", "category": "Γαλακτοκομικά", "brand": "ΦΑΓΕ", "unit": "600g", "image_url": "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600&auto=format&fit=crop"},
    {"barcode": "520101000017", "name": "Γραβιέρα Κρήτης Π.Ο.Π. 350g", "category": "Γαλακτοκομικά", "brand": "Κολιός", "unit": "350g", "image_url": "https://images.unsplash.com/photo-1452195100486-9cc805987862?w=600&auto=format&fit=crop"},
    {"barcode": "520101000018", "name": "Κασέρι Π.Ο.Π. 300g", "category": "Γαλακτοκομικά", "brand": "Φάρμα", "unit": "300g", "image_url": "https://images.unsplash.com/photo-1618160702438-9b02ab6515c9?w=600&auto=format&fit=crop"},
    {"barcode": "520101000019", "name": "Βούτυρο Αγελάδος Lurpak 225g", "category": "Γαλακτοκομικά", "brand": "Lurpak", "unit": "225g", "image_url": "https://images.unsplash.com/photo-1589985270826-4b7bb135bc9d?w=600&auto=format&fit=crop"},
    {"barcode": "520101000044", "name": "Αμυγδαλόγαλα Χωρίς Προσθήκη Ζάχαρης 1L", "category": "Γαλακτοκομικά", "brand": "Alpro", "unit": "1L", "image_url": "https://images.unsplash.com/photo-1550583724-b2692b85b150?w=600&auto=format&fit=crop"},
    {"barcode": "520101000045", "name": "Τυρί Cottage Cheese Light 200g", "category": "Γαλακτοκομικά", "brand": "Arla", "unit": "200g", "image_url": "https://images.unsplash.com/photo-1559561853-08451507cbe7?w=600&auto=format&fit=crop"},
    {"barcode": "520101000046", "name": "Τυρί Cottage Cheese Light 400g", "category": "Γαλακτοκομικά", "brand": "Arla", "unit": "400g", "image_url": "https://images.unsplash.com/photo-1559561853-08451507cbe7?w=600&auto=format&fit=crop"},

    # --- Καφέδες & Πρωινό ---
    {"barcode": "520101000004", "name": "Εσπρέσο Αλεσμένος Classico 250g", "category": "Καφέδες", "brand": "Jacobs", "unit": "250g", "image_url": "https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=600&auto=format&fit=crop"},
    {"barcode": "520101000024", "name": "Ελληνικός Καφές Παραδοσιακός 194g", "category": "Καφέδες", "brand": "Λουμίδης", "unit": "194g", "image_url": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=600&auto=format&fit=crop"},
    {"barcode": "520101000025", "name": "Καφές Φίλτρου Gold 250g", "category": "Καφέδες", "brand": "Jacobs Gold", "unit": "250g", "image_url": "https://images.unsplash.com/photo-1511920170033-f8396924c348?w=600&auto=format&fit=crop"},
    {"barcode": "520101000008", "name": "Δημητριακά Ολικής Αλέσεως 375g", "category": "Πρωινό", "brand": "Nestle Fitness", "unit": "375g", "image_url": "https://images.unsplash.com/photo-1521483451569-e33803c0330c?w=600&auto=format&fit=crop"},
    {"barcode": "520101000026", "name": "Μέλι Ανθέων & Κωνοφόρων 480g", "category": "Πρωινό", "brand": "Αττική", "unit": "480g", "image_url": "https://images.unsplash.com/photo-1587049352846-4a222e784d38?w=600&auto=format&fit=crop"},
    {"barcode": "520101000027", "name": "Merenda Κρέμα Φουντουκιού 360g", "category": "Πρωινό", "brand": "Παυλίδης", "unit": "360g", "image_url": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=600&auto=format&fit=crop"}, # 🐱 Γατάκι στη Merenda

    # --- Όσπρια, Ζυμαρικά & Κονσέρβες ---
    {"barcode": "520101000005", "name": "Μακαρόνια No 6 Σπαγγέτι 500g", "category": "Ζυμαρικά", "brand": "MISKO", "unit": "500g", "image_url": "https://images.unsplash.com/photo-1621996346565-e3d5d6281318?w=600&auto=format&fit=crop"},
    {"barcode": "520101000011", "name": "Ρύζι Καρολίνα 1kg", "category": "Όσπρια & Ρύζια", "brand": "Agrino", "unit": "1kg", "image_url": "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=600&auto=format&fit=crop"},
    {"barcode": "520101000028", "name": "Φακές Ψιλές 500g", "category": "Όσπρια & Ρύζια", "brand": "Voion", "unit": "500g", "image_url": "https://images.unsplash.com/photo-1515543237350-b3eea1ec8082?w=600&auto=format&fit=crop"},
    {"barcode": "520101000029", "name": "Φασόλια Μέτρια Ελληνικά 500g", "category": "Όσπρια & Ρύζια", "brand": "Agrino", "unit": "500g", "image_url": "https://images.unsplash.com/photo-1551462147-37885acc36f1?w=600&auto=format&fit=crop"},
    {"barcode": "520101000030", "name": "Σάλτσα Τομάτας Passata 500g", "category": "Κονσέρβες", "brand": "KYKNOS", "unit": "500g", "image_url": "https://images.unsplash.com/photo-1598170845058-32b9d6a5da37?w=600&auto=format&fit=crop"},
    {"barcode": "520101000010", "name": "Τόνος σε Νερό 3x80g", "category": "Κονσέρβες", "brand": "Rio Mare", "unit": "240g", "image_url": "https://images.unsplash.com/photo-1534483509719-3feaee7c30da?w=600&auto=format&fit=crop"},

    # --- Κρέατα, Αλλαντικά & Ψωμί ---
    {"barcode": "520101000020", "name": "Κοτόπουλο Νωπό Ολόκληρο 1.5kg", "category": "Κρέατα", "brand": "Πίνδος", "unit": "1.5kg", "image_url": "https://images.unsplash.com/photo-1587593810167-a84920ea0781?w=600&auto=format&fit=crop"},
    {"barcode": "520101000021", "name": "Κιμάς Μοσχαρίσιος Νωπός 500g", "category": "Κρέατα", "brand": "Φρέσκος", "unit": "500g", "image_url": "https://images.unsplash.com/photo-1588347818036-558601350947?w=600&auto=format&fit=crop"},
    {"barcode": "520101000022", "name": "Γαλοπούλα Καπνιστή Φέτες 160g", "category": "Αλλαντικά", "brand": "Υφαντής", "unit": "160g", "image_url": "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?w=600&auto=format&fit=crop"},
    {"barcode": "520101000047", "name": "Γαλοπούλα Βραστή Φέτες 160g", "category": "Αλλαντικά", "brand": "Creta Farm", "unit": "160g", "image_url": "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?w=600&auto=format&fit=crop"},
    {"barcode": "520101000023", "name": "Πάριζα Χαράκι En Elladi 300g", "category": "Αλλαντικά", "brand": "Creta Farm", "unit": "300g", "image_url": "https://images.unsplash.com/photo-1541529086526-db283c563270?w=600&auto=format&fit=crop"},
    {"barcode": "520101000016", "name": "Ψωμί για Τόστ Σίτου 500g", "category": "Αρτοποιία", "brand": "Karas", "unit": "500g", "image_url": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=600&auto=format&fit=crop"},

    # --- Αναψυκτικά, Σνακ & Ποτά ---
    {"barcode": "520101000009", "name": "Φυσικός Χυμός Πορτοκάλι 100% 1L", "category": "Αναψυκτικά & Χυμοί", "brand": "Amita", "unit": "1L", "image_url": "https://images.unsplash.com/photo-1600271886742-f049cd451bba?w=600&auto=format&fit=crop"},
    {"barcode": "520101000015", "name": "Εμφιαλωμένο Νερό 6x1.5L", "category": "Αναψυκτικά & Χυμοί", "brand": "Ζαγόρι", "unit": "9L", "image_url": "https://images.unsplash.com/photo-1548839140-29a749e1bc4e?w=600&auto=format&fit=crop"},
    {"barcode": "520101000032", "name": "Coca-Cola Original 4x500ml", "category": "Αναψυκτικά & Χυμοί", "brand": "Coca-Cola", "unit": "2L", "image_url": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=600&auto=format&fit=crop"},
    {"barcode": "520101000033", "name": "Μπίρα Lager 6x330ml", "category": "Αναψυκτικά & Χυμοί", "brand": "Fix Hellas", "unit": "1.98L", "image_url": "https://images.unsplash.com/photo-1608270586620-248524c67de9?w=600&auto=format&fit=crop"},
    {"barcode": "520101000012", "name": "Μπισκότα Γεμιστά Σοκολάτα 200g", "category": "Σνακ & Γλυκά", "brand": "Παπαδοπούλου", "unit": "200g", "image_url": "https://images.unsplash.com/photo-1558961363-fa8fdf82db35?w=600&auto=format&fit=crop"},
    {"barcode": "520101000034", "name": "Πατατάκια Αλάτι 150g", "category": "Σνακ & Γλυκά", "brand": "Lay's", "unit": "150g", "image_url": "https://images.unsplash.com/photo-1566478989037-eec170784d0b?w=600&auto=format&fit=crop"},
    {"barcode": "520101000035", "name": "Σοκολάτα Υγείας 100g", "category": "Σνακ & Γλυκά", "brand": "Παυλίδης", "unit": "100g", "image_url": "https://images.unsplash.com/photo-1582176647444-3e9146ec75aa?w=600&auto=format&fit=crop"},

    # --- Καθαριστικά & Προσωπική Φροντίδα ---
    {"barcode": "520101000006", "name": "Χαρτί Υγείας 3-ply 10 ρολά", "category": "Χαρτικά & Καθαριστικά", "brand": "Endless", "unit": "10 τμχ", "image_url": "https://images.unsplash.com/photo-1584556812952-905ffd0c611a?w=600&auto=format&fit=crop"},
    {"barcode": "520101000013", "name": "Υγρό Πιάτων Λεμόνι 500ml", "category": "Χαρτικά & Καθαριστικά", "brand": "Fairy", "unit": "500ml", "image_url": "https://images.unsplash.com/photo-1585842378054-ee2e52f94ba2?w=600&auto=format&fit=crop"},
    {"barcode": "520101000036", "name": "Απορρυπαντικό Πλυντηρίου 40 μεζούρες", "category": "Χαρτικά & Καθαριστικά", "brand": "Ariel", "unit": "2L", "image_url": "https://images.unsplash.com/photo-1610557892470-55d9e80c0bce?w=600&auto=format&fit=crop"},
    {"barcode": "520101000037", "name": "Μαλακτικό Ρούχων 50 μεζούρες", "category": "Χαρτικά & Καθαριστικά", "brand": "Lenor", "unit": "1.2L", "image_url": "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?w=600&auto=format&fit=crop"},
    {"barcode": "520101000040", "name": "Χαρτί Κουζίνας 2 ρολά", "category": "Χαρτικά & Καθαριστικά", "brand": "Endless", "unit": "2 τμχ", "image_url": "https://images.unsplash.com/photo-1600585152220-90363fe7e115?w=600&auto=format&fit=crop"},
    {"barcode": "520101000014", "name": "Οδοντόκρεμα Colgate Total 75ml", "category": "Προσωπική Φροντίδα", "brand": "Colgate", "unit": "75ml", "image_url": "https://images.unsplash.com/photo-1559598467-f8b76c8155d0?w=600&auto=format&fit=crop"},
    {"barcode": "520101000038", "name": "Σαμπουάν Repair & Protect 400ml", "category": "Προσωπική Φροντίδα", "brand": "Pantene", "unit": "400ml", "image_url": "https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?w=600&auto=format&fit=crop"},
    {"barcode": "520101000039", "name": "Αφρόλουτρο Deeply Nourishing 650ml", "category": "Προσωπική Φροντίδα", "brand": "Dove", "unit": "650ml", "image_url": "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=600&auto=format&fit=crop"},

    # --- Βρεφικά Είδη ---
    {"barcode": "520101000041", "name": "Μωρομάντηλα Aqua Pure 3x48 τμχ", "category": "Βρεφικά", "brand": "Pampers Aqua Pure", "unit": "144 τμχ", "image_url": "https://images.unsplash.com/photo-1555252333-9f8e92e65df9?w=600&auto=format&fit=crop"},
    {"barcode": "520101000042", "name": "Πάνες Νο 4 (9-14kg)", "category": "Βρεφικά", "brand": "Pampers Premium Care", "unit": "52 τμχ", "image_url": "https://images.unsplash.com/photo-1515488042361-ee00e0ddd4e4?w=600&auto=format&fit=crop"},
    {"barcode": "520101000043", "name": "Βρεφική Κρέμα Συγκάματος 125g", "category": "Βρεφικά", "brand": "Sudocrem", "unit": "125g", "image_url": "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=600&auto=format&fit=crop"}
]

print("📦 Αναγκαστικό update προϊόντων με βάση το barcode...")
for prod in products_catalog:
    # Κάνουμε upsert βασισμένο στη στήλη barcode (απαιτείται unique constraint στο barcode στο Supabase)
    supabase.table("products").upsert(prod, on_conflict="barcode").execute()

print("✅ Τα προϊόντα και οι νέες εικόνες ενημερώθηκαν επιτυχώς!")

