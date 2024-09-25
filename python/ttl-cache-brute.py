def count(data, queries):
    count = 0
    for query in queries:
        for cache in data:
            start = cache[0]
            end = cache[1]
            
            if start <= query < start + end:
                count += 1
                break
    return count

data = [[100, 50],[200, 30],[150, 100]]
queries = [123, 145, 456]
print(count(data, queries))
