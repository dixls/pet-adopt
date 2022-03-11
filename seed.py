from models import Pet, db
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

rocket = Pet(
    name="Rocket",
    species="Dog",
    age="15",
    photo_url="https://petsarticles.com/upload/content/47829/1/description-of-breed-of-a-dog-german-spitz-dog.webp",
    available=True,
)
odo = Pet(
    name="Odo",
    species="Dog",
    age="2",
    photo_url="https://cdn.discordapp.com/attachments/427992212010303488/946182972636291152/20220223_181050.jpg",
    available=False,
)
demon = Pet(
    name="Demon",
    species="Cat",
    age="7",
    photo_url="https://media.discordapp.net/attachments/888991256984825889/947921309646614569/20220228_101158.jpg",
    available=True,
)
cool = Pet(
    name="Cool Guy",
    species="Cat",
    age="3",
    photo_url="https://media.discordapp.net/attachments/888991256984825889/948612030976364624/20220302_110455.jpg",
    available=True,
)

db.session.add_all([rocket, odo, demon, cool])

db.session.commit()
