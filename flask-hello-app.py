from flask import Flask
from flask_sqlalchemy import sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:picasso0@localhost:5432/example'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
  app.run()    