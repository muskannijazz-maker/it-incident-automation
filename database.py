import sqlite3


def create_database():
    connection = sqlite3.connect("incidents.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT NOT NULL,
            description TEXT NOT NULL,
            severity TEXT NOT NULL,
            status TEXT NOT NULL,
            priority TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_incident(service, description, severity, status, priority):
    connection = sqlite3.connect("incidents.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO incidents (service, description, severity, status, priority)
        VALUES (?, ?, ?, ?, ?)
        """,
        (service, description, severity, status, priority)
    )

    connection.commit()
    incident_id = cursor.lastrowid
    connection.close()

    return incident_id


def get_incidents():
    connection = sqlite3.connect("incidents.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM incidents")
    rows = cursor.fetchall()

    connection.close()

    incidents = []

    for row in rows:
        incidents.append({
            "id": row[0],
            "service": row[1],
            "description": row[2],
            "severity": row[3],
            "status": row[4],
            "priority": row[5]
        })

    return incidents


def get_incident_by_id(incident_id):
    connection = sqlite3.connect("incidents.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM incidents WHERE id = ?",
        (incident_id,)
    )

    row = cursor.fetchone()
    connection.close()

    if row is None:
        return None

    return {
        "id": row[0],
        "service": row[1],
        "description": row[2],
        "severity": row[3],
        "status": row[4],
        "priority": row[5]
    }

def update_incident_status(incident_id, status):
    connection = sqlite3.connect("incidents.db")
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE incidents SET status = ? WHERE id = ?",
        (status, incident_id)
    )

    connection.commit()
    updated = cursor.rowcount
    connection.close()

    return updated > 0
create_database()
