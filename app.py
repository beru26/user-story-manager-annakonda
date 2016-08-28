import sqlite3
from flask import Flask, g, url_for, request, flash, redirect, render_template
from connect import *

app = Flask(__name__)


@app.route('/story', methods=['GET'])
def add_story():
    """Add story"""
    return render_template('form.html', title='Add story')


@app.route('/story', methods=['POST'])
def new_story():
    """Add story"""
    db = get_db()
    db.execute("""INSERT INTO app (Story title, User story, Acceptance Criteria, Business value, Estimation)
               VALUES (?, ?, ?, ?, ?)""",
               [request.form['Story title'], request.form['User story'], request.form['Acceptance Criteria'],
                request.form['Business value'], request.form['Estimation']])
    db.commit()
    return redirect(url_for('list_stories'))


@app.route('/story/<story_id>')
def edit_story():
        pass


@app.route('/list', methods=['GET'])
def list_stories():
    """Show stories"""
    db = get_db()
    query = """SELECT * FROM app"""
    cur = db.execute(query)
    stories = cur.fetchall()
    return render_template('list.html', entries=stories)


if __name__ == '__main__':
    app.run(debug=True)
