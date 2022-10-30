"""Initializes a variable storage to create
a unique filestorage instance for the application
Also, the __objects class attribute
of the FileStorage class is alwaya loaded with all
objects on the __file_path class attribute
of the FileStorage class"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload
