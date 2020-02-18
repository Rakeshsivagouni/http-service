#!flask/bin/python

from flask import Flask, request, Response
import re
import subprocess
import sys
import json
import pprint
import logging
app = Flask(__name__)

#logging.basicConfig(format='%(asctime)s %(message)s')

port = '8080'

try:
    port = sys.argv[1]
except:
    port = '8080'


@app.route ('/')
def index():
    return ("Hello, World")


@app.route('/helloworld')
def helloworld():
    args = request.args
    name = request.args.get('name')
    if len(args) == 0:
        return ("Hello Stranger")
    else:
        converted_name = re.sub("([A-Z])", " \\1", name).strip()
        return ("Hello " + converted_name)

@app.route('/versionz')
def versionz():
    git_hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().rstrip()
    a = {"hash": git_hash}
    # return (git_hash)
    cmd = "git remote -v | head -n1 | awk '{print $2}' | sed -e 's,.*:\(.*/\)\?,,' -e 's/\.git$//'"
    project_name = subprocess.check_output(['bash','-i','-c',cmd]).decode().rstrip()
    a.update({"project_name": project_name})
    return json.dumps(a, indent=4, sort_keys='true')
    


    
if __name__ == '__main__':
    app.run(port=port, debug=True, host='0.0.0.0')
