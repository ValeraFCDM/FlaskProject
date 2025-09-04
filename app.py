from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agent_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code_name = db.Column(db.String(50), nullable=False)
    contact_number = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    access_level = db.Column(db.String(50), nullable=False)

with app.app_context():
    db.create_all()


@app.route('/')
@app.route('/agents')
def get_agents():
    agents = Agent.query.order_by(Agent.access_level).all()
    return render_template('agents.html', agents=agents)

@app.route('/add', methods=['GET', 'POST'])
def add_agent():
    if request.method =='POST':
        name = request.form.get('name').lower()
        number = request.form.get('number')
        email = request.form.get('email')
        access_level = request.form.get('access_level')
        if name.strip():
            new_agent = Agent(code_name=name, contact_number=number, email = email, access_level=access_level)
            db.session.add(new_agent)
            db.session.commit()
        return redirect(url_for('get_agents'))
    return render_template('add_agent.html')

@app.route('/agent/<int:id>')
def get_agent(id):
    agent = Agent.query.get_or_404(id)
    return render_template('dossier.html', agent=agent)

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_agent(id):
    agent = Agent.query.get_or_404(id)
    if request.method == 'POST':
        new_data = request.form
        if new_data['name'].strip():
            agent.code_name = new_data['name'].lower()
        if new_data['number']:
            agent.contact_number = new_data['number']
        if new_data['email']:
            agent.email = new_data['email']
        if 'access_level' in new_data:
            agent.access_level = new_data['access_level']
        db.session.commit()
        return render_template('dossier.html', agent=agent)
    return render_template('edit_agent.html', agent=agent)

@app.route('/delete')
def delete_all():
    db.session.query(Agent).delete()
    db.session.commit()
    return redirect(url_for('get_agents'))

@app.route('/delete/<id>')
def delete_agent(id):
    agent = Agent.query.get_or_404(id)
    db.session.delete(agent)
    db.session.commit()
    return redirect(url_for('get_agents'))

@app.route('/find', methods=['POST'])
def get_agent_for_name():
    code_name = request.form.get('code_name').lower()
    agent = Agent.query.filter_by(code_name=code_name).first()
    if agent:
        return render_template('dossier.html', agent=agent)
    return render_template('add_agent.html')

if __name__ == "__main__":
    app.run(debug=True)