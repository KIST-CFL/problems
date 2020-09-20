import check50
import check50.c

@check50.check()
def exists():
    """one.c exists"""
    check50.exists("one.c")
    check50.include("1.txt", "2.txt", "3.txt")
