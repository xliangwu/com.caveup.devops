import requests
from requests.auth import HTTPBasicAuth
import json
import pandas as pd


def generate_sonar_report():
    url = "https://code.hexasino.com/sonar/api/measures/search?projectKeys=com.hexasino:bluestreak,CMB-IKE,CMB-IKENLP,HEXASINO-CMB-LCIDE,HEXASINO-CMB-LCIDI,HEXASINO-CMB-LCIE,HEXASINO-CMB-LCIEM,HEXASINO-CMB-LCIMS,HEXASINO-CMB-LCISE,HEXASINO-CMB-LRQAE,HEXASINO-CMB-TBIKE,HEXASINO-CMB-TBIKE-BBS,HEXASINO-CMB-TBIKE-DOC,com.hexasino:information-extraction,HEXASINO-PANDA2,com.cmb.pbike:ike,org.hhxr:super-spark&metricKeys=alert_status,bugs,reliability_rating,vulnerabilities,security_rating,code_smells,sqale_rating,duplicated_lines_density,coverage,ncloc,ncloc_language_distribution"

    http_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }

    response = requests.get(url, headers=http_header, auth=HTTPBasicAuth('7d86626ac041d79de1b261af0ed632a7889fdb8d', ''))
    if response.status_code == 200:
        response_text = response.text
        response_data = json.loads(response_text)
        measures = response_data['measures']
        if measures and len(measures) >= 0:
            parse_sonar_measures(measures)
    else:
        print("Call sonar request has exception")


def parse_sonar_measures(measures: []):
    columns = []
    projects = []
    values_dict = dict()
    for measure in measures:
        metric = measure['metric']
        value = measure['value']
        component = measure['component']
        if metric not in columns:
            columns.append(metric)
        if component not in projects:
            projects.append(component)

        values_dict[(component, metric)] = value

    data = []
    for project in projects:
        row = []
        for col in columns:
            row.append(values_dict.get((project, col)))

        data.append(row)

    # init data frame
    df = pd.DataFrame(data, index=projects, columns=columns)
    df.to_excel("snoar_report.xlsx")


if __name__ == '__main__':
    generate_sonar_report()
