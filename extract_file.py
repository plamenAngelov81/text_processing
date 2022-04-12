path = input().split("\\")

file = path[-1].split(".")

print(f"File name: {file[0]}")
print(f"File extension: {file[1]}")
