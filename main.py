o_s = input("Enter any word: ")
o_s_l = len(o_s)

print(f"Orginal String is {o_s}")
print("Printing only even index chars")
for num in range(o_s_l):
    if num % 2 == 0:
        print(o_s[num])