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
    if (is_one_replacement_away(string_1, string_2) || is_one_insert_away(string_1, string_2) || is_one_removal_away(string_1, string_2))
    {
        return true;
    }
    else
    {
        return false;
    }
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

function is_one_insert_away(string_1, string_2)
{
    if (string_1.length != (string_2.length - 1))
    {
        return false;
    }
    let cursor_1 = 0;
    let cursor_2 = 0;
    let incremented = false;
    while (cursor_1 < string_1.length)
    {
        if (string_1[cursor_1] != string_2[cursor_2])
        {
            if (incremented)
            {
                return false;
            }
            else
            {
                incremented = true;
                cursor_2++;
            }
        }
        else
        {
            cursor_1++;
            cursor_2++;
        }
    }
    return true;    
}

function is_one_removal_away(string_1, string_2)
{
    if (string_1.length != (string_2.length + 1))
    {
        return false;
    }
    let cursor_1 = 0;
    let cursor_2 = 0;
    let incremented = false;
    while (cursor_1 < string_1.length)
    {
        if (string_1[cursor_1] != string_2[cursor_2])
        {
            if (incremented)
            {
                return false;
            }
            else
            {
                incremented = true;
                cursor_1++;
            }
        }
        else
        {
            cursor_1++;
            cursor_2++;
        }
    }
    return true;    
}

console.log(is_one_replacement_away("sell", "hell"));  // true
console.log(is_one_replacement_away("hell", "hello"));  // false

console.log(" ");

console.log(is_one_insert_away("owl", "howl"));  // true
console.log(is_one_insert_away("hell", "hello"));  // true
console.log(is_one_insert_away("hello", "hello"));  // false
console.log(is_one_insert_away("maxw", "max"));  // false

console.log(" ");

console.log(is_one_removal_away("howl", "owl"));  // true
console.log(is_one_removal_away("hello", "hell"));  // true
console.log(is_one_removal_away("hello", "hello"));  // false
console.log(is_one_removal_away("max", "maxw"));  // false

console.log(" ");

console.log(is_one_away("sell", "hell"));  // true
console.log(is_one_away("owl", "howl"));  // true
console.log(is_one_away("hello", "hell"));  // true
console.log(is_one_away("hello", "world"));  // false