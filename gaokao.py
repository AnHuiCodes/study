from copy import deepcopy
import time
from pprint import pprint
import json
import requests
import pandas as pd

headers = {
    'authority': 'm.quark.cn',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'origin': 'https://vt.quark.cn',
    'referer': 'https://vt.quark.cn/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 QuarkPC/1.5.1.72',
}


def run():
    result = []
    schools = ['巴中职业技术学院', '常州纺织服装职业技术学院', '重庆工信职业学院', '重庆健康职业学院',
               '重庆五一职业技术学院', '大兴安岭职业学院', '福建农业职业技术学院', '贵州工贸职业学院',
               '贵州农业职业学院', '贵州盛华职业学院', '贵州文化旅游职业学院', '河北旅游职业学院', '莱芜职业技术学院',
               '益阳职业技术学院']
    for year in ['2020', '2021', '2022', '2023']:
        for school in schools:
            params = {
                'scName': 'general_entity_college_domestic',
                'province': '贵州',
                'year': year,
                'batch': '专科批',
                'genre': '理科',
                'guid': '97afcec6-5db1-11e5-ae7d-d43d7e6fab60',
                'university_name': school,  # 巴中职业技术学院
                'q': school,  # 巴中职业技术学院
            }
            url = 'https://m.quark.cn/oapi/quark/general_entity_college_domestic/getZhuanYeFenShuXian'
            try:
                response = requests.get(url, params=params, headers=headers)
                res_data = response.json()
                data = res_data.get('data')
                school_data = data.get('data')
                major_scorelines = school_data.get('major_scorelines')
                major_scorelines = json.loads(major_scorelines)
                data_list = major_scorelines.get('data')
                column = data_list.get('column')
                if not column:
                    continue
                data_source = data_list.get('dataSource')
                base_data = {
                    '年份': school_data.get('cur_year'),
                    '学校': school,
                }
                major = column[0].get('label')
                low_score_and_rank = column[1].get('label')
                luqurenshu = column[2].get('label')
                low_score_diff = column[3].get('label')
                for each in data_source:
                    tmp = deepcopy(base_data)
                    if 'major' in each:
                        tmp[major] = each.get('major')
                    if 'low_score_and_rank' in each:
                        tmp[low_score_and_rank] = each.get('low_score_and_rank')
                    if 'luqurenshu' in each:
                        tmp[luqurenshu] = each.get('luqurenshu')
                    if 'low_score_diff' in each:
                        tmp[low_score_diff] = each.get('low_score_diff')
                    print(tmp)
                    result.append(tmp)
                time.sleep(2)
            except Exception as e:
                print(e)
    df = pd.DataFrame(result)
    df.to_csv('C:\\Users\\anhui\\Desktop\\专业.csv')


if __name__ == '__main__':
    run()
