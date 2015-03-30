def leader(x,n):
    f = open('leaderboard.txt', 'r+')
    for i in range(9):
        l = f.readline()
        v = l[:2]
        v = v.strip()
        if x >= int(v):
            break
    f.seek(15*i)
    r = f.read(140-((i+1)*14))
    f.seek(15*(i+1))
    f.write(r)
    f.seek(15*i)
    f.write("{0:2s} {1:10s}".format(str(x), n))
    f.seek(0)
    print("\nLeaderboard:\n")
    print(f.read())
    f.close()
