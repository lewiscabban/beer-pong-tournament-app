import uvicorn
import strawberry

from typing import List
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

@strawberry.type
class Player:
    user_name: str
    first_name: str
    last_name: str
    password: str

def get_player() -> Player:
    return Player(
        user_name="chatooka",
        first_name="cha",
        last_name="tooka",
        password="rat",
    )

@strawberry.type
class Query:
    players: List[Player] = strawberry.field(resolver=get_player)

schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

# uvicorn.run(app, host="localhost", port=5000)


def main():
    print("Hello World!")

if __name__ == "__main__":
    main()