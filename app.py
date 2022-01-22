from flask import Flask, render_template, url_for ,escape, request,redirect
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_kampus'
mysql = MySQL(app),

@app.route('/')
def index ():
    return render_template('layout.html')

@app.route('/nav')
def nav ():
    return render_template('utama.html')

 
@app.route('/ubah/<string:id_mhs>')
def ubah (id_mhs):

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mahasiswa WHERE id=%s", (id_mhs,))
    rv = cur.fetchall()
    cur.close()
    return render_template('edit.html', mahasiswa=rv)


@app.route('/read')
def read ():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mahasiswa")
    rv = cur.fetchall()
    cur.close()
    return render_template('tampil.html', mahasiswa=rv)

@app.route('/update',methods=["POST"])
def update ():
    id_mhs = request.form['id']
    nim = request.form['nim']
    nama = request.form['nama']
    cur =mysql.connection.cursor()
    cur.execute("UPDATE mahasiswa SET nim=%s,nama=%s WHERE id=%s", (nim,nama,id_mhs,))
    mysql.connection.commit()
    return redirect (url_for('read'))

@app.route('/save',methods=["POST"])
def save ():
    nim = request.form['nim']
    nama = request.form['nama']
    cur =mysql.connection.cursor()
    cur.execute("INSERT INTO mahasiswa (nim,nama) VALUES (%s,%s)",(nim,nama))
    mysql.connection.commit()
    return redirect (url_for('read'))


@app.route('/hapus/<string:id>', methods=["GET"])
def hapus (id):
    cur =mysql.connection.cursor()
    cur.execute("DELETE FROM mahasiswa where id=%s",(id,))
    mysql.connection.commit()
    return redirect (url_for('read'))

app.run(debug=True)