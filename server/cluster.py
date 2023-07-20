import os
import time
import numpy as np
from PIL import Image
import cv2
import face_recognition
from sklearn.cluster import DBSCAN
#from imutils import build_montages
import shutil
import pickle
from sklearn.metrics import silhouette_samples, silhouette_score


from db import *

enc = "enc.pkl"


def addImages(imglist):
    data = None
    try:
        # print("addImages\n\n")
        with open(enc, 'rb') as file:
            data = pickle.load(file)
        # print("imglist\n", imglist)
        # print("data\n", data)
        c = 0
        flag = False
        for f in imglist:
            p = 'images/'+f

            tmpimg = Image.open(p).convert('RGB')
            tmpimg1 = np.array(tmpimg)
            img1 = tmpimg1[:, :, ::-1].copy()

            rgb = img1
            boxes = face_recognition.face_locations(rgb, model="hog")

            encodings = face_recognition.face_encodings(rgb, boxes)
            # print(boxes)
            d = [{"imagePath": p, "loc": box, "encoding": enc}
                 for (box, enc) in zip(boxes, encodings)]

            if (len(d)):
                data.extend(d)
                flag = True
        # print("data 2 var\n", data)
        if flag:
            with open(enc, 'wb') as file:
                pickle.dump(data, file)
            cluster()
    except:
        print("add error")


def cluster():
    try:
        shutil.rmtree('faces')	
        os.mkdir('faces')
        data = None
        with open(enc, 'rb') as file:
            data = pickle.load(file)
        # print("cluster \n\n")
        data_arr = np.array(data)
        encodings_arr = [item["encoding"] for item in data_arr]

        cluster = DBSCAN(min_samples=3)
        cluster.fit(encodings_arr)

        labelIDs = np.unique(cluster.labels_)

        lbl = cluster.fit_predict(encodings_arr)

        silhouette_vals = silhouette_samples(encodings_arr, lbl)
        silhouette_avg = np.mean(silhouette_vals)
        print("The average Silhouette Score is:", silhouette_avg)

        numUniqueFaces = len(np.where(labelIDs > -1)[0])
        # c =[]
        cnt = 0
        clu = {}
        
        for labelID in labelIDs:
            idxs = np.where(cluster.labels_ == labelID)[0]
            t = []
            x,y,w,h=0,0,0,0
            f_idx=-1
            f=True
            img = None
            for i in idxs:
                if(labelID != -1):
                    if(f):
                        f=False
                        x,y,w,h=data_arr[i]['loc']
                        f_idx = i
                        # print(data_arr[i]['imagePath'])
                        img = cv2.imread(data_arr[i]['imagePath']).copy()
                        # cv2.imshow(data_arr[i]['imagePath'], img)  
                        # cv2.waitKey(0)                      
                    t.append(data_arr[i]["imagePath"])
            if(labelID != -1):
                cnt += 1
                clu["face"+str(cnt)] = []
                for tp in t:
                    s = tp.split('/')
                    clu['face'+str(cnt)].append(s[1])

                image = face_recognition.load_image_file(data_arr[f_idx]['imagePath'])
                img = Image.fromarray(image, 'RGB').copy()
                img_cropped = img.crop((
                    h,x,y,w
                ))
                img_cropped.save(f'faces/face{str(cnt)}.jpeg')
                # img_cropped.show()
                # c.append(t)
        # print(clu)
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        # print(cur.execute('select * from clu_table').fetchall())
        cur.execute("delete from g_to_clu_rel")
        cur.execute("delete from clu_table")
        # print("truncate")
        # print(cur.execute('select * from clu_table').fetchall())
        for face in clu.keys():
            cur.execute('insert into clu_table values(?,?)', (face, face))
        # print("clu keyss\n")
        con.commit()
        for face in clu.keys():
            for pic in clu[face]:
                cur.execute(
                    'insert into g_to_clu_rel (clu_id,img_id) values (?,?)', (face, pic))

        con.commit()
        con.close()
        make_id()
    except:
        print('clu error')


cluster()
