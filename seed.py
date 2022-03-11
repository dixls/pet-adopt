from models import Pet, connect_db
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

