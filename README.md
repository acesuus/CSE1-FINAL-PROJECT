# Grandmasters REST API

A complete REST API for managing chess grandmasters using Flask and MySQL. This project demonstrates CRUD operations, JWT authentication, input validation, and multiple data formats (JSON/XML).

## 📋 Project Details

**Grandmasters REST API** provides a backend service to store, retrieve, update, and delete information about chess grandmasters. The API includes:

- ✅ Complete CRUD operations (Create, Read, Update, Delete)
- ✅ JWT token-based authentication
- ✅ Search and filtering capabilities
- ✅ Multiple output formats (JSON and XML)
- ✅ Comprehensive input validation
- ✅ Error handling and proper HTTP status codes
- ✅ Easy-to-use Python scripts for data management

## 🔧 Technology Stack

| Component | Technology |
|-----------|-----------|
| Backend Framework | Flask 3.1.0 |
| Database | MySQL |
| Authentication | PyJWT 2.8.1 |
| Data Validation | Python type checking |
| Testing | pytest |
| Data Format | JSON/XML (dicttoxml) |

## 📦 Requirements

```
Flask==3.1.0
Flask-MySQLdb==2.0.0
PyJWT==2.8.1
dicttoxml==1.7.16
mysqlclient==2.2.7
pytest==7.4.0
requests==2.31.0
```

## 🚀 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/acesuus/CSE1-FINAL-PROJECT.git
cd CSE1-FINAL-PROJECT
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Database Connection

Edit `conn.py`:
```python
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "your_password"
MYSQL_DB = "grandmaster"
```

### Step 5: Create Database and Table

```sql
CREATE DATABASE grandmaster;
USE grandmaster;

CREATE TABLE grandmasters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    country VARCHAR(3) NOT NULL,
    birth_year INT NOT NULL,
    peak_rating INT NOT NULL,
    current_rating INT NOT NULL,
    title_year INT NOT NULL,
    FIDE_id VARCHAR(20) UNIQUE NOT NULL
);
```

### Step 6: Run the Application
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## 🔐 Authentication

All POST, PUT, and DELETE requests require a **JWT token**.

### Getting a Token

```bash
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"password123"}'
```

**Response:**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### Using the Token

Include the token in the `Authorization` header:
```bash
-H "Authorization: Bearer YOUR_TOKEN_HERE"
```

**Token Expiration:** 1 hour

## 📡 API Endpoints

### 1. Login (Get JWT Token)
```
POST /api/login
```

**Request:**
```json
{
  "username": "admin",
  "password": "password123"
}
```

**Response (201):**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

### 2. Create Grandmaster (POST)
```
POST /api/gms/
```

**Headers:**
```
Authorization: Bearer <token>
Content-Type: application/json
```

**Request Body:**
```json
{
  "first_name": "Magnus",
  "last_name": "Carlsen",
  "country": "NOR",
  "birth_year": 1990,
  "peak_rating": 2882,
  "current_rating": 2850,
  "title_year": 2013,
  "FIDE_id": "1503014"
}
```

**Response (201):**
```json
{
  "message": "GM added",
  "id": 1
}
```

---

### 3. Get All Grandmasters (GET)
```
GET /api/gms/
```

**Optional Parameters:**
- `search`: Search by first or last name
- `format`: Response format (`json` or `xml`, default: `json`)

**Examples:**
```bash
# Get all grandmasters (JSON)
GET /api/gms/

# Get all grandmasters (XML)
GET /api/gms/?format=xml

# Search for "Magnus"
GET /api/gms/?search=Magnus
```

**Response (200):**
```json
{
  "grandmasters": [
    {
      "id": 1,
      "first_name": "Magnus",
      "last_name": "Carlsen",
      "country": "NOR",
      "birth_year": 1990,
      "peak_rating": 2882,
      "current_rating": 2850,
      "title_year": 2013,
      "FIDE_id": "1503014"
    }
  ]
}
```

---

### 4. Get Single Grandmaster (GET)
```
GET /api/gms/<id>
```

**Example:**
```bash
GET /api/gms/1
```

**Response (200):**
```json
{
  "gm": {
    "id": 1,
    "first_name": "Magnus",
    "last_name": "Carlsen",
    "country": "NOR",
    "birth_year": 1990,
    "peak_rating": 2882,
    "current_rating": 2850,
    "title_year": 2013,
    "FIDE_id": "1503014"
  }
}
```

**Error Response (404):**
```json
{
  "error": "GM not found"
}
```

---

### 5. Update Grandmaster (PUT)
```
PUT /api/gms/<id>
```

**Headers:**
```
Authorization: Bearer <token>
Content-Type: application/json
```

**Request Body:** (all fields required)
```json
{
  "first_name": "Magnus",
  "last_name": "Carlsen",
  "country": "NOR",
  "birth_year": 1990,
  "peak_rating": 2900,
  "current_rating": 2870,
  "title_year": 2013,
  "FIDE_id": "1503014"
}
```

**Response (200):**
```json
{
  "message": "GM updated"
}
```

---

### 6. Delete Grandmaster (DELETE)
```
DELETE /api/gms/<id>
```

**Headers:**
```
Authorization: Bearer <token>
```

**Response (200):**
```json
{
  "message": "GM deleted"
}
```

---

## 🛠️ Easy Data Management Scripts

This project includes simple, beginner-friendly Python scripts for managing data:

### 1. Add a Grandmaster
```bash
python add_gm.py
```
- Interactive script to add one grandmaster
- Automatically handles authentication
- Simple step-by-step process

**Example:**
```
Logging in...
✅ Login successful

Enter first name: Magnus
Enter last name: Carlsen
Enter country: NOR
... (more prompts)

✅ Success! Added Magnus Carlsen
   ID: 1
```

---

### 2. View All Grandmasters
```bash
python view_gms.py
```
- Displays all grandmasters in the database
- Shows: ID, Name, Country, Ratings, FIDE ID
- No authentication required

**Output:**
```
Found 5 grandmasters:

ID: 1
Name: Magnus Carlsen
Country: NOR
Rating: 2850 (peak: 2882)
FIDE ID: 1503014
----------------------------------------
```

---

### 3. View Single Grandmaster
```bash
python view_single_gm.py
```
- Search for a specific grandmaster by ID
- Shows all details

**Interactive:**
```
Enter Grandmaster ID: 1

✅ Found Grandmaster:

ID: 1
Name: Magnus Carlsen
Country: NOR
Birth Year: 1990
Current Rating: 2850
Peak Rating: 2882
Title Year: 2013
FIDE ID: 1503014
```

---

### 4. Search Grandmasters
```bash
python search_gm.py
```
- Search by first or last name
- Case-insensitive partial matching

**Interactive:**
```
Search for grandmaster (first or last name): Magnus

✅ Found 1 result(s):

ID: 1
Name: Magnus Carlsen
Country: NOR
Rating: 2850
----------------------------------------
```

---

### 5. Update a Grandmaster
```bash
python update_gm.py
```
- Update all fields of a grandmaster
- Interactive prompts for each field
- Requires authentication

**Interactive:**
```
Logging in...
✅ Login successful

Enter Grandmaster ID to update: 1

Enter new grandmaster data:
First name: Magnus
Last name: Carlsen
Country code (e.g., NOR): NOR
Birth year: 1990
Peak rating: 2900
Current rating: 2875
Title year: 2013
FIDE ID: 1503014

✅ Success! Updated Magnus Carlsen
```

---

### 6. Delete a Grandmaster
```bash
python delete_gm.py
```
- Remove a grandmaster from the database
- Requires confirmation before deletion
- Requires authentication

**Interactive:**
```
Logging in...
✅ Login successful

Enter Grandmaster ID to delete: 1
Are you sure you want to delete GM 1? (yes/no): yes

✅ Success! Deleted GM 1
```

---

## ✅ Input Validation

The API validates all grandmaster data:

| Field | Rules |
|-------|-------|
| `first_name` | Non-empty string |
| `last_name` | Non-empty string |
| `country` | Non-empty string (3 chars recommended) |
| `birth_year` | Integer between 1800 and current year |
| `peak_rating` | Non-negative integer |
| `current_rating` | Non-negative integer ≤ peak_rating |
| `title_year` | Integer between 1800 and current year |
| `FIDE_id` | Non-empty string, must be unique |

**Example Error Response:**
```json
{
  "error": "Current rating cannot exceed peak rating"
}
```

---

## 🧪 Testing

Run the test suite:

```bash
pytest test_gms_api.py -v
```

**Test Coverage:**
- ✅ Create grandmaster (valid data)
- ✅ Create with missing fields
- ✅ Create with invalid data types
- ✅ Create with negative ratings
- ✅ Create without authentication
- ✅ View all grandmasters
- ✅ Search functionality
- ✅ Get single grandmaster
- ✅ Get non-existent grandmaster
- ✅ Update operations
- ✅ Delete with authentication
- ✅ Delete non-existent grandmaster

---

## 📊 Project Structure

```
CSE1-FINAL-PROJECT/
├── app.py                 # Flask application and login endpoint
├── conn.py               # Database connection config
├── db.py                 # MySQL wrapper
├── requirements.txt      # Python dependencies
├── README.md            # This file
│
├── CRUD/
│   └── gms.py           # All API endpoints (CREATE, READ, UPDATE, DELETE)
│
├── utils/
│   ├── auth.py          # JWT authentication functions
│   └── format.py        # JSON/XML response formatting
│
├── add_gm.py            # Add grandmaster script
├── view_gms.py          # View all grandmasters script
├── view_single_gm.py    # View single grandmaster script
├── search_gm.py         # Search grandmasters script
├── update_gm.py         # Update grandmaster script
├── delete_gm.py         # Delete grandmaster script
│
└── test_gms_api.py      # Pytest test suite
```

---

## 📝 Example Workflow

### 1. Start the Server
```bash
python app.py
```

### 2. Add Some Data
```bash
python add_gm.py
```

### 3. View the Data
```bash
python view_gms.py
```

### 4. Search for a Grandmaster
```bash
python search_gm.py
```

### 5. Update Information
```bash
python update_gm.py
```

### 6. Delete if Needed
```bash
python delete_gm.py
```

---

## 🔒 Security Notes

- ⚠️ Change hardcoded credentials in `app.py` (username/password)
- ⚠️ Use environment variables for database credentials
- ⚠️ Change the `SECRET_KEY` in `utils/auth.py`
- ⚠️ Use HTTPS in production
- ⚠️ Implement rate limiting for production

---

## 🐛 Troubleshooting

### "Connection refused" error
```
Issue: MySQL not running
Solution: Start MySQL service
```

### "Unknown column 'id'" error
```
Issue: Table structure doesn't match
Solution: Verify table was created with correct columns
```

### "Invalid token" error
```
Issue: Token expired or invalid
Solution: Get a new token using login endpoint
```

### "400 Bad Request"
```
Issue: Missing required fields or invalid data
Solution: Check all fields are provided and have correct types
```

---

## 📄 License

This project is for educational purposes (CSE1 Final Project)

## 👨‍💻 Author

**acesuus** - GitHub Repository Owner

---

## 📞 Support

For issues or questions, please check:
1. README.md (this file)
2. Test examples in `test_gms_api.py`
3. API endpoint documentation above
4. Script documentation in each `.py` file

5. Run the application:
```bash
python app.py
```

The API will run on `http://localhost:5000`

## API Endpoints

### 1. Login (Get Token)
**POST** `/api/login`

Request:
```json
{
  "username": "admin",
  "password": "password123"
}
```

Response:
```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### 2. Create Grandmaster
**POST** `/api/gms/`

Headers: `Authorization: Bearer <token>`

Request:
```json
{
  "name": "Magnus Carlsen",
  "rating": 2882
}
```

Response:
```json
{
  "message": "GM added",
  "id": 1
}
```

### 3. Get All Grandmasters
**GET** `/api/gms/`

Optional Parameters:
- `search`: Search by name (e.g., `?search=Magnus`)
- `format`: Response format `json` or `xml` (e.g., `?format=xml`)

Response:
```json
{
  "grandmasters": [
    {
      "id": 1,
      "name": "Magnus Carlsen",
      "rating": 2882
    }
  ]
}
```

### 4. Get Single Grandmaster
**GET** `/api/gms/<id>`

Response:
```json
{
  "gm": {
    "id": 1,
    "name": "Magnus Carlsen",
    "rating": 2882
  }
}
```

### 5. Update Grandmaster
**PUT** `/api/gms/<id>`

Headers: `Authorization: Bearer <token>`

Request:
```json
{
  "name": "Magnus Carlsen",
  "rating": 2900
}
```

Response:
```json
{
  "message": "GM updated"
}
```

### 6. Delete Grandmaster
**DELETE** `/api/gms/<id>`

Headers: `Authorization: Bearer <token>`

Response:
```json
{
  "message": "GM deleted"
}
```

## Testing

Run tests:
```bash
pytest test_api.py -v
```

## Example Usage with cURL

1. Login:
```bash
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"password123"}'
```

2. Create GM (use token from login):
```bash
curl -X POST http://localhost:5000/api/gms/ \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{"name":"Hikaru Nakamura","rating":2789}'
```

3. Get all GMs:
```bash
curl http://localhost:5000/api/gms/
```

4. Search GMs:
```bash
curl http://localhost:5000/api/gms/?search=Magnus
```

5. Get XML format:
```bash
curl http://localhost:5000/api/gms/?format=xml
```


## Author
Kert-Ace T. Ombion

