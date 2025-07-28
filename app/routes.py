from app import app

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/hello')
def hello():
    return 'Hello, world!'

@app.route('/info')
def info():
    return 'This is an informational page.'