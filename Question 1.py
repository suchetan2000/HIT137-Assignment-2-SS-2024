def encrypt_content(raw_text, n, m):
    """
    Encrypts the given text using the provided rules based on values of n and m.

    Args:
        raw_text (str): The text to be encrypted.
        n (int): User-defined integer used for encryption logic.
        m (int): User-defined integer used for encryption logic.

    Returns:
        str: The encrypted text.
    """
    encrypted_text = ""
    for char in raw_text:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            if char <= 'm':  # First half of lowercase alphabet
                # Shift forward by n * m
                encrypted_text += chr(((ord(char) - ord('a') + n * m) % 26) + ord('a'))
            else:  # Second half of lowercase alphabet
                # Shift backward by n + m
                encrypted_text += chr(((ord(char) - ord('a') - (n + m)) % 26) + ord('a'))
        # Check if the character is an uppercase letter
        elif 'A' <= char <= 'Z':
            if char <= 'M':  # First half of uppercase alphabet
                # Shift backward by n
                encrypted_text += chr(((ord(char) - ord('A') - n) % 26) + ord('A'))
            else:  # Second half of uppercase alphabet
                # Shift forward by m^2
                encrypted_text += chr(((ord(char) - ord('A') + m**2) % 26) + ord('A'))
        else:
            # For special characters and numbers, leave unchanged
            encrypted_text += char
    return encrypted_text


def decrypt_content(encrypted_text, n, m):
    """
    Decrypts the given text using the reverse of the encryption rules.

    Args:
        encrypted_text (str): The text to be decrypted.
        n (int): User-defined integer used for decryption logic.
        m (int): User-defined integer used for decryption logic.

    Returns:
        str: The decrypted text.
    """
    decrypted_text = ""
    for char in encrypted_text:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            if char <= 'm':  # First half of lowercase alphabet
                # Reverse shift by subtracting n * m
                decrypted_text += chr(((ord(char) - ord('a') - n * m) % 26) + ord('a'))
            else:  # Second half of lowercase alphabet
                # Reverse shift by adding n + m
                decrypted_text += chr(((ord(char) - ord('a') + (n + m)) % 26) + ord('a'))
        # Check if the character is an uppercase letter
        elif 'A' <= char <= 'Z':
            if char <= 'M':  # First half of uppercase alphabet
                # Reverse shift by adding n
                decrypted_text += chr(((ord(char) - ord('A') + n) % 26) + ord('A'))
            else:  # Second half of uppercase alphabet
                # Reverse shift by subtracting m^2
                decrypted_text += chr(((ord(char) - ord('A') - m**2) % 26) + ord('A'))
        else:
            # For special characters and numbers, leave unchanged
            decrypted_text += char
    return decrypted_text


def check_correctness(raw_text, decrypted_text):
    """
    Checks if the decrypted text matches the original text.

    Args:
        raw_text (str): The original text.
        decrypted_text (str): The decrypted text.

    Returns:
        bool: True if the decrypted text matches the original text, False otherwise.
    """
    return raw_text == decrypted_text


def main():
    """
    Main function to read the input file, encrypt its contents, write the encrypted text
    to a file, decrypt the text, and verify its correctness.
    """
    # Read the raw text from "raw_text.txt"
    with open("raw_text.txt", "r") as file:
        raw_text = file.read()

    # Get user inputs for n and m
    n = int(input("Enter the value of n: "))  # Input for n
    m = int(input("Enter the value of m: "))  # Input for m

    # Encrypt the content
    encrypted_text = encrypt_content(raw_text, n, m)

    # Write the encrypted text to "encrypted_text.txt"
    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted_text)

    print("Encryption completed. Encrypted text written to 'encrypted_text.txt'.")

    # Decrypt the content
    decrypted_text = decrypt_content(encrypted_text, n, m)

    # Check the correctness of decryption
    if check_correctness(raw_text, decrypted_text):
        print("Decryption successful. The decrypted text matches the original text.")
    else:
        print("Decryption failed. The decrypted text does not match the original text.")


if __name__ == "__main__":
    main()
