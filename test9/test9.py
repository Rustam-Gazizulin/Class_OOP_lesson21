from abc import ABC, abstractmethod


class Resource(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass


# class BadFile(Resource):
#     def __init__(self):
#         pass
#
#     def get_file(self):
#         pass
#
#     def put_file(self):
#         pass

class GoodFile(Resource):
    def __init__(self):
        pass

    def read(self):
        pass

    def write(self):
        pass


my_file = GoodFile()

my_file.read()
