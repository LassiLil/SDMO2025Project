import pandas as pd
import unicodedata
import string

def filter_pairs(df, threshold, tolerance):
    df = df.copy()
    df["bal_value"] = (
    df["c1"] * 4 +
    df["c3.1"] * 2 +
    df["c3.2"] * 2 +
    df["c4"].astype(float) +
    df["c5"].astype(float)
) / 10
    
    df1 = df[df.groupby("name_1")["bal_value"].transform("max") - df["bal_value"] <= tolerance]
    df2 = df[df.groupby("name_2")["bal_value"].transform("max") - df["bal_value"] <= tolerance]

    result = pd.concat([df1, df2]).drop_duplicates()
    return result[result["bal_value"] >= threshold]


def process(dev):
    name: str = dev[0]

    trans = name.maketrans("", "", string.punctuation)
    name = name.translate(trans)
   
    name = unicodedata.normalize('NFKD', name)
    name = ''.join([c for c in name if not unicodedata.combining(c)])
   
    name = name.casefold()
   
    name = " ".join(name.split())

    parts = name.split(" ")
   
    if len(parts) == 2:
        first, last = parts
    
    elif len(parts) == 1:
        first, last = name, ""
    
    else:
        first, last = parts[0], " ".join(parts[1:])

    
    i_first = first[0] if len(first) > 1 else ""
    i_last = last[0] if len(last) > 1 else ""

    
    email: str = dev[1]
    prefix = email.split("@")[0]
    
    GENERIC = ["noreply", "contact", "info"]
    is_generic = any(prefix.startswith(g) for g in GENERIC)

    return name, first, last, i_first, i_last, email, prefix, is_generic

def compare_pairs(dev_a, dev_b, sim_func):
    name_a, first_a, last_a, i_first_a, i_last_a, email_a, prefix_a, is_generic_a = process(dev_a)
    name_b, first_b, last_b, i_first_b, i_last_b, email_b, prefix_b, is_generic_b = process(dev_b)

    
    c1 = sim_func(name_a, name_b)
    c2 = sim_func(prefix_b, prefix_a)
    c31 = sim_func(first_a, first_b)
    c32 = sim_func(last_a, last_b)
    c4 = c5 = c6 = c7 = False


    if i_first_a != "" and last_a != "":
        c4 = i_first_a in prefix_b and last_a in prefix_b
    if i_last_a != "":
        c5 = i_last_a in prefix_b and first_a in prefix_b
    if i_first_b != "" and last_b != "":
        c6 = i_first_b in prefix_a and last_b in prefix_a
    if i_last_b != "":
        c7 = i_last_b in prefix_a and first_b in prefix_a
        
    if is_generic_a or is_generic_b:
        c2 = 0
        c4 = c5 = c6 = c7 = False
        
    return [dev_a[0], email_a, dev_b[0], email_b, c1, c2, c31, c32, c4, c5, c6, c7, is_generic_a, is_generic_b]
