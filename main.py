from flask import Flask, redirect, url_for, render_template
import random
import string


def gen_rand(length: int, include=string.printable) -> str:
    return ''.join(random.choice(include) for _ in range(length))


def gen_data(n: int):
    for _ in range(n):
        yield {
            'title': gen_rand(8),
            'slug': gen_rand(8, include=string.ascii_letters),
            'description': ' '.join(gen_rand(10) for __ in range(100)),
            'tips': tuple(gen_rand(12) for __ in range(3)),
        }


data = tuple(gen_data(40))
app = Flask(__name__)


@app.route('/')
def root():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    return render_template('home.html', data=data)


@app.route('/<slug>')
def show_topic(slug):
    topics = tuple(filter(lambda topic: topic['slug'] == slug, data))
    if len(topics) == 0:
        return '<h1>No such topic</h1>'
    return render_template('topic.html', **topics[0])


if __name__ == '__main__':
    app.run(debug=True)
