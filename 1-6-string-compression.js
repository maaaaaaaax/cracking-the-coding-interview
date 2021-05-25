// 1.6 String Compression

// Implement a method to perform basic string compression using the counts of repeated characters. 
// For example, the string aabcccccaaa would become a2b1c5a3.
// If the "compressed" string would not become smaller than the original string, your method should return the original string. 
// You can assume the string has only uppercase and lowercase letters (a - z).

function compress_string(s)
{
    let count = 1;
    let compressed_string = "";
    for (let i = 0; i < s.length - 1; i++)
    {
        if (s[i] == s[i + 1])
        {
            count++;
        }
        else
        {
            compressed_string += s[i];
            compressed_string += String(count);
            count = 1;
        }
    }
    compressed_string += s[s.length - 1];
    compressed_string += String(count);
    if (compressed_string.length < s.length)
    {
        return compressed_string;
    }
    else
    {
        return s;
    }
}

console.log(compress_string("aabcccccaaa"))