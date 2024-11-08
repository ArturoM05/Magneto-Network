from mongoengine import Document, StringField, IntField, ListField, ReferenceField
from cuenta.models import Usuario

class GrupoInteres(Document):
    nombre = StringField(max_length=255, required=True)
    descrption = StringField(max_length=999, required=True)
    areas_interes = ListField(ReferenceField('AreaInteres'))
    members = ListField(ReferenceField('Usuario'))
    popularity = IntField(min_value=0)

    def update_popularity(self):
        users_count = Usuario.objects().count()
        members_count = len(self.members)
        self.popularity = (members_count/users_count)*100