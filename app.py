from flask import Flask, render_template, request, flash

import sqlite3 as sql
import traceback
import sys
 

app=Flask(__name__)
app.secret_key = "Ax1Ax1Ax1*.*16160606"

@app.route("/", methods=['GET'])
def hogar():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
