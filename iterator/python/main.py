def exemploIterator():
    mytuple = ("apple", "banana", "cherry")
    myit = iter(mytuple)
    print(next(myit))
    print(next(myit))
    print(next(myit))

def exemploLoopingIterator():
    mystr = "software"
    for x in mystr:
        print(x)


if __name__ == "__main__":
    exemploIterator()
    exemploLoopingIterator()