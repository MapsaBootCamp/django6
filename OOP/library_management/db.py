import pickle

class BaseQuery:

    def loadall(self, filename):
        with open(filename, "rb") as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break
    

    def get(self, unique_search_params, unique_data):
        pass


    def filter(self):
        pass





class QueryUsers(BaseQuery):
    pass
