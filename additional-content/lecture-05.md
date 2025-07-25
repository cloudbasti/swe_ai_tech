# 📚 Week 05: Python Development Environment & Data Visualization

## 🎯 Learning Objectives
By the end of this lecture, students will be able to:
- Configure VS Code with essential Python extensions for development
- Use Jupyter notebooks for interactive data analysis with database data
- Create data visualizations with matplotlib using real database information
- Build web interfaces using Flask templates connected to databases
- Test REST APIs effectively using Postman with persistent data
- Integrate complete data science workflows with database-backed web development

## 🔧 Prerequisites
<details>
<summary>Required Setup & Knowledge</summary>

- VS Code installed
- Python environment from previous weeks
- Flask knowledge from Week 3
- **Database integration knowledge from Week 4**  
- **SQL basics and database connections**
- Basic understanding of REST APIs
- Command line familiarity
</details>

## 📖 Part 1: VS Code Python Development Setup
<!-- Setting up a professional Python development environment -->

### ⭐ Key Concepts
<details>
<summary>Essential VS Code Extensions</summary>

- **Core Python Extensions**
  - Python (Microsoft) - Official Python support
  - Pylance - Advanced language server with IntelliSense
  - Jupyter - Interactive notebook support
  - Python Debugger - Enhanced debugging capabilities
- **Code Quality Extensions**
  - Python Docstring Generator - Automatic documentation
  - autoDocstring - Smart docstring templates
  - Black Formatter - Consistent code formatting
  - isort - Import sorting and organization
- **Testing & Productivity**
  - Python Test Explorer - Visual test running
  - Python Environment Manager - Virtual environment management
  - GitLens - Enhanced Git integration
  - Thunder Client - API testing directly in VS Code
- **Database Extensions (from Week 4)**
  - SQLTools - Universal database client
  - PostgreSQL Explorer - PostgreSQL specific tools
  - SQLite Viewer - SQLite database browser

> 💡 **Key Point**: A well-configured development environment increases productivity and code quality significantly
</details>

### 💻 Installation & Configuration
<details>
<summary>Step-by-Step Setup</summary>

```bash
# Install essential extensions via command line
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-toolsai.jupyter
code --install-extension ms-python.debugpy
code --install-extension njpwerner.autodocstring
code --install-extension ms-python.black-formatter
code --install-extension ms-python.isort
code --install-extension ms-python.python-environment-manager
# Database extensions from Week 4
code --install-extension mtxr.sqltools
code --install-extension ms-ossdata.vscode-postgresql
```

```json
// VS Code settings.json configuration
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "python.sortImports.enabled": true,
    "jupyter.askForKernelRestart": false,
    "python.testing.autoTestDiscoverOnSaveEnabled": true,
    "[python]": {
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        }
    },
    "sqltools.connections": [
        {
            "name": "Local PostgreSQL",
            "driver": "PostgreSQL",
            "server": "localhost",
            "port": 5432,
            "database": "myapp_db",
            "username": "postgres"
        }
    ]
}
```

```python
# Sample Python file to test extensions with database integration
"""
This module demonstrates VS Code Python features with database connectivity.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine
import os


def create_sample_data(size: int = 100) -> np.ndarray:
    """
    Generate sample data for visualization.
    
    Args:
        size (int): Number of data points to generate
        
    Returns:
        np.ndarray: Array of random data points
    """
    return np.random.randn(size)


def load_data_from_database(connection_string: str) -> pd.DataFrame:
    """
    Load data from database for analysis.
    
    Args:
        connection_string (str): Database connection string
        
    Returns:
        pd.DataFrame: Loaded data from database
    """
    engine = create_engine(connection_string)
    query = "SELECT * FROM sales_data ORDER BY date DESC LIMIT 100"
    return pd.read_sql(query, engine)


if __name__ == "__main__":
    # Use database data if available, otherwise generate sample data
    try:
        db_url = os.getenv('DATABASE_URL', 'sqlite:///app.db')
        data_df = load_data_from_database(db_url)
        data = data_df['sales_amount'].values
        print(f"Loaded {len(data)} records from database")
    except Exception as e:
        print(f"Database connection failed: {e}")
        print("Using sample data instead")
        data = create_sample_data()
    
    plt.hist(data, bins=20)
    plt.title("Sales Data Distribution")
    plt.xlabel("Sales Amount")
    plt.ylabel("Frequency")
    plt.show()
```

> ⚠️ **Common Mistake**: Not configuring database connections properly leads to development issues
</details>

### 🏃 Hands-on Activity
<details>
<summary>Activity: Configure Your Full Development Environment</summary>

#### Steps:
1. **Install Extensions**: Use the command palette (`Ctrl+Shift+P`) to install all Python and database extensions
2. **Create Test Project**: Set up a new Python project with virtual environment and database connection
3. **Configure Settings**: Add the settings.json configuration including database connections
4. **Test Features**: 
   - Create a Python file and test autocompletion
   - Try debugging with breakpoints
   - Format code with Black formatter
   - Generate docstrings automatically
   - Test database connections using SQLTools

> 📝 **Note**: Restart VS Code after installing extensions and ensure your database from Week 4 is running
</details>

### 💭 Discussion
<details>
<summary>Discussion Topics</summary>

- Key Question: How do development tools impact code quality and team collaboration?
- Follow-up Questions:
  - Which extensions are most valuable for your workflow?
  - How does consistent formatting help in team projects?
  - How do database tools improve development efficiency?
</details>

## 📖 Part 2: Data Science with Database-Connected Python Libraries
<!-- Advanced data analysis using real database data -->

### ⭐ Key Concepts
<details>
<summary>Database-Integrated Data Science</summary>

- **NumPy with Database Data**
  - Loading numerical data from databases
  - Efficient array operations on database results
  - Memory management for large datasets
- **Matplotlib with Real Data**
  - Visualizing database query results
  - Time series plots from database timestamps
  - Interactive plots with real business data
- **Pandas Integration**
  - Direct SQL query execution
  - Data manipulation and cleaning
  - Database write-back capabilities
- **TensorFlow with Persistent Data**
  - Training models on database data
  - Model persistence and versioning
  - Production model deployment

> 💡 **Key Point**: Real database integration transforms data science from toy examples to production-ready analysis
</details>

### 💻 Implementation Examples
<details>
<summary>Database-Connected Data Analysis</summary>

```python
# Advanced data science with database integration
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from sqlalchemy import create_engine, text
from datetime import datetime, timedelta
import seaborn as sns

# Database connection setup
DATABASE_URL = "postgresql://username:password@localhost:5432/sales_db"
# For development: DATABASE_URL = "sqlite:///sales.db"

def setup_database_connection():
    """Setup database connection with error handling."""
    try:
        engine = create_engine(DATABASE_URL)
        # Test connection
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print("Database connection successful")
        return engine
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None

def load_sales_data(engine, days_back=30):
    """Load sales data from database for analysis."""
    query = """
    SELECT 
        DATE(sale_date) as date,
        product_category,
        SUM(sale_amount) as daily_sales,
        COUNT(*) as transaction_count,
        AVG(sale_amount) as avg_transaction
    FROM sales 
    WHERE sale_date >= %s
    GROUP BY DATE(sale_date), product_category
    ORDER BY date DESC, product_category
    """
    
    start_date = datetime.now() - timedelta(days=days_back)
    return pd.read_sql(query, engine, params=[start_date])

def create_advanced_visualizations(df):
    """Create comprehensive visualizations from database data."""
    
    # Set up the plotting style
    plt.style.use('seaborn-v0_8')
    fig = plt.figure(figsize=(16, 12))
    
    # 1. Time series analysis
    ax1 = plt.subplot(2, 3, 1)
    daily_totals = df.groupby('date')['daily_sales'].sum()
    ax1.plot(daily_totals.index, daily_totals.values, 'o-', linewidth=2)
    ax1.set_title('Daily Sales Trend', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Sales ($)')
    ax1.tick_params(axis='x', rotation=45)
    ax1.grid(True, alpha=0.3)
    
    # 2. Category performance
    ax2 = plt.subplot(2, 3, 2)
    category_sales = df.groupby('product_category')['daily_sales'].sum().sort_values(ascending=True)
    bars = ax2.barh(category_sales.index, category_sales.values)
    ax2.set_title('Sales by Category', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Total Sales ($)')
    
    # Color bars by performance
    colors = plt.cm.RdYlGn(np.linspace(0.2, 0.8, len(bars)))
    for bar, color in zip(bars, colors):
        bar.set_color(color)
    
    # 3. Transaction analysis
    ax3 = plt.subplot(2, 3, 3)
    ax3.scatter(df['transaction_count'], df['daily_sales'], 
               c=df['avg_transaction'], cmap='viridis', alpha=0.6, s=50)
    ax3.set_title('Sales vs Transaction Count', fontsize=14, fontweight='bold')
    ax3.set_xlabel('Number of Transactions')
    ax3.set_ylabel('Daily Sales ($)')
    plt.colorbar(ax3.collections[0], ax=ax3, label='Avg Transaction ($)')
    
    # 4. Distribution analysis
    ax4 = plt.subplot(2, 3, 4)
    ax4.hist(df['daily_sales'], bins=20, alpha=0.7, edgecolor='black')
    ax4.axvline(df['daily_sales'].mean(), color='red', linestyle='--', 
                label=f'Mean: ${df["daily_sales"].mean():.2f}')
    ax4.axvline(df['daily_sales'].median(), color='orange', linestyle='--', 
                label=f'Median: ${df["daily_sales"].median():.2f}')
    ax4.set_title('Sales Distribution', fontsize=14, fontweight='bold')
    ax4.set_xlabel('Daily Sales ($)')
    ax4.set_ylabel('Frequency')
    ax4.legend()
    
    # 5. Correlation heatmap
    ax5 = plt.subplot(2, 3, 5)
    correlation_data = df[['daily_sales', 'transaction_count', 'avg_transaction']].corr()
    im = ax5.imshow(correlation_data.values, cmap='coolwarm', aspect='auto')
    ax5.set_xticks(range(len(correlation_data.columns)))
    ax5.set_yticks(range(len(correlation_data.columns)))
    ax5.set_xticklabels(correlation_data.columns, rotation=45)
    ax5.set_yticklabels(correlation_data.columns)
    ax5.set_title('Correlation Matrix', fontsize=14, fontweight='bold')
    
    # Add correlation values
    for i in range(len(correlation_data.columns)):
        for j in range(len(correlation_data.columns)):
            text = ax5.text(j, i, f'{correlation_data.iloc[i, j]:.2f}',
                           ha="center", va="center", color="black", fontweight='bold')
    
    # 6. Trend analysis with moving average
    ax6 = plt.subplot(2, 3, 6)
    daily_totals_sorted = daily_totals.sort_index()
    
    # Calculate moving average
    window = min(7, len(daily_totals_sorted))  # 7-day moving average or available data
    moving_avg = daily_totals_sorted.rolling(window=window).mean()
    
    ax6.plot(daily_totals_sorted.index, daily_totals_sorted.values, 
             'o-', alpha=0.5, label='Daily Sales')
    ax6.plot(moving_avg.index, moving_avg.values, 
             'r-', linewidth=3, label=f'{window}-day Moving Average')
    ax6.set_title('Sales Trend with Moving Average', fontsize=14, fontweight='bold')
    ax6.set_xlabel('Date')
    ax6.set_ylabel('Sales ($)')
    ax6.legend()
    ax6.tick_params(axis='x', rotation=45)
    ax6.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('sales_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return fig

def predictive_modeling_with_database(engine):
    """Build predictive model using database data."""
    
    # Load expanded dataset for modeling
    query = """
    SELECT 
        EXTRACT(DOW FROM sale_date) as day_of_week,
        EXTRACT(HOUR FROM sale_date) as hour_of_day,
        product_category,
        sale_amount,
        customer_age,
        promotion_active::int as promotion
    FROM sales s
    JOIN customers c ON s.customer_id = c.id
    WHERE sale_date >= NOW() - INTERVAL '90 days'
    """
    
    df = pd.read_sql(query, engine)
    
    # Feature engineering
    categorical_features = pd.get_dummies(df['product_category'], prefix='category')
    features = pd.concat([
        df[['day_of_week', 'hour_of_day', 'customer_age', 'promotion']],
        categorical_features
    ], axis=1)
    
    target = df['sale_amount']
    
    # Split data
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=42
    )
    
    # Build TensorFlow model
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(X_train.shape[1],)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dense(1)
    ])
    
    model.compile(
        optimizer='adam',
        loss='mse',
        metrics=['mae']
    )
    
    # Train model
    history = model.fit(
        X_train, y_train,
        epochs=100,
        batch_size=32,
        validation_data=(X_test, y_test),
        verbose=0
    )
    
    # Visualize training results
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 2, 1)
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title('Model Loss Over Time')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(history.history['mae'], label='Training MAE')
    plt.plot(history.history['val_mae'], label='Validation MAE')
    plt.title('Model MAE Over Time')
    plt.xlabel('Epoch')
    plt.ylabel('Mean Absolute Error')
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    # Make predictions and evaluate
    predictions = model.predict(X_test)
    
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, predictions, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel('Actual Sales Amount')
    plt.ylabel('Predicted Sales Amount')
    plt.title('Actual vs Predicted Sales')
    plt.show()
    
    return model, history

def save_analysis_to_database(engine, analysis_results):
    """Save analysis results back to database."""
    
    results_df = pd.DataFrame({
        'analysis_date': [datetime.now()],
        'total_sales': [analysis_results['total_sales']],
        'avg_daily_sales': [analysis_results['avg_daily_sales']],
        'best_category': [analysis_results['best_category']],
        'model_accuracy': [analysis_results['model_mae']]
    })
    
    results_df.to_sql('analysis_results', engine, if_exists='append', index=False)
    print("Analysis results saved to database")

# Main execution
if __name__ == "__main__":
    # Setup database connection
    engine = setup_database_connection()
    
    if engine:
        # Load and analyze data
        sales_df = load_sales_data(engine, days_back=30)
        print(f"Loaded {len(sales_df)} records for analysis")
        
        # Create visualizations
        create_advanced_visualizations(sales_df)
        
        # Build predictive model
        model, history = predictive_modeling_with_database(engine)
        
        # Prepare analysis results
        analysis_results = {
            'total_sales': sales_df['daily_sales'].sum(),
            'avg_daily_sales': sales_df['daily_sales'].mean(),
            'best_category': sales_df.groupby('product_category')['daily_sales'].sum().idxmax(),
            'model_mae': min(history.history['val_mae'])
        }
        
        # Save results back to database
        save_analysis_to_database(engine, analysis_results)
        
        print("Analysis complete!")
    else:
        print("Cannot proceed without database connection")
```

> ⚠️ **Common Mistake**: Not handling database connection failures gracefully in data science workflows
</details>

### 🏃 Hands-on Activity
<details>
<summary>Activity: Real Data Analysis Pipeline</summary>

#### Prerequisites:
```bash
pip install numpy matplotlib pandas tensorflow sqlalchemy psycopg2-binary seaborn scikit-learn
```

#### Steps:
1. **Connect to Your Week 4 Database**: Use the database you set up in the previous lecture
2. **Load Real Data**: Query your database for analysis
3. **Create Advanced Visualizations**: Build comprehensive dashboards from database data
4. **Predictive Modeling**: Train ML models on your database data
5. **Save Results**: Write analysis results back to the database

#### Sample Project Structure:
```python
# analysis_pipeline.py
from database_analysis import (
    setup_database_connection,
    load_sales_data,
    create_advanced_visualizations,
    predictive_modeling_with_database
)

def main():
    engine = setup_database_connection()
    data = load_sales_data(engine)
    create_advanced_visualizations(data)
    model, history = predictive_modeling_with_database(engine)
    print("Analysis pipeline complete!")

if __name__ == "__main__":
    main()
```

> 📝 **Note**: Use Jupyter notebooks for exploration, then convert successful analysis to Python scripts for production
</details>

## 📖 Part 3: Flask Templating with Database Integration
<!-- Building dynamic web interfaces with persistent data -->

### ⭐ Key Concepts
<details>
<summary>Database-Driven Web Applications</summary>

- **Database-Connected Templates**
  - Real-time data rendering from database queries
  - Efficient query optimization for web performance
  - Caching strategies for frequently accessed data
- **Advanced Jinja2 Features**
  - Custom filters for database data formatting
  - Template macros for repeated database operations
  - Context processors for global database data
- **Performance Optimization**
  - Query optimization for template rendering
  - Pagination for large datasets
  - Lazy loading and caching strategies

> 💡 **Key Point**: Database integration transforms static templates into dynamic, data-driven web applications
</details>

### 💻 Implementation Examples
<details>
<summary>Database-Connected Flask Application</summary>

```python
# app.py - Complete database-integrated Flask application
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, text
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
from datetime import datetime, timedelta
import pandas as pd

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/sales_db'
# For development: app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sales.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models (from Week 4)
class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sale_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    product_category = db.Column(db.String(100), nullable=False)
    sale_amount = db.Column(db.Float, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sales = db.relationship('Sale', backref='customer', lazy=True)

# Custom Jinja2 filters
@app.template_filter('currency')
def currency_filter(amount):
    """Format currency values."""
    return f"${amount:,.2f}"

@app.template_filter('percentage')
def percentage_filter(value):
    """Format percentage values."""
    return f"{value:.1f}%"

@app.template_filter('datetime_format')
def datetime_format(value, format='%Y-%m-%d'):
    """Format datetime values."""
    return value.strftime(format)

# Context processor for global data
@app.context_processor
def inject_global_data():
    """Inject commonly used data into all templates."""
    total_sales = db.session.query(func.sum(Sale.sale_amount)).scalar() or 0
    total_customers = Customer.query.count()
    
    return {
        'global_stats': {
            'total_sales': total_sales,
            'total_customers': total_customers,
            'current_year': datetime.now().year
        }
    }

@app.route('/')
def index():
    """Enhanced homepage with database insights."""
    
    # Recent sales activity
    recent_sales = db.session.query(
        Sale.sale_date,
        Sale.product_category,
        Sale.sale_amount,
        Customer.name
    ).join(Customer).order_by(Sale.sale_date.desc()).limit(10).all()
    
    # Top performing categories
    top_categories = db.session.query(
        Sale.product_category,
        func.sum(Sale.sale_amount).label('total_sales'),
        func.count(Sale.id).label('transaction_count')
    ).group_by(Sale.product_category).order_by(func.sum(Sale.sale_amount).desc()).limit(5).all()
    
    # Sales trend (last 7 days)
    week_ago = datetime.now() - timedelta(days=7)
    daily_sales = db.session.query(
        func.date(Sale.sale_date).label('date'),
        func.sum(Sale.sale_amount).label('daily_total')
    ).filter(Sale.sale_date >= week_ago).group_by(func.date(Sale.sale_date)).all()
    
    return render_template('index.html', 
                         recent_sales=recent_sales,
                         top_categories=top_categories,
                         daily_sales=daily_sales)

@app.route('/dashboard')
def dashboard():
    """Comprehensive dashboard with database analytics."""
    
    # Time period filter
    days_back = request.args.get('days', 30, type=int)
    start_date = datetime.now() - timedelta(days=days_back)
    
    # Sales analytics
    sales_query = db.session.query(
        func.date(Sale.sale_date).label('date'),
        Sale.product_category,
        func.sum(Sale.sale_amount).label('daily_sales'),
        func.count(Sale.id).label('transaction_count'),
        func.avg(Sale.sale_amount).label('avg_transaction')
    ).filter(Sale.sale_date >= start_date).group_by(
        func.date(Sale.sale_date), Sale.product_category
    ).all()
    
    # Convert to DataFrame for analysis
    sales_data = pd.DataFrame([{
        'date': row.date,
        'category': row.product_category,
        'daily_sales': float(row.daily_sales),
        'transaction_count': row.transaction_count,
        'avg_transaction': float(row.avg_transaction)
    } for row in sales_query])
    
    if not sales_data.empty:
        # Calculate statistics
        stats = {
            'total_sales': sales_data['daily_sales'].sum(),
            'avg_daily_sales': sales_data['daily_sales'].mean(),
            'best_day': sales_data.loc[sales_data['daily_sales'].idxmax()],
            'growth_rate': calculate_growth_rate(sales_data)
        }
        
        # Category performance
        category_stats = sales_data.groupby('category').agg({
            'daily_sales': 'sum',
            'transaction_count': 'sum',
            'avg_transaction': 'mean'
        }).round(2).to_dict('index')
        
        # Chart data for frontend
        chart_data = prepare_chart_data(sales_data)
    else:
        stats = {'total_sales': 0, 'avg_daily_sales': 0, 'best_day': None, 'growth_rate': 0}
        category_stats = {}
        chart_data = {'labels': [], 'datasets': []}
    
    return render_template('dashboard.html',
                         stats=stats,
                         category_stats=category_stats,
                         chart_data=chart_data,
                         days_back=days_back)

@app.route('/customers')
def customers():
    """Customer management with pagination."""
    
    page = request.args.get('page', 1, type=int)
    per_page = 20
    
    # Customer data with sales summary
    customers_query = db.session.query(
        Customer.id,
        Customer.name,
        Customer.email,
        Customer.age,
        func.count(Sale.id).label('total_purchases'),
        func.sum(Sale.sale_amount).label('total_spent'),
        func.max(Sale.sale_date).label('last_purchase')
    ).outerjoin(Sale).group_by(Customer.id).order_by(Customer.name)
    
    customers = customers_query.paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return render_template('customers.html', customers=customers)

@app.route('/analytics')
def analytics():
    """Advanced analytics page with machine learning insights."""
    
    # Get prediction results from database (saved by data science pipeline)
    predictions = db.session.execute(text("""
        SELECT analysis_date, model_accuracy, total_sales, best_category
        FROM analysis_results 
        ORDER BY analysis_date DESC 
        LIMIT 10
    """)).fetchall()
    
    # Customer segmentation
    customer_segments = db.session.execute(text("""
        WITH customer_stats AS (
            SELECT 
                c.id,
                c.name,
                COUNT(s.id) as purchase_count,
                SUM(s.sale_amount) as total_spent,
                AVG(s.sale_amount) as avg_purchase
            FROM customers c
            LEFT JOIN sales s ON c.id = s.customer_id
            GROUP BY c.id, c.name
        )
        SELECT 
            CASE 
                WHEN total_spent > 1000 THEN 'High Value'
                WHEN total_spent > 500 THEN 'Medium Value'
                ELSE 'Low Value'
            END as segment,
            COUNT(*) as customer_count,
            AVG(total_spent) as avg_spent
        FROM customer_stats
        GROUP BY segment
    """)).fetchall()
    
    return render_template('analytics.html', 
                         predictions=predictions,
                         customer_segments=customer_segments)

def calculate_growth_rate(sales_data):
    """Calculate sales growth rate."""
    if len(sales_data) < 2:
        return 0
    
    daily_totals = sales_data.groupby('date')['daily_sales'].sum().sort_index()
    if len(daily_totals) < 2:
        return 0
    
    first_week = daily_totals.iloc[:len(daily_totals)//2].mean()
    second_week = daily_totals.iloc[len(daily_totals)//2:].mean()
    
    if first_week == 0:
        return 0
    
    return ((second_week - first_week) / first_week) * 100

def prepare_chart_data(sales_data):
    """Prepare data for frontend charts."""
    
    # Daily sales trend
    daily_totals = sales_data.groupby('date')['daily_sales'].sum().sort_index()
    
    # Category breakdown
    category_totals = sales_data.groupby('category')['daily_sales'].sum()
    
    return {
        'daily_sales': {
            'labels': [date.strftime('%Y-%m-%d') for date in daily_totals.index],
            'data': daily_totals.values.tolist()
        },
        'category_breakdown': {
            'labels': category_totals.index.tolist(),
            'data': category_totals.values.tolist()
        }
    }

# API endpoints with database integration
@app.route('/api/sales/summary')
def api_sales_summary():
    """API endpoint for sales summary."""
    
    days_back = request.args.get('days', 30, type=int)
    start_date = datetime.now() - timedelta(days=days_back)
    
    summary = db.session.query(
        func.sum(Sale.sale_amount).label('total_sales'),
        func.count(Sale.id).label('total_transactions'),
        func.avg(Sale.sale_amount).label('avg_transaction')
    ).filter(Sale.sale_date >= start_date).first()
    
    return jsonify({
        'status': 'success',
        'data': {
            'total_sales': float(summary.total_sales or 0),
            'total_transactions': summary.total_transactions or 0,
            'avg_transaction': float(summary.avg_transaction or 0),
            'period_days': days_back
        },
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/dashboard.html - Enhanced with database data -->
{% extends "base.html" %}

{% block title %}Sales Dashboard - {{ global_stats.total_sales|currency }} Total{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-12">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h2>Sales Analytics Dashboard</h2>
            <div class="btn-group" role="group">
                <a href="{{ url_for('dashboard', days=7) }}" 
                   class="btn btn-outline-primary {{ 'active' if days_back == 7 }}">7 Days</a>
                <a href="{{ url_for('dashboard', days=30) }}" 
                   class="btn btn-outline-primary {{ 'active' if days_back == 30 }}">30 Days</a>
                <a href="{{ url_for('dashboard', days=90) }}" 
                   class="btn btn-outline-primary {{ 'active' if days_back == 90 }}">90 Days</a>
            </div>
        </div>
    </div>
</div>

<!-- Key Metrics Cards -->
<div class="row mb-4">
    <div class="col-md-3">
        <div class="card border-primary">
            <div class="card-body text-center">
                <h5 class="card-title text-primary">Total Sales</h5>
                <h3 class="card-text">{{ stats.total_sales|currency }}</h3>
                <small class="text-muted">Last {{ days_back }} days</small>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card border-success">
            <div class="card-body text-center">
                <h5 class="card-title text-success">Avg Daily Sales</h5>
                <h3 class="card-text">{{ stats.avg_daily_sales|currency }}</h3>
                <small class="text-muted">Per day average</small>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card border-info">
            <div class="card-body text-center">
                <h5 class="card-title text-info">Growth Rate</h5>
                <h3 class="card-text {{ 'text-success' if stats.growth_rate > 0 else 'text-danger' }}">
                    {{ stats.growth_rate|percentage }}
                </h3>
                <small class="text-muted">Period over period</small>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card border-warning">
            <div class="card-body text-center">
                <h5 class="card-title text-warning">Best Day</h5>
                {% if stats.best_day %}
                <h6 class="card-text">{{ stats.best_day.date|datetime_format }}</h6>
                <p class="card-text">{{ stats.best_day.daily_sales|currency }}</p>
                {% else %}
                <p class="card-text">No data available</p>
                {% endif %}
            </div>
        </div>
    </div>
</div>

<!-- Charts Row -->
<div class="row">
    <div class="col-md-8">
        <div class="card">
            <div class="card-header">
                <h5>Daily Sales Trend</h5>
            </div>
            <div class="card-body">
                <canvas id="salesTrendChart" height="100"></canvas>
            </div>
        </div>
    </div>
    <div class="col-md-4">
        <div class="card">
            <div class="card-header">
                <h5>Category Breakdown</h5>
            </div>
            <div class="card-body">
                <canvas id="categoryChart" height="200"></canvas>
            </div>
        </div>
    </div>
</div>

<!-- Category Performance Table -->
<div class="row mt-4">
    <div class="col-md-12">
        <div class="card">
            <div class="card-header">
                <h5>Category Performance</h5>
            </div>
            <div class="card-body">
                <div class="table-responsive">
                    <table class="table table-hover">
                        <thead>
                            <tr>
                                <th>Category</th>
                                <th>Total Sales</th>
                                <th>Transactions</th>
                                <th>Avg Transaction</th>
                                <th>Performance</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for category, data in category_stats.items() %}
                            <tr>
                                <td><strong>{{ category }}</strong></td>
                                <td>{{ data.daily_sales|currency }}</td>
                                <td>{{ data.transaction_count }}</td>
                                <td>{{ data.avg_transaction|currency }}</td>
                                <td>
                                    {% set percentage = (data.daily_sales / stats.total_sales * 100) if stats.total_sales > 0 else 0 %}
                                    <div class="progress" style="height: 20px;">
                                        <div class="progress-bar" role="progressbar" 
                                             style="width: {{ percentage }}%" 
                                             aria-valuenow="{{ percentage }}" 
                                             aria-valuemin="0" aria-valuemax="100">
                                            {{ percentage|percentage }}
                                        </div>
                                    </div>
                                </td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
    // Sales Trend Chart
    const trendCtx = document.getElementById('salesTrendChart').getContext('2d');
    const salesTrendChart = new Chart(trendCtx, {
        type: 'line',
        data: {
            labels: {{ chart_data.daily_sales.labels | tojsonfilter }},
            datasets: [{
                label: 'Daily Sales',
                data: {{ chart_data.daily_sales.data | tojsonfilter }},
                borderColor: 'rgb(54, 162, 235)',
                backgroundColor: 'rgba(54, 162, 235, 0.1)',
                tension: 0.2,
                fill: true
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: function(value) {
                            return '$' + value.toLocaleString();
                        }
                    }
                }
            }
        }
    });

    // Category Breakdown Chart
    const categoryCtx = document.getElementById('categoryChart').getContext('2d');
    const categoryChart = new Chart(categoryCtx, {
        type: 'doughnut',
        data: {
            labels: {{ chart_data.category_breakdown.labels | tojsonfilter }},
            datasets: [{
                data: {{ chart_data.category_breakdown.data | tojsonfilter }},
                backgroundColor: [
                    '#FF6384',
                    '#36A2EB',
                    '#FFCE56',
                    '#4BC0C0',
                    '#9966FF',
                    '#FF9F40'
                ]
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            }
        }
    });

    // Auto-refresh dashboard every 5 minutes
    setTimeout(function() {
        location.reload();
    }, 300000);
</script>
{% endblock %}
```

> ⚠️ **Common Mistake**: Not optimizing database queries for web performance can lead to slow page loads
</details>

### 🏃 Hands-on Activity
<details>
<summary>Activity: Build Production-Ready Dashboard</summary>

#### Steps:
1. **Connect Flask to Your Database**: Use SQLAlchemy with your Week 4 database
2. **Create Advanced Templates**: Build responsive templates with real-time data
3. **Optimize Performance**: Add caching and query optimization
4. **Add Interactivity**: Implement filtering, sorting, and pagination
5. **Mobile Responsiveness**: Ensure dashboard works on all devices

#### Dashboard Features to Implement:
- [ ] Real-time data updates
- [ ] Interactive charts with drill-down capability
- [ ] Export functionality (PDF, CSV)
- [ ] User authentication and permissions
- [ ] Performance monitoring and alerts

> 📝 **Note**: Focus on user experience and data visualization best practices
</details>

## 📖 Part 4: Advanced API Testing with Database Integration
<!-- Comprehensive testing of database-backed APIs -->

### ⭐ Key Concepts
<details>
<summary>Database-Aware API Testing</summary>

- **Data-Driven Testing**
  - Testing with real database scenarios
  - Transaction rollback for clean test environments
  - Data validation and integrity testing
- **Performance Testing with Load**
  - Database connection pooling under load
  - Query performance optimization
  - Memory usage monitoring
- **Integration Testing**
  - End-to-end workflow testing
  - Cross-service data consistency
  - Error handling with database failures

> 💡 **Key Point**: Database integration requires comprehensive testing of data flows, performance, and error scenarios
</details>

### 💻 Advanced Testing Implementation
<details>
<summary>Comprehensive API Testing Suite</summary>

```json
{
    "info": {
        "name": "Database-Integrated Sales API",
        "description": "Comprehensive testing of Flask API with PostgreSQL backend"
    },
    "variable": [
        {
            "key": "base_url",
            "value": "http://localhost:5000"
        },
        {
            "key": "test_customer_id",
            "value": ""
        }
    ],
    "item": [
        {
            "name": "Health Check - Database Connection",
            "request": {
                "method": "GET",
                "header": [],
                "url": {
                    "raw": "{{base_url}}/api/health",
                    "host": ["{{base_url}}"],
                    "path": ["api", "health"]
                }
            },
            "event": [
                {
                    "listen": "test",
                    "script": {
                        "exec": [
                            "pm.test('Database connection is healthy', function () {",
                            "    pm.response.to.have.status(200);",
                            "    const jsonData = pm.response.json();",
                            "    pm.expect(jsonData.database_status).to.eql('connected');",
                            "});"
                        ]
                    }
                }
            ]
        },
        {
            "name": "Create Test Customer",
            "request": {
                "method": "POST",
                "header": [
                    {
                        "key": "Content-Type",
                        "value": "application/json"
                    }
                ],
                "body": {
                    "mode": "raw",
                    "raw": "{\n    \"name\": \"Test Customer {{ $randomFirstName }}\",\n    \"email\": \"test{{ $randomInt }}@example.com\",\n    \"age\": {{ $randomInt }}\n}"
                },
                "url": {
                    "raw": "{{base_url}}/api/customers",
                    "host": ["{{base_url}}"],
                    "path": ["api", "customers"]
                }
            },
            "event": [
                {
                    "listen": "test",
                    "script": {
                        "exec": [
                            "pm.test('Customer created successfully', function () {",
                            "    pm.response.to.have.status(201);",
                            "    const jsonData = pm.response.json();",
                            "    pm.expect(jsonData.status).to.eql('success');",
                            "    pm.expect(jsonData.data).to.have.property('id');",
                            "    ",
                            "    // Store customer ID for subsequent tests",
                            "    pm.globals.set('test_customer_id', jsonData.data.id);",
                            "});",
                            "",
                            "pm.test('Database transaction successful', function () {",
                            "    const jsonData = pm.response.json();",
                            "    pm.expect(jsonData.data.id).to.be.a('number');",
                            "    pm.expect(jsonData.data.id).to.be.above(0);",
                            "});"
                        ]
                    }
                }
            ]
        },
        {
            "name": "Create Multiple Sales - Load Test",
            "request": {
                "method": "POST",
                "header": [
                    {
                        "key": "Content-Type",
                        "value": "application/json"
                    }
                ],
                "body": {
                    "mode": "raw",
                    "raw": "{\n    \"customer_id\": {{test_customer_id}},\n    \"product_category\": \"Electronics\",\n    \"sale_amount\": {{ $randomInt }}.99\n}"
                },
                "url": {
                    "raw": "{{base_url}}/api/sales",
                    "host": ["{{base_url}}"],
                    "path": ["api", "sales"]
                }
            },
            "event": [
                {
                    "listen": "test",
                    "script": {
                        "exec": [
                            "pm.test('Sale created with database persistence', function () {",
                            "    pm.response.to.have.status(201);",
                            "    const jsonData = pm.response.json();",
                            "    pm.expect(jsonData.data).to.have.property('id');",
                            "    pm.expect(jsonData.data.customer_id).to.eql(parseInt(pm.globals.get('test_customer_id')));",
                            "});",
                            "",
                            "pm.test('Response time acceptable for database write', function () {",
                            "    pm.expect(pm.response.responseTime).to.be.below(1000);",
                            "});"
                        ]
                    }
                }
            ]
        },
        {
            "name": "Get Sales Analytics - Complex Query",
            "request": {
                "method": "GET",
                "header": [],
                "url": {
                    "raw": "{{base_url}}/api/sales/analytics?customer_id={{test_customer_id}}&days=30",
                    "host": ["{{base_url}}"],
                    "path": ["api", "sales", "analytics"],
                    "query": [
                        {
                            "key": "customer_id",
                            "value": "{{test_customer_id}}"
                        },
                        {
                            "key": "days",
                            "value": "30"
                        }
                    ]
                }
            },
            "event": [
                {
                    "listen": "test",
                    "script": {
                        "exec": [
                            "pm.test('Analytics query executed successfully', function () {",
                            "    pm.response.to.have.status(200);",
                            "    const jsonData = pm.response.json();",
                            "    pm.expect(jsonData.data).to.have.property('total_sales');",
                            "    pm.expect(jsonData.data).to.have.property('transaction_count');",
                            "});",
                            "",
                            "pm.test('Complex query performance acceptable', function () {",
                            "    pm.expect(pm.response.responseTime).to.be.below(2000);",
                            "});",
                            "",
                            "pm.test('Data consistency check', function () {",
                            "    const jsonData = pm.response.json();",
                            "    if (jsonData.data.transaction_count > 0) {",
                            "        pm.expect(jsonData.data.total_sales).to.be.above(0);",
                            "    }",
                            "});"
                        ]
                    }
                }
            ]
        },
        {
            "name": "Test Database Constraints - Duplicate Email",
            "request": {
                "method": "POST",
                "header": [
                    {
                        "key": "Content-Type",
                        "value": "application/json"
                    }
                ],
                "body": {
                    "mode": "raw",
                    "raw": "{\n    \"name\": \"Duplicate Customer\",\n    \"email\": \"test@example.com\",\n    \"age\": 25\n}"
                },
                "url": {
                    "raw": "{{base_url}}/api/customers",
                    "host": ["{{base_url}}"],
                    "path": ["api", "customers"]
                }
            },
            "event": [
                {
                    "listen": "test",
                    "script": {
                        "exec": [
                            "pm.test('Database constraint properly enforced', function () {",
                            "    pm.response.to.have.status(400);",
                            "    const jsonData = pm.response.json();",
                            "    pm.expect(jsonData.status).to.eql('error');",
                            "    pm.expect(jsonData.message).to.include('email');",
                            "});"
                        ]
                    }
                }
            ]
        },
        {
            "name": "Test Transaction Rollback - Invalid Sale",
            "request": {
                "method": "POST",
                "header": [
                    {
                        "key": "Content-Type",
                        "value": "application/json"
                    }
                ],
                "body": {
                    "mode": "raw",
                    "raw": "{\n    \"customer_id\": 999999,\n    \"product_category\": \"Electronics\",\n    \"sale_amount\": 100.00\n}"
                },
                "url": {
                    "raw": "{{base_url}}/api/sales",
                    "host": ["{{base_url}}"],
                    "path": ["api", "sales"]
                }
            },
            "event": [
                {
                    "listen": "test",
                    "script": {
                        "exec": [
                            "pm.test('Foreign key constraint properly handled', function () {",
                            "    pm.response.to.have.status(400);",
                            "    const jsonData = pm.response.json();",
                            "    pm.expect(jsonData.status).to.eql('error');",
                            "    pm.expect(jsonData.message).to.include('customer');",
                            "});"
                        ]
                    }
                }
            ]
        },
        {
            "name": "Cleanup - Delete Test Customer",
            "request": {
                "method": "DELETE",
                "header": [],
                "url": {
                    "raw": "{{base_url}}/api/customers/{{test_customer_id}}",
                    "host": ["{{base_url}}"],
                    "path": ["api", "customers", "{{test_customer_id}}"]
                }
            },
            "event": [
                {
                    "listen": "test",
                    "script": {
                        "exec": [
                            "pm.test('Cleanup successful - cascade delete working', function () {",
                            "    pm.response.to.have.status(200);",
                            "    const jsonData = pm.response.json();",
                            "    pm.expect(jsonData.status).to.eql('success');",
                            "});",
                            "",
                            "// Verify cascade delete worked",
                            "pm.sendRequest({",
                            "    url: pm.variables.get('base_url') + '/api/sales/analytics?customer_id=' + pm.globals.get('test_customer_id'),",
                            "    method: 'GET'",
                            "}, function (err, response) {",
                            "    pm.test('Cascade delete verification', function () {",
                            "        const jsonData = response.json();",
                            "        pm.expect(jsonData.data.transaction_count).to.eql(0);",
                            "    });",
                            "});"
                        ]
                    }
                }
            ]
        }
    ]
}
```

```python
# Advanced database testing with Python
import requests
import threading
import time
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt

class DatabaseAPITester:
    def __init__(self, base_url, db_connection_string):
        self.base_url = base_url
        self.db_engine = create_engine(db_connection_string)
        self.response_times = []
        self.error_count = 0
        
    def test_concurrent_database_operations(self, num_threads=10, operations_per_thread=50):
        """Test API under concurrent database load."""
        
        print(f"Starting concurrent test: {num_threads} threads, {operations_per_thread} ops each")
        
        def worker_thread(thread_id):
            thread_response_times = []
            thread_errors = 0
            
            for i in range(operations_per_thread):
                start_time = time.time()
                
                try:
                    # Create customer
                    customer_data = {
                        "name": f"LoadTest-{thread_id}-{i}",
                        "email": f"loadtest{thread_id}{i}@example.com",
                        "age": 25 + (i % 50)
                    }
                    
                    response = requests.post(
                        f"{self.base_url}/api/customers",
                        json=customer_data,
                        timeout=10
                    )
                    
                    if response.status_code == 201:
                        customer_id = response.json()['data']['id']
                        
                        # Create sale
                        sale_data = {
                            "customer_id": customer_id,
                            "product_category": "Electronics",
                            "sale_amount": 100.0 + (i * 10)
                        }
                        
                        sale_response = requests.post(
                            f"{self.base_url}/api/sales",
                            json=sale_data,
                            timeout=10
                        )
                        
                        # Clean up
                        requests.delete(f"{self.base_url}/api/customers/{customer_id}")
                        
                    response_time = time.time() - start_time
                    thread_response_times.append(response_time)
                    
                except Exception as e:
                    thread_errors += 1
                    print(f"Thread {thread_id}, Operation {i}: Error - {e}")
            
            # Store results
            self.response_times.extend(thread_response_times)
            self.error_count += thread_errors
            print(f"Thread {thread_id} completed: Avg response time: {sum(thread_response_times)/len(thread_response_times):.3f}s")
        
        # Start all threads
        threads = []
        start_time = time.time()
        
        for i in range(num_threads):
            thread = threading.Thread(target=worker_thread, args=(i,))
            threads.append(thread)
            thread.start()
        
        # Wait for completion
        for thread in threads:
            thread.join()
        
        total_time = time.time() - start_time
        
        # Generate report
        self.generate_performance_report(total_time, num_threads * operations_per_thread)
    
    def generate_performance_report(self, total_time, total_operations):
        """Generate comprehensive performance report."""
        
        if self.response_times:
            avg_response_time = sum(self.response_times) / len(self.response_times)
            min_response_time = min(self.response_times)
            max_response_time = max(self.response_times)
            
            # Calculate percentiles
            sorted_times = sorted(self.response_times)
            p95 = sorted_times[int(0.95 * len(sorted_times))]
            p99 = sorted_times[int(0.99 * len(sorted_times))]
            
            print("\n" + "="*50)
            print("PERFORMANCE TEST RESULTS")
            print("="*50)
            print(f"Total Operations: {total_operations}")
            print(f"Total Time: {total_time:.2f} seconds")
            print(f"Operations/Second: {total_operations/total_time:.2f}")
            print(f"Error Rate: {(self.error_count/total_operations)*100:.2f}%")
            print(f"Average Response Time: {avg_response_time:.3f}s")
            print(f"Min Response Time: {min_response_time:.3f}s")
            print(f"Max Response Time: {max_response_time:.3f}s")
            print(f"95th Percentile: {p95:.3f}s")
            print(f"99th Percentile: {p99:.3f}s")
            
            # Generate performance visualization
            plt.figure(figsize=(15, 5))
            
            # Response time distribution
            plt.subplot(1, 3, 1)
            plt.hist(self.response_times, bins=50, alpha=0.7, edgecolor='black')
            plt.axvline(avg_response_time, color='red', linestyle='--', label=f'Avg: {avg_response_time:.3f}s')
            plt.axvline(p95, color='orange', linestyle='--', label=f'95%: {p95:.3f}s')
            plt.title('Response Time Distribution')
            plt.xlabel('Response Time (seconds)')
            plt.ylabel('Frequency')
            plt.legend()
            
            # Response time over time
            plt.subplot(1, 3, 2)
            plt.plot(range(len(self.response_times)), self.response_times, alpha=0.6)
            plt.title('Response Time Over Time')
            plt.xlabel('Request Number')
            plt.ylabel('Response Time (seconds)')
            plt.axhline(avg_response_time, color='red', linestyle='--', alpha=0.7)
            
            # Database connection analysis
            plt.subplot(1, 3, 3)
            connection_query = """
            SELECT 
                state,
                COUNT(*) as connection_count
            FROM pg_stat_activity 
            WHERE datname = 'sales_db'
            GROUP BY state
            """
            
            try:
                db_stats = pd.read_sql(connection_query, self.db_engine)
                plt.pie(db_stats['connection_count'], labels=db_stats['state'], autopct='%1.1f%%')
                plt.title('Database Connection States')
            except Exception as e:
                plt.text(0.5, 0.5, f'DB Stats Error:\n{str(e)}', 
                        ha='center', va='center', transform=plt.gca().transAxes)
                plt.title('Database Connection Analysis (Error)')
            
            plt.tight_layout()
            plt.savefig('api_performance_report.png', dpi=300, bbox_inches='tight')
            plt.show()
    
    def test_database_integrity(self):
        """Test database integrity after API operations."""
        
        integrity_queries = [
            "SELECT COUNT(*) as orphaned_sales FROM sales s WHERE NOT EXISTS (SELECT 1 FROM customers c WHERE c.id = s.customer_id)",
            "SELECT COUNT(*) as invalid_amounts FROM sales WHERE sale_amount <= 0",
            "SELECT COUNT(*) as future_dates FROM sales WHERE sale_date > NOW()",
            "SELECT COUNT(*) as duplicate_emails FROM (SELECT email, COUNT(*) FROM customers GROUP BY email HAVING COUNT(*) > 1) AS dups"
        ]
        
        print("\n" + "="*50)
        print("DATABASE INTEGRITY CHECK")
        print("="*50)
        
        for query in integrity_queries:
            try:
                result = pd.read_sql(query, self.db_engine)
                print(f"✓ {query.split(' as ')[1].split()[0]}: {result.iloc[0, 0]} issues found")
            except Exception as e:
                print(f"✗ Query failed: {e}")

# Usage example
if __name__ == "__main__":
    tester = DatabaseAPITester(
        base_url="http://localhost:5000",
        db_connection_string="postgresql://user:password@localhost/sales_db"
    )
    
    # Run concurrent load test
    tester.test_concurrent_database_operations(num_threads=5, operations_per_thread=20)
    
    # Check database integrity
    tester.test_database_integrity()
```

> ⚠️ **Common Mistake**: Not testing database connection limits and transaction handling under load
</details>

### 🏃 Hands-on Activity
<details>
<summary>Activity: Complete Database API Testing</summary>

#### Steps:
1. **Set Up Test Environment**: Create test database with sample data
2. **Implement Postman Collection**: Create comprehensive test suite with database scenarios
3. **Load Testing**: Test API performance under database load
4. **Data Integrity Testing**: Verify database constraints and transactions
5. **Error Scenario Testing**: Test database failure handling
6. **Performance Monitoring**: Set up monitoring for database and API performance

#### Testing Scenarios to Cover:
- [ ] CRUD operations with database persistence
- [ ] Complex query performance under load
- [ ] Database constraint enforcement
- [ ] Transaction rollback scenarios
- [ ] Connection pool management
- [ ] Data integrity across API operations
- [ ] Error handling for database failures

> 📝 **Note**: Use separate test databases to avoid affecting production data
</details>

### 💭 Discussion
<details>
<summary>Discussion Topics</summary>

- Key Question: How does database integration change your API testing strategy?
- Follow-up Questions:
  - What are the key differences between testing with mock data vs real databases?
  - How do you balance test speed with database realism?
  - What database-specific scenarios require special testing attention?
</details>

## 📚 Additional Resources
<details>
<summary>Learning Materials</summary>

### Required Reading
- [VS Code Python Extensions Guide](https://code.visualstudio.com/docs/languages/python)
- [SQLAlchemy Flask Integration](https://flask-sqlalchemy.palletsprojects.com/)
- [NumPy Documentation](https://numpy.org/doc/stable/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Flask Templates Documentation](https://flask.palletsprojects.com/en/2.3.x/templating/)
- [Postman API Testing Guide](https://learning.postman.com/docs/writing-scripts/test-scripts/)

### Optional Further Reading
- [Database Performance Optimization](https://use-the-index-luke.com/)
- [Jupyter Notebook Best Practices](https://jupyter-notebook.readthedocs.io/en/stable/)
- [TensorFlow with Database Integration](https://www.tensorflow.org/tutorials)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
- [API Load Testing Best Practices](https://blog.postman.com/api-load-testing/)
</details>

## 📋 Assignment Preview
<details>
<summary>Upcoming Tasks</summary>

Students will integrate all learned concepts by:
- Setting up a complete Python development environment with database tools
- Creating data visualizations and analysis using real database data
- Building a Flask web application with database-connected templates
- Implementing comprehensive API testing with database scenarios
- Documenting their complete development and testing workflow with database integration
</details>

## ⏭️ Next Steps
<details>
<summary>Preparation for Next Session</summary>

- Install and configure all VS Code extensions including database tools
- Practice creating visualizations with matplotlib using database data
- Experiment with Flask template inheritance and database queries
- Familiarize yourself with Postman database testing scenarios
- Review advanced SQL queries for analytics and reporting
</details>


