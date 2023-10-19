import os
from flask import Flask, redirect, url_for, render_template
from scraper import get_carbon_level

solutions = [
    {
        'title': 'CO\u2082 reduction',
        'slug': 'co2-reduction',
        'short-description': 'Individuals can reduce their carbon footprint to reduce the buildup of CO\u2082 in the atmosphere.',
    },
    {
        'title': 'Reduction of other greenhouse gases',
        'slug': 'greenhouse-gas-reduction',
        'short-description': 'Gases such as methane and CFCs also contribute to the enhanced greenhouse effect and their use must be reduced.',
    },
    {
        'title': 'Land use management',
        'slug': 'land-use-management',
        'short-description': "Forests and other ecosystems play an important role in absorbing CO\u2082 from the atmosphere and are referred to as 'carbon sinks'. These must be promoted.",
    },
    {
        'title': 'Technological innovation',
        'slug': 'technological-innovation',
        'short-description': 'New technologies are being developed to help reduce greenhouse gas emissions.',
    },
]

app = Flask(__name__)


@app.route('/')
def root():
    return redirect(url_for(the_problem.__name__))


@app.route('/the-problem')
def the_problem():
    return render_template('the-problem.html', solutions=solutions)


@app.route('/co2-reduction')
def co2_reduction():
    data = get_carbon_level()
    if not data['status']:
        data = False
    return render_template('co2-reduction.html', data=data)


@app.route('/greenhouse-gas-reduction')
def greenhouse_gas_reduction():
    return render_template('greenhouse-gas-reduction.html')


@app.route('/land-use-management')
def land_use_management():
    return render_template('land-use-management.html')


@app.route('/technological-innovation')
def technological_innovation():
    return render_template('technological-innovation.html')


@app.errorhandler(404)
def page_not_found(_):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
