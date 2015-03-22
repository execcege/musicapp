import datetime
from peewee import *
import json


sqldatabase = SqliteDatabase('data.db')


class BaseModel(Model):
    class Meta:
        database = sqldatabase

    date_created = DateTimeField(db_column='date_created', default=datetime.datetime.now())
    date_modified = DateTimeField(db_column='date_modified', default=datetime.datetime.now())

    def save(self, *args, **kwargs):
        self.date_modified = datetime.datetime.now()
        return super(BaseModel, self).save(*args, **kwargs)

    def getDict(self):
        r = {}
        for k in self._data.keys():
            r[k] = unicode(getattr(self, k)).encode("UTF-8")
        return r

    def __str__(self):
        r = {}
        for k in self._data.keys():
            r[k] = unicode(getattr(self, k)).encode("UTF-8")
        return unicode(r)

    def __getitem__(self, key):
        for k in self._data.keys():
            if k == key:
                return unicode(getattr(self, k)).encode("UTF-8")
        return None

    def toJSON(self):
        r = {}
        for k in self._data.keys():
            try:
                r[k] = str(getattr(self, k))
            except:
                r[k] = json.dumps(getattr(self, k))
        return r
