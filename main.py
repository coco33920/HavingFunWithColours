from operation import Operation
from progressbar import Progressbar
try:
    import readline
except:
    pass
if __name__ == "__main__":
    b = Operation("")
    while(not b.exist()):
        i = input("Please enter the file you wish to act upon: ")
        b = Operation(i);
    b.prints()
