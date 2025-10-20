import csv
import pandas as pd
from itertools import combinations
from Levenshtein import ratio as sim
import os
import functions as f

# This block of code take the repository, fetches all the commits,
# retrieves name and email of both the author and commiter and saves the unique
# pairs to csv
# If you provide a URL, it clones the repo, fetches the commits and then deletes it,
# so for a big project better clone the repo locally and provide filesystem path

from pydriller import Repository

DEVS = set()
for commit in Repository("C:\\Opiskelu\\tkt\\SDMO\\projekti\\koodi\\Python").traverse_commits(): #this would only work on my pc
     DEVS.add((commit.author.name, commit.author.email))
     DEVS.add((commit.committer.name, commit.committer.email))

DEVS = sorted(DEVS)

with open(os.path.join("project1devs", "devs.csv"), 'w', encoding="utf_8", newline='') as csvfile:
     writer = csv.writer(csvfile, delimiter=',', quotechar='"')
     writer.writerow(["name", "email"])
     writer.writerows(DEVS)


# This block of code reads an existing csv of developers

DEVS = []
# Read csv file with name,dev columns
with open(os.path.join("project1devs", "devs.csv"), 'r', encoding="utf_8", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        DEVS.append(row)
# First element is header, skip
DEVS = DEVS[1:]





# Compute similarity between all possible pairs
SIMILARITY = []
for dev_a, dev_b in combinations(DEVS, 2):
    # Pre-process both developers
    name_a, first_a, last_a, i_first_a, i_last_a, email_a, prefix_a, domain_a = f.process(dev_a)
    name_b, first_b, last_b, i_first_b, i_last_b, email_b, prefix_b, domain_b = f.process(dev_b)

    #list of prefixes and email domains to filter:
    filteredPrefixes = ["contact", "me", "mail"]
    filteredDomains = ["users.noreply.github.com"]

    #filter out domains
    if ( (domain_a in filteredDomains) or (domain_b in filteredDomains) ):
        continue
    #if the prefix is on the blacklist, name might be in domain instead, so domain and prefix are swapped in those cases.
    if(prefix_a in filteredPrefixes):
        prefix_a, domain_a = domain_a, prefix_a

    if(prefix_b in filteredPrefixes):
        prefix_b, domain_b = domain_b, prefix_b

    # Conditions of Bird heuristic
    c1 = c2 = c31 = c32 = c4 = c5 = c6 = c7 = False
    #empty names were considered the same, so check if they are empty
    if(name_a != "" and name_b != "" and prefix_a != "" and prefix_b != ""):
        c1 = sim(name_a, name_b)
        c2 = sim(prefix_b, prefix_a)
        c31 = sim(first_a, first_b)
        c32 = sim(last_a, last_b)
    
    #Set similarity threshold 
    t=0.9

    c4 = f.containsNameAndInitial(prefix_b, i_first_a, first_a, last_a, t) 
    c5 = f.containsNameAndInitial(prefix_b, i_last_a, last_a, first_a, t)
    c6 = f.containsNameAndInitial(prefix_a, i_first_b, first_a, last_b, t)
    c7 = f.containsNameAndInitial(prefix_a, i_last_b, last_b, first_b, t)

    # Save similarity data for each conditions. Original names are saved
    SIMILARITY.append([dev_a[0], email_a, dev_b[0], email_b, c1, c2, c31, c32, c4, c5, c6, c7])



# Save data on all pairs (might be too big -> comment out to avoid)
cols = ["name_1", "email_1", "name_2", "email_2", "c1", "c2",
        "c3.1", "c3.2", "c4", "c5", "c6", "c7"]
df = pd.DataFrame(SIMILARITY, columns=cols)
#df.to_csv(os.path.join("project1devs", "devs_similarity.csv"), index=False, header=True)


#check c1-c3 against the threshold

print("Threshold:", t)
df["c1_check"] = df["c1"] >= t
df["c2_check"] = df["c2"] >= t
df["c3_check"] = (df["c3.1"] >= t) & (df["c3.2"] >= t)
# Keep only rows where at least one condition is True
df = df[df[["c1_check", "c2_check", "c3_check", "c4", "c5", "c6", "c7"]].any(axis=1)]


# Omit "check" columns, save to csv
df = df[["name_1", "email_1", "name_2", "email_2", "c1", "c2",
        "c3.1", "c3.2", "c4", "c5", "c6", "c7"]]
df.to_csv(os.path.join("project1devs", f"devs_similarity_t={t}.csv"), index=False, header=True)
