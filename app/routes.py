from flask import render_template, request, redirect, url_for
from app import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def form():
    return render_template('contact.html')

@app.route('/submit', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        return render_template('result.html')

    return redirect(url_for('form'))