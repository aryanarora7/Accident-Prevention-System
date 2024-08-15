from brute_force_password_cracker import brute_force_password_cracker

if __name__ == '__main__':
    password_to_guess = input("Enter the password to be guessed: ")
    cracked_password, num_attempts = brute_force_password_cracker(password_to_guess)

    if cracked_password:
        print(f"Password cracked: {cracked_password}")
    else:
        print("Password not cracked")

    print(f"Number of attempts: {num_attempts}")
