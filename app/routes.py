from flask import render_template, request, redirect, url_for
from datetime import datetime
from app import app

@app.route('/')
def home():
    current_datetime = datetime.now()
    return render_template('home.html', current_datetime=current_datetime)

@app.route('/about')
def about():
    team_members = [
        {'name': 'Alice', 'role': 'Developer'},
        {'name': 'Bob', 'role': 'Designer'},
        {'name': 'Charlie', 'role': 'Project Manager'}
    ]
    return render_template('about.html', team_members=team_members)

@app.route('/contact')
def form():
    contact_manager = {
        'name': 'Ivan A.',
        'address': {
            'street': 'Qwerty Street',
            'city': 'MeowLand',
            'house_num': '152'
        }
    }
    return render_template('contact.html', contact_manager=contact_manager)

@app.route('/submit', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        return render_template('result.html')

    return redirect(url_for('form'))