def method1():
    f1 = "Test_A.txt" # has more entries
    f2 = "Test_B.txt" # has less entries
    a = open(f1, "r") 
    b = open(f2, "r") 


    aline = 0
    bline = 0

    # everytime the reader moves to another line, it adds a 1 to "aline"
    # if you want to see the line counting, just print "line" in the for statement
    for line in a:
        aline += 1

    for line in b:
        bline += 1

    if aline > bline:
        End = aline
        print("{0} is longer, it has {1} lines".format(f1, End))
        a.close() ; b.close()

    elif bline > aline:
        End = bline
        print("{0} is longer, it has {1} lines".format(f2, End))
        a.close() ; b.close()




def method2():
    a = "Test_A.txt"
    b = "Test_B.txt"

    aline = 0
    bline = 0

    with open(a, "r") as f:
        with open(b, "r") as g:
            for line in f:
                aline += 1

            for line in g:
                bline += 1

            if aline > bline:
                End = aline
                print("{0} is longer, it has {1} lines".format(a, End))
                f.close() ; g.close()
            elif bline > aline:
                End = bline
                print("{0} is longer, it has {1} lines".format(b, End))
                f.close() ; g.close()

method1()

