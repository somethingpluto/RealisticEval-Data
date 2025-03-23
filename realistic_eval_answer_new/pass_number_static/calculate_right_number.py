import math

import pandas as pd

LANGUAGE_NUMBER = {
    "Python": 392,
    "JavaScript": 376,
    "TypeScript": 372,
    "Java": 339,
    "C++": 353
}
if __name__ == '__main__':
    raw_data = pd.read_excel("./data/realistic_count.xlsx", sheet_name="pass1")
    result_list = []
    for index, row in raw_data.iterrows():
        print(row)
        temp_data = {
            "model": row.get("Model")
        }
        for language, count in LANGUAGE_NUMBER.items():
            percentage = row.get(language) / 100
            need_count = math.floor(count * percentage)
            temp_data[language] = need_count
        result_list.append(temp_data)
    pd.DataFrame(result_list).to_excel("./data/realistic_pass1.xlsx")
