def removeWhite(s):
    return ("".join([char.lower() for char in s if char.isalpha()]))

def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse(s[:-1])


def isPal(s):
    return (removeWhite(s) == removeWhite(reverse(s)))

print isPal(removeWhite("x"))
print isPal(removeWhite("radar"))
print isPal(removeWhite("hello"))
print isPal(removeWhite(""))
print isPal(removeWhite("hannah"))
print isPal(removeWhite("madam i'm adam"))
