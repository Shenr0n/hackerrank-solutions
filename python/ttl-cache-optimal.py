# Binary search to check if data start time is earlier than query
# Return the index of start time in data, which is <= query.

#O(logn)
def binarys(data, query):
    left = 0
    right = len(data)-1
    found = -1

    while left <= right:
        mid = left+(right-left)//2
        if data[mid][0] <= query:
            found = mid
            left = mid + 1
        else:
            right = mid - 1
    return found


def count(data, queries):
    count = 0
    
    #Sort events/ cache based on start time
    # O(nlogn)
    data.sort()

    # O(qlogn)
    for query in queries:

        #Gives the latest data start time which is <= query
        found = binarys(data, query)

        if found >= 0:
            start = data[found][0]
            end = data[found][1]

            if start <= query <= start + end:
                count += 1

    return count


data = [[100, 50],[200, 30],[150, 100], [400,60]]
queries = [123, 145, 456, 300]
print(count(data, queries))
