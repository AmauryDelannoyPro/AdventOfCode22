

if __name__ == '__main__':
    with open("input", "r") as input_list:
        elf_calory_list = [0, 0]
        current_elf = 1

        for line in input_list:
            if line == "\n":
                current_elf += 1
                # Ajoute le prochain elf avec 0 cal pour l'instant
                elf_calory_list.append(0)
            else:
                elf_calory_list[current_elf] += int(line)

        elf_calory_list.sort(reverse=True)
        print(f"Le plus de calories : {elf_calory_list[0]}")

        # PART 2
        sum_cal = 0
        for cal in elf_calory_list[:3]:
            sum_cal += cal
        print(f"Le top 3 plus de calories : {sum_cal}")



