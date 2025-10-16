from Levenshtein import ratio as sim

def containsNameAndInitial(prefix, Initial1, name1, name2, treshold):
    condition = False
    if Initial1 != "" and len(name2) > 1:
        if name2 in prefix:
            prefix = prefix.replace(name2, "")
            if prefix != "":
                if Initial1 == prefix[0]:
                    condition = True
    #also check if the other name is similar enough, if it is more than just the initial
    if len(name1) > 1:
        if sim(name1, prefix) < treshold:
            condition = False
    return condition
