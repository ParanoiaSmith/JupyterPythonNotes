point = {'x':-4,'y':"five", 'z': 0}

def stringFunctions( sentence ):
    print( "1. BASIC OPERATIONS:")
    print( "Addition with (+): ", sentence + " Maginfic" )
    print( "Repeat with (*): ", sentence*2 )
    print( "Accesing, slicing: ", sentence[3:8] )
    
    print( "\n2. LOWER/UPPER:")
    print( "Upper first char: ", sentence.capitalize() )
    print( "Are all chars UPPER?: ", sentence.isupper() )
    print( "Upper all chars: ", sentence.upper() ) 
    print( "Has title format?:", sentence.istitle(), "Title: Every word with first char upper" )
    print( "Convert to title format", sentence.title() )
    print( "Swap Upper<->Lower: ", sentence.swapcase() )
    print( "LOWER all chars: ", sentence.casefold() )#
    print( "Are all chars LOWER?:", sentence.islower() )
    print( "LOWER all chars", sentence.lower() )# casefold() will convert more characters into lower case
    
    print( "\n3. SEARCH:")
    # Index does the same as find but if value is not found it raises an excepton, no -1
    print( "Find and returns the position: ", sentence.find("javier") )#
    print( "Find and returns the position: ", sentence.rfind("Javier") )# rindex == rfind
    print( "Find and returns the position: ", sentence.index("Javier") )#
    print( "Find and returns the position: ", sentence.rindex("Javier") )#
    print( "Count 'a' ocurrences: ", sentence.count('a') )
    print( "Ends with 'i'?: ", sentence.endswith('i') )
    print( "Starts with 'aa'?: ", sentence.startswith("aa") )    
    
    print( "\n4. ARE ALL CHARS...")
    print( "Alphanumerics?:", sentence.isalnum() )
    print( "Alphabets?:", sentence.isalpha() )
    print( "Decimals?:", sentence.isdecimal() )
    print( "Digits?:", sentence.isdigit() )
    print( "Valid identifier?:", sentence.isidentifier(), "Valid identifier if it only contains (a-z)|(0-9)|(_)" )
    print( "Numerics?:", sentence.isnumeric() )
    print( "Printables?:", sentence.isprintable(), "Non-printable: '\n', '\t', etc" )
    print( "Whitespaces?:", sentence.isspace() )
    
    print( "\n5. FORMAT: ")
    print( "PARAM: len(string) + newChars")
    # Seems that once a dict mode is introduced it must continiue in this format, Javer-Pol-25 Err
    print( "Format, place arguments before:", "Halo {0}, I'm {1:10d}, I'm {name}".format( "Javier", 25, name="Pol" ))
    print( "Fortmat with a dictionary: ", 'Point({x}, {y}, {z})'.format_map(point))
    print( "Encode to (ASCII, etc...): ", sentence.encode(encoding="ascii",errors="strict") )
    print( "Replace string for other string: ", sentence.replace("name","alter ego") )
    # Could be: (tuple|list ("hello", "Javier", ...)) | string 
    print( "Joins the elements of an iterable with '#Halo_*': ", '#Halo_*'.join( ("Paranoia", "Smith") ) )
    print( "Set the \t length to PARAM: ", sentence.expandtabs(50) )
    print( "Centered, PARAM: ", sentence.center(50, 'ñ') )#
    print( "Justify-left, PARAM", sentence.ljust(50, '*') )#
    print( "Left-zeros fill, PARAM: ", sentence.zfill(50) )# kind of rjust(50, '0')
    
    print( "\nSPLIT: ")
    print( "Removes specific final string: ", sentence.rstrip("ste") )
    print( "Removes repeated 'a' in the left", sentence.lstrip('a') )
    print( "Triplet-tuple with 'name' at middle: ", sentence.partition("name") ) #
    print( "Same but right-last ocurrence: ", sentence.rpartition("name") ) #
    print( "List-split looking ', ': ", sentence.split(", "), " Default whitespaces" ) #
    print( "Same beginning right: ", sentence.rsplit(", ", 1), " Last param indicates number splits") #
    print( "Splits at line-breacks: ", sentence.splitlines() )
    # This method returns a translate table to be used translate() function
    print( "Convert some chars to others: ", sentence.translate( str.maketrans("aeiou", "12345") ))
    
    print( "\n\nPLUS SOME BUILT-IN FUNCTIONS")