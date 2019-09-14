import requests
import base64
import json
from flask import Flask, request, abort, render_template
# from google.cloud import Storage

# storage_client = storage.Client()
app = Flask(__name__)

def get_token():
   client_id = "5528abffd5994d4e8768a7a5f6bd5e26"
   client_secret = "3ff9e4f40b1f4567bc438fae15275304"
   auth_str = "{}:{}".format(client_id, client_secret)
   b64_auth_str = base64.b64encode(auth_str.encode()).decode()
   head = {"Authorization": "Basic " + b64_auth_str}
   dat = {"grant_type": "client_credentials"}
   url = "https://accounts.spotify.com/api/token"
   token = requests.post(url, headers=head, data=dat).json()['access_token']
   return token
# call query and return
def query(_q):
   head = {"Authorization": "Bearer " + get_token()}
   para = {"query": _q, "type": "track"}
   url = "https://api.spotify.com/v1/search"
   req = requests.get(url, headers=head, params=para).json()
   ids = [req['tracks']['items'][i]['id'] for i in range(5)]
   return json.dumps(ids)


@app.route('/uploadData', methods = ['POST'])
def upload():
    # return request.form
    # The kind for the new entity
    kind = 'Task'
    # # The name/ID for the new entity
    # name = 'MusicTest'
    # # The Cloud Datastore key for the new entity
    # task_key = storage_client.key(kind, name)

    # task['description'] = request.form['text']
    # storage_client.put(task)
    # return "SUCCESS"

@app.route('/getData', methods = ['GET'])
def getData():
    q = request.args.get('q')
    out = query(q)
    print(out)
    return out

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, port = 5005)

