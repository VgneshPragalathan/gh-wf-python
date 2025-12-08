# output will be written to result.txt

message = "Hello, this is the output!"

with open("src/result.txt", "w") as file:
    file.write(message)

print("Output written to result.txt")