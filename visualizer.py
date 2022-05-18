import pandas as pd
import sys
import numpy as np


def table2list(table_path):
    df = pd.read_excel(table_path)
    for column_name in df.columns.values:
        df[column_name] = df[column_name].apply(lambda x: str(x).replace(u'\xa0', u''))
        df[column_name] = df[column_name].apply(lambda x: str(x).replace(u' ', u''))
    df_list = df.values.tolist()
    return df_list

def index_2d(data, search):
    for i, e in enumerate(data):
        try:
            return i, e.index(search)
        except ValueError:
            pass
    raise ValueError("{!r} is not in list".format(search))


def compute_num_param(size):
    size = size[1:-1]
    l = [int(x) for x in size.split(",")]
    return np.prod(l)


if len(sys.argv) != 4:
    print(">>> Incorrect usage, check README for instructions.")
    print(">>> Quitting.")
    exit(1)

# ==============================================
# Begin table data processing
# ==============================================

layer_table_path = sys.argv[1]
dependency_table_path = sys.argv[2]
suffix = sys.argv[3]

layer_table_list = table2list(layer_table_path)
dependency_table_list = table2list(dependency_table_path)

# ==============================================
# Begin DOT code generation
# ==============================================

print("graph {")

# layer info
for entry in layer_table_list:
    print(f"{entry[0]}[xlabel=\"{entry[1]}s\"]")
    # print(f"{entry[1]}s, {entry[2]}mb")

# layer dependency
for entry in dependency_table_list:
    src = entry[1]
    dst = entry[2]
    i, e = index_2d(layer_table_list, src)
    src_data_size = layer_table_list[i][4]
    src_data_param = compute_num_param(src_data_size)
    print(f"{src} -- {dst}[label=\"{src_data_size}({src_data_param})\"];")

print("}")
