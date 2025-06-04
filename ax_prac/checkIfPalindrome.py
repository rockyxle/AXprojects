def main():
    answer = 'yes'
    while answer.lower() == 'yes':
        word = input("Enter a String: ")
        if is_palindrome(word):
            print(f"{word} is a palindrome")
        else:
            print(f"{word} is not a palindrome")
        while True:
            answer = input("Do you want to enter another string? (yes/no)").lower()
            if answer == 'yes' or answer == 'no':
                break
            else:
                print("Please enter 'yes' or 'no'.")
    
def is_palindrome(word):
    return word == word[::-1]

main()
