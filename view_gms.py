"""
Simple script to view all Grandmasters
Usage: python view_gms.py
"""

import requests

BASE_URL = "http://localhost:5000"

# Get all grandmasters
print("Fetching all grandmasters...\n")
response = requests.get(f'{BASE_URL}/api/gms/')

if response.status_code == 200:
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
else:
    print(f"Error: {response.json().get('error', 'Unknown error')}")
