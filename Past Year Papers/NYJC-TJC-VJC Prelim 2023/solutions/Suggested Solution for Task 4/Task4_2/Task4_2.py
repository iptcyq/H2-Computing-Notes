import sqlite3
from flask import Flask, render_template

app = Flask(__name__)
app.config.update(
    TEMPLATES_AUTO_RELOAD = True
)

# For Task 4.1
@app.route('/')
def index():
    return render_template('index.html')

# For Task 4.2
@app.route('/deletecert')
def delcert():
    query = """
            DELETE FROM "Certificate"
            WHERE "status" = ?;
            """

    params = ('404',)

    with sqlite3.connect('Task4.db') as conn:
        cursor = conn.cursor()
        cursor.execute('pragma foreign_keys=on')

        cursor.execute(query, params)
        conn.commit()
        row_count = cursor.rowcount         

        cursor.close()
        # conn.close() is called automatically

    return render_template('deletecert.html', certs_deleted=row_count)

app.run()
