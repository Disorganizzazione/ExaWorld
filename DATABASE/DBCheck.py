from ExaDB import *

def connect():
    return ExaDB()

def creature():
    db=connect()
    creature=null
    while(creature != "fine"):
        try:
            a=1
            creature= db.getcreature(a)
            if creature.__len__()>8 :
                animals(creature)
            else : plant(creature)
