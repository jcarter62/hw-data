from flask import Flask, jsonify, send_from_directory
from flask_bootstrap import Bootstrap
from appsettings import Settings
from os import path
from ui.ui_routes import ui_routes

app = Flask(__name__)
app.register_blueprint(ui_routes, url_prefix='')
Bootstrap(app)

@app.route('/')
def rootPath():
    return ''

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(path.join(app.root_path, 'static'), 'favicon.ico')

if __name__ == '__main__':
    from waitress import serve
    s = Settings()
    serve(app, host=s.ip, port=s.port)