from mongoengine import Document, StringField

class AreaInteres(Document):
    nombre = StringField(max_length=50, required=True)