"""
Simple script to add a Grandmaster to the database
Usage: python add_gm.py
"""

import requests

BASE_URL = "http://localhost:5000"

# Step 1: Login to get a token
print("Logging in")
response = requests.post(f'{BASE_URL}/api/login', 
    json={"username": "admin", "password": "password123"})
token = response.json()['token']
print(f"Login successful\n")

# Step 2: Create your grandmaster data
gm = {
    "first_name": "Magnus",
    "last_name": "Carlsen",
    "country": "NOR",
    "birth_year": 1990,
    "peak_rating": 2882,
    "current_rating": 2850,
    "title_year": 2013,
    "FIDE_id": "1503014"
}

# Step 3: Send the data to the API
headers = {"Authorization": f"Bearer {token}"}
response = requests.post(f'{BASE_URL}/api/gms/', 
    json=gm, headers=headers)

# Step 4: Check the result
if response.status_code == 201:
    result = response.json()
    print(f"Success! Added {gm['first_name']} {gm['last_name']}")
    print(f"   ID: {result['id']}")
else:
    error = response.json().get('error', 'Unknown error')
    print(f"Failed: {error}")