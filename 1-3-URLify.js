//  1.3 URLify

//  Write a method to replace all spaces in a string with '%20'. 
// You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.
// (Note: If implementing in Java, please use a character array so that you an perform this operation in place.)

function URLify(s)
{
    let trimmed = s.trim();
    let url = trimmed.replace(" ", "%20");
    return url;
}

console.log(URLify(' hello world '));