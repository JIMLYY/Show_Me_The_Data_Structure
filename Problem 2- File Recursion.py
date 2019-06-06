import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    files= []
    for file in os.listdir(path):
        fullPath = os.path.join(path,file)
        if os.path.isfile(fullPath) and fullPath.endswith(suffix):
            files.append(fullPath)
        elif os.path.isdir(fullPath):
            files = files + find_files(suffix,fullPath)
    return files

# Test cases 
print(find_files('.c','./testdir'))
print(find_files('.h','./testdir'))
print(find_files('.gitkeep','./testdir'))
