import csv
import pandas as pd
from itertools import combinations
from Levenshtein import ratio as sim
import os
import functions as fun
from pydriller import Repository
import traceback

try:

    DEVS = set()
    for commit in Repository("https://github.com/run-llama/llama_index.git").traverse_commits():
        DEVS.add((commit.author.name, commit.author.email))
        DEVS.add((commit.committer.name, commit.committer.email))

    DEVS = sorted(DEVS)
    with open(os.path.join("project1devs", "devs.csv"), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        writer.writerow(["name", "email"])
        writer.writerows(DEVS)


    DEVS = []
    with open(os.path.join("project1devs", "devs.csv"), 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            DEVS.append(row)
    DEVS = DEVS[1:]


    SIMILARITY = []
    for dev_a, dev_b in combinations(DEVS, 2):
        line = fun.compare_pairs(dev_a, dev_b, sim)
        SIMILARITY.append(line)


    cols = ["name_1", "email_1", "name_2", "email_2", "c1", "c2",
            "c3.1", "c3.2", "c4", "c5", "c6", "c7"]
    df = pd.DataFrame(SIMILARITY, columns=cols)
    df.to_csv(os.path.join("project1devs", "devs_similarity.csv"), index=False, header=True)


    df = df[["name_1", "email_1", "name_2", "email_2", "c1", "c2",
        "c3.1", "c3.2", "c4", "c5", "c6", "c7"]]

    t = 0.73

    filtered_df = fun.filter_pairs(df, t)
    filtered_df.to_csv(os.path.join("project1devs", f"devs_similarity_filtered_t={t}.csv"), index=False, header=True)

except Exception as ex:
    print("Error occurred: {ex}, see the traceback")
    traceback.print_exc()
