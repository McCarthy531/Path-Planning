def LineGen(pt1,pt2):
    line = []
    if pt1[0] == pt2[0]:
        if pt1[1] < pt2[1]: inc = 1
        else: inc = -1
        for i in range(pt1[1],pt2[1],inc):
            line.append((pt1[0],i))
    elif pt1[1] == pt2[1]:
        if pt1[0] < pt2[0]: inc = 1
        else: inc = -1
        for i in range(pt1[1],pt2[1],inc):
            line.append((i,pt1[1]))    
    elif abs(pt1[1]-pt2[1]) <= abs(pt1[0]-pt2[0]): #y = mx + b
        m = (pt1[1]-pt2[1])/(pt1[0]-pt2[0])
        b = pt1[1]-pt1[0]*m
        if pt1[0] < pt2[0]: inc = 1
        else: inc = -1
        for i in range(pt1[0],pt2[0],inc):
            line.append((i,round(m*i+b)))
    elif abs(pt1[1]-pt2[1]) > abs(pt1[0]-pt2[0]): #x = my + b
        m = (pt1[0]-pt2[0])/(pt1[1]-pt2[1])
        b = pt1[0]-pt1[1]*m
        if pt1[1] < pt2[1]: inc = 1
        else: inc = -1
        for i in range(pt1[1],pt2[1],inc):
            line.append((round(m*i+b),i))
    line.append(pt2)
    return line

def DistCheck(points, pt_random):
    dist = []
    for point in points:
        dist.append(((float(point[1])-float(pt_random[1]))**2 + (float(point[0])-float(pt_random[0]))**2)**(0.5))
    short_dist = dist.index(min(dist))
    return short_dist

def NoGoCheck(line, img, img2):
    for point in line:
        print(point, "=", img[point[0]][point[1]], " : ", img2[point[0]][point[1]])
        if img[point[0]][point[1]] == 0:
            return False
    return True