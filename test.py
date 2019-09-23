import plyvel

db = plyvel.DB('/tmp/testdb/', create_if_missing=True)

print(db.closed)
db.close()
print(db.closed)
