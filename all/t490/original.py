def fix(x):
    if type(x) != str:
        x = str(x)
    if x.count("```")%2 == 1:
        x = x + "\n```"
    return "\n".join("> "+line for line in x.split("\n"))