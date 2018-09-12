import os
import sqlite3

db_filename = 'todo.db'

db_is_new = not os.path.exists(db_filename)

# The database is created the first time the file is accessed.
conn = sqlite3.connect(db_filename)

if db_is_new:
    print 'Need to create schema'
else:
    print 'Database exists, assume schema does, too.'

conn.close()