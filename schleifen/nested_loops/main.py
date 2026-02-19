produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

# 1. groceries als Liste von Listen aufbauen
groceries = [produce, dairy]

# 2. Äußere Schleife über die Kategorien
for section in groceries:
    # 3. Innere Schleife über die einzelnen Artikel
    for item in section:
        print("Item name:", item)