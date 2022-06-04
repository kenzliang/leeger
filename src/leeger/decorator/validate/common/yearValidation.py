from src.leeger.decorator.validate.common import teamValidation, weekValidation
from src.leeger.exception.InvalidYearFormatException import InvalidYearFormatException
from src.leeger.model.Year import Year


def checkAllTypes(year: Year) -> None:
    """
    Checks all types that are within the Year object.
    """

    if type(year.yearNumber) != int:
        raise InvalidYearFormatException("Year number must be type 'int'.")
    if type(year.teams) != list:
        raise InvalidYearFormatException("Year teams must be type 'list'.")
    if type(year.weeks) != list:
        raise InvalidYearFormatException("Year weeks must be type 'list'.")

    for team in year.teams:
        teamValidation.checkAllTypes(team)

    for week in year.weeks:
        weekValidation.checkAllTypes(week)


def checkOnlyOneChampionshipWeekInYear(year: Year) -> None:
    """
    Checks that there is a maximum of 1 championship week in the given Year.
    """
    championshipWeekCount = 0
    for week in year.weeks:
        if week.isChampionshipWeek:
            championshipWeekCount += 1
        if championshipWeekCount > 1:
            raise InvalidYearFormatException(f"Year {year.yearNumber} has more than 1 championship week.")