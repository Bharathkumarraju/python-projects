text = "bat ball"
replaced_text = text.replace("ba", "ca")
print(replaced_text)

print(text.find("ba"))
print(text.upper())


# get two string inputs
text1 = input("enter 1st one")
text2 = input("enter 2nd one")
print(text1[0])
print(text1[ :4])
print(text2[-4: ])

# create the result string
# hint: use slicing
result  = text1[ :4] + text2[-4: ]

# print the result
print(result)

print("bharath" in text1)
print("hell" in text2)

