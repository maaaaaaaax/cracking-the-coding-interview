# 1.6 String Compression

# Implement a method to perform basic string compression using the counts of repeated characters. 
# For example, the string aabcccccaaa would become a2b1c5a3.
# If the "compressed" string would not become smaller than the original string, your method should return the original string. 
# You can assume the string has only uppercase and lowercase letters (a - z).

def compress_string(string_1):
    # Create an empty string called compression
    compression = ''
    # Set a counter to 1
    counter = 1
    # For each character in string 1
    for i in range(0, len(string_1) - 1):
        # If the next character equals the current character
        if string_1[i + 1] == string_1[i]:
            # Increment the counter
            counter += 1
        # Else
        else:
            # Append the character to the empty / compression string
            compression += string_1[i]
            # Append the count (as a string) to the empty / compression string
            compression += str(counter)
            # Set the counter to 1
            counter = 1
    # Append the last character to the empty / compression string
    compression += string_1[-1]
    # Append the count (as a string) to the empty / compression string
    compression += str(counter)
    # If the compression is shorter than the original string
    if len(compression) < len(string_1):
        # Return the compression
        return compression
    # Else
    else:
        # Return the given string
        return string_1

print(compress_string('aabcccccaaa')) # a2b1c5a3