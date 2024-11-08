from mongoengine import Document, StringField, IntField
from cuenta.models import Usuario

class AreaInteres(Document):
    nombre = StringField(max_length=255, required=True)
    interested = IntField(min_value=0)
    popularity = IntField(min_value=0)

    def update_popularity(self):
        users_count = Usuario.objects().count()
        self.popularity = (self.interested/users_count)*100
