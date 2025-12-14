
## Requirements

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
  

## 🔐 Authentication

All POST, PUT, and DELETE requests require a **JWT token**.

### Getting a Token

```bash
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"password123"}'
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



5. Run the application:
```bash
python app.py
```
The API will run on `http://localhost:5000`

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

