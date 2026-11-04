# Kate Macias
# Software Engineering 1
# Fall 2026
#
# Challenge 5.2
#
'''Implement wrapped_divide() so that it calls divide() but converts the ZeroDivisionError into a return value of -1.

Implement wrapped_get_element() that it calls get_element(), but converts that -1 return value into a thrown IndexError.

You must call the originals from your wrappers. Your goal is not to reimplement the functionality; your only goal is to translate the return value to what you want.

'''

# Do not change this function!
def divide(n, d):
    if d == 0:
        raise ZeroDivisionError

    return n / d

# Do not change this function!
def get_element(a, i):
    if i < 0 or i >= len(a):
        return -1

    return a[i]

def wrapped_divide(n, d):
    try:
        return divide(n, d)
    except ZeroDivisionError:
        return -1

def wrapped_get_element(a, i):
    result = get_element(a, i)
    if result == -1:
        raise IndexError
    return result
