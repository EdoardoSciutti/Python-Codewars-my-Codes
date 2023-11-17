def is_interesting(number, awesome_phrases):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    def is_all_same(n):
        return len(set(str(n))) == 1

    def is_sequential_increment(n):
        return str(n) in '1234567890'

    def is_sequential_decrement(n):
        return str(n) in '9876543210'

    def is_followed_by_zeros(n):
        return set(str(n)[1:]) == {'0'}

    for i in range(3):
        if number + i < 100: continue
        num_str = str(number + i)
        if (is_palindrome(num_str) or is_all_same(num_str) or
            is_sequential_increment(num_str) or is_sequential_decrement(num_str) or
            is_followed_by_zeros(num_str) or number + i in awesome_phrases):
            return 2 if i == 0 else 1
    return 0