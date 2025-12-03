from helperFunctions import plot_position_stat_bar, get_player_stats, dataframe_to_png, export_player_season_png,plot_player_stat_by_week
import matplotlib.pyplot as plt

#1      
plot_position_stat_bar(2024, "RB", "rushing_yards", save_path="rb_rushing_2024.png", top_n=25)

'The leading rusher over this period is saquon barkley with around 4900'

#2
plot_player_stat_by_week(2024, 'Jalen', 'Hurts', 'passing_yards', save_path='jalen_hurts_passing_yards_2024.png')

'Jalen hurts has actually declined since 2022 where he had 5 games with 300 yards or more,'
' he followed up 2022 with a good year in 2023 where he also had 5 games with 300 or more yards,'
' but in 2024 he oinly had one game with 300 yards or more'