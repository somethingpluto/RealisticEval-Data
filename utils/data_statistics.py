import pandas as pd

data = pd.read_excel("./RealisticEval-Data (2).xlsx")
author_counts = data['author'].value_counts()
print(author_counts)
question_type = data['question_type'].value_counts()
print(question_type)
language_type = data['language'].value_counts()
print(language_type)