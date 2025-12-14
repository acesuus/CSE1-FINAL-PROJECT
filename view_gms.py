import requests

BASE_URL = "http://localhost:5000"

# Ask user for format
print("Choose output format:")
print("1. JSON (default)")
print("2. XML")
choice = input("Enter choice (1 or 2): ").strip() or "1"

fmt = "xml" if choice == "2" else "json"

# Get all grandmasters
print(f"\nFetching all grandmasters ({fmt.upper()})...\n")
response = requests.get(f'{BASE_URL}/api/gms/', params={"format": fmt})

if response.status_code == 200:
    if fmt == "json":
        data = response.json()
        gms = data.get('grandmasters', [])
        
        if not gms:
            print("No grandmasters found")
        else:
            print(f"Found {len(gms)} grandmasters:\n")
            for gm in gms:
                print(f"ID: {gm['id']}")
                print(f"Name: {gm['first_name']} {gm['last_name']}")
                print(f"Country: {gm['country']}")
                print(f"Rating: {gm['current_rating']} (peak: {gm['peak_rating']})")
                print(f"FIDE ID: {gm['FIDE_id']}")
                print("-" * 40)
    else:  # XML format
        print("XML Response:")
        print("-" * 40)
        print(response.text)
        print("-" * 40)
else:
    print(f"Error: {response.json().get('error', 'Unknown error')}")
