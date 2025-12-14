"""
Simple script to view a single Grandmaster by ID
Usage: python view_gm.py
"""

import requests

BASE_URL = "http://localhost:5000"

# Ask user for ID
gm_id = input("Enter Grandmaster ID: ")

# Get the grandmaster
response = requests.get(f'{BASE_URL}/api/gms/{gm_id}')

if response.status_code == 200:
    gm = response.json()['gm']
    
    print(f"\nFound Grandmaster:\n")
    print(f"ID: {gm['id']}")
    print(f"Name: {gm['first_name']} {gm['last_name']}")
    print(f"Country: {gm['country']}")
    print(f"Birth Year: {gm['birth_year']}")
    print(f"Current Rating: {gm['current_rating']}")
    print(f"Peak Rating: {gm['peak_rating']}")
    print(f"Title Year: {gm['title_year']}")
    print(f"FIDE ID: {gm['FIDE_id']}")
    
elif response.status_code == 404:
    print(f"Grandmaster with ID {gm_id} not found")
else:
    print(f"Error: {response.json().get('error', 'Unknown error')}")
