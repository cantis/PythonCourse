''' contact db creation '''
import sqlite3

DB = sqlite3.connect("createDB/contacts.sqlite")

NEW_EMAIL = "anotherupdate@update.com"
PHONE = "1234"
#UPDATE_SQL = "UPDATE contacts SET email = 'anotherupdate@update.com' WHERE phone = 1234"
UPDATE_SQL = "UPDATE contacts SET email = ? WHERE phone = ?"
UPDATE_CURSOR = DB.cursor()
UPDATE_CURSOR.execute(UPDATE_SQL, (NEW_EMAIL, PHONE))
print(f"{UPDATE_CURSOR.rowcount} rows updated")

UPDATE_CURSOR.connection.commit()
UPDATE_CURSOR.close()

for name, PHONE, email in DB.execute("SELECT * FROM contacts"):
    print(name)
    print(PHONE)
    print(email)
    print("-" * 20)

DB.close()
