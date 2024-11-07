from mongoengine import Document, StringField, DateTimeField, IntField, ReferenceField
import datetime

class Publicacion(Document):
    user = ReferenceField('Usuario')
    text = StringField(required=True)
    likes = IntField(min_value=0)
    fecha_creacion = DateTimeField(default=datetime.datetime.now)