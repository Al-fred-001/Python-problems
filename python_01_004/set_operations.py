# This marks the beginning of a python script. 

# def union(a:list[str|int], b:list[str|int]) -> list[str|int]:
#     ...


def intersection(a:list[str|int], b:list[str|int]) -> list[str|int]:
    result: list = []
    for i in a:
        if (i in b):
            result.append(i)
        else:
            continue
    return result

def union(a:list[str|int], b:list[str|int]) -> list[str|int]:
    result : list =[]
    uncommon: list =[]
    common: list =[]
    for i in a:
        if (i in b):
            common.append(i)
            b.remove(i)
        else:
            uncommon.append(i)
    result = sorted(uncommon+common+b)
    return result

def difference(a:list[str|int], b:list[str|int]) -> list[str|int]:
    # result: list = []
    for i in a:
        if (i in b):
            a.remove(i)
    return a


'''--Needs appending and debugging--'''
# def symmetric_difference(a:list[str|int], b:list[str|int]) -> list[str|int]:
#     a_u_b = union(a,b)
#     a_n_b = intersection(a,b)
#     result = difference(a_u_b, a_n_b)
#     return result



def main():
    list_01 = [1,2,3,4,5,6]
    list_02 = [2,3,4,78,9]

    testing0 = intersection(list_01, list_02)
    testing1 = union(list_01,list_02)
    testing2 = difference(list_01, list_02)
    testing3 = symmetric_difference(list_01,list_02)
    print(testing0)
    print(testing1)
    print(testing2)
    print(testing3)


if __name__ =="__main__":
    main()