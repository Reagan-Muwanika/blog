from flask import Flask, render_template, abort

articles = [
	{"slug": "Python", "title": "Learn Python", "content": "This is an Object Oriented Programming (OOP) Language"},
	{"slug": "Flask", "title": "Learn Flask", "content": "This is a Python framework used for small projects"},
	{"slug": "Jinja", "title": "Learn Jinja", "content": "This is a Scripting Language used in Python Frameworks"},
]

app = Flask(__name__)

@app.route('/')
def home_page():
	return render_template('home.html')

@app.route('/about')
def about_page():
	return render_template('about.html')

@app.route('/articles')
def articles_page():
	return render_template('articles.html', articles = articles)

@app.route('/articles/<article_slug>')
def article_page(article_slug):
	try:
		article = next((a for a in articles if a.get("slug") == article_slug))
	except StopIteration:
		abort(404)
	return render_template('article.html', title = article.get('title'), content = article.get('content'))

@app.errorhandler(404)
def not_found_page(err):
	return render_template('not_found.html')