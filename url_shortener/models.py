import string
from datetime import datetime
from random import choices

from .extensions import db

class Link(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    original_url=db.Column(db.String(512)) 
    short_url=db.Column(db.String(3),unique=True)
    visits= db.Column(db.Integer, default=0)
    date_created= db.Column(db.DateTime, default=datetime.now)

    def __init__(self,**kargs):
        super().__init__(**kargs)
        self.short_url='something'

    def generate_short_link(self):
        characters=string.digits+string.ascii_letters
        short_url=''.join(choices(characters, k=3))

        link=self.query.filter_by(short_url=short_url).first()

        if link:
            return self.generate_short_link()
        
        return short_url

