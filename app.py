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
    if data['type'] == 'poolDraws':
        if data['singlesDoubles'] == 'doubles':
            rounds = functions.fourDoublesReturn(data['players'])
        elif data['singlesDoubles'] == 'singles':
            rounds = functions.fourSinglesReturn(data['players'])

    comp = models.Comp(
        name = data['compName'],
        comp_type = data['type'],
        singlesDoubles = data['singlesDoubles'],
        players = data['players'],
        rounds = rounds,
        scores = []
        #scores = [1,2,3,4]
    )
    comp.save()
    print(data['players'])
    return str(comp.getHash())

@app.route('/comp/<compHash>')
def comp(compHash):
    #rounds = processed['rounds'] # HACK: should either be stored or generated here!
    comp = models.Comp.get(models.Comp.id == hashids.decode(compHash))
    # players = (BlogPost
    #             .select(BlogPost.tags[0].alias('first_tag'))
    #             .where(BlogPost.id == 1)
    #             .dicts()
    #             .get())
    return render_template('comp.html', comp=comp)

if __name__ == '__main__':
    models.init()
    app.run(host='0.0.0.0', port=8000, debug=True)
