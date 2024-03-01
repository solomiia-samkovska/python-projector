def find_sum(target: int, li: list[int]) -> tuple[int, int]:
    
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            if li[i] + li[j] == target:
                return i, j   
                   

def find_sum_fast(target: int, li: list[int]) -> tuple[int, int]:
    d = {}
    for i, el1 in enumerate(li):
        el2 = target - el1
        if el2 in d:
            return d[el2], i
        else:
            d[el1] = i


print(find_sum(7, [1, 3, 2, 0, 5])) 
print(find_sum_fast(7, [1, 3, 2, 0, 5]))
