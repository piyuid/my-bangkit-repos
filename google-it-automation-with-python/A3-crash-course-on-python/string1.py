email = "leopuji17@gmail.com"
old_domain = "gmail.com"
new_domain = "rf.com"

def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email
print(replace_domain)