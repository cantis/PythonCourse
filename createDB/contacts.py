''' contact db creation '''
import sqlite3

DB = sqlite3.connect("createDB/contacts.sqlite")

DB.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
DB.execute("INSERT INTO contacts(name, phone, email) VALUES ('Tim', 6545678, 'tim@email.com')")
DB.execute("INSERT INTO contacts(name, phone, email) VALUES ('Brian', 1234, 'brian@myemail.com')")

CURSOR = DB.cursor()
CURSOR.execute("Select * from contacts")

print(CURSOR.fetchone())
print(CURSOR.fetchone())
print(CURSOR.fetchone())

for name, phone, email in CURSOR:
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

CURSOR.close()
DB.commit()
DB.close()
