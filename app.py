from flask import Flask, render_template, url_for, redirect, request
import functions
import json

app = Flask(__name__)
# For development
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 3

@app.route('/')
def index():
    return render_template('index.html')

# ===== Authentication ===== #

@app.route('/login')
def login():
    return render_template('auth.html')

# ===== Competitions ===== #

@app.route('/newComp', methods=['POST'])
def newComp():
    data = request.json
    # print(data['compName'])
    # print(data['players'][0])
    processed = functions.fourDoublesReturn(data)
    print(processed)
    print('=====')
    print(processed['rounds'][0])
    # TODO: store info and hash in model

    # NOTE: we can do this two ways:
    # 1. return json and handle display in js --> this is more scalable for interactivity later on
    return json.dumps(processed)
    # 2. render new flask page --> this is easier

    #return redirect(url_for('comp', compHash=0)) # TODO: compHash should be retrieved from the model, processed shouldn't be passed

@app.route('/comp/<compHash>')
def comp(compHash, processed):
    rounds = processed['rounds'] # HACK: should either be stored or generated here!
    return render_template('comp.html', rounds=rounds)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
