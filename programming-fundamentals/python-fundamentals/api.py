from flask import Flask, request, jsonify
import sqlite3
import os
from contextlib import contextmanager

app = Flask(__name__)

# Database connection management using context manager pattern
# This ensures proper cleanup and prevents connection leaks
@contextmanager
def get_db_connection():
    """Context manager for database connections - ensures proper cleanup"""
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row  # Enable column access by name
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

def validate_user_data(data, required_fields=None):
    """Centralized validation function for reusability and maintainability"""
    if not data:
        return False, 'No data provided'
    
    if required_fields:
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return False, f'Missing required fields: {", ".join(missing_fields)}'
    
    # Validate field types and constraints
    if 'firstname' in data and (not isinstance(data['firstname'], str) or not data['firstname'].strip()):
        return False, 'firstname must be a non-empty string'
    
    if 'lastname' in data and (not isinstance(data['lastname'], str) or not data['lastname'].strip()):
        return False, 'lastname must be a non-empty string'
    
    return True, None

def user_exists(user_id):
    """Check if user exists in database"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM users WHERE id = ?', (user_id,))
        return cursor.fetchone() is not None

@app.route('/api/users', methods=['POST'])
def add_user():
    """Create a new user - demonstrates proper error handling and validation"""
    data = request.get_json()
    
    # Validate required fields
    is_valid, error_msg = validate_user_data(data, required_fields=['firstname', 'lastname'])
    if not is_valid:
        return jsonify({'error': error_msg}), 400
    
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO users (firstname, lastname) VALUES (?, ?)',
                (data['firstname'].strip(), data['lastname'].strip())
            )
            conn.commit()
            user_id = cursor.lastrowid
            
        return jsonify({
            'id': user_id, 
            'message': 'User created successfully',
            'user': {
                'id': user_id,
                'firstname': data['firstname'].strip(),
                'lastname': data['lastname'].strip()
            }
        }), 201
        
    except sqlite3.Error as e:
        return jsonify({'error': 'Database error occurred'}), 500

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Retrieve a specific user - essential for a complete CRUD API"""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
            user = cursor.fetchone()
            
        if not user:
            return jsonify({'error': 'User not found'}), 404
            
        return jsonify({
            'user': {
                'id': user['id'],
                'firstname': user['firstname'],
                'lastname': user['lastname'],
                'created_at': user['created_at'],
                'updated_at': user['updated_at']
            }
        }), 200
        
    except sqlite3.Error as e:
        return jsonify({'error': 'Database error occurred'}), 500

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user_full(user_id):
    """
    Full user update (PUT) - replaces entire resource
    
    Educational Insight: PUT is idempotent and should replace the entire resource.
    This endpoint requires all fields to be provided, following REST conventions.
    Use PUT when you want to completely replace a resource.
    """
    if not user_exists(user_id):
        return jsonify({'error': 'User not found'}), 404
    
    data = request.get_json()
    
    # For PUT, require all fields as we're replacing the entire resource
    is_valid, error_msg = validate_user_data(data, required_fields=['firstname', 'lastname'])
    if not is_valid:
        return jsonify({'error': error_msg}), 400
    
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE users 
                SET firstname = ?, lastname = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            ''', (data['firstname'].strip(), data['lastname'].strip(), user_id))
            conn.commit()
            
            if cursor.rowcount == 0:
                return jsonify({'error': 'User not found'}), 404
                
        return jsonify({
            'message': 'User updated successfully',
            'user': {
                'id': user_id,
                'firstname': data['firstname'].strip(),
                'lastname': data['lastname'].strip()
            }
        }), 200
        
    except sqlite3.Error as e:
        return jsonify({'error': 'Database error occurred'}), 500

@app.route('/api/users/<int:user_id>', methods=['PATCH'])
def update_user_partial(user_id):
    """
    Partial user update (PATCH) - updates only provided fields
    
    Educational Insight: PATCH allows partial updates, making APIs more flexible.
    This is ideal for scenarios where clients only want to update specific fields
    without affecting others. More efficient for large resources and better UX.
    
    Design Pattern: This demonstrates the partial update pattern with dynamic
    SQL generation based on provided fields.
    """
    if not user_exists(user_id):
        return jsonify({'error': 'User not found'}), 404
    
    data = request.get_json()
    
    # For PATCH, validate provided fields but don't require all fields
    is_valid, error_msg = validate_user_data(data)
    if not is_valid:
        return jsonify({'error': error_msg}), 400
    
    # Check if at least one valid field is provided
    valid_fields = ['firstname', 'lastname']
    update_fields = {k: v.strip() for k, v in data.items() if k in valid_fields}
    
    if not update_fields:
        return jsonify({'error': 'No valid fields provided for update'}), 400
    
    try:
        # Dynamic SQL generation for partial updates
        set_clause = ', '.join([f'{field} = ?' for field in update_fields.keys()])
        sql = f'UPDATE users SET {set_clause}, updated_at = CURRENT_TIMESTAMP WHERE id = ?'
        values = list(update_fields.values()) + [user_id]
        
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, values)
            conn.commit()
            
            if cursor.rowcount == 0:
                return jsonify({'error': 'User not found'}), 404
            
            # Fetch updated user data to return complete information
            cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
            updated_user = cursor.fetchone()
            
        return jsonify({
            'message': 'User updated successfully',
            'updated_fields': list(update_fields.keys()),
            'user': {
                'id': updated_user['id'],
                'firstname': updated_user['firstname'],
                'lastname': updated_user['lastname'],
                'updated_at': updated_user['updated_at']
            }
        }), 200
        
    except sqlite3.Error as e:
        return jsonify({'error': 'Database error occurred'}), 500

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete user endpoint - completes the CRUD operations
    
    Educational Insight: DELETE should be idempotent. Multiple calls to delete
    the same resource should not cause errors (returning 404 for non-existent
    resources is acceptable but not required).
    """
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
            conn.commit()
            
            if cursor.rowcount == 0:
                return jsonify({'error': 'User not found'}), 404
                
        return jsonify({'message': 'User deleted successfully'}), 200
        
    except sqlite3.Error as e:
        return jsonify({'error': 'Database error occurred'}), 500

@app.route('/api/users', methods=['GET'])
def list_users():
    """
    List all users with pagination support
    
    Educational Insight: Always implement pagination for list endpoints
    to prevent performance issues as data grows. This is a scalability
    best practice often overlooked in simple implementations.
    """
    # Pagination parameters
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)  # Cap at 100
    offset = (page - 1) * per_page
    
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            # Get total count for pagination metadata
            cursor.execute('SELECT COUNT(*) FROM users')
            total_count = cursor.fetchone()[0]
            
            # Get paginated results
            cursor.execute('''
                SELECT id, firstname, lastname, created_at, updated_at 
                FROM users 
                ORDER BY id 
                LIMIT ? OFFSET ?
            ''', (per_page, offset))
            users = cursor.fetchall()
            
        return jsonify({
            'users': [dict(user) for user in users],
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': total_count,
                'pages': (total_count + per_page - 1) // per_page
            }
        }), 200
        
    except sqlite3.Error as e:
        return jsonify({'error': 'Database error occurred'}), 500

# Error handlers for better API experience
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({'error': 'Method not allowed'}), 405

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    init_db()
    # Enable debug mode for development - disable in production
    app.run(debug=True, host='0.0.0.0', port=5000) 