from flask import Flask, render_template, request, flash

import sqlite3 as sql
import traceback
import sys
 

app=Flask(__name__)
app.secret_key = "Ax1Ax1Ax1*.*16160606"

@app.route("/", methods=['GET', 'POST'])
def hogar():
    if request.method=='POST':
        try:
            nombre=request.form['nombre']
            fono=request.form['fono']
            fecha=request.form['fecha']
            hora=request.form['hora']



            with sql.connect("db") as con:
                cur=con.cursor()
                cur.execute("INSERT INTO hora (nombre, fono, fecha, hora) VALUES (?,?,?,?)",(nombre, fono, fecha, hora))
                con.commit()
                msg="Todo Ok..."



        except con.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
            con.close()
        finally:


            flash("Hora agendada con exito!, Espere su llamado o Whatsapp para confirmacion.")
            return render_template("index.html", msg=msg)
    else:
        return render_template('index.html')




@app.route('/lista')
def lista():
    con=sql.connect("db")
    con.row_factory=sql.Row

    cur=con.cursor()
    cur.execute("select * from hora")

    rows=cur.fetchall()

    return render_template("lista.html", rows=rows)

if __name__ == '__main__':
    app.run(debug=True, port=4000, host="0.0.0.0")
