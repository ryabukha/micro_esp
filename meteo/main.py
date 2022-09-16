import am2302
import json

def read_conf():
    with open("env") as f:
        data = json.load(f)
    for k, v in data.items():
        print(k, ": ", v)
        print()

    return data



# am2302.start_measure()
