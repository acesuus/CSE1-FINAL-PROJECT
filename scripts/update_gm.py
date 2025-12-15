"""
Simple script to update a Grandmaster
Usage: python update_gm.py
"""

import requests

BASE_URL = "http://localhost:5000"

# Step 1: Login to get a token
print("Logging in...")
response = requests.post(f'{BASE_URL}/api/login', 
    json={"username": "admin", "password": "password123"})
token = response.json()['token']
print("Login successful\n")

# Step 2: Get the ID to update
gm_id = input("Enter Grandmaster ID to update: ")

# Step 3: Enter new data
print("\nEnter new grandmaster data:")
gm = {
    "first_name": input("First name: "),
    "last_name": input("Last name: "),
    "country": input("Country code (e.g., NOR): "),
    "birth_year": int(input("Birth year: ")),
    "peak_rating": int(input("Peak rating: ")),
    "current_rating": int(input("Current rating: ")),
    "title_year": int(input("Title year: ")),
    "FIDE_id": input("FIDE ID: ")
}

# Step 4: Send update request
headers = {"Authorization": f"Bearer {token}"}
response = requests.put(f'{BASE_URL}/api/gms/{gm_id}', 
    json=gm, headers=headers)

# Step 5: Check result
if response.status_code == 200:
    print(f"\nSuccess! Updated {gm['first_name']} {gm['last_name']}")
else:
    error = response.json().get('error', 'Unknown error')
    print(f"\nFailed: {error}")
