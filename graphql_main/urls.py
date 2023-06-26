from django.http import JsonResponse  # нужен для того чтобы возвращать результат как json
from graphene_django.views import GraphQLView  # это нужно для обработки представлений
from .schema import schema #определение графа (ядро, сердце)
from django.urls import path

class MyGraphQLView(GraphQLView):
    def execute_graphql_request(self, request, data, query, variables, operation_name, show_graphiql=False):
        return super().execute_graphql_request(request, data, query, variables, operation_name, show_graphiql)
    

def graphql_view(request):
    view = MyGraphQLView.as_view(graphiql=True, schema=schema)
    return view(request)


urlpatterns = [
    path('', graphql_view),
]