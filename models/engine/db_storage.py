#!/usr/bin/python3
"""Create a mysql engine"""

from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    """Engine for MySQL"""

    __engine = None
    __session = None

    def __init__(self):
        """Init Engine"""

        usrnm = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(usrnm, passwd, host, db),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """all objects"""
        dic = {}
        if cls is None:
            objs = []
            classes = ['User', 'State', 'City', 'Place', 'Review', 'Amenity']
            for _class in classes:
                results = self.__session.query(eval(_class))
                for result in results:
                    objs.append(result)
        else:
            objs = self.__session.query(cls).all()
        for obj in objs:
            key = type(obj).__name__ + "." + str(obj.id)
            dic[key] = obj
        return dic

    def new(self, obj):
        """Add the object to the current database sessiont"""
        self.__session.add(obj)
        self.__session.flush()

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """Close the session in the database"""
        self.__session.close()
