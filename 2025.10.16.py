from func import *

school_code = {
    '广师大实中': '106', '江村中学': '105', '江高三中': '107', '培文学校': '338', '神山中学': '089', '石龙中学': '090',
    '珠江中学': '295', '广州龙外': '350', '空港中学东校区': '121', '空港中学西校区': '125', '六中实验福和公办': '344',
    '六中实验福和民办': '340', '六中实验空港校区': '122', '市73中': '124', '白云实验初中部': '323', '大朗中学': '165',
    '广大附实北校区': '331', '广大附实南校区': '286', '广附云湖实验': '356', '广云外语初中部': '347', '华侨中学': '309',
    '元培实验中学': '172', '南悦中学': '327', '彭中初中': '177', '庆丰实验学校初中部': '167', '石井中学': '015',
    '市114中': '164', '市65中明德': '205', '市65中桃园': '182', '市65中同德': '310', '云雅实验学校': '288',
    '省实白云': '359', '金广实验学校': '306', '广外实验': '299', '华赋太和': '312', '龙归中学': '135', '市115中': '069',
    '市70中': '136', '穗丰中学': '321', '太和中学': '068', '源雅学校': '339', '白云外国语中学': '221',
    '白云中学汇侨校区': '146', '白云中学棠景校区': '355', '广园中学': '013', '黄石学校': '231', '景泰中学': '196',
    '龙江中学': '232', '民航中学': '188', '三元里中学': '186', '市67中': '145', '新市中学': '144', '梓元岗中学': '187',
    '东平学校': '314', '华联学校': '076', '华新学校': '272', '嘉禾中学': '246', '京师实验': '258', '培英鹤洞': '334',
    '培英岭南': '315', '培英云城': '353', '平沙培英初中': '297', '实验外语学校': '166', '同和中学': '014',
    '新都中学': '266', '颜乐天中学': '016', '颐和实验': '349', '云英实验': '265', '珠江实验': '322', '铁一白云': '336',
    '启明中学': '077', '成龙中学': '289', '大同中学初中部': '051', '二师实验初中': '035', '龙岗中学': '036',
    '新和中学': '037', '竹料三中': '046', '竹料一中北校区': '045', '竹料一中南校区': '044', '穗丰学校': '321',
    '龙归学校': '135',
    '培英实验云景校区': '265', '民航人和校区': '370', '龙归学校校本部': '135', '竹料一中': '044+045', '民航学校': '188'
}


def remove_school_prefix(schools, prefixes):
    result = []
    for school in schools:
        # 标记是否找到前缀
        found = False
        for prefix in prefixes:
            if school.startswith(prefix):
                # 去除前缀
                result.append(school[len(prefix):])
                found = True
                break
        # 如果没有找到任何前缀，保留原名称
        if not found:
            result.append(school)
    return result


import os


def get_xlsx_files(directory):
    """
    获取指定目录下所有.xlsx文件的绝对路径

    Args:
        directory: 要搜索的目录路径

    Returns:
        list: 包含所有.xlsx文件绝对路径的列表
    """
    xlsx_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.xlsx'):
                absolute_path = os.path.abspath(os.path.join(root, file))
                xlsx_files.append(absolute_path)
    return xlsx_files


file_list = [item for item in get_xlsx_files(fr"C:\Users\1012986131\Desktop\python\random\output") if
             "学校数据" in item]

for file in file_list:

    data = read_xlsx_to_list(file_path=file)

    data[0].insert(1, "学校代码")

    for i in range(1, len(data)):
        school_name = data[i][0][3:] if data[i][0][:4] != "钟落潭镇" else data[i][0][4:]

        data[i].insert(1, school_code.get(school_name, school_name))

    save_excel(two_dimension_list=data, excel_name="output/" + file[49:55] + "（学校代码）")
