def jumpingOnClouds(c):
    location = 0
    step = 0
    for i in range(0,100):
        i=location
        if location == len(c)-1:
            print(step)
            break
        elif c[i+1] == 0 and i+1 == len(c)-1:
            location+=1
            step+=1

        elif c[i+1]==1 and c[i+2]==0:
            location = i+2
            step +=1
        elif c[i+1]==0 and c[i+2]==1:
            location = i+1
            step +=1
        elif c[i+1]==0 and c[i+2] == 0:
            location = i+2
            step +=1
jumpingOnClouds([0, 0, 0, 1, 0, 0])




