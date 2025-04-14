from func import *

dict_check = {
    "985": [
        "10003",
        "10001",
        "10614",
        "10335",
        "10384",
        "10533",
        "10558",
        "10486",
        "10246",
        "10487",
        "10284",
        "10286",
        "10610",
        "10247",
        "10055",
        "10422",
        "10002",
        "10248",
        "10561",
        "10183",
        "10269",
        "10532",
        "10611",
        "10698",
        "10213",
        "18213",
        "10358",
        "10423",
        "10141",
        "10056",
        "10027",
        "10145",
        "10007",
        "10006",
        "10730",
        "10699",
        "10712",
        "10019",
        "10052",
        "19248",
        "91002",
        "19246",
        "7321"
    ],
    "国优计划": [
        "10001",
        "10003",
        "10027",
        "19027",
        "10056",
        "10141",
        "10183",
        "10200",
        "10246",
        "10248",
        "10247",
        "10269",
        "10284",
        "10286",
        "10335",
        "10384",
        "10486",
        "10487",
        "10511",
        "10533",
        "10558",
        "10611",
        "10635",
        "10698",
        "10718",
        "10730",
        "10006",
        "10007",
        "14430",
        "10285",
        "10300",
        "10532",
        "10542",
        "10610",
        "10213",
        "10699",
        "10422",
        "14325",
        "10295",
        "10028",
        "10319",
        "10574"
    ],
    "部属师范": [
        "10027",
        "10269",
        "10200",
        "10511",
        "10718",
        "10635"
    ],
    "211": [
        "10003",
        "10001",
        "10614",
        "10335",
        "10384",
        "10533",
        "10558",
        "10486",
        "10246",
        "10487",
        "10284",
        "10286",
        "10610",
        "10247",
        "10055",
        "10422",
        "10002",
        "10248",
        "10561",
        "10183",
        "10269",
        "10532",
        "10611",
        "10698",
        "10213",
        "18213",
        "10358",
        "10423",
        "10141",
        "10056",
        "10027",
        "10145",
        "10007",
        "10006",
        "10730",
        "10699",
        "10712",
        "10019",
        "10052",
        "19248",
        "91002",
        "19246",
        "7321",
        "10635",
        "10559",
        "10033",
        "10280",
        "10285",
        "10613",
        "10497",
        "10459",
        "10295",
        "10520",
        "10697",
        "10255",
        "10403",
        "10651",
        "10294",
        "10290",
        "10030",
        "10511",
        "10589",
        "10251",
        "10359",
        "19359",
        "10710",
        "10701",
        "10288",
        "10272",
        "10054",
        "10079",
        "10008",
        "10287",
        "10004",
        "10386",
        "10053",
        "10574",
        "10036",
        "10034",
        "10319",
        "10357",
        "10080",
        "10718",
        "10217",
        "10013",
        "10673",
        "10005",
        "10542",
        "10200",
        "10593",
        "10140",
        "10112",
        "10151",
        "10504",
        "10657",
        "10271",
        "10626",
        "10022",
        "10759",
        "10184",
        "10010",
        "10045",
        "10307",
        "10316",
        "10225",
        "10043",
        "10126",
        "10026",
        "10755",
        "10224",
        "10749",
        "10425",
        "10062",
        "10694",
        "10743",
        "11414",
        "10491",
        "11413",
        "11415",
        "19635",
        "19414",
        "91030",
        "90026"
    ]
}

school_data = execute_sql_sentence(
    sentence=f'select * from teacher_data_0 where "采集年份" == 2024'
)

output_985 = []
output_211 = []
for data in school_data:
    if data[15] in dict_check["985"]:
        output_985.append(data)
    if data[15] in dict_check["211"]:
        output_211.append(data)

save_excel(two_dimension_list=output_985, excel_name="985名单")
save_excel(two_dimension_list=output_211, excel_name="211名单")
