from mongoengine import Document, StringField, DateTimeField, IntField, ReferenceField, ListField
import datetime

class Publicacion(Document):
    user = ReferenceField('Usuario')
    text = StringField(required=True)
    likes = IntField(min_value=0)
    group = ReferenceField('GrupoInteres')
    comments = ListField(ReferenceField('Comentario'))  
    fecha_creacion = DateTimeField(default=datetime.datetime.now)

class Comentario(Document):
    user = ReferenceField('Usuario')
    text = StringField(required=True)
    likes = IntField(min_value=0)
    fecha_creacion = DateTimeField(default=datetime.datetime.now)