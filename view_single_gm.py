"""
Simple script to view a single Grandmaster by ID
Usage: python view_single_gm.py
Supports JSON and XML output formats
"""

import requests

BASE_URL = "http://localhost:5000"

# Ask user for ID
gm_id = input("Enter Grandmaster ID: ")

# Ask user for format
print("\nChoose output format:")
print("1. JSON (default)")
print("2. XML")
choice = input("Enter choice (1 or 2): ").strip() or "1"

fmt = "xml" if choice == "2" else "json"

# Get the grandmaster
print(f"\nFetching grandmaster {gm_id} ({fmt.upper()})...\n")
response = requests.get(f'{BASE_URL}/api/gms/{gm_id}', params={"format": fmt})

if response.status_code == 200:
    if fmt == "json":
        gm = response.json()['gm']
        
        print(f"✅ Found Grandmaster:\n")
        print(f"ID: {gm['id']}")
        print(f"Name: {gm['first_name']} {gm['last_name']}")
        print(f"Country: {gm['country']}")
        print(f"Birth Year: {gm['birth_year']}")
        print(f"Current Rating: {gm['current_rating']}")
        print(f"Peak Rating: {gm['peak_rating']}")
        print(f"Title Year: {gm['title_year']}")
        print(f"FIDE ID: {gm['FIDE_id']}")
    else:  # XML format
        print("XML Response:")
        print("-" * 40)
        print(response.text)
        print("-" * 40)
    
elif response.status_code == 404:
    print(f"❌ Grandmaster with ID {gm_id} not found")
else:
    print(f"❌ Error: {response.json().get('error', 'Unknown error')}")
