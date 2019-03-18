from . import db


class UserProfile(db.Model):
   
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80))
    lname = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    biography = db.Column(db.String(500))
    pp = db.Column(db.String(250))
    created_on = db.Column(db.String(100))
    
    
    def __init__(self, fname, lname, gender, email,location,biography,pp,created_on):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.email = email
        self.location = location
        self.biography = biography
        self.pp = pp
        self.created_on = created_on
        

  
    def __repr__(self):
        return "User: {0} {1}".format(self.fname, self.lname)