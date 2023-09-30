
input_string = input()


result_string = ""


vowels = set("AEIOUYaeiouy")


for char in input_string:

    if char in vowels:
        continue
    
    
    result_string += "." + char.lower()

print(result_string)
