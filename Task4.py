def process_user_input():
    """Takes user's full name and a sentence, and performs operations."""

    full_name = input("Enter your full name: ")
    sentence = input("Enter a short sentence: ")

    # 1. Name in uppercase
    name_uppercase = full_name.upper()
    print("Name in uppercase:", name_uppercase)

    # 2. First word of the sentence
    first_word = sentence.split()[0]  # Split by spaces and take the first element
    print("First word of the sentence:", first_word)

    
    # 3. Replace a substring (user specifies)
    substring_to_replace = input("Enter the substring you want to replace: ")
    replacement_substring = input("Enter the replacement substring: ")
    modified_sentence = sentence.replace(substring_to_replace, replacement_substring)
    print("Modified sentence:", modified_sentence)


# Get user input and process it
process_user_input()

