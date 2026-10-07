# Kate Macias
# Software Engineering 1
# Fall 2026
#
#-----------------My Version--------------------:

name = "Johanna Jackson"

def name_array(name_for_splitting):
    split_name = name_for_splitting.split()
    print(f"Name Array: {split_name}")

    return split_name

name_array(name)

def reverse_array(array):
    reversed_array = list(reversed(array))
    print(f"Reversed Array: {reversed_array}")
    return reversed_array

print(reverse_array(name_array(name)))

def add_borg(array):
    array.append("Borg")
    print(f"Array with Borg: {array}")
    return array

print(add_borg(reverse_array(name_array(name))))

print(add_borg(reverse_array(name_array(name))))

print(f"New name: {add_borg(reverse_array(name_array(name)))}")


#---------------Origional Code-------------------

# #Mangle the name by reversing it or borgifying it
# def modified_name(choose):
#     #global name
#     # Split the name into first and last in an array
#     #split_name = name.split()
#     #reversed_twice = list(reversed(reversed(split_name)))
#     #mangled_name = reversed_twice.append("Mangled")
#     #return mangled_name * 2
#     # Reverse the array of name components so the array is [last, first]
#     reversed_name_components = list(reversed(split_name))
#     # Rejoin the array of name components
#     new_name1 = ' '.join(reversed_name_components)
#     # Store the mangled name
#     name = new_name1
#     print(new_name1)
#     if choose:
#         # Split the name into last and first in an array
#         split_name2 = new_name1.split()
#         # Reverse the array of name components so the array is [last, first]
#         reversed_name_components2 = list(reversed(split_name2))
#         # Add borg to the end of the array
#         reversed_name_components2.append("Borg")
#         # Rejoin the array of name components
#         new_name2 = ' '.join(reversed_name_components2)
#         print(new_name2)
#         name = new_name2
#     return name


#print(f"New borg name: {modified_name(True)}")
