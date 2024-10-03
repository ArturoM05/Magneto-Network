from mongoengine import Document, StringField, EmailField, DateTimeField
import datetime

class Usuario(Document):
    nombre = StringField(max_length=50, required=True)
    email = EmailField(required=True, unique=True)
    phone_number = StringField(max_length=10,required=True) 
    birthdate = DateTimeField(default=datetime.datetime.now)
    description = StringField(required=True)
    password = StringField(required=True)
    fecha_creacion = DateTimeField(default=datetime.datetime.now)