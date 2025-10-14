def containsNameAndInitial(prefix, Initial1, name2):
    condition = False
    if Initial1 != "" and len(name2) > 1:
        if name2 in prefix:
            prefix = prefix.replace(name2, "")
            if prefix != "":
                if Initial1 == prefix[0]: #vielä vois kattoo, onko toiset nimet tarpeeksi samanlaiset siinä tapauksessa, että ne eivät ole pelkät alkukirjaimet
                    condition = True
    return condition