import check50
import check50.c

@check50.check()
def exists():
    """one.c exists"""
    check50.exists("one.c")
    check50.include("1.txt", "2.txt", "3.txt")
    
@check50.check(exists)
def compiles():
    """mario.c compiles."""
    check50.c.compile("one.c", lcs50=True)
    
@check50.check(compiles)
def test1():
    """handles 2, 3 correctly"""
    out = check50.run("./one").stdin("2\n3").stdout()
    check_pyramid(out, open("1.txt").read())

@check50.check(compiles)
def test2():
    """handles 10, 20 correctly"""
    out = check50.run("./one").stdin("10\n20").stdout()
    check_pyramid(out, open("2.txt").read())

@check50.check(compiles)
def test3():
    """handles -2, 2837 correctly"""
    out = check50.run("./one").stdin("-2\n2837").stdout()
    check_pyramid(out, open("3.txt").read())
