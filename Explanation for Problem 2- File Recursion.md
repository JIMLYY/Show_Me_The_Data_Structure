### Explanation for Problem 2: File Recursion
1. Data structure
In this problem, I use array to store path of the files.

2. Basically, I use for loop to check every item in the directory. If it is a file and with desired suffix, we add it into the file list: If not, we will call find_files recursively to check subdirectory.

_Time complexity is O(M*N). Space complexity is O(n)._
_M is the depth of directory * N is the average number of files in each depth_
