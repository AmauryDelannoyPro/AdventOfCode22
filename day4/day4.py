# source:  https://www.geeksforgeeks.org/python-intersection-two-lists/
def intersect(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


if __name__ == '__main__':
    with open("input", "r") as input_list:
        score1 = 0
        score2 = 0
        for line in input_list.read().splitlines():
            # Do your job here !
            section1 = []
            section2 = []
            elf1, elf2 = line.split(",")

            start1, end1 = elf1.split("-")
            section1.extend(range(int(start1), int(end1) + 1))

            start2, end2 = elf2.split("-")
            section2.extend(range(int(start2), int(end2) + 1))
            common_part = intersect(section1, section2)
            if len(common_part) == len(section1) or len(common_part) == len(section2):
                score1 += 1
            if len(common_part) > 0:
                score2 += 1

        print(f"result1 here : {score1}")  # 507
        print(f"result2 here : {score2}")  # 897
