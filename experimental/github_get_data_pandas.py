import pandas as pd

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/' \
      'csse_covid_19_daily_reports/03-24-2020.csv'
df = pd.read_csv(url)

cur_country_row = df.loc[(df['Country_Region'] == "France") & (df['Combined_Key'] == "France")]
cur_country_confirmed = cur_country_row['Confirmed'].values[0]
cur_country_deaths = cur_country_row['Deaths'].values[0]
cur_country_recovered = cur_country_row['Recovered'].values[0]


print("France has {} confirmed cases, {} deaths, and {} recovered cases.".format(cur_country_confirmed,
      cur_country_deaths, cur_country_recovered))
