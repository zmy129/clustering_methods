import json
import random
import os
import argparse
directory = "D:\\PYcharm_project\\pythonProject\\clustering\\similarity_DBSCAN\\result1"

# 读取每个类的json文件，并随机抽取一个样本
samples = {}
for filename in os.listdir(directory):
    if filename != "cluster_-1.json":
        with open(os.path.join(directory, filename), "r",encoding='utf-8') as f:
            data = json.load(f)
            sample = random.choice(data)
            samples[filename] = sample

# 读取-1这个类的json文件，并将其与随机抽取的样本合并
with open(os.path.join(directory, "cluster_-1.json"), "r",encoding='utf-8') as f:
    data = json.load(f)
    for filename, sample in samples.items():
        data.append(sample)


# 将合并后的数据写入一个新的json文件
with open(os.path.join(directory, "new_data.json"), "w",encoding='utf-8') as f:
    json.dump(data, f,ensure_ascii=False, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_data_path',default='D:\\PYcharm_project\\pythonProject\\Corpus_Quality_Optimization\\corpus\\cot_data_cn.json',type=str, help="json file path for input data")
    parser.add_argument('--output_path', default="./result_DBSCAN.json", type=str,help="json file path for output data")
    parser.add_argument('--CONTENT_FIELD_NAME', default=["instruction", "input"], help='field name of content in json')
    parser.add_argument('--eps', default=0.5, type=float, help='DBSCAN parameters')
    parser.add_argument('--min_samples', default=2, type=int, help='DBSCAN parameters')
    args = parser.parse_args()
    datas,texts=load_data(args)
    DBSCAN_SIM(args,datas,texts)