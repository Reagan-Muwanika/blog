from flask import Flask, abort, render_template

app = Flask(__name__)

@app.route('/sql')
def sql():
	return render_template('sql.html')