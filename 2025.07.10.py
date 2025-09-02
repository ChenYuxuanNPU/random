from func import *

data = read_xlsx_to_list(
    file_path=fr"C:\Users\1012986131\Desktop\1.xlsx", sheet_name="学生名册"
)

for item in data:
    print(f"when '{item[0]}' then '{item[1]}'")

# output = ",".join([f"'{item[0]}'" for item in data])
#
# print(output)
