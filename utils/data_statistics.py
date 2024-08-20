import pandas as pd

data = pd.read_excel("./RealisticEval-Data.xlsx")
author_counts = data['author'].value_counts()
print(author_counts)
question_type = data['question_type'].value_counts()
print(question_type)
language_type = data['language'].value_counts()
print(language_type)
status_type = data['status'].value_counts()
print(status_type)