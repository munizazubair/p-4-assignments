import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    hashed_input_password = hash_password(password_to_check)

    return stored_logins.get(email) == hashed_input_password

def main():
    stored_logins = {
        "user@example.com": hash_password("secure123"),
        "admin@example.com": hash_password("adminpass")
    }

    print(login("user@example.com", "secure123", stored_logins))  
    print(login("user@example.com", "wrongpass", stored_logins)) 
    print(login("someone@example.com", "secure123", stored_logins))  

main()
