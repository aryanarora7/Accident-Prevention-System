import string
import itertools
#21BIT0089 KHUSHI SHARMA

def brute_force_password_cracker(target_password):
    attempts = 0
    chars = string.ascii_letters + string.digits + string.punctuation

    for length in range(1, 9):  # Limit the password length to a maximum of 8 characters
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            password = ''.join(guess)
            if password == target_password:
                return password, attempts

            if attempts >= 500000:
                return None, attempts  # Stop the program if the number of attempts exceeds 500,000

    return None, attempts

# Main program
if __name__ == '__main__':
    password_to_guess = input("Enter the password to be guessed: ")
    cracked_password, num_attempts = brute_force_password_cracker(password_to_guess)

    if cracked_password:
        print(f"Password cracked: {cracked_password}")
    else:
        print("Password not cracked")

    print(f"Number of attempts: {num_attempts}")

