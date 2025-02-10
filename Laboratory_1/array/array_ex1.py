name = list("MICHELLE")

# Accessing a specific character:
print("The first character:", name[0])  # M

# Iterating through the array:
print("\nAll characters in the name:")
for char in name:
    print(char)

# Adding a new character:
name.append("!")  # Adding an exclamation mark
print("\nName after adding '!':")
print("".join(name))

# Removing a character:
name.remove("E")  # Removing the first 'E'
print("\nName after removing the first 'E':")
print("".join(name))


# Finding the length of the array:
length_of_name = len(name)
print("\nLength of the name:", length_of_name)

# Counting occurrences of a character:
count_of_L = name.count("L")
print("\nNumber of 'L's:", count_of_L)


# Reversing the name (using slicing):
reversed_name = name[::-1]
print("\nReversed name:", "".join(reversed_name))