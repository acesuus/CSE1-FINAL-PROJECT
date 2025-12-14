"""
Simple script to search for Grandmasters
Usage: python search_gm.py
Supports JSON and XML output formats
"""

import requests

BASE_URL = "http://localhost:5000"

# Get search term from user
search = input("Search for grandmaster (first or last name): ")

# Ask user for format
print("\nChoose output format:")
print("1. JSON (default)")
print("2. XML")
choice = input("Enter choice (1 or 2): ").strip() or "1"

fmt = "xml" if choice == "2" else "json"

# Search
print(f"\nSearching for '{search}' ({fmt.upper()})...\n")
response = requests.get(f'{BASE_URL}/api/gms/', 
    params={"search": search, "format": fmt})

if response.status_code == 200:
    if fmt == "json":
        data = response.json()
        gms = data.get('grandmasters', [])
        
        if not gms:
            print(f"No grandmasters found matching '{search}'")
        else:
            print(f"✅ Found {len(gms)} result(s):\n")
            for gm in gms:
                print(f"ID: {gm['id']}")
                print(f"Name: {gm['first_name']} {gm['last_name']}")
                print(f"Country: {gm['country']}")
                print(f"Rating: {gm['current_rating']}")
                print("-" * 40)
    else:  # XML format
        print("XML Response:")
        print("-" * 40)
        print(response.text)
        print("-" * 40)
else:
    print(f"❌ Error: {response.json().get('error', 'Unknown error')}")
