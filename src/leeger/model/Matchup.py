from dataclasses import dataclass
from decimal import Decimal

from src.leeger.model.abstract.UniqueId import UniqueId


@dataclass(kw_only=True)
class Matchup(UniqueId):
    teamAId: str
    teamBId: str
    teamAScore: Decimal
    teamBScore: Decimal