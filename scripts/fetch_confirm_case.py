import json
from collections import defaultdict
from datetime import datetime, timezone

import requests

PATH = "data/data.json"

COVID19 = "19CoV"

cities = [
    "新北市",
    "台北市",
    "桃園市",
    "彰化縣",
    "基隆市",
    "宜蘭縣",
    "台中市",
    "高雄市",
    "屏東縣",
    "南投縣",
    "台南市",
    "新竹市",
    "新竹縣",
    "雲林縣",
    "苗栗縣",
    "花蓮縣",
    "嘉義市",
    "嘉義縣",
    "連江縣",
    "金門縣",
    "台東縣",
    "澎湖縣",
]

url = "https://nidss.cdc.gov.tw/nndss/DiseaseMap_Pro"

headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://nidss.cdc.gov.tw",
    "Connection": "keep-alive",
    "Referer": "https://nidss.cdc.gov.tw/nndss/DiseaseMap?id=19CoV",
    "Save-Data": "on",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "TE": "Trailers",
}

today = datetime.today()

raw_data = {
    "pty_Q": "N",
    "pty_disease": COVID19,
    "position": "1",
    "pty_period": "y",
    "pty_y_s": today.year,
    "pty_y_e": today.year,
    "pty_m_s": "1",
    "pty_m_e": today.month,
    "pty_d_s": "1",
    "pty_d_e": today.day,
    "pty_w_s": "1",
    "pty_w_e": today.isocalendar()[1],
    "pty_sickclass_value": "determined_cnt",
    "pty_immigration": "0",
    "pty_date_type": "3",
    "pty_level": "area",
    "region_name": "",
}

data = defaultdict(dict)
total = 0

for city in cities:
    raw_data.update({"region_name": city})
    area_resp = requests.post(url, headers=headers, data=raw_data)
    area_results = area_resp.json()
    for area_result in area_results:
        data[city][area_result["code"]] = area_result["value"]
        total += area_result["value"]

result = {
    "meta": {"total": total, "last_update_at": datetime.now(timezone.utc).isoformat()},
    "data": dict(data),
}

with open(PATH, "w") as f:
    json.dump(result, f, indent=4, ensure_ascii=False)
