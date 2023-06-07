
from flask import Flask, send_file, jsonify, request
from flask_cors import CORS
import os
import random
from werkzeug.utils import secure_filename

from datetime import *
import time

from db import *
import cluster

import pickle

app = Flask(__name__)

CORS(app)
base = "http://localhost:5000"

UPLOAD_FOLDER = 'images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
album = 'alk.pkl'


@app.route('/')
def getAllImages():
    con = None
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        cur.execute("select img_id from g_table;")
        allimgs = cur.fetchall()
        imgs = [base+'/images/'+f[0] for f in allimgs]

        cur.execute('select clu_id from clu_table')
        clu = [f[0] for f in cur.fetchall()]
        clu_lbl = []
        cluImgs = {}
        for c in clu:
            cur.execute(f'''select img_id from g_to_clu_rel where clu_id="{c}"''')
            cimgs = [base+'/images/'+f[0] for f in cur.fetchall()]
            clu_lbl.append({
                'p_id': c, 'link': (base+'/faces/'+c+'.jpeg')
            })
            cluImgs[c] = cimgs

        con.close()
        res = jsonify({
            "imgs": imgs,
            "clusters": clu_lbl,
            "clusterImages": cluImgs
        })
        return res
    except:
        print("get images error")
    return "error"


@app.route('/deleteImages/', methods=['POST'])
def deleteImages():
    global db_file
    con = None
    if request.method == 'POST':
        pics = []
        try:
            con = sqlite3.connect(db_file)
            cur = con.cursor()
            data = request.json
            # load cluster
            file1 = open('enc.pkl', 'rb')
            clust = pickle.load(file1)
            # end
            for img in data['Images']:
                # print(img)
                print(cur.execute(f""" select img_id from g_table  """).fetchall())
                cur.execute(
                    f""" delete from g_table where img_id = '{img}' """)
                print(cur.execute(f""" select img_id from g_table  """).fetchall())
                cur.execute(
                    f""" delete from g_to_clu_rel where img_id = '{img}' """)
                # print(cur.execute(f'''select img_id from g_table''').fetchall())
                # print(cur.execute(f''' select * from  g_to_clu_rel where img_id = "{img}"''').fetchall())
                # deleting the entries
            con.commit()
            con.close()
            # v changes 20-05
            # print(len(clust))
            for path in data['Images']:
                clust = [i for i in clust if i['imagePath'].split(
                    '/')[1] != path]
            # print(clust)
            file1.close()
            print(len(clust))
            file1 = open('enc.pkl', 'wb')
            pickle.dump(clust, file1)
            file1.close()
            cluster.cluster()
            # end changes
            return 'sucess'
        except Error as e:
            print(e)


@app.route('/images/<imge>')
def getImage(imge):
    return send_file('images\\'+imge)


@app.route('/faces/<imge>')
def getFace(imge):
    return send_file('faces\\'+imge)


@app.route('/imageupload/', methods=['POST'])
def imageUpload():
    global db_file
    con = None
    if request.method == 'POST':
        pics = []
        try:
            con = sqlite3.connect(db_file)
            cur = con.cursor()
            imgs = request.files.getlist('files')
            for f in imgs:
                time.sleep(1/10**5)
                k = datetime.now()
                # print(k)
                name = "IMG"+k.strftime('%Y%m%d%H%M%S_%f')
                cur.execute("insert into g_table values(?,?,?)",
                            ((name+'.jpeg'), name, k))
                f.save(
                    os.path.join(app.config['UPLOAD_FOLDER'], name+".jpeg"))
                pics.append(name+".jpeg")
                print("sucess")
            con.commit()
            con.close()
            cluster.addImages(pics)
        except Error as e:
            print(e)
        return "success"


@app.route("/createAlbum/", methods=["POST"])
def createAlbum():
    if request.method == "POST":
        file1 = open(album, 'rb')
        alb = {}
        if os.path.getsize(album) > 0:
            alb = pickle.load(file1)
        print(alb)
        data = request.json
        for i in data['Img']:
            print(i)
        print(data['title'])
        print(data['title'] in alb)
        if data['title'] in alb:
            return 'already exists'
        alb[data['title']] = data['Img']
        print(album)
        file1.close()
        file1 = open(album, 'wb')
        pickle.dump(alb, file1)
    return 'success'


@app.route('/getalb/')
def getalb():
    if not os.path.exists(album):
        with open(album, 'wb') as file:
            pickle.dump({}, file)
    file1 = open(album, 'rb')
    alb = pickle.load(file1)
    print(alb)
    return jsonify({"var": alb})


if __name__ == "__main__":
    if not os.path.exists(cluster.enc):
        with open(cluster.enc, 'wb') as file:
            pickle.dump([], file)
    if not os.path.exists(album):
        with open(album, 'wb') as file:
            pickle.dump({}, file)
    # cluster.cluster()
    db_init()

    app.run()
