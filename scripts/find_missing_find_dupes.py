import json
import os
import collections

def find_missing(lst):
    return [x for x in range(lst[0], lst[-1]+1) if x not in lst]

def find_duplicates(lst):
    return [item for item, count in collections.Counter(lst).items() if count > 1]


json_directory = './assets'

files = os.listdir(json_directory)

punks = []
for file in files:
    if not file == ".DS_Store":

        file_path = json_directory + "/" + file

        with open(file_path, 'r', encoding='utf-8') as f:
            file_dict = json.load(f)
            punk_name = file_dict["name"]
            right_side = punk_name.split("#")[1]
            punk_num = right_side.split(",")[0]
            punks.append(int(punk_num))

punks.sort()

print("GNC PUNKS:")
print(len(punks))
print(punks)

  
print("MISSING GNC PUNKS:")
print(find_missing(punks))

print("DUPLICATE GNC PUNKS:")
print(find_duplicates(punks))