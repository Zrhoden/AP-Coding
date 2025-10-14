import pandas as pd
import nfl_data_py as nfl

from helperFunctions import get_team_records

scheduels = nfl.import_schedules([2024])

print(scheduels.columns.tolist())


records = get_team_records(2024)

print(records)