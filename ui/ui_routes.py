from flask import Blueprint, render_template, request, session
from appsettings import Settings
import requests, json

ui_routes = Blueprint('ui_routes', __name__, static_folder='static', template_folder='templates')


@ui_routes.route('/')
def ui_home():
    context = {
        'title': 'home'
    }
    return render_template('home.html', context=context)


@ui_routes.route('/about')
def ui_about():
    context = {
        'title': 'about'
    }
    return render_template('about.html', context=context)


@ui_routes.route('/sites')
def ui_sites():
    s = Settings()
    url = s.api_ip + ':' + s.api_port + '/api/v1/sitelist'
    formdata = {}
    records = {}
    try:
        data = requests.post(url, data=formdata)
        if data.status_code != 200:
            return
        records = data.json()
    except Exception as e:
        pass

    context = {
        'title': 'sites',
        'data': records
    }
    return render_template('sites.html', context=context)


@ui_routes.route('/site/<sitename>', methods=['GET', 'POST'])
def ui_site(sitename):
    if request.method == 'POST':
        session['days'] = request.form.get('numdays')

    s = Settings()
    site = sitename
    freq = '4PerDay'
    # Load default days.
    days = session.get('days', 15)
    if days is None:
        days = 15
    #
    url = s.api_ip + ':' + s.api_port + '/api/v1/site/{}/{}/{}'.format(site, freq, days)
    #
    formdata = {}
    records = {}
    try:
        data = requests.post(url, data=formdata)
        if data.status_code != 200:
            return
        records = data.json()
    except Exception as e:
        pass

    context = {
        'title': 'Site {}'.format(sitename),
        'data': records,
        'posturl': '/site/' + sitename,
        'def_days': days
    }
    return render_template('site.html', context=context)

