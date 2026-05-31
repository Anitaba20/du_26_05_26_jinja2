from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://neondb_owner:npg_I5zs0OAwrtVm@ep-old-sun-ala7ftma-pooler.c-3.eu-central-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Author(db.Model):
    __tablename__ = 'authors'

    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    bio = db.Column(db.String)


@app.route('/authors')
def authors():
    authors = Author.query.all()
    return render_template('authors.html', authors=authors)


if __name__ == '__main__':
    app.run()
