from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

GENERIC_IMAGE = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"



class Pet(db.Model):
  """Pet Model"""

  __tablename__ = "pets"

  # id: auto-incrementing integer
  # name: text, required
  # species: text, required
  # photo_url: text, optional
  # age: integer, optional
  # notes: text, optional
  # available: true/false, required, should default to available

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.Text, nullable=False)
  species = db.Column(db.Text, nullable=False)
  photo_url = db.Column(db.Text)
  age = db.Column(db.Integer)
  notes = db.Column(db.Text)
  available = db.Column(db.Boolean, nullable=False, default=True)

  def image_url(self):
    """Sets photo url or defaults to generic image"""
    return self.photo_url or GENERIC_IMAGE

def connect_db(app):
  db.app=app
  db.init_app(app)