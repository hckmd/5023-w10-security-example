class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.Text, unique = True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean)
    pets = db.relationship('Pet', backref='owner')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))