# __author__ = 'jakey'

import pymysql
from data.country_province_city import data1

connect = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='buzhidao', db='hyou8', charset='utf8')
cur = connect.cursor()

for item in data1:
    province_sql = "insert into province_city(NAME , pid) VALUES ('%s', %d)" % (item["name"], 0)
    try:
        cur.execute(province_sql)
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()

    province_id = "select max(id) from province_city"
    cur.execute(province_id)
    cur_province_id = cur.fetchone()[0]
    for city in item["cities"]:
        city_sql = "insert into province_city(NAME , pid) VALUES ('%s', %d)" % (city["name"], cur_province_id)
        try:
            cur.execute(city_sql)
            connect.commit()
        except Exception as e:
            print(e)
            connect.rollback()

        city_id = "select max(id) from province_city"
        cur.execute(city_id)
        cur_city_id = cur.fetchone()[0]
        for county in city["county"]:
            county_sql = "insert into province_city(NAME , pid) VALUES ('%s', %d)" % (county, cur_city_id)
            try:
                cur.execute(county_sql)
                connect.commit()
            except Exception as e:
                print(e)
                connect.rollback()
