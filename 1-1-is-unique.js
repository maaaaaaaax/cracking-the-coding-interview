// 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

function is_unique(string)
{
    let length = string.length;
    let seen = new Set();
    for (i = 0; i < length; i++)
    {
        let char = string[i];
        if (seen.has(char)) {
            return false;
        } else {
            seen.add(char);
        }        
    }
    return true;
}

console.log(is_unique('halo')); // true
console.log(is_unique('hello')); // false