def listSort(argument):
    print( "List before: ", argument )
    try:
        argument.sort()
        print( "List cleared: ", argument )
    except Exception:
        print("Different type elements") 
    # If elements HAVE the same type you can:   
    def myFunc(e):
        return len(e)
    cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
    cars.sort(reverse=True, key=myFunc)
    
def listClear(argument):
    print( "List before: ", argument )
    numsClear.clear()
    print( "List cleared: ", argument )

def listCopy(argument): 
    print( "List original: ", argument )
    numsCopy = argument.copy()
    print( "List copy: ", numsCopy )

def listAppend(argument):
    # [1, 2, 3, [4, 5]] Appends object at the end.
    print( "List before: ", argument )
    argument.append("Halo")
    print( "List appended: ", argument )
    
def listExtend(argument):
    # [1, 2, 3, 4, 5] Extends list by appending elements from the iterable.
    print( "List before: ", argument )
    numEntend = ["hello", "world"]
    argument.extend(numEntend)
    print( "List extended: ", argument )

def listInsert(argument):
    print( "List before: ", argument )
    numInsert = ["hello", "world"]
    argument.insert(1, numInsert)
    print( "List inserted: ", argument )
    
def listCount(argument):
    print( "Number of '42'", argument.count(42) )
    
def listIndex(argument):
    print( "Index of '42'", argument.index(42) )
    
def listPopAndRemove(argument):
    print( "List before: ", argument )
    argument.remove(42)
    print( "List removed element in '42': ", argument )
    argument.pop()
    print( "List poped: ", argument )
    
def listReverse(argument):
    print( "List before: ", argument )
    argument.reverse()
    print( "List reversed: ", argument )

def listFlatten(argument):
    nums = [ [1,2,3], [4,5], [6,7], [8] ]
    print("Multi-dimensional list or list of objects/lists: ", nums)
    # Python std doesn't have a flatten built in function
    # The recommended way is:
    flatNums = [item for sublist in nums for item in sublist]
    print("Flattened list", flatNums)
    # Numpy.array has that beloved function
    
def listBasicOps(argument):
    nums = [1, 2, 3]
    print("The (+)[1, 2, 3] of: ", argument, " is ", argument + nums)
    print("The mult by 2 is: ", argument*2)

def listAccesingSlicing(argument):
    print( "The 3rd elem from back is: ", argument[-3] )
    print( "Slicing 1:3 is: ", argument[1:3] )
    print( "\nTelephone matrix (list of lists)..." )
    nums = [[1,2,3], [4,5,6], [7,8,9]]
    print( "Selection of [1][1]: ", nums[1][1] )
    # If I want a column... imposible, nums[1:1][], because
    # Lists don't keep homogeneous magnitudes in inner lists
    # To manage multi-dim lists/arrays see NUMPY

def listComprehension(argument):
    print( "List before: ", argument )
    # Apply a transformation if a condition is true
    # [ /output function/ /for VARIABLE in REFERENCESEQUENCE/ /CONDITION/ ]
    print("List doubled by list comprehension: ", [i*2 for i in argument if type(i) is int])
    print("Nested List doubled by list comprehension: ",  
          [[j*2 for j in i if type(j) is int] for i in argument if type(i) is list] )
    
# dictionary of functions
switcher = {
    0: listSort,
    1: listClear,
    2: listCopy,
    3: listAppend,
    4: listExtend,
    5: listInsert,
    6: listCount,
    7: listIndex,
    8: listPopAndRemove,
    9: listReverse,
    10: listFlatten,
    11: listBasicOps,
    12: listAccesingSlicing,
    13: listComprehension
}

def listFunctions( funcSelector, argument ):
    # Python doesn't have switch, 
    # Using 'if' is not much efficient 
    # instead it's recomended:
    
    # search in the dictionary
    try:
        switcher[funcSelector](argument)
    except Exception:
        print("You've introduced a non valid selector")  
        
        
#     TODO: 
#         Lists, tuples, arrays and sets
# Arrays in python are a port/wraper of C arrays, much faster than 
# lists  and only support homogeneous data but nobody uses them

#         Built-in function vs C++ stl 
#         Map filter and reduce