# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file does not exist, just return 0.

def count_letter_a(filename):
    if type(filename) != str:
        raise TypeError("Input is not a string.")
    else:
        counter = 0
        for letter in filename:
            if letter.lower() == "a":
                counter += 1
        return counter

print(count_letter_a("MASvalami.txt"))
