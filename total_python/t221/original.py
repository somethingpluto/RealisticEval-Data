def prepare_dict(filename):
    def parse_dict(s):
        s = s.replace("\n", "")
        # Using regular expressions to find the dictionary in the string
        match = re.search(r'translations\s*=\s*({.*?})', s)

        if match:
            dict_str = match.group(1)
            try:
                dict_str = re.sub(r',\s*([}\]])', r'\1', dict_str)
                dict_str = re.sub(r'#.*?(,|})', r'\1', dict_str)
                my_dict = json.loads(dict_str) 

                if my_dict is None:
                    my_dict = {}

                return my_dict
            
            except:                
                print(f"Couldn't parse the string: {dict_str}")
                return {}
        else:
            return {}