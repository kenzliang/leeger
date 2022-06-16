from src.leeger.calculator.PointsScoredCalculator import PointsScoredCalculator
from src.leeger.calculator.parent.YearCalculator import YearCalculator
from src.leeger.decorator.validate.validators import validateYear
from src.leeger.model.Year import Year
from src.leeger.util.Deci import Deci
from src.leeger.util.YearNavigator import YearNavigator


class PlusMinusCalculator(YearCalculator):
    """
    Used to calculate all plus/minuses.
    """

    @classmethod
    @validateYear
    def getPlusMinus(cls, year: Year, **kwargs) -> dict[str, Deci]:
        """
        Plus/Minus (+/-) is used to show the net score differential for a team in Year.
        Plus/Minus = ΣA - ΣB
        WHERE:
        A = All scores by a team in a Year
        B = All scores against a team in a Year
        Returns the Plus/Minus for each team in the given Year.

        Example response:
            {
            "someTeamId": Deci("10.7"),
            "someOtherTeamId": Deci("-11.2"),
            "yetAnotherTeamId": Deci("34.1"),
            ...
            }
        """
        cls.loadFilters(year, validateYear=False, **kwargs)

        teamIdAndPlusMinus = dict()
        teamIdAndPointsScored = PointsScoredCalculator.getPointsScored(year, **kwargs)
        teamIdAndOpponentPointsScored = PointsScoredCalculator.getOpponentPointsScored(year, **kwargs)
        for teamId in YearNavigator.getAllTeamIds(year):
            teamIdAndPlusMinus[teamId] = teamIdAndPointsScored[teamId] - teamIdAndOpponentPointsScored[teamId]

        return teamIdAndPlusMinus