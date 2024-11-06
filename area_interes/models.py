from mongoengine import Document, StringField, IntField

class AreaInteres(Document):
    nombre = StringField(max_length=255, required=True)
    popularity = IntField(min_value=0)