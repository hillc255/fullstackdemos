from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_sqlalchemy import sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:picasso0@localhost:5432/hello'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# db = sqlalchemy.SQLAlchemy(engine)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<User {self.id}, {self.name}>'
        #return f'<Person name: {self.name}>'    


db.create_all()    

@app.route('/')
def index():
    person = Person.query.first()
    return 'Hello ' + person.name

if __name__ == '__main__':
  app.run()    