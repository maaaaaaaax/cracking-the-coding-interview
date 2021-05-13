// 1.5 One Away

// There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character.
// Given two strings, write a function to check if they are one edit (or zero edits) away.

function is_one_away(string_1, string_2)
{
    let length_difference = Math.abs(string_1.length - string_2.length);
    if (length_difference > 1)
    {
        return false; 
    }
    return true;
}

console.log(is_one_away("hell", "hello"));