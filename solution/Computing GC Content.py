# file_path = "dataset/test.txt"
file_path = "dataset/rosalind_gc.txt"
with open(file_path, 'r') as f:
    s = f.readlines()

s_strip = list(map(lambda x : x.strip(), s))
rs_dict = dict()
dict_value = ""
for value in s_strip:
    if len(dict_value) == 0 and value.startswith(">"):
        dict_key = value[1:]
    elif len(dict_value) > 0 and value.startswith(">"):
        rs_dict[dict_key] = (dict_value.count("G") + dict_value.count("C"))/len(dict_value) * 100
        dict_key, dict_value = value[1:], ""
    else:
        dict_value += value

rs_dict[dict_key] = (dict_value.count("G") + dict_value.count("C"))/len(dict_value) * 100

# max key
max_key = max(rs_dict, key=rs_dict.get)
print(max_key, "\n",rs_dict[max_key])