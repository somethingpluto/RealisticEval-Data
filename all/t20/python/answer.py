def process_markdown(s: str) -> str:
    if s.count('*') <= 2:
        return s
    first_star_index = s.find('*')
    last_star_index = s.rfind('*')
    return s[:first_star_index + 1] + s[first_star_index + 1:last_star_index].replace('*', '') + s[last_star_index:]
