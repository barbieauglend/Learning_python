#Python 3.5

list = []

n = int(input())

for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("list."+cmd)
    else:
        print(list)