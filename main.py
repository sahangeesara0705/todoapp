from fastapi import FastAPI
from ariadne import gql, make_executable_schema, QueryType
from ariadne.asgi import GraphQL

type_defs = gql("""
    type Query {
        hello: String!
    }
""")

query = QueryType()

@query.field("hello")
def resolve_hello(_, info):
    return "Hello, todoapp!"

schema = make_executable_schema(type_defs, query)

app = FastAPI()
app.mount(
    "/graphql",
    GraphQL(schema, debug=True),
)