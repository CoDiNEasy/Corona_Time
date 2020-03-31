import pandas as pd

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/' \
      'csse_covid_19_daily_reports/03-24-2020.csv'
df = pd.read_csv(url, error_bad_lines=False)

CA_data = df.loc[(df['Country_Region'] == 'Canada') & (df['Combined_Key'] == 'Canada')]

print(CA_data)
