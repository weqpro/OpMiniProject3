'''
module of RepositoryBase implementation
'''
from abc import ABC, abstractmethod
from typing import Type, TypeVar, Generic, List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

T = TypeVar("T")

class RepositoryBase(ABC, Generic[T]):
    '''
    Class of RepositoryBase implementation
    '''

    def __init__(self, session: Session, model: Type[T]):
        self.session = session
        self.model = model


    @abstractmethod
    def create(self, model_instance: T) -> T:
        '''
        Adds new object to database
        '''
        try:
            self.session.add(model_instance)
            self.session.commit()
            self.session.refresh(model_instance)
            return model_instance
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e


    @abstractmethod
    def delete_by_id(self, obj_id : int) -> None:
        '''
        Deletes object by id
        '''
        query = self.session.query(self.model)
        obj = query.get(obj_id)
        if obj:
            self.session.delete(obj)
            self.session.commit()


    @abstractmethod
    def read_by_id(self, obj_id: int) -> T | None:
        '''
        Gets object by id
        '''
        query = self.session.query(self.model)
        return query.filter(self.model.obj_id == obj_id).first()


    @abstractmethod
    def update(self, obj_id: int, scheme: dict) -> T | None:
        '''
        Partly updates object
        '''
        query = self.session.query(self.model)
        obj = query.filter(self.model.obj_id == obj_id).first()
        if obj:
            for key, value in scheme.items():
                setattr(obj, key, value)
            self.session.commit()
            self.session.refresh(obj)
            return obj
        return None


    @abstractmethod
    def get_all(self) -> List[T]:
        '''
        Gets all requests from database
        '''
        query = self.session.query(self.model)
        return query.all()
