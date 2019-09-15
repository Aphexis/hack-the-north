import requests
import base64
import json
from flask import Flask, request, abort, render_template
from google.cloud import storage
import binascii
import collections
import datetime
import hashlib
import sys
# pip install six
from six.moves.urllib.parse import quote
# pip install google-auth
from google.oauth2 import service_account
import compile

storage_client = storage.Client()
app = Flask(__name__)
google_credentials = service_account.Credentials.from_service_account_file( "C:\\Users\\alex.zhang\\Downloads\\My First Project-9b83f8fdfa25.json")
bucket = storage_client.get_bucket("hackthenorth-lads")
def generate_signed_url(bucket_name, object_name,
                        expiration, http_method='GET', query_parameters=None,
                        headers=None):

    if expiration > 604800:
        print('Expiration Time can\'t be longer than 604800 seconds (7 days).')
        sys.exit(1)

    escaped_object_name = quote(object_name, safe='')
    canonical_uri = '/{}/{}'.format(bucket_name, escaped_object_name)

    datetime_now = datetime.datetime.utcnow()
    request_timestamp = datetime_now.strftime('%Y%m%dT%H%M%SZ')
    datestamp = datetime_now.strftime('%Y%m%d')

    
    client_email = google_credentials.service_account_email
    credential_scope = '{}/auto/storage/goog4_request'.format(datestamp)
    credential = '{}/{}'.format(client_email, credential_scope)

    if headers is None:
        headers = dict()
    headers['host'] = 'storage.googleapis.com'

    canonical_headers = ''
    ordered_headers = collections.OrderedDict(sorted(headers.items()))
    for k, v in ordered_headers.items():
        lower_k = str(k).lower()
        strip_v = str(v).lower()
        canonical_headers += '{}:{}\n'.format(lower_k, strip_v)

    signed_headers = ''
    for k, _ in ordered_headers.items():
        lower_k = str(k).lower()
        signed_headers += '{};'.format(lower_k)
    signed_headers = signed_headers[:-1]  # remove trailing ';'

    if query_parameters is None:
        query_parameters = dict()
    query_parameters['X-Goog-Algorithm'] = 'GOOG4-RSA-SHA256'
    query_parameters['X-Goog-Credential'] = credential
    query_parameters['X-Goog-Date'] = request_timestamp
    query_parameters['X-Goog-Expires'] = expiration
    query_parameters['X-Goog-SignedHeaders'] = signed_headers

    canonical_query_string = ''
    ordered_query_parameters = collections.OrderedDict(
        sorted(query_parameters.items()))
    for k, v in ordered_query_parameters.items():
        encoded_k = quote(str(k), safe='')
        encoded_v = quote(str(v), safe='')
        canonical_query_string += '{}={}&'.format(encoded_k, encoded_v)
    canonical_query_string = canonical_query_string[:-1]  # remove trailing ';'

    canonical_request = '\n'.join([http_method,
                                   canonical_uri,
                                   canonical_query_string,
                                   canonical_headers,
                                   signed_headers,
                                   'UNSIGNED-PAYLOAD'])

    canonical_request_hash = hashlib.sha256(
        canonical_request.encode()).hexdigest()

    string_to_sign = '\n'.join(['GOOG4-RSA-SHA256',
                                request_timestamp,
                                credential_scope,
                                canonical_request_hash])

    signature = binascii.hexlify(
        google_credentials.signer.sign(string_to_sign)
    ).decode()

    host_name = 'https://storage.googleapis.com'
    signed_url = '{}{}?{}&X-Goog-Signature={}'.format(host_name, canonical_uri,
                                                      canonical_query_string,
                                                      signature)
    return signed_url

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

number = 1
@app.route('/uploadData', methods = ['POST'])
def upload():
    args = compile.compile('Unravel.mid','BB.mid')
    global number
    url = "song" + str(number)
    print(url)
    blob = bucket.blob(url)
    number += 1
    blob.upload_from_filename(args)
    output = json.dumps({"link": generate_signed_url("hackthenorth-lads", url, 600000)})
    return output

@app.route('/downloadData', methods = ['GET'])
def download():
    return generate_signed_url("hackthenorth-lads", request.args.get('songName'), 600000)


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

