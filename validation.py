import re

def validation(data, option):
    if option == 1:
        try:
            float(data)
            return True
        except ValueError:
            return False
    if option == 2:
        pattern = re.compile(r'-?\d+(\.\d+)?(,\s-?\d+(\.\d+)?)*')
        if pattern.fullmatch(data):
            return True
        else:
            return False
    if option == 3:
        pattern = re.compile(r'\[\s*-?\d+\.\d+\s*,\s*-?\d+\.\d+\s*\](\s*,\s*\[\s*-?\d+\.\d+\s*,\s*-?\d+\.\d+\s*\])*')
        patternTwo = re.compile(r'\[\s*-?\d+(\.\d+)?\s*,\s*-?\d+(\.\d+)?\s*\](\s*,\s*\[\s*-?\d+(\.\d+)?\s*,\s*-?\d+(\.\d+)?\s*\])*')
        if pattern.fullmatch(data) or patternTwo.fullmatch(data):
            return True
        else:
            return False
        