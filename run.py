from app import app, db
from app.models import User

with app.app_context():
    db.create_all()

    # Create a default user for testing purposes
    if not User.query.filter_by(username='admin').first():
        admin_user = User(username='admin')
        admin_user.set_password('admin_password')
        db.session.add(admin_user)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
