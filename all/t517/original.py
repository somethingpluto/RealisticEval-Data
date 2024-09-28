def read_jsonl(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
        json_list = []
        for line in lines:
            json_obj = json.loads(line)
            json_list.append(json_obj)
    return json_list