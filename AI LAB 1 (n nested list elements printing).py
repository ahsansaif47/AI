#This is a Recursive programme to print elements of a list.
#If a list element is a list then print those elements also.

from collections.abc import Iterable

sampleList = ["Animals", "Plants", "Humans", [1,2,3,[4,5,6],8,9,0]]

# Display list is a function as discussed earlier.
def displayList(sampList):
    for i in sampList:
        if isinstance(i, Iterable):
            if(len(i)>1):
                displayList(i)
            else:
                print(i)
        else:
            print(i)

displayList(sampleList)
