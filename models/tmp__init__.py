#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
import os
storey = os.getenv('HBNB_TYPE_STORAGE')

if storey == "db":
    import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    import FileStorage
    storage = FileStorage()
    storage.reload()