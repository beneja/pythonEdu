# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
# {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
inpDict = {"I": "S001", "II": "S002", "III": "S001",
            "IV": "S005", "V": "S005", "VI": "S009", "VII": "S007"}
res = set(inpDict.values())
print(inpDict.values())
print(sorted(res))

