from helperFunctions import get_team_records, get_season_Results_By_team, weeklyPlayerStats

Qb= weeklyPlayerStats(2024,'WR')

print(Qb)

# 1. Who are the top 5 quarterbacks by passing yards? What’s their average completion percentage (cmp_pct)?
'Jared Goff, Joe Burrow, Baker Mayfield, Patrick Mahomes, Lamar Jackson, 69.2'
# 2. What might a high cmp_pct tell you about a quarterback’s style of play?
'It could tell you that theyre more accurate, or it can tell you that they may be a pocket passer'
# 3. Which RB had the highest rushing yards in 2024? Who had the best yards per carry (rush_ypc)?
'Saquan Barkley, Derrick Henery'
# 4. If a RB has high rush_yards but low rush_ypc, what could that mean?
'It could mean that theyre getting a lot of attempts and not doing much with them'
#5. Find a player who has the best recieving yards on the fewest passing attempts
'Ladd McConkey'