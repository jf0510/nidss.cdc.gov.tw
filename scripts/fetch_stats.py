import requests

PATH = "data/{file_name}"

urls = {
    "covid19_tw_sampling_hospital": "http://od.cdc.gov.tw/icb/%E6%8C%87%E5%AE%9A%E6%8E%A1%E6%AA%A2%E9%86%AB%E9%99%A2%E6%B8%85%E5%96%AE.csv",
    "covid19_tw_stats": "https://od.cdc.gov.tw/eic/covid19/covid19_tw_stats.csv",
    "covid19_tw_age_gender__month": "https://od.cdc.gov.tw/eic/Age_County_Gender_19Cov.csv",
    "covid19_tw_age_gender__date": "https://od.cdc.gov.tw/eic/Day_Confirmation_Age_County_Gender_19CoV.csv",
    "covid19_tw_specimen": "https://od.cdc.gov.tw/eic/covid19/covid19_tw_specimen.csv",
}

for key, url in urls.items():
    resp = requests.get(url)
    content = resp.content
    csv_file = open(PATH.format(file_name=f"{key}.csv"), "wb")
    csv_file.write(content)
    csv_file.close()
