from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('auth.html')

@app.route('/newComp', methods=['POST'])
def newComp():
    data = request.json
    print(data['compName'])
    print(data['players'][0])
    return 'did something'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
