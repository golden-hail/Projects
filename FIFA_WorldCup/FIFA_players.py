import pandas as pd

# match_events = pd.read_csv('data/match_events.csv')
# match_lineups = pd.read_csv('data/match_lineups.csv')
# match_team_stats = pd.read_csv('data/match_team_stats.csv')
# matches = pd.read_csv('data/matches.csv')
# matches_detailed = pd.read_csv('data/matches_detailed.csv')
# referees = pd.read_csv('data/referees.csv')
# squads_and_players = pd.read_csv('data/squads_and_players.csv')
# tournament_stages = pd.read_csv('data/tournament_stages.csv')
# venues = pd.read_csv('data/venues.csv')

player_stats = pd.read_csv('data/player_stats.csv')
teams = pd.read_csv('data/teams.csv')

# goals from players... see how good they are on their team vs the league.. 
# can we project how many goals we'd *think* they'd score if they played more?
# that might be hard because each goalie has a different skill and each cddefense does too.. this is a ML thing :( much time 

# Team Player Stats


# Goals per team - start here
goals_per_team = player_stats.groupby('team_id')['goals'].sum().reset_index()

goals_per_country = pd.merge(
    goals_per_team, teams, how = 'inner', on = 'team_id')[
        ['goals', 'team_name']].sort_values(by = 'goals', ascending = False)

player_team_goals = player_stats[['player_name', 'team_id', 'goals']].sort_values(by = ['team_id', 'goals'], ascending = False)
        
# Goalie stats per team
keeper_stats = player_stats.loc[player_stats['position'] == 'GK', ['player_name', 'team_id', 'saves', 'goals_conceded']]

keeper_data = pd.merge(
    keeper_stats, teams, how = 'inner', on = 'team_id')[
        ['player_name','saves','goals_conceded','team_name']].sort_values(
            by = 'saves', ascending = False)
            
saves_per_team = keeper_data.groupby('team_name')[['saves', 'goals_conceded']].sum()





# players who got red cards for each team?




# correlate with how good each team is? 

