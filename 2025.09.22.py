from func import *

data = read_xlsx_to_list(file_path=fr"C:\Users\1012986131\Desktop\2.xlsx")
print(data)

output = {item: 0 for item in ["永平", "新市", "石井", "江高", "人和", "太和", "钟落潭"]}

for item in data:
    if item[0] == "直管":
        if item[1] not in output.keys():
            output[item[1]] = 1
        else:
            output[item[1]] += 1

    else:
        output[item[0]] += 1

print(output
      )