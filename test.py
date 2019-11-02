def maxArea( height):
    max_area,area = 0,0
    for i in range(len(height)):
        for j in range(i +1,len(height)):
            if i < j:
                area = height[i] * height[i]
            else:
                area = height[j] * height[j]
            if max_area < area:
                max_area = area
    return max_area

print(maxArea([1,2,3]))

//test