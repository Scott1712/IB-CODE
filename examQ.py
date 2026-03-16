#30/10/2025

code = "COMP-2025-LAB-001"

codeList = code.split("-")
oldYear = codeList[1]

newCode = code.replace(oldYear,"2026")

print("Old code ->",code)
print("New code ->",newCode)