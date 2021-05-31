from credit_card import db

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(64), nullable = False)
    age = db.Column(db.Integer(), nullable = False)
    gender = db.Column(db.Integer(), nullable = False)
    dependent = db.Column(db.Integer(), nullable = False)
    Edu_Level = db.Column(db.Integer(), nullable = False)
    marige = db.Column(db.Integer(), nullable = False)
    income = db.Column(db.Integer(), nullable = False)
    
    def __repr__(self):
        return f"User {self.user_id}, {self.username}, {self.age}, {self.gender}, {self.dependent}, {self.Edu_Level}, {self.marige}, {self.income}"


def add_user(raw_user) :
    # 파싱
    new_user = User(
        username = raw_user.username,
        age = raw_user.age,
        gender = raw_user.gender,
        dependent = raw_user.dependent,
        Edu_Level = raw_user.Edu_Level,
        marige = raw_user.marige,
        income = raw_user.income,
        )
    # 있으면 저장 안함
    if User.query.filter(User.username == new_user.username).first() == None :
        db.session.add(new_user)
        db.session.commit()
    return User.query.filter(
            (User.username == new_user.username) 
            and (User.age == new_user.age) 
            and (User.Edu_Level == new_user.Edu_Level)
            and (User.marige == new_user.marige)
            ).first()

def get_users() :
    return User.query.all()

def get_user(username):
    return User.query.filter(User.username == username).first()

def get_user1(user_id):
    return User.query.filter(User.user_id == user_id).first()

def delete_user(newuser_id) :
    user = User.query.filter(User.user_id == newuser_id).first()
    db.session.delete(user)
    db.session.commit()

