from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/story'):
    def add_story():
        pass


@app.route('/story/<story_id>'):
    def edit_story():
        pass


@app.route('/and/list'):
    def product_backlog():
        pass


if __name__ == '__main__':
    app.run()
