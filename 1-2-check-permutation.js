// 1.2 Check Permutation

// Given two strings, write a method to decide if one is a permutation of the other.
function check_permutation(string_1, string_2)
{
    if (string_1.length != string_2.length)
    {
        return false;
    }
    let string_1_array = to_array(string_1);
    let string_2_array = to_array(string_2);
    // console.log(string_1_array);
    // console.log(string_2_array);
    merge_sort(string_1_array);
    merge_sort(string_2_array);
    let string_1_sorted = string_1_array.join("");
    let string_2_sorted = string_2_array.join("");
    // console.log(string_1_sorted);
    // console.log(string_2_sorted);
    if (string_1_sorted == string_2_sorted)
    {
        return true;
    }
    else
    {
        return false;
    }
}

console.log(check_permutation('hello', 'world')); // false
console.log(check_permutation('dog', 'god')); // true

// Sort an array of character or integers
function merge_sort(array)
{
    // Base case: If the length of the string is 1, consider it sorted.
    if (array.length == 1)
    {
        return;
    }
    else
    {
        // Split the array in halves.
        let left_length = Math.floor(array.length / 2);
        let right_length = array.length - left_length;
        
        let left_half = [];
        for (let i = 0; i < left_length; i++) {
            left_half.push(array[i]);
        }

        let right_half = [];
        for (let i = 0; i < right_length; i++) 
        {
            right_half.push(array[i + left_length]);
        }

        // Sort the left half.
        merge_sort(left_half);

        // Sort the right half.
        merge_sort(right_half);

        // Merge the sorted halves.
        for (let i = 0, l = 0, r = 0; i < array.length; i++)
        {
            if (r >= right_length)
            {
                array[i] = left_half[l];
                l++;
            }
            else if (l >= left_length)
            {
                array[i] = right_half[r];
                r++;
            }
            else if (left_half[l] > right_half[r])
            {
                array[i] = right_half[r];
                r++;
            }
            else
            {
                array[i] = left_half[l];
                l++;
            }
        }
    }
}

// String To Array: Given a string, convert it to an array
function to_array(s)
{
    array = []
    for (let i = 0; i < s.length; i++)
    {
        array.push(s[i]);
    }
    return array;
}


// Comment in this block of code to quickly test the merge_sort() function:

// let string_1 = 'zyxabcd';
// console.log(string_1);
// let string_1_array = [];
// for (let i = 0; i < string_1.length; i++)
// {
//     string_1_array.push(string_1[i]);
// }
// merge_sort(string_1_array);
// string_1_sorted = string_1_array.join("");
// console.log(string_1_sorted);