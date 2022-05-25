import sqlite3, csv

# CREATE nodes.csv
osmdb = 'nashville_osm.db'

connection = sqlite3.connect(osmdb)
write_cursor = connection.cursor()
write_cursor.execute('''
                    CREATE TABLE nodes(id INTEGER, lat TEXT, lon TEXT, user TEXT, uid INTEGER, version TEXT, changeset TEXT, timestamp TEXT)''')

connection.commit()

with open('nodes.csv', 'r', encoding="utf-8") as csvfile:
    middleman = csv.DictReader(csvfile) # comma is default delimiter
    to_db = [(i['id'], i['lat'], i['lon'], i['user'], i["uid"], i["version"],i["changeset"],i["timestamp"]) for i in middleman]

write_cursor.executemany("INSERT INTO nodes (id, lat, lon, user, uid, version, changeset, timestamp) VALUES (?,?,?,?,?,?,?,?);", to_db)

connection.commit()
connection.close()


#CREATE nodes_tags.csv
connection = sqlite3.connect(osmdb)
write_cursor = connection.cursor()
write_cursor.execute('''
                    CREATE TABLE nodes_tags(id INTEGER, key TEXT, value TEXT, type TEXT)''')

connection.commit()

with open('nodes_tags.csv', 'r', encoding="utf-8") as csvfile:
    middleman = csv.DictReader(csvfile) # comma is default delimiter
    to_db = [(i['id'], i['key'], i['value'], i['type']) for i in middleman]

write_cursor.executemany("INSERT INTO nodes_tags(id, key, value, type) VALUES (?,?,?,?);", to_db)

connection.commit()
connection.close()

#CREATE ways.csv
connection = sqlite3.connect(osmdb)
write_cursor = connection.cursor()
write_cursor.execute('''
                    CREATE TABLE ways(id INTEGER, user TEXT, uid TEXT, version TEXT, changeset TEXT, timestamp TEXT)''')

connection.commit()

with open('ways.csv', 'r', encoding="utf-8") as csvfile:
    middleman = csv.DictReader(csvfile) # comma is default delimiter
    to_db = [(i['id'], i['user'], i['uid'], i['version'], i["changeset"], i["timestamp"]) for i in middleman]

write_cursor.executemany("INSERT INTO ways (id, user, uid, version, changeset, timestamp) VALUES (?,?,?,?,?,?);", to_db)

connection.commit()
connection.close()


#CREATE ways_tags.csv
connection = sqlite3.connect(osmdb)
write_cursor = connection.cursor()
write_cursor.execute('''
                    CREATE TABLE ways_tags(id INTEGER, key TEXT, value TEXT, type TEXT)''')

connection.commit()

with open('ways_tags.csv', 'r', encoding="utf-8") as csvfile:
    middleman = csv.DictReader(csvfile) # comma is default delimiter
    to_db = [(i['id'], i['key'], i['value'], i['type']) for i in middleman]

write_cursor.executemany("INSERT INTO ways_tags(id, key, value, type) VALUES (?,?,?,?);", to_db)

connection.commit()
connection.close()

#CREATE ways_nodes.csv
connection = sqlite3.connect(osmdb)
write_cursor = connection.cursor()
write_cursor.execute('''
                    CREATE TABLE ways_nodes(id INTEGER, node_id INTEGER, position INTEGER)''')

connection.commit()

with open('ways_nodes.csv', 'r', encoding="utf-8") as csvfile:
    middleman = csv.DictReader(csvfile) # comma is default delimiter
    to_db = [(i['id'], i['node_id'], i['position']) for i in middleman]

write_cursor.executemany("INSERT INTO ways_nodes(id, node_id, position) VALUES (?,?,?);", to_db)

connection.commit()
connection.close()
