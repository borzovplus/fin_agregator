from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

class MyDb:
    def __init__(self,path_to_db):
        self.engine=create_engine('sqlite:///'+path_to_db)
        self.Session=sessionmaker(self.engine)
        self.session=self.Session()
        Base.metadata.create_all(self.engine)



