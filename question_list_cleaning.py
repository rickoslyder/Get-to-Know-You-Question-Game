import re

with open("QuestionsList.txt", "r") as file:
    text = file.readlines()

stripped = [line for line in text if line != "\n"]
stripped = stripped[1:]

with open("Stripped.txt", "a") as file:
    for line in stripped:
        newline = re.sub(r"^(\d{1,3}\.\s)", "", line)
        file.write(newline)
