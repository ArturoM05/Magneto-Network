from mongoengine import Document, StringField, DateTimeField, IntField
import datetime

class Publicacion(Document):
    user = StringField(required=True)
    text = StringField(required=True)
    likes = IntField(min_value=0)
    fecha_creacion = DateTimeField(default=datetime.datetime.now)