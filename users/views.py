from rest_framework.views import APIView
from rest_framework.response import Response

# GET
# POST
# PUT
# PATCH
# DELETE
# CRUD
# Create
# Read/Retrieve
# Update
# Delete/Destroy

# class UserView(APIView):
#     def get(self, *args, **kwargs):
#         return Response('Hello from get')
#
#     def post(self, *args, **kwargs):
#         print(self.request.data)
#         print(self.request.query_params.dict())
#         return Response('Hello from post')
#
#     def put(self, *args, **kwargs):
#         return Response('Hello from put')
#
#     def patch(self, *args, **kwargs):
#         return Response('Hello from patch')
#
#     def delete(self, *args, **kwargs):
#         return Response('Hello from delete')
#
#
# class UserTestView(APIView):
#     def get(self, *args, **kwargs):
#         print(kwargs)
#         return Response('ok')

users = [
    {"name": "Max", "age": 15},
    {"name": "Kira", "age": 20},
    {"name": "Olha", "age": 30},
    {"name": "Kamila", "age": 25},
]


class UserListCreateView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print('__init__')

    def get(self, *args, **kwargs):
        return Response(users)

    def post(self, *args, **kwargs):
        user = self.request.data
        users.append(user)
        return Response(user)


class UserRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')

        try:
            user = users[pk]
        except IndexError:
            return Response('Not Found')

        return Response(user)

    def put(self, *args, **kwargs):
        new_user = self.request.data
        pk = kwargs.get('pk')
        try:
            user = users[pk]
        except IndexError:
            return Response('Not Found')
        user['name'] = new_user['name']
        user['age'] = new_user['age']
        return Response(new_user)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')

        try:
            del users[pk]
        except IndexError:
            return Response('Not Found')

        return Response('deleted')
