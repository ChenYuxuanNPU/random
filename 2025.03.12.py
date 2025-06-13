"""
数据脱敏
"""

while True:
    name_col_list = input("请输入需要脱敏的姓名列序数，以空格分隔：\n").split()

    flag = True
    for c in name_col_list:
        if not c.isnumeric():
            flag = False
            break

    if flag:
        print(name_col_list)
        break

while True:
    id_col_list = input("请输入需要脱敏的身份证号列序数，以空格分隔：\n").split()
    flag = True
    for i in id_col_list:
        if not i.isnumeric():
            flag = False
            break

    if flag:
        print(id_col_list)
        break

while True:
    phone_number_col_list = input("请输入需要脱敏的手机号列序数，以空格分隔：\n").split()
    flag = True
    for p in phone_number_col_list:
        if not p.isnumeric():
            flag = False
            break

    if flag:
        print(phone_number_col_list)
        break

while True:
    email_col_list = input("请输入需要脱敏的邮箱列序数，以空格分隔：\n").split()
    flag = True
    for e in email_col_list:
        if not e.isnumeric():
            flag = False
            break

    if flag:
        print(email_col_list)
        break

while True:
    location_col_list = input("请输入需要脱敏的地址列序数，以空格分隔：\n").split()
    flag = True
    for l in location_col_list:
        if not l.isnumeric():
            flag = False
            break

    if flag:
        print(location_col_list)
        break

