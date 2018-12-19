def listClear(argument):
    numsClear = argument
    print( "List before: ", numsClear )
    numsClear.clear()
    print( "List after: ", numsClear )

def listCopy(argument):
    numsCopy = argument.copy()
    print( "List before: ", numsCopy )
    numsCopy.clear()
    print( "List after: ", numsCopy )

def listAppend(argument):
    print( "List before: ", argument )
    argument = argument.append("Halo")
    print( "List after: ", argument )
    
def listExtend(argument):
    print( "List before: ", argument )
    numAppend = ["hello", "world"]
    numAppend = argument.append(numApend)
    print( "List after: ", numAppend )
    
# dictionary
switcher = {
    1: listClear,
    2: listCopy,
    3: listAppend
}

def listFunctions( funcSelector, argument ):
    # Python doesn't have switch, 
    # Using 'if' is not much efficient 
    # instead it's recomended:
    
    # search in the dictionary
    # 
    try:
        switcher[funcSelector](argument)
    except Exception:
        print("You've introduced a non valid selector")    
  