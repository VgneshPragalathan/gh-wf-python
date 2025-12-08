# output will be written to result.txt
import os

message = "Hello, this is the output!"

os.makedirs('src',exist_ok=True)

with open("src/result.txt", "w") as file:
    file.write(message)

print("Output written to result.txt")