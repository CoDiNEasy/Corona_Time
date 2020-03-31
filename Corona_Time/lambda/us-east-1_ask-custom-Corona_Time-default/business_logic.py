import pandas as pd

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/' \
      'csse_covid_19_daily_reports/03-24-2020.csv'

def get_data_for_country(cur_country):
    # type: str -> str

    df = pd.read_csv(url, error_bad_lines=False)

    return cur_country + "blah"
