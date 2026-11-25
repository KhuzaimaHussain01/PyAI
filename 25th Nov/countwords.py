template = """
{text}

Write a summary within {limit} words.
"""

text = "You are a patient python tutor"

prompt = template.format(text=text, limit=40)

print(prompt)