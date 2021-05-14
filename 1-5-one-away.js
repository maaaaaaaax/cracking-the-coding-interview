// 1.5 One Away

// There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character.
// Given two strings, write a function to check if they are one edit (or zero edits) away.

function is_one_away(string_1, string_2)
{
    // If the difference between the two strings' lengths is greater than one, return false
    let length_difference = Math.abs(string_1.length - string_2.length);
    if (length_difference > 1)
    {
        return false; 
    }

    return true;
}

function is_one_replacement_away(string_1, string_2)
{
    if (string_1.length != string_2.length)
    {
        return false;
    }
    let replaced = false;
    for (let i = 0; i < string_1.length; i++)
    {
        if (string_1[i] != string_2[i])
        {
            if (replaced == false)
            {
                replaced = true;
            }
            else
            {
                return false;
            }
        }
    }
    return true;
}

console.log(is_one_replacement_away("sell", "hell"));  // true
console.log(is_one_replacement_away("hell", "hello"));  // false