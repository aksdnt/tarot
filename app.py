from flask import Flask, render_template
from functions import get_tarot_definition

tarot_app = Flask(__name__)

@tarot_app.route('/')
def render_html_for_home_page():
    return render_template('home.html')

@tarot_app.route('/answer')
def render_html_for_answer_page():
    answer_data = get_tarot_definition('The Fool')
    title = answer_data['cards'][0]['name']
    definition = answer_data['cards'][0]['desc']
    return render_template('answer.html', definition=definition, title=title)

