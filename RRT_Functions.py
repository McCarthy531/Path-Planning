def DistCheck(points, pt_random):
    dist = []
    for point in points:
        dist.append(((float(point[1])-float(pt_random[1]))**2 + (float(point[0])-float(pt_random[0]))**2)**(0.5))
    short_dist = dist.index(min(dist))
    return short_dist

def LineGen(pt1,pt2):
    h_start = pt1[0]
    h_end = pt2[0]
    w_start = pt1[1]
    w_end = pt2[1]
    line = []
    if h_start == h_end:
        if w_start < w_end: inc = 1
        else: inc = -1
        for i in range(w_start,w_end,inc):
            line.append((h_start,i))
    elif w_start == w_end:
        if h_start < h_end: inc = 1
        else: inc = -1
        for i in range(h_start,h_end,inc):
            line.append((i,w_start))    
    elif abs(w_start-w_end) <= abs(h_start-h_end): 
        m = (w_start-w_end)/(h_start-h_end)
        b = w_start-(m*h_start)
        if h_start < h_end: inc = 1
        else: inc = -1
        for i in range(h_start,h_end,inc):
            line.append((i,round(m*i+b)))
    elif abs(w_start-w_end) > abs(h_start-h_end): 
        m = (h_start-h_end)/(w_start-w_end)
        b = h_start-(m*w_start)
        if w_start < w_end: inc = 1
        else: inc = -1
        for i in range(w_start,w_end,inc):
            line.append((round((m*i+b)),i))
    line.append(pt2)
    return line

def NoGoCheck(line, img):
    for point in line:
        if img[(point[0],point[1])] == 0:
            return False
    return True