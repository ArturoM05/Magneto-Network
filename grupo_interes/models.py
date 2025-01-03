from mongoengine import Document, StringField, IntField, ListField, ReferenceField, DateTimeField
from cuenta.models import Usuario
import datetime


class GrupoInteres(Document):
    nombre = StringField(max_length=255, required=True)
    description = StringField(max_length=999, required=True)
    areas_interes = ListField(ReferenceField('AreaInteres'))
    members = ListField(ReferenceField('Usuario'))
    popularity = IntField(min_value=0)
    fecha_creacion = DateTimeField(default=datetime.datetime.now)

    def count_members(self):
        return len(self.members)
    
    def update_popularity(self):
        users_count = Usuario.objects().count()
        members_count = self.count_members()
        self.popularity = (members_count/users_count)*100