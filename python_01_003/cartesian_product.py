# this marks the beginning of a python script. 

def get_cartesian_product(a:list[int|str], b:list[int|str]) -> list[list[int|str]]:
    result: list = []
    for i in a:
        for j in b:
            result.append([i,j])
    return result


def main():
    set_A= [1,2,3,4,5]
    set_B = ["A", "B", "c", "D", "E"]

    testing = get_cartesian_product(set_A,set_B)
    print(testing)


if __name__=="__main__":
    main()