# GitHub-ID-seula
def compare_github_id(email1, email2):
    def check_noreply(email):
        if "users@noreply.github.com" not in email or "+" not in email:
            return None, None 
        try:
            prefix = email.split("@")[0]
            id = prefix.split("+", 1)[0]
            return id
        except ValueError:
            return None
    id1 = check_noreply(email1)
    id2 = check_noreply(email2)
    
    if id1 and id2:
        return True
    return False

# DOMAIN-tutka
def compare_domain(email1, email2):
    def check_domain(email):
        return email.split("@")[-1].lower()
    domain1 = check_domain(email1)
    domain2 = check_domain(email2)
    
    if domain1 and domain2:
        return True
    return False

# ALIAS?
ALIASES = {
    "": "",
    "": ""
}
