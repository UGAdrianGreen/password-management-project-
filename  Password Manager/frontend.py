import subprocess

def generate_password():
    # Call C++ executable to generate a password
    password = subprocess.check_output(["./password_generator"])
    return password.decode("utf-8").strip()

def hash_password(password):
    # Call Rust executable to hash the password
    hashed_password = subprocess.check_output(["./password_hasher", password])
    return hashed_password.decode("utf-8").strip()

def main():
    # Example usage
    password = generate_password()
    print("Generated password:", password)
    hashed_password = hash_password(password)
    print("Hashed password:", hashed_password)

if __name__ == "__main__":
    main()
