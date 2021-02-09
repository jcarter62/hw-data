from flask import Flask, jsonify, send_from_directory, session, request
from flask_bootstrap import Bootstrap
from appsettings import Settings
from os import path
from ui.ui_routes import ui_routes
from sess_data import Log

app = Flask(__name__)

env_set = Settings()
app.secret_key = env_set.session_secret_key
env_set = None

app.register_blueprint(ui_routes, url_prefix='')
Bootstrap(app)

@app.before_request
def app_before_request():
    req = request
    if req is None:
        return
    url = request.url
    l = Log(session)
    l.exec(url)
    session['last_request'] = url


@app.route('/')
def rootPath():
    return ''

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(path.join(app.root_path, 'static'), 'favicon.ico')

if __name__ == '__main__':
    from waitress import serve
    s = Settings()
    serve(app, host=s.ip, port=s.port, threads=8)