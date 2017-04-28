from flask import Flask, render_template, url_for, redirect, request
from hashids import Hashids


import json

import models
import functions

app = Flask(__name__)
# For development
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 3
hashids = Hashids(salt='TOMISGREAT', min_length=4)

@app.route('/')
def index():
    comps = models.Comp.select().limit(100)
    return render_template('index.html', comps=comps)

# ===== Authentication ===== #

@app.route('/login')
def login():
    return render_template('auth.html')

# ===== Competitions ===== #

@app.route('/comps')
def comps():
    comps = models.Comp.select().limit(100)
    return render_template('comps.html', comps=comps)

@app.route('/comp/new')
def newComp():
    return render_template('newcomp.html')

@app.route('/createComp', methods=['POST'])
def createComp():
    data = request.json
    comp = models.Comp(
        name = data['compName'],
        comp_type = data['type'],
        singlesDoubles = data['singlesDoubles']
    )
    comp.save()
    # print(data['compName'])
    # print(data['players'][0])
    # processed = functions.fourDoublesReturn(data)
    # print(processed)
    # print('=====')
    # print(processed['rounds'][0])
    # TODO: store info and hash in model

    # NOTE: we can do this two ways:
    # 1. return json and handle display in js --> this is more scalable for interactivity later on
    return str(comp.getHash()) #json.dumps(processed)
    # 2. render new flask page --> this is easier

    #return redirect(url_for('comp', compHash=0)) # TODO: compHash should be retrieved from the model, processed shouldn't be passed

@app.route('/comp/<compHash>')
def comp(compHash):
    #rounds = processed['rounds'] # HACK: should either be stored or generated here!
    comp = models.Comp.get(models.Comp.id == hashids.decode(compHash))
    return render_template('comp.html', comp=comp)

if __name__ == '__main__':
    models.init()
    app.run(host='0.0.0.0', port=8000, debug=True)
