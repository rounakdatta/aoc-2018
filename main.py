import sys

pnum = sys.argv[1]
fnum = sys.argv[2]

from getter import getQuestionInput
exec("from src.d%s import p%s as prog" % (pnum, fnum))

getQuestionInput(int(pnum))

out = prog()
print(out)