from graphene.relay import Node

from ..types import MongoengineObjectType
from .models import Article, Editor, Player, Reporter


class EditorType(MongoengineObjectType):
    class Meta:
        model = Editor


class ArticleType(MongoengineObjectType):
    class Meta:
        model = Article


class PlayerType(MongoengineObjectType):
    class Meta:
        model = Player


class ReporterType(MongoengineObjectType):
    class Meta:
        model = Reporter


class ArticleNode(MongoengineObjectType):

    class Meta:
        model = Article
        interfaces = (Node,)


class EditorNode(MongoengineObjectType):

    class Meta:
        model = Editor
        interfaces = (Node,)


class PlayerNode(MongoengineObjectType):

    class Meta:
        model = Player
        interfaces = (Node,)


class ReporterNode(MongoengineObjectType):

    class Meta:
        model = Reporter
        interfaces = (Node,)

