username = create_username("John", "Doe", "pilot")
password = create_password("John", "Doe", "pilot")

# Veritabanına yeni kullanıcıyı ekle
cursor = connection.cursor()
cursor.execute("""
    INSERT INTO Authentication (username, password, role) VALUES (%s, %s, %s)
""", (username, password, "pilot"))  
