## Description for Problem 2: File Recursion

For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

Here is an example of a test directory listing, which can be found in __*test.dir*__:
>>
./testdir<br>
./testdir/subdir1<br>
./testdir/subdir1/a.c<br>
./testdir/subdir1/a.h<br>
./testdir/subdir2<br>
./testdir/subdir2/.gitkeep<br>
./testdir/subdir3<br>
./testdir/subdir3/subsubdir1<br>
./testdir/subdir3/subsubdir1/b.c<br>
./testdir/subdir3/subsubdir1/b.h<br>
./testdir/subdir4<br>
./testdir/subdir4/.gitkeep<br>
./testdir/subdir5<br>
./testdir/subdir5/a.c<br>
./testdir/subdir5/a.h<br>
./testdir/t1.c<br>
./testdir/t1.h<br>

Python's ```os``` module will be useful—in particular, you may want to use the following resources:<br>
[os.path.isdir(path)](https://docs.python.org/3.7/library/os.path.html#os.path.isdir)<br>
[os.path.isfile(path)](https://docs.python.org/3.7/library/os.path.html#os.path.isfile)<br>
[os.listdir(directory)](https://docs.python.org/3.7/library/os.html#os.listdir)<br>
[os.path.join(...)](https://docs.python.org/3.7/library/os.path.html#os.path.join)<br>

_**Note**_: ```os.walk()``` is a handy Python method which can achieve this task very easily. However, for this problem you are not allowed to use ```os.walk()```.
