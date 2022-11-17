#!/usr/bin/python3
"""Class of database storage"""
from sqlalchemy import MetaData
from sqlalchemy.orm import Session
import os

class DBStorage:
    meta = MetaData()
    
    """Database storage class"""
    __engine = None
    __session = None
    def __init__(self):
        """Instatntiates db storage"""
        from sqlalchemy import create_engine
        import sys
        database_url = os.getenv('HBNB_MYSQL_DB')
        sql_pwd = os.getenv('HBNB_MYSQL_PWD')
        sql_usr = os.getenv('HBNB_MYSQL_USER')
        sql_host = os.getenv('HBNB_MYSQL_HOST')
        env = os.getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'\
            .format(sql_usr, sql_pwd, database_url), pool_pre_ping=True)
        if env == "test":
            for tbl in reversed(meta.sorted_tables):
                engine.execute(tbl.delete())

    def all(self, cls=None):
        """query on the current database session"""
        session = Session(self.__engine)
        some_dict = {}
        key = obj.__class__.__name__ + "." + obj.id
        some_dict[key]=obj

    def new(self, obj):
        """add obj to current db"""
    
    def save(self):
        """commit all changes"""

    def delete(self, obj=None):
        """del obj if exists"""
        if obj is not None:
            # create key to check if it exists
            key = obj.__class__.__name__ + "." + obj.id
            # if key in the dictionary then we use the key to delete the obj
            if key in self.__objects:
                self.__objects.pop(key)
        else:
            return

    def reload(self):
        """Reload it"""

    def close(self):
        """close it"""
        self.__session.remove()