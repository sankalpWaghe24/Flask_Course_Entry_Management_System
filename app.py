from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)


@app.route('/')
def register():
    return render_template('services.html')


@app.route('/form', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        fm = request.form
        a = fm['sname']
        b = fm['semail']
        c = fm['scontact']
        d = fm['scourse']
        cursor = mysql.connection.cursor()
        q = "insert into student(name,email,contact,course) values('" + \
            a+"','"+b+"','"+c+"','"+d+"')"
        cursor.execute(q)
        mysql.connection.commit()
        return redirect('/form')
    else:
        return render_template('form.html')


@app.route('/show')
def show():
    cursor = mysql.connection.cursor()
    q = "select * from student"
    res = cursor.execute(q)
    if(res > 0):
        det = cursor.fetchall()
        return render_template('show.html', details=det)
    else:
        return render_template('show.html')


@app.route('/delete/<string:id>')
def delfun(id):
    cursor = mysql.connection.cursor()
    q = "delete from student where id='"+id+"'"
    cursor.execute(q)
    mysql.connection.commit()
    return redirect('/show')


@app.route('/edit/<string:id>')
def edit(id):
    cursor = mysql.connection.cursor()
    q = "select * from student where id='"+id+"'"
    res = cursor.execute(q)
    if(res > 0):
        det = cursor.fetchall()
        return render_template('edit.html', details=det)


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        fm = request.form
        a = fm['sname']
        b = fm['semail']
        c = fm['scontact']
        e = fm['scourse']
        d = fm['sid']
        cursor = mysql.connection.cursor()
        q = "update student set name='"+a+"',email='" + \
            b+"',contact='"+c+"',course='"+e+"' where id='"+d+"'"
        cursor.execute(q)
        mysql.connection.commit()
        return redirect('/show')


app.run(debug=True)
