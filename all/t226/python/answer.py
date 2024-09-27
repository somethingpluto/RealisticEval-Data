import pandas as pd


def tsv_to_jsonl(tsv_file, jsonl_file):
    # 读取 TSV 文件
    df = pd.read_csv(tsv_file, sep='\t')

    # 打开 JSONL 文件进行写入
    with open(jsonl_file, 'w', encoding='utf-8') as jsonl:
        for _, row in df.iterrows():
            # 将每一行转换为字典
            json_line = row.to_json(force_ascii=False)
            # 写入到 JSONL 文件中
            jsonl.write(json_line + '\n')
