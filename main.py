# output will be written to result.txt

message = "Hello, this is the output!"

with open("result.txt", "w") as file:
    file.write(message)

print("Output written to result.txt")