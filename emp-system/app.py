from flask import Flask, request
import psycopg2
import json
import datetime
app = Flask(__name__)

conn_string = "host='localhost' dbname='employeecheckinsystem' user='emp' password='emp'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://emp:emp@localhost:5432/employeecheckinsystem'
#db = SQLAlchemy(app)

# Create new employee, or get employees
@app.route('/employee', methods = ['POST', 'GET'])
def hello_world():
    content = ''
    if request.method == "POST":
        content = request.get_json()
        query = '''INSERT INTO puntor(emri, mbiemri, numri_i_telefonit) VALUES(\'{}\', \'{}\', \'{}\');'''.format(content.get("emri"), content.get("mbiemri"), content.get("numri_i_telefonit"))
        cursor.execute(query)
        conn.commit()
        return json.dumps({'success': True,'message': 'Puntori u regjistrua me sukses'})
    elif request.method == "GET":
        query = '''SELECT * FROM puntor;'''
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        return json.dumps(result)
    return 'nothing happened'


@app.route('/attendance', methods = ['POST', 'GET'])
def attendence():
    if request.method == "POST":
        content = request.get_json()
        cursor.execute("INSERT INTO evidenca (p_id, check_in) VALUES (%s, %s)", (content.get("p_id"), datetime.datetime.now()))
        conn.commit()
        return 'Attendance added'
    else:
        return 'Something happened'
