from Levenshtein import ratio as sim
import string
import unicodedata

def containsNameAndInitial(prefix, initial1, name1, name2, treshold=1):
    """
    Returns true, if prefix contains name2 and initial1 after removing name2 from it and if similarity between name1
    and prefix then is greater than treshold.
    """
    condition = False
    if initial1 != "" and len(name2) > 1:
        if name2 in prefix:
            prefix = prefix.replace(name2, "")
            if prefix != "":
                if initial1 == prefix[0]:
                    condition = True
    #also check if the other name is similar enough, if it is more than just the initial
    if len(name1) > 1:
        if sim(name1, prefix) < treshold:
            condition = False
    return condition

# Function for pre-processing each name,email
def process(dev):
    """
    Function for pre-processing each name,email \n
    dev is tuple of two strings, e.g. ("name","email@domain")
    """
    name: str = dev[0]

    # Remove punctuation
    trans = name.maketrans("", "", string.punctuation)
    name = name.translate(trans)
    # Remove accents, diacritics
    name = unicodedata.normalize('NFKD', name)
    name = ''.join([c for c in name if not unicodedata.combining(c)])
    # Lowercase
    name = name.casefold()
    # Strip whitespace
    name = " ".join(name.split())


    # Attempt to split name into firstname, lastname by space
    parts = name.split(" ")
    # Expected case
    if len(parts) == 2:
        first, last = parts
    # If there is no space, firstname is full name, lastname empty
    elif len(parts) == 1:
        first, last = name, ""
    # If there is more than 1 space, firstname is until first space, rest is lastname
    else:
        first, last = parts[0], " ".join(parts[1:])

    # Take initials of firstname and lastname if they are long enough
    i_first = first[0] if len(first) > 1 else ""
    i_last = last[0] if len(last) > 1 else ""

    # Determine email prefix and domain
    email: str = dev[1]
    if(email != ""):
        prefix = email.split("@")[0]
        domain = email.split("@")[1]
    else:
        prefix = ""
        domain = ""
    

    return name, first, last, i_first, i_last, email, prefix, domain
