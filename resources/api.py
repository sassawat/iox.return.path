import os, json, requests
import pandas as pd
from flask_restful  import Resource
from flask          import config, request, jsonify
from werkzeug.utils import secure_filename
from models.sensor import sensor
from config.config import Development
from .login import talegur_login


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Development.ALLOWED_EXTENSIONS

class bulkConfig( Resource ):
    def post( self ):
        file = request.files["file"]

        headers = {
            "Content-Type": 'application/json',
            "Accept": "*/*",
            "Authorization": "Bearer " + talegur_login(Development.TALEGUR_URL, Development.LOGIN_USERNAME, Development.LOGIN_PASSWORD),
        }

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(Development.UPLOAD_FOLDER, filename))

        data = pd.read_csv(os.path.join(Development.UPLOAD_FOLDER, filename))
        data = data.to_json(orient="records")
        parsed = json.loads(data)

        sensor_list = []
        resp_log = []
        for item in parsed:
            for col in item:
                sensor[col] = item[col]
            try:
                resp = requests.request("POST", Development.TALEGUR_URL+"Sensor", data=json.dumps(sensor), headers=headers)
            except:
                resp_log.append({"sensor_id" : item['id'], "resp_code": resp.status_code})
            else:
                resp_log.append({"sensor_id" : item['id'], "resp_code": resp.status_code})

        return jsonify(resp_log)
