from app import app
from models import db, User, ClothingItem

with app.app_context():
    u = User(username="admin")
    u.set_password("admin123")
    db.session.add(u)

    db.session.add_all([
        ClothingItem(name="Camiseta básica", gender="masculino", size="M", color="Branca", type="camiseta", season="verão", price=39.90),
        ClothingItem(name="Vestido floral", gender="feminino", size="P", color="Azul", type="vestido", season="primavera", price=99.90),
        ClothingItem(name="Bermuda jeans", gender="masculino", size="G", color="Azul", type="bermuda", season="verão", price=59.90),
        ClothingItem(name="Saia midi", gender="feminino", size="M", color="Preta", type="saia", season="outono", price=79.90)
    ])

    db.session.commit()
