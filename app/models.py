from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()

class User(db.Document):
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.StringField(unique=True, required=True)
    password = db.StringField(required=True) 

    def to_json(self):
        return {
            "id": str(self.id),
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
        }

class Template(db.Document):
    template_name = db.StringField(required=True)
    subject = db.StringField(required=True)
    body = db.StringField(required=True)
    user = db.ReferenceField(User, required=True)

    def to_json(self):
        return {
            "id": str(self.id),
            "template_name": self.template_name,
            "subject": self.subject,
            "body": self.body,
            "user_id": str(self.user.id)
        }
