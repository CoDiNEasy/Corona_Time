import json
import requests
from datetime import datetime, timedelta


def get_data_for_country(cur_country):
    # type str -> str

    response = requests.get("https://pkgstore.datahub.io/core/covid-19/countries-aggregated_json/data"
                            "/f5c53a1772cc835a18c50eb32ea2e9c7/countries-aggregated_json.json")
    data = json.loads(response.text)

    today_date = datetime.today()
    modified_date = today_date - timedelta(days=1)
    modified_date = modified_date.strftime('%Y-%m-%d')

    cur_country_confirmed = "unknown"
    cur_country_deaths = "unknown"
    cur_country_recovered = "unknown"

    for row in data:
        if row['Country'] == cur_country:
            if row['Date'] == modified_date:
                cur_country_confirmed = row['Confirmed']
                cur_country_deaths = row['Deaths']
                cur_country_recovered = row['Recovered']

    output = "{} has {} confirmed cases, {} deaths, and {} recovered cases.".format(cur_country,
                                                                                    cur_country_confirmed,
                                                                                    cur_country_deaths,
                                                                                    cur_country_recovered
                                                                                    )

    return output
