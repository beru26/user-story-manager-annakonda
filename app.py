from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/story')
def add_story():
        return render_template('form.html')


@app.route('/story/<story_id>')
def edit_story():
        pass


@app.route('/and/list')
def product_backlog():
        pass


if __name__ == '__main__':
    app.run(debug=True)
