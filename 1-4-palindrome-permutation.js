// 1.4 Palindrome Permutation

// Given a string, write a function to check if it is a permutation of a palindrome. 
// A palindrome is a word or phrase that is the same forwards and backwards. (E.e., "deed", "civic", "madam", "radar", "level", "Stanley Yelnats")
// A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
// In this implementation, we assume a user has provided a string with no spaces.

function is_palindrome_permutation(s)
{
    // Create a dictionary where the keys are unique characters in the given strings 
    // and the values are the number of times that character is seen in the string.
    let character_counts = {};
    for(let i = 0, length = s.length; i < length; i++)
    {
        if(character_counts[s[i]])
        {
            character_counts[s[i]] += 1;
        }
        else
        {
            character_counts[s[i]] = 1;
        }
    }

    // If the given string has an odd length, exactly one character must have an odd character count.
    if (s.length % 2 == 1)
    {
        let odd_count_seen = false;
        for (let count in character_counts)
        {
            if(character_counts[count] % 2 == 1)
            {
                if (odd_count_seen)
                {
                    return false;
                }
                else
                {
                    odd_count_seen = true;
                }
            }
        }
        if (odd_count_seen)
        {
            return true;
        }
        else
        {
            return false;
        }        
    }

    // If the given string has an even length, all characters must have an even character count.
    else
    {
        for (let count in character_counts)
        {
            if(character_counts[count] % 2 == 1)
            {
                return false;
            }
        }        
    }

    return true;
}

console.log(
    is_palindrome_permutation("civic")
);  // true

console.log(
    is_palindrome_permutation("deed")
);  // true

console.log(
    is_palindrome_permutation("Max Wiederholt")
);  // false