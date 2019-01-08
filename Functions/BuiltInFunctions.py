vec = ["apple", "banana", "cherry"]

def builtInFunctions():
    print( id(8) )
    print( id(7) )

    abs( -7.42 ) # only numeric types
    print ( all( [False, True] ) ) # Usually combined with 
    print( any( [False, True] ) )  # Usually combined with 

    print( bytearray("hola", 'ascii') )
    # bytearray() returns an object that can be modified but byte() not
    print( bytes("hola", 'ascii') )
    # A callable obj is llike a C++ functor
    print( callable(str) )
    print( memoryview(b"Hello") ) # List[2] accesible

    print( complex(3, 5) ) # complex('3+5j') is valid too
    print( divmod(5.3,2) ) # quotient and remainder
    print( format(255, 'b') ) # see the amount options
    print( chr(97) ) # Number to unicode char
    print( ord("h") ) # Unicode char to number
    print( max(vec) ) # Alphabetic sort in strings
    print( min(vec) )
    print( sum([1,2,3]) ) # Only numeric values
    print( round(5.76543, 2) ) 
    print( pow(4, 3) )

    # Compile a code block, it's not interpreted 
    exec( compile('print(55)\nprint(88)', 'test', 'exec') )
    # exec() accepts code blocks, unlike eval() which accepts single expression
    eval( 'print("HelloW")' )

    class Person:
      name = "John"
      age = 36
      country = "Norway"
    delattr(Person, 'age')
    print( getattr(Person, "Age", "Age doesn't exists") ) # Same as Person.age but with excep handle
    print( hasattr(Person, 'age') )
    class employee(Person):
      empNumber = 9995
    print( issubclass(employee, Person) )
    print( isinstance("Hello", (float, int, str, list, dict, tuple)) ) #Is one of this types?    
    print( dir(Person) ) # returns all properties and methods of a class    

    print( list(  range(-10, 5, 2)  ) ) 
    print( list(enumerate(  reversed(vec)  )) )
    print( dict(enumerate(vec)) )
    print( dict(name = "John", age = 36, country = "Norway") )
    print( tuple(enumerate(vec)) )
    print( set(enumerate(vec)) )
    print( frozenset(enumerate(vec)) ) # A non-mutable set
    x = iter(vec)
    print( next(x)) # Like a C pointer
    print(list(zip(vec, ("Jenny", "Christy", "Monica", "Vicky")  ))) # zipped as an iterator of tuples
    print( len(vec) ) 

    # filter( [T, F, T, ...], [a, b, c, ...]) -> [a, b, ...]
    def myFunc(x):
        return (True if len(x)>5 else False)
    adults = filter(myFunc, vec)
    for x in adults:
      print(x, end=" ")
    # function to each element
    print("\n",list(  map(myFunc, vec) ))

    # Casting variables float
    print( float(3) )
    print( int(3.5) )
    print( hex(15) )
    print( ascii("My name is Ståle") ) # like str.encode('ascii')
    print( bin(5) )
    print( bin(9) )
    # The object will always return True, unless: is empty, like [], (), {}, is False, is 0, is None
    print( bool(0) ) 
    print( str(42) )

    x = locals()
    y = globals()
    # returns a dictionary of a namespace "elements"
    #print(x)

    # Maybe needs a 'w'
    f = open("demofile.txt", "wt")
    f.write("Hello World") 
    f.close()
    f = open("demofile.txt", "rt")
    print(f.read())
    f.close()