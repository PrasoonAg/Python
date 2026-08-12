#=========================================================================#
# 09 - if __name__=='__main__'
#=========================================================================#
# Every Python file gets a special variable called __name__.
# if the module is being run directly from the command line, the '__name__' is set to "__main__". Thus, this behaviour is used to check whether the module is run direclty or imported to another file.

# When a file is run directly:
# __name__ = "__main__"

# When a file is imported:
# __name__ = module_name

# Used to check whether a file is being run directly or imported.

from module import myFunc
#=========================================================================#