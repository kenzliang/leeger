import unittest

from src.leeger.calculator.all_time_calculator.GameOutcomeAllTime import GameOutcomeAllTime
from src.leeger.enum.MatchupType import MatchupType
from src.leeger.model.league.League import League
from src.leeger.model.league.Matchup import Matchup
from src.leeger.model.league.Week import Week
from src.leeger.model.league.Year import Year
from test.helper.prototypes import getNDefaultOwnersAndTeams, getTeamsFromOwners


class TestGameOutcomeAllTime(unittest.TestCase):

    def test_getWins_happyPath(self):
        owners, teamsA = getNDefaultOwnersAndTeams(2)
        teamsB = getTeamsFromOwners(owners)
        teamsC = getTeamsFromOwners(owners)

        matchup1_a = Matchup(teamAId=teamsA[0].id, teamBId=teamsA[1].id, teamAScore=1, teamBScore=2)
        matchup2_a = Matchup(teamAId=teamsA[0].id, teamBId=teamsA[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.PLAYOFF)
        matchup3_a = Matchup(teamAId=teamsA[0].id, teamBId=teamsA[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.CHAMPIONSHIP)
        week1_a = Week(weekNumber=1, matchups=[matchup1_a])
        week2_a = Week(weekNumber=2, matchups=[matchup2_a])
        week3_a = Week(weekNumber=3, matchups=[matchup3_a])
        yearA = Year(yearNumber=2000, teams=teamsA, weeks=[week1_a, week2_a, week3_a])

        matchup1_b = Matchup(teamAId=teamsB[0].id, teamBId=teamsB[1].id, teamAScore=1, teamBScore=2)
        matchup2_b = Matchup(teamAId=teamsB[0].id, teamBId=teamsB[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.PLAYOFF)
        matchup3_b = Matchup(teamAId=teamsB[0].id, teamBId=teamsB[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.CHAMPIONSHIP)
        week1_b = Week(weekNumber=1, matchups=[matchup1_b])
        week2_b = Week(weekNumber=2, matchups=[matchup2_b])
        week3_b = Week(weekNumber=3, matchups=[matchup3_b])
        yearB = Year(yearNumber=2001, teams=teamsB, weeks=[week1_b, week2_b, week3_b])

        matchup1_c = Matchup(teamAId=teamsC[0].id, teamBId=teamsC[1].id, teamAScore=1, teamBScore=2)
        matchup2_c = Matchup(teamAId=teamsC[0].id, teamBId=teamsC[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.PLAYOFF)
        matchup3_c = Matchup(teamAId=teamsC[0].id, teamBId=teamsC[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.CHAMPIONSHIP)
        week1_c = Week(weekNumber=1, matchups=[matchup1_c])
        week2_c = Week(weekNumber=2, matchups=[matchup2_c])
        week3_c = Week(weekNumber=3, matchups=[matchup3_c])
        yearC = Year(yearNumber=2002, teams=teamsC, weeks=[week1_c, week2_c, week3_c])

        league = League(name="TEST", owners=owners, years=[yearA, yearB, yearC])

        response = GameOutcomeAllTime.getWins(league)

        self.assertIsInstance(response, dict)
        self.assertEqual(2, len(response.keys()))
        self.assertEqual(0, response[owners[0].id])
        self.assertEqual(9, response[owners[1].id])

    def test_getWins_onlyPostSeasonIsTrue(self):
        owners, teamsA = getNDefaultOwnersAndTeams(2)
        teamsB = getTeamsFromOwners(owners)
        teamsC = getTeamsFromOwners(owners)

        matchup1_a = Matchup(teamAId=teamsA[0].id, teamBId=teamsA[1].id, teamAScore=1, teamBScore=2)
        matchup2_a = Matchup(teamAId=teamsA[0].id, teamBId=teamsA[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.PLAYOFF)
        matchup3_a = Matchup(teamAId=teamsA[0].id, teamBId=teamsA[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.CHAMPIONSHIP)
        week1_a = Week(weekNumber=1, matchups=[matchup1_a])
        week2_a = Week(weekNumber=2, matchups=[matchup2_a])
        week3_a = Week(weekNumber=3, matchups=[matchup3_a])
        yearA = Year(yearNumber=2000, teams=teamsA, weeks=[week1_a, week2_a, week3_a])

        matchup1_b = Matchup(teamAId=teamsB[0].id, teamBId=teamsB[1].id, teamAScore=1, teamBScore=2)
        matchup2_b = Matchup(teamAId=teamsB[0].id, teamBId=teamsB[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.PLAYOFF)
        matchup3_b = Matchup(teamAId=teamsB[0].id, teamBId=teamsB[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.CHAMPIONSHIP)
        week1_b = Week(weekNumber=1, matchups=[matchup1_b])
        week2_b = Week(weekNumber=2, matchups=[matchup2_b])
        week3_b = Week(weekNumber=3, matchups=[matchup3_b])
        yearB = Year(yearNumber=2001, teams=teamsB, weeks=[week1_b, week2_b, week3_b])

        matchup1_c = Matchup(teamAId=teamsC[0].id, teamBId=teamsC[1].id, teamAScore=1, teamBScore=2)
        matchup2_c = Matchup(teamAId=teamsC[0].id, teamBId=teamsC[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.PLAYOFF)
        matchup3_c = Matchup(teamAId=teamsC[0].id, teamBId=teamsC[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.CHAMPIONSHIP)
        week1_c = Week(weekNumber=1, matchups=[matchup1_c])
        week2_c = Week(weekNumber=2, matchups=[matchup2_c])
        week3_c = Week(weekNumber=3, matchups=[matchup3_c])
        yearC = Year(yearNumber=2002, teams=teamsC, weeks=[week1_c, week2_c, week3_c])

        league = League(name="TEST", owners=owners, years=[yearA, yearB, yearC])

        response = GameOutcomeAllTime.getWins(league, onlyPostSeason=True)

        self.assertIsInstance(response, dict)
        self.assertEqual(2, len(response.keys()))
        self.assertEqual(0, response[owners[0].id])
        self.assertEqual(6, response[owners[1].id])

    def test_getWins_onlyRegularSeasonIsTrue(self):
        owners, teamsA = getNDefaultOwnersAndTeams(2)
        teamsB = getTeamsFromOwners(owners)
        teamsC = getTeamsFromOwners(owners)

        matchup1_a = Matchup(teamAId=teamsA[0].id, teamBId=teamsA[1].id, teamAScore=1, teamBScore=2)
        matchup2_a = Matchup(teamAId=teamsA[0].id, teamBId=teamsA[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.PLAYOFF)
        matchup3_a = Matchup(teamAId=teamsA[0].id, teamBId=teamsA[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.CHAMPIONSHIP)
        week1_a = Week(weekNumber=1, matchups=[matchup1_a])
        week2_a = Week(weekNumber=2, matchups=[matchup2_a])
        week3_a = Week(weekNumber=3, matchups=[matchup3_a])
        yearA = Year(yearNumber=2000, teams=teamsA, weeks=[week1_a, week2_a, week3_a])

        matchup1_b = Matchup(teamAId=teamsB[0].id, teamBId=teamsB[1].id, teamAScore=1, teamBScore=2)
        matchup2_b = Matchup(teamAId=teamsB[0].id, teamBId=teamsB[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.PLAYOFF)
        matchup3_b = Matchup(teamAId=teamsB[0].id, teamBId=teamsB[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.CHAMPIONSHIP)
        week1_b = Week(weekNumber=1, matchups=[matchup1_b])
        week2_b = Week(weekNumber=2, matchups=[matchup2_b])
        week3_b = Week(weekNumber=3, matchups=[matchup3_b])
        yearB = Year(yearNumber=2001, teams=teamsB, weeks=[week1_b, week2_b, week3_b])

        matchup1_c = Matchup(teamAId=teamsC[0].id, teamBId=teamsC[1].id, teamAScore=1, teamBScore=2)
        matchup2_c = Matchup(teamAId=teamsC[0].id, teamBId=teamsC[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.PLAYOFF)
        matchup3_c = Matchup(teamAId=teamsC[0].id, teamBId=teamsC[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.CHAMPIONSHIP)
        week1_c = Week(weekNumber=1, matchups=[matchup1_c])
        week2_c = Week(weekNumber=2, matchups=[matchup2_c])
        week3_c = Week(weekNumber=3, matchups=[matchup3_c])
        yearC = Year(yearNumber=2002, teams=teamsC, weeks=[week1_c, week2_c, week3_c])

        league = League(name="TEST", owners=owners, years=[yearA, yearB, yearC])

        response = GameOutcomeAllTime.getWins(league, onlyRegularSeason=True)

        self.assertIsInstance(response, dict)
        self.assertEqual(2, len(response.keys()))
        self.assertEqual(0, response[owners[0].id])
        self.assertEqual(3, response[owners[1].id])

    def test_getWins_onlyChampionshipIsTrue(self):
        owners, teamsA = getNDefaultOwnersAndTeams(2)
        teamsB = getTeamsFromOwners(owners)
        teamsC = getTeamsFromOwners(owners)

        matchup1_a = Matchup(teamAId=teamsA[0].id, teamBId=teamsA[1].id, teamAScore=1, teamBScore=2)
        matchup2_a = Matchup(teamAId=teamsA[0].id, teamBId=teamsA[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.PLAYOFF)
        matchup3_a = Matchup(teamAId=teamsA[0].id, teamBId=teamsA[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.CHAMPIONSHIP)
        week1_a = Week(weekNumber=1, matchups=[matchup1_a])
        week2_a = Week(weekNumber=2, matchups=[matchup2_a])
        week3_a = Week(weekNumber=3, matchups=[matchup3_a])
        yearA = Year(yearNumber=2000, teams=teamsA, weeks=[week1_a, week2_a, week3_a])

        matchup1_b = Matchup(teamAId=teamsB[0].id, teamBId=teamsB[1].id, teamAScore=1, teamBScore=2)
        matchup2_b = Matchup(teamAId=teamsB[0].id, teamBId=teamsB[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.PLAYOFF)
        matchup3_b = Matchup(teamAId=teamsB[0].id, teamBId=teamsB[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.CHAMPIONSHIP)
        week1_b = Week(weekNumber=1, matchups=[matchup1_b])
        week2_b = Week(weekNumber=2, matchups=[matchup2_b])
        week3_b = Week(weekNumber=3, matchups=[matchup3_b])
        yearB = Year(yearNumber=2001, teams=teamsB, weeks=[week1_b, week2_b, week3_b])

        matchup1_c = Matchup(teamAId=teamsC[0].id, teamBId=teamsC[1].id, teamAScore=1, teamBScore=2)
        matchup2_c = Matchup(teamAId=teamsC[0].id, teamBId=teamsC[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.PLAYOFF)
        matchup3_c = Matchup(teamAId=teamsC[0].id, teamBId=teamsC[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.CHAMPIONSHIP)
        week1_c = Week(weekNumber=1, matchups=[matchup1_c])
        week2_c = Week(weekNumber=2, matchups=[matchup2_c])
        week3_c = Week(weekNumber=3, matchups=[matchup3_c])
        yearC = Year(yearNumber=2002, teams=teamsC, weeks=[week1_c, week2_c, week3_c])

        league = League(name="TEST", owners=owners, years=[yearA, yearB, yearC])

        response = GameOutcomeAllTime.getWins(league, onlyChampionship=True)

        self.assertIsInstance(response, dict)
        self.assertEqual(2, len(response.keys()))
        self.assertEqual(0, response[owners[0].id])
        self.assertEqual(3, response[owners[1].id])

    def test_getWins_yearNumberStartGivenWeekNumberStartGiven(self):
        owners, teamsA = getNDefaultOwnersAndTeams(2)
        teamsB = getTeamsFromOwners(owners)
        teamsC = getTeamsFromOwners(owners)

        matchup1_a = Matchup(teamAId=teamsA[0].id, teamBId=teamsA[1].id, teamAScore=1, teamBScore=2)
        matchup2_a = Matchup(teamAId=teamsA[0].id, teamBId=teamsA[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.PLAYOFF)
        matchup3_a = Matchup(teamAId=teamsA[0].id, teamBId=teamsA[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.CHAMPIONSHIP)
        week1_a = Week(weekNumber=1, matchups=[matchup1_a])
        week2_a = Week(weekNumber=2, matchups=[matchup2_a])
        week3_a = Week(weekNumber=3, matchups=[matchup3_a])
        yearA = Year(yearNumber=2000, teams=teamsA, weeks=[week1_a, week2_a, week3_a])

        matchup1_b = Matchup(teamAId=teamsB[0].id, teamBId=teamsB[1].id, teamAScore=1, teamBScore=2)
        matchup2_b = Matchup(teamAId=teamsB[0].id, teamBId=teamsB[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.PLAYOFF)
        matchup3_b = Matchup(teamAId=teamsB[0].id, teamBId=teamsB[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.CHAMPIONSHIP)
        week1_b = Week(weekNumber=1, matchups=[matchup1_b])
        week2_b = Week(weekNumber=2, matchups=[matchup2_b])
        week3_b = Week(weekNumber=3, matchups=[matchup3_b])
        yearB = Year(yearNumber=2001, teams=teamsB, weeks=[week1_b, week2_b, week3_b])

        matchup1_c = Matchup(teamAId=teamsC[0].id, teamBId=teamsC[1].id, teamAScore=1, teamBScore=2)
        matchup2_c = Matchup(teamAId=teamsC[0].id, teamBId=teamsC[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.PLAYOFF)
        matchup3_c = Matchup(teamAId=teamsC[0].id, teamBId=teamsC[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.CHAMPIONSHIP)
        week1_c = Week(weekNumber=1, matchups=[matchup1_c])
        week2_c = Week(weekNumber=2, matchups=[matchup2_c])
        week3_c = Week(weekNumber=3, matchups=[matchup3_c])
        yearC = Year(yearNumber=2002, teams=teamsC, weeks=[week1_c, week2_c, week3_c])

        league = League(name="TEST", owners=owners, years=[yearA, yearB, yearC])

        response = GameOutcomeAllTime.getWins(league, yearNumberStart=2001, weekNumberStart=2)

        self.assertIsInstance(response, dict)
        self.assertEqual(2, len(response.keys()))
        self.assertEqual(0, response[owners[0].id])
        self.assertEqual(5, response[owners[1].id])

    def test_getWins_yearNumberEndGivenWeekNumberEndGiven(self):
        owners, teamsA = getNDefaultOwnersAndTeams(2)
        teamsB = getTeamsFromOwners(owners)
        teamsC = getTeamsFromOwners(owners)

        matchup1_a = Matchup(teamAId=teamsA[0].id, teamBId=teamsA[1].id, teamAScore=1, teamBScore=2)
        matchup2_a = Matchup(teamAId=teamsA[0].id, teamBId=teamsA[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.PLAYOFF)
        matchup3_a = Matchup(teamAId=teamsA[0].id, teamBId=teamsA[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.CHAMPIONSHIP)
        week1_a = Week(weekNumber=1, matchups=[matchup1_a])
        week2_a = Week(weekNumber=2, matchups=[matchup2_a])
        week3_a = Week(weekNumber=3, matchups=[matchup3_a])
        yearA = Year(yearNumber=2000, teams=teamsA, weeks=[week1_a, week2_a, week3_a])

        matchup1_b = Matchup(teamAId=teamsB[0].id, teamBId=teamsB[1].id, teamAScore=1, teamBScore=2)
        matchup2_b = Matchup(teamAId=teamsB[0].id, teamBId=teamsB[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.PLAYOFF)
        matchup3_b = Matchup(teamAId=teamsB[0].id, teamBId=teamsB[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.CHAMPIONSHIP)
        week1_b = Week(weekNumber=1, matchups=[matchup1_b])
        week2_b = Week(weekNumber=2, matchups=[matchup2_b])
        week3_b = Week(weekNumber=3, matchups=[matchup3_b])
        yearB = Year(yearNumber=2001, teams=teamsB, weeks=[week1_b, week2_b, week3_b])

        matchup1_c = Matchup(teamAId=teamsC[0].id, teamBId=teamsC[1].id, teamAScore=1, teamBScore=2)
        matchup2_c = Matchup(teamAId=teamsC[0].id, teamBId=teamsC[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.PLAYOFF)
        matchup3_c = Matchup(teamAId=teamsC[0].id, teamBId=teamsC[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.CHAMPIONSHIP)
        week1_c = Week(weekNumber=1, matchups=[matchup1_c])
        week2_c = Week(weekNumber=2, matchups=[matchup2_c])
        week3_c = Week(weekNumber=3, matchups=[matchup3_c])
        yearC = Year(yearNumber=2002, teams=teamsC, weeks=[week1_c, week2_c, week3_c])

        league = League(name="TEST", owners=owners, years=[yearA, yearB, yearC])

        response = GameOutcomeAllTime.getWins(league, yearNumberEnd=2001, weekNumberEnd=2)

        self.assertIsInstance(response, dict)
        self.assertEqual(2, len(response.keys()))
        self.assertEqual(0, response[owners[0].id])
        self.assertEqual(5, response[owners[1].id])

    def test_getWins_yearNumberStartGivenWeekNumberStartGivenAndYearNumberEndGivenWeekNumberEndGiven(self):
        owners, teamsA = getNDefaultOwnersAndTeams(2)
        teamsB = getTeamsFromOwners(owners)
        teamsC = getTeamsFromOwners(owners)
        teamsD = getTeamsFromOwners(owners)

        matchup1_a = Matchup(teamAId=teamsA[0].id, teamBId=teamsA[1].id, teamAScore=1, teamBScore=2)
        matchup2_a = Matchup(teamAId=teamsA[0].id, teamBId=teamsA[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.PLAYOFF)
        matchup3_a = Matchup(teamAId=teamsA[0].id, teamBId=teamsA[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.CHAMPIONSHIP)
        week1_a = Week(weekNumber=1, matchups=[matchup1_a])
        week2_a = Week(weekNumber=2, matchups=[matchup2_a])
        week3_a = Week(weekNumber=3, matchups=[matchup3_a])
        yearA = Year(yearNumber=2000, teams=teamsA, weeks=[week1_a, week2_a, week3_a])

        matchup1_b = Matchup(teamAId=teamsB[0].id, teamBId=teamsB[1].id, teamAScore=1, teamBScore=2)
        matchup2_b = Matchup(teamAId=teamsB[0].id, teamBId=teamsB[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.PLAYOFF)
        matchup3_b = Matchup(teamAId=teamsB[0].id, teamBId=teamsB[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.CHAMPIONSHIP)
        week1_b = Week(weekNumber=1, matchups=[matchup1_b])
        week2_b = Week(weekNumber=2, matchups=[matchup2_b])
        week3_b = Week(weekNumber=3, matchups=[matchup3_b])
        yearB = Year(yearNumber=2001, teams=teamsB, weeks=[week1_b, week2_b, week3_b])

        matchup1_c = Matchup(teamAId=teamsC[0].id, teamBId=teamsC[1].id, teamAScore=1, teamBScore=2)
        matchup2_c = Matchup(teamAId=teamsC[0].id, teamBId=teamsC[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.PLAYOFF)
        matchup3_c = Matchup(teamAId=teamsC[0].id, teamBId=teamsC[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.CHAMPIONSHIP)
        week1_c = Week(weekNumber=1, matchups=[matchup1_c])
        week2_c = Week(weekNumber=2, matchups=[matchup2_c])
        week3_c = Week(weekNumber=3, matchups=[matchup3_c])
        yearC = Year(yearNumber=2002, teams=teamsC, weeks=[week1_c, week2_c, week3_c])

        matchup1_d = Matchup(teamAId=teamsD[0].id, teamBId=teamsD[1].id, teamAScore=1, teamBScore=2)
        matchup2_d = Matchup(teamAId=teamsD[0].id, teamBId=teamsD[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.PLAYOFF)
        matchup3_d = Matchup(teamAId=teamsD[0].id, teamBId=teamsD[1].id, teamAScore=1, teamBScore=2,
                             matchupType=MatchupType.CHAMPIONSHIP)
        week1_d = Week(weekNumber=1, matchups=[matchup1_d])
        week2_d = Week(weekNumber=2, matchups=[matchup2_d])
        week3_d = Week(weekNumber=3, matchups=[matchup3_d])
        yearD = Year(yearNumber=2003, teams=teamsD, weeks=[week1_d, week2_d, week3_d])

        league = League(name="TEST", owners=owners, years=[yearA, yearB, yearC, yearD])

        response = GameOutcomeAllTime.getWins(league, yearNumberStart=2001, weekNumberStart=2, yearNumberEnd=2002,
                                              weekNumberEnd=2)

        self.assertIsInstance(response, dict)
        self.assertEqual(2, len(response.keys()))
        self.assertEqual(0, response[owners[0].id])
        self.assertEqual(4, response[owners[1].id])
