"""
Simple script to delete a Grandmaster
Usage: python delete_gm.py
"""

import requests

BASE_URL = "http://localhost:5000"

# Step 1: Login to get a token
print("Logging in...")
response = requests.post(f'{BASE_URL}/api/login', 
    json={"username": "admin", "password": "password123"})
token = response.json()['token']
print("Login successful\n")

# Step 2: Get the ID to delete
id = input("Enter Grandmaster ID to delete: ")

# Step 3: Confirm deletion
confirm = input(f"Are you sure you want to delete GM {id}? (yes/no): ")

if confirm.lower() != 'yes':
    print("Cancelled.")
    exit()

# Step 4: Send delete request
headers = {"Authorization": f"Bearer {token}"}
response = requests.delete(f'{BASE_URL}/api/gms/{id}', 
    headers=headers)

# Step 5: Check result
if response.status_code == 200:
    print(f"\nSuccess! Deleted GM {id}")
else:
    error = response.json().get('error', 'Unknown error')
    print(f"\nFailed: {error}")
