# 📚 Week 04: Database Integration & SQL Fundamentals

## 🎯 Learning Objectives
By the end of this lecture, students will be able to:
- Understand SQL fundamentals and database design principles
- Set up and configure database development environments
- Connect Flask applications to databases using SQLAlchemy
- Choose between SQL and NoSQL databases for different use cases
- Use VS Code extensions for database development and visualization
- Implement data persistence for REST APIs from Week 3

## 🔧 Prerequisites
<details>
<summary>Required Setup & Knowledge</summary>

- Flask REST API knowledge from Week 3
- Basic understanding of data structures
- Command line familiarity
- Python environment setup
- Text editor or IDE (VS Code recommended)
</details>

## 📖 Part 1: SQL Fundamentals & Database Design
<!-- Understanding relational databases and SQL operations -->

### ⭐ Key Concepts
<details>
<summary>Database Fundamentals</summary>

- **Relational Database Concepts**
  - Tables, rows, and columns
  - Primary and foreign keys
  - Relationships (one-to-one, one-to-many, many-to-many)
  - Data integrity and constraints
- **SQL Operations (CRUD)**
  - CREATE - Insert new data
  - READ - Query and retrieve data
  - UPDATE - Modify existing data
  - DELETE - Remove data
- **Database Design Principles**
  - Normalization to reduce redundancy
  - Entity-Relationship (ER) modeling
  - Indexing for performance
  - ACID properties (Atomicity, Consistency, Isolation, Durability)

> 💡 **Key Point**: Good database design is crucial for scalable applications and data integrity
</details>

### 💻 SQL Implementation Examples
<details>
<summary>Practical SQL Examples</summary>

```sql
-- Database Creation and Table Setup
CREATE DATABASE sales_app;
USE sales_app;

-- Create Customers table
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    age INTEGER CHECK (age >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create Categories table
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Sales table with foreign keys
CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    product_category_id INTEGER NOT NULL,
    sale_amount DECIMAL(10,2) NOT NULL CHECK (sale_amount > 0),
    sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE,
    FOREIGN KEY (product_category_id) REFERENCES categories(id) ON DELETE RESTRICT,
    INDEX idx_customer_id (customer_id),
    INDEX idx_sale_date (sale_date),
    INDEX idx_category_amount (product_category_id, sale_amount)
);

-- Insert sample data
INSERT INTO categories (name, description) VALUES 
('Electronics', 'Electronic devices and gadgets'),
('Clothing', 'Apparel and fashion items'),
('Books', 'Books and educational materials'),
('Home & Garden', 'Home improvement and gardening supplies');

INSERT INTO customers (name, email, age) VALUES 
('Alice Johnson', 'alice@example.com', 28),
('Bob Smith', 'bob@example.com', 35),
('Carol Williams', 'carol@example.com', 42),
('David Brown', 'david@example.com', 29);

INSERT INTO sales (customer_id, product_category_id, sale_amount, notes) VALUES 
(1, 1, 599.99, 'Laptop purchase'),
(2, 2, 89.50, 'Winter jacket'),
(1, 3, 45.00, 'Programming books'),
(3, 1, 1299.99, 'Smartphone and accessories'),
(4, 4, 156.75, 'Garden tools'),
(2, 3, 29.99, 'Mystery novel');
```

```sql
-- Advanced SQL Queries

-- 1. Basic SELECT with filtering and sorting
SELECT 
    c.name AS customer_name,
    c.email,
    s.sale_amount,
    s.sale_date,
    cat.name AS category
FROM sales s
JOIN customers c ON s.customer_id = c.id
JOIN categories cat ON s.product_category_id = cat.id
WHERE s.sale_amount > 50.00
ORDER BY s.sale_date DESC, s.sale_amount DESC;

-- 2. Aggregation and grouping
SELECT 
    cat.name AS category,
    COUNT(s.id) AS total_sales,
    SUM(s.sale_amount) AS total_revenue,
    AVG(s.sale_amount) AS avg_sale_amount,
    MIN(s.sale_amount) AS min_sale,
    MAX(s.sale_amount) AS max_sale
FROM sales s
JOIN categories cat ON s.product_category_id = cat.id
GROUP BY cat.id, cat.name
HAVING SUM(s.sale_amount) > 100.00
ORDER BY total_revenue DESC;

-- 3. Customer analysis with window functions
SELECT 
    c.name,
    c.email,
    s.sale_amount,
    s.sale_date,
    SUM(s.sale_amount) OVER (PARTITION BY c.id) AS customer_total,
    AVG(s.sale_amount) OVER (PARTITION BY c.id) AS customer_avg,
    ROW_NUMBER() OVER (PARTITION BY c.id ORDER BY s.sale_date DESC) AS purchase_rank,
    LAG(s.sale_amount) OVER (PARTITION BY c.id ORDER BY s.sale_date) AS previous_purchase
FROM customers c
JOIN sales s ON c.id = s.customer_id
ORDER BY c.name, s.sale_date DESC;

-- 4. Time-based analysis
SELECT 
    DATE(s.sale_date) as sale_day,
    COUNT(*) as daily_transactions,
    SUM(s.sale_amount) as daily_revenue,
    AVG(s.sale_amount) as avg_transaction_size
FROM sales s
WHERE s.sale_date >= DATE_SUB(CURRENT_DATE, INTERVAL 30 DAY)
GROUP BY DATE(s.sale_date)
ORDER BY sale_day DESC;

-- 5. Complex joins and subqueries
SELECT 
    c.name AS customer_name,
    c.email,
    customer_stats.total_spent,
    customer_stats.purchase_count,
    customer_stats.avg_purchase,
    customer_stats.first_purchase,
    customer_stats.last_purchase,
    CASE 
        WHEN customer_stats.total_spent > 1000 THEN 'VIP'
        WHEN customer_stats.total_spent > 500 THEN 'Premium'
        ELSE 'Standard'
    END AS customer_tier
FROM customers c
JOIN (
    SELECT 
        customer_id,
        COUNT(*) as purchase_count,
        SUM(sale_amount) as total_spent,
        AVG(sale_amount) as avg_purchase,
        MIN(sale_date) as first_purchase,
        MAX(sale_date) as last_purchase
    FROM sales
    GROUP BY customer_id
) customer_stats ON c.id = customer_stats.customer_id
ORDER BY customer_stats.total_spent DESC;

-- 6. Data modification with complex conditions
UPDATE customers 
SET age = age + 1 
WHERE id IN (
    SELECT DISTINCT customer_id 
    FROM sales 
    WHERE sale_date >= DATE_SUB(CURRENT_DATE, INTERVAL 1 YEAR)
    AND sale_amount > 500
);

-- 7. Performance optimization queries
EXPLAIN ANALYZE
SELECT c.name, SUM(s.sale_amount) as total
FROM customers c
JOIN sales s ON c.id = s.customer_id
WHERE s.sale_date >= '2024-01-01'
GROUP BY c.id, c.name
ORDER BY total DESC;

-- Create indexes for better performance
CREATE INDEX idx_sales_date_amount ON sales(sale_date, sale_amount);
CREATE INDEX idx_customers_email ON customers(email);
```

> ⚠️ **Common Mistake**: Not using indexes properly can lead to poor query performance as data grows
</details>

### 🏃 Hands-on Activity
<details>
<summary>Activity: Design Your Database Schema</summary>

#### Steps:
1. **Analyze Requirements**: Think about the data your Week 3 API needs to store
2. **Design Tables**: Create an Entity-Relationship diagram
3. **Write DDL**: Create tables with proper constraints and relationships
4. **Insert Test Data**: Add sample data for testing
5. **Write Queries**: Practice SELECT, JOIN, and aggregation queries

#### Sample Schema Design:
```sql
-- E-commerce example
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    stock_quantity INTEGER DEFAULT 0,
    category_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    status ENUM('pending', 'processing', 'shipped', 'delivered', 'cancelled'),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

> 📝 **Note**: Start simple and add complexity gradually - you can always modify the schema later
</details>

### 💭 Discussion
<details>
<summary>Discussion Topics</summary>

- Key Question: How does database design impact application performance and scalability?
- Follow-up Questions:
  - When should you denormalize data for performance?
  - How do you handle database schema changes in production?
  - What are the trade-offs between different data types?
</details>

## 📖 Part 2: VS Code Database Extensions & Tools
<!-- Setting up professional database development environment -->

### ⭐ Key Concepts
<details>
<summary>Database Development Tools</summary>

- **Essential VS Code Extensions**
  - SQLTools - Universal database client and query runner
  - PostgreSQL Explorer - PostgreSQL-specific functionality
  - SQLite Viewer - Lightweight database browser
  - Database Client JDBC - Enterprise database connections
- **Database Visualization Tools**
  - DBeaver - Professional database administration
  - pgAdmin - PostgreSQL administration and development
  - SQLite Browser - Simple SQLite database management
  - Adminer - Web-based database management
- **Development Workflow**
  - Query development and testing
  - Schema version control
  - Database migrations
  - Performance monitoring

> 💡 **Key Point**: Professional database tools significantly improve development productivity and reduce errors
</details>

### 💻 Setup & Configuration
<details>
<summary>Database Development Environment</summary>

```bash
# Install essential VS Code extensions
code --install-extension mtxr.sqltools
code --install-extension mtxr.sqltools-driver-pg
code --install-extension mtxr.sqltools-driver-sqlite
code --install-extension ms-ossdata.vscode-postgresql
code --install-extension alexcvzz.vscode-sqlite

# Install database servers
# PostgreSQL (Production-ready)
# Ubuntu/Debian:
sudo apt update
sudo apt install postgresql postgresql-contrib

# macOS:
brew install postgresql
brew services start postgresql

# Windows: Download from https://www.postgresql.org/download/

# SQLite (Development/Testing)
# Usually pre-installed on most systems, or:
sudo apt install sqlite3  # Ubuntu/Debian
brew install sqlite       # macOS

# Install Python database drivers
pip install psycopg2-binary  # PostgreSQL driver
pip install sqlite3          # SQLite driver (usually built-in)
pip install sqlalchemy       # ORM for Python
pip install flask-sqlalchemy # Flask integration
```

```json
// VS Code settings.json for database development
{
    "sqltools.connections": [
        {
            "name": "Local PostgreSQL",
            "driver": "PostgreSQL", 
            "server": "localhost",
            "port": 5432,
            "database": "sales_app",
            "username": "postgres",
            "askForPassword": true,
            "connectionTimeout": 15
        },
        {
            "name": "Development SQLite",
            "driver": "SQLite",
            "database": "./database/sales_dev.db"
        },
        {
            "name": "Test Database",
            "driver": "PostgreSQL",
            "server": "localhost", 
            "port": 5432,
            "database": "sales_test",
            "username": "test_user"
        }
    ],
    "sqltools.format": {
        "language": "sql",
        "indentSize": 2
    },
    "sqltools.results": {
        "limit": 1000,
        "location": "next"
    }
}
```

```python
# Database connection testing script
import os
import sqlite3
import psycopg2
from sqlalchemy import create_engine, text
import pandas as pd

def test_sqlite_connection():
    """Test SQLite connection and basic operations."""
    try:
        # Create/connect to SQLite database
        conn = sqlite3.connect('test_database.db')
        cursor = conn.cursor()
        
        # Create test table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS test_users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Insert test data
        cursor.execute('''
            INSERT OR IGNORE INTO test_users (name, email) 
            VALUES (?, ?)
        ''', ('Test User', 'test@example.com'))
        
        # Query data
        cursor.execute('SELECT * FROM test_users')
        results = cursor.fetchall()
        
        print("✓ SQLite connection successful")
        print(f"✓ Found {len(results)} test records")
        
        conn.commit()
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ SQLite connection failed: {e}")
        return False

def test_postgresql_connection():
    """Test PostgreSQL connection and basic operations."""
    try:
        # Connection parameters
        conn_params = {
            'host': 'localhost',
            'port': 5432,
            'database': 'postgres',  # Connect to default database first
            'user': 'postgres',
            'password': os.getenv('POSTGRES_PASSWORD', 'password')
        }
        
        # Test connection
        conn = psycopg2.connect(**conn_params)
        cursor = conn.cursor()
        
        # Test query
        cursor.execute('SELECT version();')
        version = cursor.fetchone()[0]
        
        print("✓ PostgreSQL connection successful")
        print(f"✓ PostgreSQL version: {version[:50]}...")
        
        cursor.close()
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ PostgreSQL connection failed: {e}")
        print("Make sure PostgreSQL is running and credentials are correct")
        return False

def test_sqlalchemy_integration():
    """Test SQLAlchemy with both databases."""
    try:
        # SQLite with SQLAlchemy
        sqlite_engine = create_engine('sqlite:///sqlalchemy_test.db')
        
        # Test query
        with sqlite_engine.connect() as conn:
            result = conn.execute(text("SELECT 'SQLAlchemy SQLite' as test"))
            print(f"✓ SQLAlchemy SQLite: {result.fetchone()[0]}")
        
        # PostgreSQL with SQLAlchemy (if available)
        try:
            pg_url = f"postgresql://postgres:{os.getenv('POSTGRES_PASSWORD', 'password')}@localhost:5432/postgres"
            pg_engine = create_engine(pg_url)
            
            with pg_engine.connect() as conn:
                result = conn.execute(text("SELECT 'SQLAlchemy PostgreSQL' as test"))
                print(f"✓ SQLAlchemy PostgreSQL: {result.fetchone()[0]}")
                
        except Exception as e:
            print(f"△ SQLAlchemy PostgreSQL not available: {e}")
        
        return True
        
    except Exception as e:
        print(f"✗ SQLAlchemy test failed: {e}")
        return False

def performance_comparison():
    """Compare database performance for common operations."""
    import time
    
    print("\n" + "="*50)
    print("DATABASE PERFORMANCE COMPARISON")
    print("="*50)
    
    # SQLite performance test
    try:
        start_time = time.time()
        sqlite_engine = create_engine('sqlite:///perf_test.db')
        
        # Create test data
        test_data = pd.DataFrame({
            'id': range(1000),
            'value': [f'test_value_{i}' for i in range(1000)],
            'amount': [i * 1.5 for i in range(1000)]
        })
        
        test_data.to_sql('performance_test', sqlite_engine, if_exists='replace', index=False)
        
        # Query test
        query_start = time.time()
        result = pd.read_sql('SELECT COUNT(*) as count FROM performance_test WHERE amount > 500', sqlite_engine)
        query_time = time.time() - query_start
        
        total_time = time.time() - start_time
        print(f"SQLite: Insert 1000 records + query: {total_time:.3f}s (query: {query_time:.3f}s)")
        
    except Exception as e:
        print(f"SQLite performance test failed: {e}")

if __name__ == "__main__":
    print("Testing Database Connections...")
    print("="*40)
    
    # Test all connections
    sqlite_ok = test_sqlite_connection()
    postgres_ok = test_postgresql_connection()
    sqlalchemy_ok = test_sqlalchemy_integration()
    
    print("\n" + "="*40)
    print("CONNECTION SUMMARY")
    print("="*40)
    print(f"SQLite: {'✓ Ready' if sqlite_ok else '✗ Failed'}")
    print(f"PostgreSQL: {'✓ Ready' if postgres_ok else '✗ Failed'}")
    print(f"SQLAlchemy: {'✓ Ready' if sqlalchemy_ok else '✗ Failed'}")
    
    if sqlite_ok:
        performance_comparison()
    
    print("\nSetup complete! You can now use VS Code database extensions.")
```

```sql
-- SQLTools query examples to test in VS Code

-- @block Test basic connection
SELECT 'Database connection working!' as status, NOW() as current_time;

-- @block Create sample schema
DROP TABLE IF EXISTS sample_products;
CREATE TABLE sample_products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    category VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- @block Insert sample data
INSERT INTO sample_products (name, price, category) VALUES 
('Laptop Pro', 1299.99, 'Electronics'),
('Wireless Mouse', 29.99, 'Electronics'),
('Office Chair', 199.50, 'Furniture'),
('Coffee Mug', 12.99, 'Kitchenware'),
('Notebook', 5.99, 'Stationery');

-- @block Query with formatting
SELECT 
    p.name,
    CONCAT('$', FORMAT(p.price, 2)) as formatted_price,
    p.category,
    p.created_at
FROM sample_products p
WHERE p.price BETWEEN 10 AND 200
ORDER BY p.price DESC;

-- @block Performance analysis
EXPLAIN ANALYZE
SELECT category, COUNT(*) as product_count, AVG(price) as avg_price
FROM sample_products
GROUP BY category
ORDER BY avg_price DESC;
```

> ⚠️ **Common Mistake**: Not configuring connection timeouts can lead to hanging connections in development
</details>

### 🏃 Hands-on Activity
<details>
<summary>Activity: Set Up Your Database Development Environment</summary>

#### Steps:
1. **Install Database Server**: Set up PostgreSQL for production and SQLite for development
2. **Configure VS Code Extensions**: Install and configure SQLTools and database-specific extensions
3. **Create Connection Profiles**: Set up connections for development, testing, and production
4. **Test Connections**: Verify all database connections work properly
5. **Practice Queries**: Write and execute SQL queries using VS Code

#### Environment Checklist:
- [ ] PostgreSQL server installed and running
- [ ] SQLite available for lightweight development
- [ ] VS Code extensions installed and configured
- [ ] Database connections tested successfully
- [ ] Sample database created with test data
- [ ] Query execution working in VS Code

> 📝 **Note**: Keep different connection profiles for development, testing, and production environments
</details>

## 📖 Part 3: Flask + SQLAlchemy Integration
<!-- Connecting Flask APIs to databases for persistent data -->

### ⭐ Key Concepts
<details>
<summary>Database Integration Concepts</summary>

- **Object-Relational Mapping (ORM)**
  - Converting database tables to Python classes
  - Automatic SQL generation from Python code
  - Database-agnostic operations
  - Relationship management
- **SQLAlchemy Features**
  - Database session management
  - Query building and optimization
  - Migration support with Alembic
  - Connection pooling
- **Flask-SQLAlchemy Integration**
  - Application factory pattern
  - Database configuration management
  - Model definition and relationships
  - Automatic table creation

> 💡 **Key Point**: ORM abstracts database operations while maintaining flexibility for complex queries
</details>

### 💻 Flask Database Integration
<details>
<summary>Complete Flask Database Application</summary>

```python
# app.py - Flask application with database integration
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, text
from datetime import datetime
import os
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app
app = Flask(__name__)

# Database configuration
if os.getenv('ENVIRONMENT') == 'production':
    # Production PostgreSQL
    DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/sales_production')
else:
    # Development SQLite
    DATABASE_URL = 'sqlite:///sales_development.db'

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_pre_ping': True,
    'pool_recycle': 300,
}

# Initialize database
db = SQLAlchemy(app)

# Database Models
class Customer(db.Model):
    __tablename__ = 'customers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    sales = db.relationship('Sale', backref='customer', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        """Convert model to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'age': self.age,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    def __repr__(self):
        return f'<Customer {self.name}>'

class Category(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    sales = db.relationship('Sale', backref='category', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
    
    def __repr__(self):
        return f'<Category {self.name}>'

class Sale(db.Model):
    __tablename__ = 'sales'
    
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    sale_amount = db.Column(db.Numeric(10, 2), nullable=False)
    sale_date = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.Text)
    
    # Add constraints
    __table_args__ = (
        db.CheckConstraint('sale_amount > 0', name='positive_sale_amount'),
        db.Index('idx_sale_date', 'sale_date'),
        db.Index('idx_customer_amount', 'customer_id', 'sale_amount'),
    )
    
    def to_dict(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'category_id': self.category_id,
            'sale_amount': float(self.sale_amount),
            'sale_date': self.sale_date.isoformat() if self.sale_date else None,
            'notes': self.notes,
            'customer_name': self.customer.name if self.customer else None,
            'category_name': self.category.name if self.category else None
        }
    
    def __repr__(self):
        return f'<Sale {self.id}: ${self.sale_amount}>'

# API Routes
@app.route('/api/health')
def health_check():
    """Health check endpoint with database connectivity test."""
    try:
        # Test database connection
        db.session.execute(text('SELECT 1'))
        db_status = 'connected'
    except Exception as e:
        db_status = f'error: {str(e)}'
    
    return jsonify({
        'status': 'healthy',
        'database_status': db_status,
        'timestamp': datetime.utcnow().isoformat()
    })

@app.route('/api/customers', methods=['GET'])
def get_customers():
    """Get all customers with optional filtering."""
    try:
        # Query parameters
        page = request.args.get('page', 1, type=int)
        per_page = min(request.args.get('per_page', 20, type=int), 100)
        search = request.args.get('search', '').strip()
        
        # Build query
        query = Customer.query
        
        if search:
            query = query.filter(
                db.or_(
                    Customer.name.ilike(f'%{search}%'),
                    Customer.email.ilike(f'%{search}%')
                )
            )
        
        # Paginate results
        customers_paginated = query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        # Convert to dictionaries
        customers_data = [customer.to_dict() for customer in customers_paginated.items]
        
        return jsonify({
            'status': 'success',
            'data': customers_data,
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': customers_paginated.total,
                'pages': customers_paginated.pages,
                'has_next': customers_paginated.has_next,
                'has_prev': customers_paginated.has_prev
            }
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/customers', methods=['POST'])
def create_customer():
    """Create a new customer."""
    try:
        data = request.get_json()
        
        # Validation
        if not data or not data.get('name') or not data.get('email'):
            return jsonify({
                'status': 'error',
                'message': 'Name and email are required'
            }), 400
        
        # Check for duplicate email
        existing_customer = Customer.query.filter_by(email=data['email']).first()
        if existing_customer:
            return jsonify({
                'status': 'error',
                'message': 'Email already exists'
            }), 400
        
        # Create new customer
        customer = Customer(
            name=data['name'],
            email=data['email'],
            age=data.get('age')
        )
        
        db.session.add(customer)
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'message': 'Customer created successfully',
            'data': customer.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    """Get a specific customer by ID."""
    try:
        customer = Customer.query.get(customer_id)
        
        if not customer:
            return jsonify({
                'status': 'error',
                'message': 'Customer not found'
            }), 404
        
        # Include sales data
        customer_data = customer.to_dict()
        customer_data['sales'] = [sale.to_dict() for sale in customer.sales]
        customer_data['total_sales'] = sum(float(sale.sale_amount) for sale in customer.sales)
        customer_data['sales_count'] = len(customer.sales)
        
        return jsonify({
            'status': 'success',
            'data': customer_data
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    """Update a customer."""
    try:
        customer = Customer.query.get(customer_id)
        
        if not customer:
            return jsonify({
                'status': 'error',
                'message': 'Customer not found'
            }), 404
        
        data = request.get_json()
        
        # Update fields
        if 'name' in data:
            customer.name = data['name']
        if 'email' in data:
            # Check for duplicate email (excluding current customer)
            existing = Customer.query.filter(
                Customer.email == data['email'],
                Customer.id != customer_id
            ).first()
            if existing:
                return jsonify({
                    'status': 'error',
                    'message': 'Email already exists'
                }), 400
            customer.email = data['email']
        if 'age' in data:
            customer.age = data['age']
        
        customer.updated_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'message': 'Customer updated successfully',
            'data': customer.to_dict()
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    """Delete a customer and all associated sales."""
    try:
        customer = Customer.query.get(customer_id)
        
        if not customer:
            return jsonify({
                'status': 'error',
                'message': 'Customer not found'
            }), 404
        
        db.session.delete(customer)
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'message': 'Customer deleted successfully'
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/sales', methods=['POST'])
def create_sale():
    """Create a new sale."""
    try:
        data = request.get_json()
        
        # Validation
        required_fields = ['customer_id', 'category_id', 'sale_amount']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    'status': 'error',
                    'message': f'{field} is required'
                }), 400
        
        # Validate references
        customer = Customer.query.get(data['customer_id'])
        if not customer:
            return jsonify({
                'status': 'error',
                'message': 'Customer not found'
            }), 400
        
        category = Category.query.get(data['category_id'])
        if not category:
            return jsonify({
                'status': 'error',
                'message': 'Category not found'
            }), 400
        
        # Create sale
        sale = Sale(
            customer_id=data['customer_id'],
            category_id=data['category_id'],
            sale_amount=data['sale_amount'],
            notes=data.get('notes')
        )
        
        db.session.add(sale)
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'message': 'Sale created successfully',
            'data': sale.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/sales/analytics')
def sales_analytics():
    """Get sales analytics data."""
    try:
        # Query parameters
        customer_id = request.args.get('customer_id', type=int)
        days = request.args.get('days', 30, type=int)
        
        # Base query
        query = db.session.query(
            func.count(Sale.id).label('transaction_count'),
            func.sum(Sale.sale_amount).label('total_sales'),
            func.avg(Sale.sale_amount).label('avg_transaction'),
            func.min(Sale.sale_amount).label('min_sale'),
            func.max(Sale.sale_amount).label('max_sale')
        )
        
        # Apply filters
        if customer_id:
            query = query.filter(Sale.customer_id == customer_id)
        
        if days:
            cutoff_date = datetime.utcnow() - timedelta(days=days)
            query = query.filter(Sale.sale_date >= cutoff_date)
        
        result = query.first()
        
        analytics_data = {
            'transaction_count': result.transaction_count or 0,
            'total_sales': float(result.total_sales or 0),
            'avg_transaction': float(result.avg_transaction or 0),
            'min_sale': float(result.min_sale or 0),
            'max_sale': float(result.max_sale or 0),
            'period_days': days
        }
        
        return jsonify({
            'status': 'success',
            'data': analytics_data
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

# Database initialization
@app.before_first_request
def create_tables():
    """Create database tables if they don't exist."""
    db.create_all()
    
    # Create default categories if none exist
    if Category.query.count() == 0:
        default_categories = [
            Category(name='Electronics', description='Electronic devices and gadgets'),
            Category(name='Clothing', description='Apparel and fashion items'),
            Category(name='Books', description='Books and educational materials'),
            Category(name='Home & Garden', description='Home improvement and gardening supplies')
        ]
        
        for category in default_categories:
            db.session.add(category)
        
        try:
            db.session.commit()
            print("Default categories created successfully")
        except Exception as e:
            db.session.rollback()
            print(f"Error creating default categories: {e}")

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'status': 'error',
        'message': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify({
        'status': 'error',
        'message': 'Internal server error'
    }), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```python
# database_setup.py - Database initialization and seeding script
from app import app, db, Customer, Category, Sale
from datetime import datetime, timedelta
import random

def init_database():
    """Initialize database with tables and sample data."""
    
    with app.app_context():
        # Drop and recreate all tables
        print("Dropping existing tables...")
        db.drop_all()
        
        print("Creating new tables...")
        db.create_all()
        
        # Create categories
        print("Creating categories...")
        categories = [
            Category(name='Electronics', description='Electronic devices and gadgets'),
            Category(name='Clothing', description='Apparel and fashion items'),
            Category(name='Books', description='Books and educational materials'),
            Category(name='Home & Garden', description='Home improvement and gardening supplies'),
            Category(name='Sports', description='Sports and fitness equipment'),
            Category(name='Beauty', description='Beauty and personal care products')
        ]
        
        for category in categories:
            db.session.add(category)
        
        db.session.commit()
        print(f"Created {len(categories)} categories")
        
        # Create customers
        print("Creating customers...")
        customers_data = [
            ('Alice Johnson', 'alice@example.com', 28),
            ('Bob Smith', 'bob@example.com', 35),
            ('Carol Williams', 'carol@example.com', 42),
            ('David Brown', 'david@example.com', 29),
            ('Eva Davis', 'eva@example.com', 31),
            ('Frank Wilson', 'frank@example.com', 26),
            ('Grace Miller', 'grace@example.com', 38),
            ('Henry Taylor', 'henry@example.com', 45),
            ('Ivy Anderson', 'ivy@example.com', 33),
            ('Jack Thompson', 'jack@example.com', 27)
        ]
        
        customers = []
        for name, email, age in customers_data:
            customer = Customer(name=name, email=email, age=age)
            customers.append(customer)
            db.session.add(customer)
        
        db.session.commit()
        print(f"Created {len(customers)} customers")
        
        # Create sales
        print("Creating sales...")
        sales_count = 50
        created_sales = []
        
        for i in range(sales_count):
            sale = Sale(
                customer_id=random.choice(customers).id,
                category_id=random.choice(categories).id,
                sale_amount=round(random.uniform(10.0, 500.0), 2),
                sale_date=datetime.utcnow() - timedelta(
                    days=random.randint(0, 90),
                    hours=random.randint(0, 23),
                    minutes=random.randint(0, 59)
                ),
                notes=f'Sample sale #{i+1}'
            )
            created_sales.append(sale)
            db.session.add(sale)
        
        db.session.commit()
        print(f"Created {len(created_sales)} sales")
        
        # Display summary
        print("\n" + "="*50)
        print("DATABASE INITIALIZATION COMPLETE")
        print("="*50)
        print(f"Categories: {Category.query.count()}")
        print(f"Customers: {Customer.query.count()}")
        print(f"Sales: {Sale.query.count()}")
        print(f"Total Revenue: ${sum(float(sale.sale_amount) for sale in Sale.query.all()):.2f}")
        print("="*50)

if __name__ == '__main__':
    init_database()
```

> ⚠️ **Common Mistake**: Not handling database transactions properly can lead to data inconsistency
</details>

### 🏃 Hands-on Activity
<details>
<summary>Activity: Convert Your Week 3 API to Use Database</summary>

#### Steps:
1. **Install Dependencies**: Add SQLAlchemy and database drivers to your project
2. **Design Models**: Convert your Week 3 in-memory data structures to SQLAlchemy models
3. **Update API Endpoints**: Modify your routes to use database operations instead of in-memory lists
4. **Add Error Handling**: Implement proper error handling for database operations
5. **Test Integration**: Verify all CRUD operations work with persistent data

#### Migration Checklist:
- [ ] SQLAlchemy models defined with proper relationships
- [ ] Database connection configured for development and production
- [ ] All API endpoints updated to use database operations
- [ ] Error handling implemented for database failures
- [ ] Data validation added to models
- [ ] Database indexes created for performance

> 📝 **Note**: Start with SQLite for development, then configure PostgreSQL for production
</details>

## 📖 Part 4: SQL vs NoSQL & Use Case Analysis
<!-- Understanding when to use different database types -->

### ⭐ Key Concepts
<details>
<summary>Database Types Comparison</summary>

- **SQL Databases (Relational)**
  - Structured data with defined schema
  - ACID compliance and data integrity
  - Complex queries with JOINs
  - Examples: PostgreSQL, MySQL, SQLite
- **NoSQL Databases**
  - Document stores (MongoDB, CouchDB)
  - Key-value stores (Redis, DynamoDB)
  - Column-family (Cassandra, HBase)
  - Graph databases (Neo4j, Amazon Neptune)
- **Hybrid Approaches**
  - NewSQL databases (CockroachDB, TiDB)
  - Multi-model databases (ArangoDB)
  - PostgreSQL with JSONB support

> 💡 **Key Point**: Choose the database type based on your data structure, consistency requirements, and scaling needs
</details>

### 💻 Use Case Analysis
<details>
<summary>Domain-Specific Database Choices</summary>

```python
# Use case examples and database recommendations

class DatabaseUseCase:
    """Analysis of different database use cases."""
    
    @staticmethod
    def web_application_backend():
        """Traditional web application with structured data."""
        return {
            'use_case': 'E-commerce, CRM, Financial Applications',
            'recommended_db': 'PostgreSQL or MySQL',
            'reasons': [
                'ACID compliance for transactions',
                'Complex relationships between entities',
                'Strong consistency requirements',
                'Mature ecosystem and tooling',
                'SQL expertise widely available'
            ],
            'example_schema': '''
            users (id, email, password_hash, created_at)
            orders (id, user_id, total, status, order_date)
            order_items (id, order_id, product_id, quantity, price)
            products (id, name, description, price, stock)
            ''',
            'sample_query': '''
            SELECT u.email, COUNT(o.id) as order_count, SUM(o.total) as total_spent
            FROM users u
            LEFT JOIN orders o ON u.id = o.user_id
            WHERE u.created_at >= '2024-01-01'
            GROUP BY u.id, u.email
            ORDER BY total_spent DESC;
            '''
        }
    
    @staticmethod
    def data_science_analytics():
        """Data science and analytics workloads."""
        return {
            'use_case': 'Data Warehousing, Business Intelligence, ML Feature Stores',
            'recommended_db': 'PostgreSQL + Extensions or Specialized (Snowflake, BigQuery)',
            'reasons': [
                'Complex analytical queries',
                'Time-series data support',
                'Statistical functions built-in',
                'Integration with Python/R ecosystems',
                'Columnar storage for analytics'
            ],
            'postgresql_extensions': [
                'TimescaleDB for time-series data',
                'PostGIS for geospatial analysis',
                'pg_stat_statements for query analytics',
                'MADlib for machine learning'
            ],
            'example_schema': '''
            events (timestamp, user_id, event_type, properties JSONB)
            user_features (user_id, feature_vector, updated_at)
            model_predictions (id, model_version, input_data, prediction, confidence)
            ''',
            'sample_query': '''
            WITH daily_metrics AS (
                SELECT 
                    DATE(timestamp) as date,
                    COUNT(*) as event_count,
                    COUNT(DISTINCT user_id) as unique_users,
                    AVG((properties->>'value')::numeric) as avg_value
                FROM events
                WHERE timestamp >= NOW() - INTERVAL '30 days'
                GROUP BY DATE(timestamp)
            )
            SELECT 
                date,
                event_count,
                unique_users,
                avg_value,
                LAG(event_count) OVER (ORDER BY date) as prev_day_events,
                (event_count - LAG(event_count) OVER (ORDER BY date)) / 
                LAG(event_count) OVER (ORDER BY date) * 100 as growth_rate
            FROM daily_metrics
            ORDER BY date;
            '''
        }
    
    @staticmethod
    def machine_learning_applications():
        """ML model serving and feature storage."""
        return {
            'use_case': 'Model Training, Feature Engineering, Real-time Predictions',
            'recommended_db': 'Hybrid: PostgreSQL + Redis + Vector Database',
            'reasons': [
                'Feature store capabilities',
                'Vector similarity search',
                'Real-time inference requirements',
                'Model versioning and metadata',
                'Training data lineage'
            ],
            'architecture': {
                'postgresql': 'Feature metadata, model registry, training logs',
                'redis': 'Real-time feature cache, model predictions',
                'vector_db': 'Embeddings, similarity search (Pinecone, Weaviate)',
                'object_storage': 'Model artifacts, training datasets (S3, GCS)'
            },
            'example_schema': '''
            -- PostgreSQL for metadata
            models (id, name, version, algorithm, metrics JSONB, created_at)
            features (id, name, data_type, description, last_updated)
            training_runs (id, model_id, dataset_version, hyperparams JSONB, results JSONB)
            
            -- Redis for caching
            user:123:features -> {"age": 25, "location": "NYC", "preferences": [...]}
            model:rec_engine:v2:prediction:user123 -> {"items": [1,5,9], "scores": [0.9,0.8,0.7]}
            ''',
            'python_example': '''
            import redis
            import json
            from sqlalchemy import create_engine
            
            # Feature store integration
            def get_user_features(user_id, use_cache=True):
                if use_cache:
                    cached = redis_client.get(f"user:{user_id}:features")
                    if cached:
                        return json.loads(cached)
                
                # Fallback to database
                features = db.session.execute(
                    "SELECT feature_name, feature_value FROM user_features WHERE user_id = %s",
                    (user_id,)
                ).fetchall()
                
                feature_dict = dict(features)
                redis_client.setex(f"user:{user_id}:features", 300, json.dumps(feature_dict))
                return feature_dict
            '''
        }
    
    @staticmethod
    def content_management_cms():
        """Content management and document storage."""
        return {
            'use_case': 'CMS, Blogs, Documentation, Content APIs',
            'recommended_db': 'MongoDB or PostgreSQL with JSONB',
            'reasons': [
                'Flexible document structure',
                'Nested data and arrays',
                'Full-text search capabilities',
                'Schema evolution over time',
                'Content versioning support'
            ],
            'mongodb_example': '''
            // Articles collection
            {
                "_id": ObjectId("..."),
                "title": "Database Selection Guide",
                "slug": "database-selection-guide",
                "content": {
                    "blocks": [
                        {"type": "paragraph", "text": "Introduction..."},
                        {"type": "code", "language": "sql", "code": "SELECT * FROM..."},
                        {"type": "image", "url": "...", "caption": "..."}
                    ]
                },
                "metadata": {
                    "author": "John Doe",
                    "tags": ["database", "sql", "nosql"],
                    "published_at": ISODate("2024-01-15"),
                    "status": "published"
                },
                "seo": {
                    "meta_description": "...",
                    "keywords": ["database", "sql"]
                }
            }
            ''',
            'postgresql_jsonb_example': '''
            CREATE TABLE articles (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                slug VARCHAR(255) UNIQUE NOT NULL,
                content JSONB NOT NULL,
                metadata JSONB NOT NULL,
                created_at TIMESTAMP DEFAULT NOW(),
                updated_at TIMESTAMP DEFAULT NOW()
            );
            
            CREATE INDEX idx_articles_metadata_tags ON articles USING GIN ((metadata->'tags'));
            CREATE INDEX idx_articles_content_search ON articles USING GIN (to_tsvector('english', content->>'text'));
            
            -- Query with JSONB
            SELECT title, metadata->'author' as author
            FROM articles
            WHERE metadata->'tags' ? 'database'
            AND metadata->>'status' = 'published'
            ORDER BY created_at DESC;
            '''
        }
    
    @staticmethod
    def real_time_applications():
        """Real-time applications and caching."""
        return {
            'use_case': 'Chat Applications, Gaming, Live Dashboards, Session Storage',
            'recommended_db': 'Redis + WebSocket + PostgreSQL',
            'reasons': [
                'Sub-millisecond response times',
                'In-memory data structures',
                'Pub/Sub messaging',
                'Session and cache management',
                'Real-time analytics'
            ],
            'redis_patterns': {
                'caching': 'Cache database queries and computed results',
                'sessions': 'Store user session data',
                'pub_sub': 'Real-time messaging and notifications',
                'rate_limiting': 'API rate limiting and throttling',
                'leaderboards': 'Sorted sets for rankings and scores'
            },
            'example_usage': '''
            # Python Redis examples
            import redis
            import json
            from datetime import datetime, timedelta
            
            r = redis.Redis(host='localhost', port=6379, decode_responses=True)
            
            # Caching pattern
            def get_user_data(user_id):
                cache_key = f"user:{user_id}"
                cached_data = r.get(cache_key)
                
                if cached_data:
                    return json.loads(cached_data)
                
                # Fetch from database
                user_data = fetch_from_database(user_id)
                r.setex(cache_key, 300, json.dumps(user_data))  # 5 min TTL
                return user_data
            
            # Real-time leaderboard
            def update_score(user_id, score):
                r.zadd("leaderboard", {user_id: score})
                
            def get_leaderboard(top_n=10):
                return r.zrevrange("leaderboard", 0, top_n-1, withscores=True)
            
            # Rate limiting
            def is_rate_limited(user_id, limit=100, window=3600):
                key = f"rate_limit:{user_id}:{datetime.now().hour}"
                current = r.incr(key)
                if current == 1:
                    r.expire(key, window)
                return current > limit
            '''
        }

# Comparison matrix
def create_comparison_matrix():
    """Create a comparison matrix for different database types."""
    
    comparison = {
        'criteria': [
            'ACID Compliance', 'Horizontal Scaling', 'Schema Flexibility',
            'Query Complexity', 'Consistency', 'Performance', 'Learning Curve'
        ],
        'databases': {
            'PostgreSQL': ['Excellent', 'Good', 'Limited', 'Excellent', 'Strong', 'Very Good', 'Medium'],
            'MongoDB': ['Good', 'Excellent', 'Excellent', 'Good', 'Eventual', 'Good', 'Low'],
            'Redis': ['Limited', 'Good', 'Excellent', 'Limited', 'Eventual', 'Excellent', 'Low'],
            'Cassandra': ['Limited', 'Excellent', 'Good', 'Limited', 'Eventual', 'Excellent', 'High'],
            'SQLite': ['Excellent', 'None', 'Limited', 'Good', 'Strong', 'Good', 'Low']
        }
    }
    
    return comparison

# Decision tree for database selection
def database_decision_tree():
    """Decision tree to help choose the right database."""
    
    questions = [
        {
            'question': 'Do you need ACID transactions?',
            'yes': 'Consider SQL databases (PostgreSQL, MySQL)',
            'no': 'Continue to next question'
        },
        {
            'question': 'Is your data structure highly flexible/changing?',
            'yes': 'Consider NoSQL (MongoDB, CouchDB)',
            'no': 'SQL databases are fine'
        },
        {
            'question': 'Do you need real-time performance (<1ms)?',
            'yes': 'Consider Redis or other in-memory stores',
            'no': 'Disk-based databases are fine'
        },
        {
            'question': 'Will you need complex queries and reporting?',
            'yes': 'SQL databases (PostgreSQL recommended)',
            'no': 'NoSQL or simple key-value stores'
        },
        {
            'question': 'Do you need to scale to multiple servers?',
            'yes': 'Consider distributed databases (MongoDB, Cassandra)',
            'no': 'Single-node databases (PostgreSQL, SQLite)'
        }
    ]
    
    return questions

if __name__ == "__main__":
    # Print use case analysis
    use_cases = [
        DatabaseUseCase.web_application_backend(),
        DatabaseUseCase.data_science_analytics(),
        DatabaseUseCase.machine_learning_applications(),
        DatabaseUseCase.content_management_cms(),
        DatabaseUseCase.real_time_applications()
    ]
    
    for i, use_case in enumerate(use_cases, 1):
        print(f"\n{'='*60}")
        print(f"USE CASE {i}: {use_case['use_case']}")
        print(f"{'='*60}")
        print(f"Recommended: {use_case['recommended_db']}")
        print("\nReasons:")
        for reason in use_case['reasons']:
            print(f"  • {reason}")
```

> ⚠️ **Common Mistake**: Choosing NoSQL just because it's "modern" without considering data relationships and consistency requirements
</details>

### 🏃 Hands-on Activity
<details>
<summary>Activity: Database Selection Analysis</summary>

#### Steps:
1. **Analyze Your Project**: Consider the data structure and requirements of your current project
2. **Compare Options**: Use the decision tree to evaluate different database types
3. **Prototype Testing**: Set up small tests with different databases
4. **Performance Comparison**: Compare query performance for your specific use case
5. **Document Decision**: Create a technical decision document explaining your choice

#### Analysis Framework:
```markdown
# Database Selection Analysis

## Project Requirements
- [ ] Data structure (relational vs document vs key-value)
- [ ] Consistency requirements (strong vs eventual)
- [ ] Query complexity (simple lookups vs complex joins)
- [ ] Scalability needs (single node vs distributed)
- [ ] Performance requirements (latency/throughput)

## Evaluation Matrix
| Criteria | PostgreSQL | MongoDB | Redis | Score |
|----------|------------|---------|-------|-------|
| ACID     | ✓         | ✓       | ✗     |       |
| Scaling  | ✓         | ✓✓      | ✓     |       |
| Queries  | ✓✓        | ✓       | ✗     |       |

## Final Recommendation
Based on analysis: [Your choice and reasoning]
```

> 📝 **Note**: Consider starting with PostgreSQL for most web applications - you can always add specialized databases later
</details>

### 💭 Discussion
<details>
<summary>Discussion Topics</summary>

- Key Question: How do different database types affect application architecture and development workflow?
- Follow-up Questions:
  - When would you choose eventual consistency over strong consistency?
  - How do you handle data migrations when changing database types?
  - What are the operational considerations for different database types?
</details>

## 📚 Additional Resources
<details>
<summary>Learning Materials</summary>

### Required Reading
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [SQLAlchemy Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)
- [Flask-SQLAlchemy Guide](https://flask-sqlalchemy.palletsprojects.com/)
- [SQL Tutorial](https://www.w3schools.com/sql/)
- [Database Design Best Practices](https://www.vertabelo.com/blog/database-design-best-practices/)

### Optional Further Reading
- [MongoDB Documentation](https://docs.mongodb.com/)
- [Redis Documentation](https://redis.io/documentation)
- [Database Internals Book](https://www.databass.dev/)
- [Use The Index, Luke! - SQL Performance](https://use-the-index-luke.com/)
- [CAP Theorem Explained](https://www.ibm.com/cloud/learn/cap-theorem)

### Tools and Extensions
- [DBeaver - Universal Database Tool](https://dbeaver.io/)
- [pgAdmin - PostgreSQL Administration](https://www.pgadmin.org/)
- [SQLTools VS Code Extension](https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools)
- [Adminer - Database Management](https://www.adminer.org/)
</details>

## 📋 Assignment Preview
<details>
<summary>Upcoming Tasks</summary>

Students will apply database integration concepts by:
- Converting their Week 3 REST API to use persistent database storage
- Designing and implementing proper database schemas with relationships
- Setting up development and production database environments
- Creating comprehensive API tests that include database operations
- Comparing performance between different database solutions for their use case
</details>

## ⏭️ Next Steps
<details>
<summary>Preparation for Week 5</summary>

- Install and configure all database tools and VS Code extensions
- Set up both SQLite (development) and PostgreSQL (production) environments
- Convert your Week 3 API to use database persistence
- Practice writing complex SQL queries for data analysis
- Prepare sample data for use in Week 5 data visualization exercises
</details>
