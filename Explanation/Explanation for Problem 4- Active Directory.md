### Explanation for Problem 4: Active Directory
1. Data structure
This question use array to store the groups and users

2. Basically, I check if the user in a group by using "if user in group.get_users()" statement. If is user is not found, I recursively call the function on all the subgroups. If the user is found, return True. Otherwise, return False. 

_Time complexity is O(M*N). Space complexity is O(M*N)._
_M is the depth of group * N is the average users of files in each depth_
