"""
Simple script to search for Grandmasters
Usage: python search_gm.py
"""

import requests

BASE_URL = "http://localhost:5000"

# Get search from user
search = input("Search for grandmaster (first or last name): ")

# Search
response = requests.get(f'{BASE_URL}/api/gms/', 
    params={"search": search})

if response.status_code == 200:
    data = response.json()
    gms = data.get('grandmasters', [])
    
    if not gms:
        print(f"\nNo grandmasters found '{search}'")
    else:
        print(f"\nFound {len(gms)} result(s):\n")
        for gm in gms:
            print(f"ID: {gm['id']}")
            print(f"Name: {gm['first_name']} {gm['last_name']}")
            print(f"Country: {gm['country']}")
            print(f"Rating: {gm['current_rating']}")
            print("-" * 40)
else:
    print(f"Error: {response.json().get('error', 'Unknown error')}")
