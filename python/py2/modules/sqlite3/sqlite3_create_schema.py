import os
import sqlite3

db_filename = 'todo.db'
schema_filename = 'todo_schema.sql'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print 'Creating schema'
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

        print 'Inserting initial data'

        conn.execute("""
        insert into project (name, description, deadline)
        values ('pymotw', 'Python Module of the week', '2014-10-22')
        """)

        conn.execute("""
        insert into task (details, status, deadline, project)
        values ('write about select', 'done', '2014-10-20', 'pymotw')
        """)

        conn.execute("""
        insert into task (details, status, deadline, project)
        values ('write about random', 'waiting', '2014-10-21', 'pymotw')
        """)

        conn.execute("""
        insert into task (details, status, deadline, project)
        values ('write about sqlite3', 'active', '2014-10-22', 'pymotw')
        """)
    else:
        print 'Database exists, assume schema does, too.'
