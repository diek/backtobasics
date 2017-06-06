# Modified from a question on SO
# sample data, has intentionl error
import json

data = {}
with open('j_data.txt', 'r') as f_handle:
    for index, line in enumerate(f_handle):
        try:
            key, value = line.split(';')
            if key == "ID":
                id = value.strip()
                data[id] = {}
            else:
                data[id][key] = value.strip()
        except Exception as e:
            print('Data Error: {}, on line number {}'.format(e, index + 1))


print(json.dumps(data, indent=2))
