def validate_input(n, s):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Registration number must be a positive integer.")
    if not isinstance(s, str) or not s.isalpha() or len(s) == 0:
        raise ValueError("Content string must be a non-empty string containing only letters.")

def process_string(n, s):
    vowels = 'aeiouAEIOU'
    if n % 2 == 0:
        return s[::-1]
    else:
        return ''.join([ch.upper() if ch in vowels else ch.lower() for ch in s])

def count_set_bits(n):
    return bin(n).count('1')

def extract_substrings(s, k):
    return [s[i:i+k] for i in range(len(s)-k+1)]

def sort_or_reverse(n, s, substrings):
    if n & len(s) == 0:
        return sorted(substrings)
    else:
        return list(reversed(substrings))

def main():
    print("Smart Text-Processing Tool")
    while True:
        try:
            n_input = input("Enter registration number or 'q' to quit: ").strip()
            if n_input.lower() == 'q':
                break
            n = int(n_input)
            s = input("Enter content string: ").strip()
            validate_input(n, s)
            processed = process_string(n, s)
            k = count_set_bits(n)
            if k == 0 or k > len(processed):
                print("No substrings can be extracted with length", k)
                continue
            substrings = extract_substrings(processed, k)
            result = sort_or_reverse(n, processed, substrings)
            print(' '.join(result))
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()