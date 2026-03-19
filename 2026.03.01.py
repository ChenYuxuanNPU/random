from collections import Counter

from func import *

result_grade_8 = read_xlsx_to_list(file_path=fr"2026.03.01/八年级.xlsx")[1:]
# 七年级：考号，选择题分值，选择题情况，英文打字，中文打字，Windows分值，Windows情况，总分，学片

school_id_dict = dict({
    '106': '广师大实中', '广师大实中': '106', '105': '江村中学', '江村中学': '105',
    '107': '江高三中', '江高三中': '107', '338': '培文学校', '培文学校': '338', '089': '神山中学',
    '神山中学': '089', '090': '石龙中学', '石龙中学': '090', '295': '珠江中学', '珠江中学': '295',
    '350': '广州龙外', '广州龙外': '350', '121': '空港中学东校区', '空港中学东校区': '121',
    '125': '空港中学西校区', '空港中学西校区': '125', '344': '六中实验福和公办',
    '六中实验福和公办': '344', '340': '六中实验福和民办', '六中实验福和民办': '340',
    '122': '六中实验空港校区', '六中实验空港校区': '122', '124': '市73中', '市73中': '124',
    '323': '白云实验初中部', '白云实验初中部': '323', '165': '大朗中学', '大朗中学': '165',
    '331': '广大附实北校区', '广大附实北校区': '331', '286': '广大附实南校区',
    '广大附实南校区': '286', '356': '广附云湖实验', '广附云湖实验': '356',
    '347': '广云外语初中部', '广云外语初中部': '347', '309': '华侨中学', '华侨中学': '309',
    '172': '元培实验中学', '元培实验中学': '172', '327': '南悦中学', '南悦中学': '327',
    '177': '彭中初中', '彭中初中': '177', '167': '庆丰实验学校初中部',
    '庆丰实验学校初中部': '167', '015': '石井中学', '石井中学': '015', '164': '市114中',
    '市114中': '164', '205': '市65中明德', '市65中明德': '205', '182': '市65中桃园',
    '市65中桃园': '182', '310': '市65中同德', '市65中同德': '310', '377': '市65中江府',
    '市65中江府': '377', '288': '云雅实验学校', '云雅实验学校': '288', '359': '省实白云',
    '省实白云': '359', '306': '金广实验学校', '金广实验学校': '306', '299': '广外实验',
    '广外实验': '299', '312': '华赋太和', '华赋太和': '312', '135': '龙归中学', '龙归中学': '135',
    '069': '市115中', '市115中': '069', '136': '市70中', '市70中': '136', '321': '穗丰中学',
    '穗丰中学': '321', '068': '太和中学', '太和中学': '068', '339': '源雅学校', '源雅学校': '339',
    '221': '白云外国语中学', '白云外国语中学': '221', '146': '白云中学汇侨校区',
    '白云中学汇侨校区': '146', '355': '白云中学棠景校区', '白云中学棠景校区': '355',
    '013': '广园中学', '广园中学': '013', '231': '黄石学校', '黄石学校': '231', '196': '景泰中学',
    '景泰中学': '196', '232': '龙江中学', '龙江中学': '232', '188': '民航中学', '民航中学': '188',
    '186': '三元里中学', '三元里中学': '186', '145': '市67中', '市67中': '145', '144': '新市中学',
    '新市中学': '144', '187': '梓元岗中学', '梓元岗中学': '187', '314': '东平学校',
    '东平学校': '314', '076': '华联学校', '华联学校': '076', '272': '华新学校', '华新学校': '272',
    '246': '嘉禾中学', '嘉禾中学': '246', '258': '京师实验', '京师实验': '258', '334': '培英鹤洞',
    '培英鹤洞': '334', '315': '培英岭南', '培英岭南': '315', '353': '培英云城', '培英云城': '353',
    '297': '平沙培英初中', '平沙培英初中': '297', '166': '实验外语学校', '实验外语学校': '166',
    '014': '同和中学', '同和中学': '014', '266': '新都中学', '新都中学': '266',
    '016': '颜乐天中学', '颜乐天中学': '016', '349': '颐和实验', '颐和实验': '349',
    '265': '云英实验', '云英实验': '265', '322': '珠江实验', '珠江实验': '322', '336': '铁一白云',
    '铁一白云': '336', '077': '启明中学', '启明中学': '077', '289': '成龙中学', '成龙中学': '289',
    '051': '大同中学初中部', '大同中学初中部': '051', '035': '二师实验初中',
    '二师实验初中': '035', '036': '龙岗中学', '龙岗中学': '036', '037': '新和中学',
    '新和中学': '037', '046': '竹料三中', '竹料三中': '046', '045': '竹料一中北校区',
    '竹料一中北校区': '045', '044': '竹料一中南校区', '竹料一中南校区': '044', '培英中学科技城校区': '369',
    '369': '培英中学科技城校区', '培英实验同和校区': '368', '368': '培英实验同和校区', '370': '民航学校人和校区',
    '民航学校人和校区': '370'
})

check = []
ans_grade_8 = "C,A,A,D,C,C,B,C,B,C,A,D,C,B,B,B,B,B,B,B,B,C,C,C,B,D,C,B,A,D,B,C,C,C,C,A,A,B,A,C,".split(",")[:-1]

result = {}

# 这里统计所有选择题的正确率
choice_result = []
for i in range(len(ans_grade_8)):
    correct_ans = ans_grade_8[i]
    temp = []

    for item in result_grade_8:
        #  school_name = school_id_dict.get(str(result_grade_8[i][0])[2:5], "我草")
        temp.append(item[2].split(",")[:-1][i])

    choice_result.append(f"{Counter(temp)[correct_ans] / len(result_grade_8) * 100:.2f}%")

for i, k in enumerate(choice_result):
    print(fr"第{i + 1}题正确率：{k}")

print("")
print(fr"全区选择题均分：{sum(int(item[1]) for item in result_grade_8) / len(result_grade_8):.2f}")
print("")
for area in ["新市", "永平", "石井", "江高", "人和", "太和", "钟落潭", ]:
    print(
        fr"{area}选择题均分：{sum(int(item[1]) for item in result_grade_8 if item[6] == area) / sum(1 for item in result_grade_8 if item[6] == area):.2f}")

print("")
print(fr"全区英文打字均分：{sum(float(item[3]) for item in result_grade_8) / len(result_grade_8):.2f}")
print("")
for area in ["新市", "永平", "石井", "江高", "人和", "太和", "钟落潭", ]:
    print(
        fr"{area}英文打字均分：{sum(float(item[3]) for item in result_grade_8 if item[6] == area) / sum(1 for item in result_grade_8 if item[6] == area):.2f}")

print("")
print(fr"全区中文打字均分：{sum(float(item[4]) for item in result_grade_8) / len(result_grade_8):.2f}")
print("")
for area in ["新市", "永平", "石井", "江高", "人和", "太和", "钟落潭", ]:
    print(
        fr"{area}中文打字均分：{sum(float(item[4]) for item in result_grade_8 if item[6] == area) / sum(1 for item in result_grade_8 if item[6] == area):.2f}")

# 统计打字前几和后几的学校
print("")
num = 5
output = {}
for item in result_grade_8:
    school_name = school_id_dict.get(str(item[0])[2:5], "我草")
    if school_name not in output.keys():
        output[school_name] = {
            "英文打字成绩": [float(item[3])],
            "英文打字均分": [],
            "英文打字0分数": 0,
            "英文打字0分占比": 0,
            "中文打字成绩": [float(item[4])],
            "中文打字均分": [],
            "中文打字0分数": 0,
            "中文打字0分占比": 0,
        }
    else:
        output[school_name]["英文打字成绩"].append(float(item[3]))
        output[school_name]["中文打字成绩"].append(float(item[4]))

    if str(item[3]) == "0":
        output[school_name]["英文打字0分数"] += 1
    if str(item[4]) == "0":
        output[school_name]["中文打字0分数"] += 1

for key in output.keys():
    output[key]["英文打字均分"] = sum(output[key]["英文打字成绩"]) / len(output[key]["英文打字成绩"])
    output[key]["中文打字均分"] = sum(output[key]["中文打字成绩"]) / len(output[key]["中文打字成绩"])
    output[key]["英文打字0分占比"] = output[key]["英文打字0分数"] / len(output[key]["英文打字成绩"])
    output[key]["中文打字0分占比"] = output[key]["中文打字0分数"] / len(output[key]["中文打字成绩"])

sorted_schools_chn = sorted(
    output.items(),
    key=lambda x: x[1]["英文打字均分"],  # 按均分排序
    reverse=True  # 从高到低
)
print(f"===== 英文打字均分 前{num}名 =====")
for school, info in sorted_schools_chn[:num]:
    print(f"{school}：{info['英文打字均分']:.1f} 分")

# 输出后 N 名
print(f"\n===== 英文打字均分 后{num}名 =====")
for school, info in sorted_schools_chn[-num:]:
    print(f"{school}：{info['英文打字均分']:.1f} 分")

sorted_schools_chn = sorted(
    output.items(),
    key=lambda x: x[1]["中文打字均分"],  # 按均分排序
    reverse=True  # 从高到低
)
print(f"===== 中文打字均分 前{num}名 =====")
for school, info in sorted_schools_chn[:num]:
    print(f"{school}：{info['中文打字均分']:.1f} 分")

# 输出后 N 名
print(f"\n===== 中文打字均分 后{num}名 =====")
for school, info in sorted_schools_chn[-num:]:
    print(f"{school}：{info['中文打字均分']:.1f} 分")

sorted_schools_eng = sorted(
    output.items(),
    key=lambda x: x[1]["英文打字0分占比"],  # 按均分排序
    reverse=True  # 从高到低
)

print("")
print(f"===== 英文打字0分率 前{num}名 =====")
for school, info in sorted_schools_eng[:num]:
    print(f"{school}：{info['英文打字0分占比'] * 100:.2f}%")

sorted_schools_chn = sorted(
    output.items(),
    key=lambda x: x[1]["中文打字0分占比"],  # 按均分排序
    reverse=True  # 从高到低
)

print("")
print(f"===== 中文打字0分率 前{num}名 =====")
for school, info in sorted_schools_chn[:num]:
    print(f"{school}：{info['中文打字0分占比'] * 100:.2f}%")

# 统计某几题正确率前几的学校
print("")
no = 5
std_answer = ans_grade_8[no - 1]
output_1 = {}
for item in result_grade_8:
    school_name = school_id_dict.get(str(item[0])[2:5], "我草")
    if school_name not in output_1.keys():
        output_1[school_name] = {
            f"第{no}题答案列": [item[2].split(",")[no - 1]],
            f"第{no}题正确率": 0
        }
    else:
        output_1[school_name][f"第{no}题答案列"].append(item[2].split(",")[no - 1])

for key in output_1.keys():
    output_1[key][f"第{no}题正确率"] = Counter(output_1[key][f"第{no}题答案列"])[std_answer] / len(
        output_1[key][f"第{no}题答案列"])

sorted_schools = sorted(
    output_1.items(),
    key=lambda x: x[1][f"第{no}题正确率"],  # 按均分排序
    reverse=True  # 从高到低
)

# 输出前 N 名
print(f"===== 第{no}题正确率 前{5}名 =====")
for school, info in sorted_schools[:5]:
    print(f"{school}：{info[f'第{no}题正确率'] * 100:.2f}%")

# 输出后 N 名
print(f"\n===== 第{no}题正确率 后{5}名 =====")
for school, info in sorted_schools[-5:]:
    print(f"{school}：{info[f'第{no}题正确率'] * 100:.2f}%")
