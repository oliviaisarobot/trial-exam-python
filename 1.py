# Create a function that takes a list as a parameter,
# and returns a new list with all its element's values doubled.
# It should raise an error if the parameter is not a list.

def double_list_elements(input_list):
    if type(input_list) != list:
        raise TypeError("Input is not a list.")
    else:
        output = []
        for item in input_list:
            output.append(item*2)
        return output

test = [1, 2, 3, 4, 5, 6]

print(double_list_elements(test))
print(double_list_elements("test"))
