if (rec1[0] >= rec2[2]) or (rec1[2] < rec2[0]):
    return False
if (rec1[3] < rec2[1]) or (rec1[1] > rec2[3]):
    return False
return True