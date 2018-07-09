# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:53:04 2018

@author: Dyass
"""
"""
    Topics:
            What happens when procedure execution
            hits an unexpected condition?
            
            get an exception....to what was expected
                trying to access beyond list limits
                    test=[1,7,4]
                    test[4]  ->index error
                trying to convert an inappropriate type
                    int(test) ->type error
                referencing a non-existent value
                    a ->name error
                mixing data types without coercion
                    'a'/4 ->Type error
"""
"""
    Other types of Eceptions:
        SyntaxError:Python can't parse program
        NameError:Local or global name not found
        AttributeError:Attribute reference fails
        TypeError:Operand does not have correct type
        ValueError:Operand type okay but value is illegal
        IOError:IO system reports malfunction(e.g file not found)
"""
"""
    What to do with exceptions?:
        What to do when encounter an error?
        Fail silently:
            substitute default values or just continue
            bad idea!!!user gets no warning
        return an error value:
            what value to choose?
            complicates code having to check for a special value
        stop execution,signal error condition
            in Python:raise an exception
            raise Exception("Descriptive String")
"""
"""
    Dealing with exceptions:
        Python code can provide handlers for exceptions:
        try:
            a=int(input("Tell me one number"))
            b=int(input("Tell me another number"))
            print(a/b)
            print("Okay")
        except:
            print("Bug in user input")
        print("Outside")
        If an exception is raised in try block then the program will go to the
    except block otherwise it will not enter the except block.
"""
#try:
#    a=int(input("Please enter the first number:"))
#    b=int(input("Please enter the second number:"))
#    print(a/b)
#    print("Okay")
#except:
#    print("Bug in user input")
""
    
print("Outside")
"""
    Handling specific exceptions:
        have seperate except clauses to deal with a particular type of exception
"""
#try:
#    a=int(input("Please enter the first number"))
#    b=int(input("Please enter the second number"))
#    print("a/b",a/b)
#    print("a+b",a+b)
#except ValueError:#only executes if these error come up else default except is runned
#    print("Could not conver to a number")
#except ZeroDivisionError:
#    print("Can't divivde by zero")
#except:
#    "Print something went very wrong"
"""
    Other Exceptions:
        else:
            body of this is executed when execution of associated try body
            completes with no exceptions
        finally:
            body of this is always executed after try,else and
            except clauses even if they raised another error or executed a break
            continue or return.
            Useful for clean-up code that should be run no matter
            what else happened(e.g close a file)
"""
"""Example of else in exceptions"""
#try:
#    print(a)
#except NameError:
#    print("It is an ivalid name")
#else:
#    print("It is a valid name")
"""Example of above code with else block execution"""
#try:
#    b=4
#    print(b)
#except:
#    print("Something went very wrong")
#else:
#    print("Nothing went very wrong")
"""Example of finally"""
#try:
#    a="2"
#    print(a/2)
#except:
#    print("Something is wrong in the try block")
#finally:
#    print("This block will always be executed")
