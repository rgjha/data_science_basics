def solution(S):

    longest = -1
    n_letters = 0
    n_digits = 0
    n_others = 0

    for char in S:
        if char.isalpha():
            n_letters += 1
        elif char.isdigit():
            n_digits += 1
        elif char == " ":
            # Check whether it's a valid password.
            if n_others == 0 and n_letters % 2 == 0 and n_digits % 2 == 1:
                if longest < n_letters + n_digits:
                    longest = n_letters + n_digits

            # Reset the counters for the next word.
            n_letters = 0
            n_digits = 0
            n_others = 0
            
        else:
            n_others += 1

    # Check whether the last word is a valid password.

    if n_others == 0 and n_letters % 2 == 0 and n_digits % 2 == 1:
            if longest < n_letters + n_digits:
                longest = n_letters + n_digits

    return longest