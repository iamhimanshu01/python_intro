import re 
message = "the current python version is 3.13. other previous version are 3.12,3.11,3.10."
# match_obj = re.search('13',message)
# print(match_obj)
 
# if re.search('13',message):
#     print("found")
# else:
#     print("not found")
# print(message[32:34])
match_object = re.search("[0-9][0-9]",message)
print(match_object)
match_object = re.search("[0-9][0-9]", "house number:251/A")
print(match_object)
print(match_object)
print(match_object)

mesage_1 = "The year is 2011"
match_object = re.search('[0-9][0-9][0-9]',mesage_1)
print(match_object)
match_object = re.search('[0-9][0-9][0-9]',message)
print(match_object)