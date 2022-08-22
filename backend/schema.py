# import strawberry

# from typing import List

# from backend.types import Player


# def get_player() -> Player:
#     return Player(
#         user_name="chatooka",
#         first_name="cha",
#         last_name="tooka",
#         password="rat",
#     )

# @strawberry.type
# class Query:
#     players: List[Player] = strawberry.field(resolver=get_player)

# schema = strawberry.Schema(Query)