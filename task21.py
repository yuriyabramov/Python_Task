# Напишите программу для печати всех уникальных
# значений в словаре. 
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

 
# list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},  {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# res = []
# for i in range(len(list)):
#     for (k, v) in list[i].items():
#         if res.count(v) < 1:
#             res.append(v)
# print(res)

list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},  {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
uniq_el = set()
for i in list:
    for key in i:
        element = i[key]
        uniq_el.add(element)
print(uniq_el)
