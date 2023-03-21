import pandas as pd
from datetime import datetime as dt
import matplotlib.pyplot as plt
from plotly_calplot import calplot

data = pd.read_pickle('d:/Python Work/Capstone/data/final_datasets/Total_data.pkl')

data['month_day'] = data['date_time'].dt.strftime('%m-%d')

date_of_year = data.groupby('month_day').count()
date_of_year['count'] = date_of_year['home_team']
date_of_year = date_of_year['count'].sort_values().reset_index()

date_of_year['total_date'] = '2024-' + date_of_year['month_day']
print(date_of_year['month_day'])
print(date_of_year['total_date'])

date_of_year['total_date']= pd.to_datetime(date_of_year['total_date'], format = "%Y-%m-%d")

print(date_of_year)

fig = calplot(date_of_year, x = 'total_date', y = 'count', years_title = False)
# fig.show()
fig.savefig('results/combined_calendar_heatmap.png')