from config import get_db_connection

def execute_query(query, values=None):
    """Executes a query and returns results if available."""
    conn = get_db_connection()
    if not conn:
        return None  # Handle connection error
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, values)
    result = cursor.fetchall() if cursor.description else None
    conn.commit()
    cursor.close()
    conn.close()
    return result
