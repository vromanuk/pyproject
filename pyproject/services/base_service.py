from sqlalchemy.sql import select, update
from pyproject.database import engine
from pyproject.models import Contracts, Payments


class BaseService:
    def __init__(self, model):
        self.model = model

    def is_resource_exist(self, id_: int) -> bool:
        with engine.connect() as conn:
            query = select([self.model]).where(self.model.c.id == id_)
            result = conn.execute(query).rowcount

        return result

    def get_resource_id(self, resource_id: int) -> dict:
        """
        Retrieve resource's id.

        :param resource_id: int
        :return: dict
        """
        if not self.is_resource_exist(resource_id):
            return {'Message': 'Such id does not exist'}
        with engine.connect() as conn:
            query = select([self.model]).where(self.model.c.id == resource_id)
            result = conn.execute(query).first()

            return dict(result)

    def add_new_resource(self, json_data: dict) -> dict:
        """
        Create a new resource.

        :param json_data: dict
        :return: dict
        """
        with engine.connect() as conn:
            query = self.model.insert()
            conn.execute(query, json_data)

            return {'Message': 'Created successfully'}

    def update_resource(self, json_data: dict, resource_id: int) -> dict:
        """
        Update an existing resource.

        :param json_data: dict
        :param resource_id: int
        :return: dict
        """
        if not self.is_resource_exist(resource_id):
            return {'Message': 'Such id does not exist'}
        with engine.connect() as conn:
            query = update(self.model).where(self.model.c.id == resource_id).values(**json_data)
            conn.execute(query)
            resource = self.get_resource_id(resource_id)

            return dict(resource)

    def delete_resource(self, resource_id: int) -> dict:
        """
        Delete resource.

        :param resource_id: int
        :return: dict
        """
        if not self.is_resource_exist(resource_id):
            return {'Message': 'Such id does not exist'}
        with engine.connect() as conn:
            query = self.model.delete().where(self.model.c.id == resource_id)
            conn.execute(query)

            return {'Message': f'resource {resource_id} deleted successfully'}

    def get_resources(self):
        """
        Retrieve all resources.

        :return:
        """
        with engine.connect() as conn:
            query = select([self.model])
            result = conn.execute(query).fetchall()
            json_data = [dict(i) for i in result]

            return json_data


contract_ = BaseService(Contracts)
payment_ = BaseService(Payments)
