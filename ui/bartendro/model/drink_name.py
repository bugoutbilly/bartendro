# -*- coding: utf-8 -*-
from sqlalchemy.orm import mapper, relationship
from sqlalchemy import Table, Column, Integer, String, MetaData, Unicode, UnicodeText, UniqueConstraint, Text
from sqlalchemy.ext.declarative import declarative_base
from bartendro.utils import session, metadata

Base = declarative_base(metadata=metadata)
class DrinkName(Base):
    """
    Name of a drink, complete with a sortname
    """

    __tablename__ = 'drink_name'
    id = Column(Integer, primary_key=True)
    name = Column(UnicodeText, nullable=False)
    sortname = Column(UnicodeText, nullable=False)
    is_common = Column(Integer, default=False)
 
    query = session.query_property()

    def __init__(self, name = u'', sortname = u'', is_common = False):
        self.name = name
        self.sortname = sortname
        self.is_common = is_common
        session.add(self)

    def json(self):
        return { 
                 'id' : self.id, 
                 'name' : self.name,
                 'sortname' : self.sortname,
                 'is_common' : self.is_common
               }

    def __repr__(self):
        return "<DrinkName(%d,'%s')>" % (self.id, self.name)

