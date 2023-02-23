size_slot_character = 4
stack_list = []
score1, score2 = "", ""


def fill_stack_list():
    for i in range(1, len(line_with_size_regularized), size_slot_character):
        if line_with_size_regularized[i].isalpha():
            letter = line_with_size_regularized[i]
            current_stack = i // size_slot_character
            stack = stack_list[current_stack]
            if stack is None:
                stack = []
            stack.append(letter)
            stack_list[current_stack] = stack


def move_objects_part1(quantity, start, dest):
    start_stack = stack_list[start]
    dest_stack = stack_list[dest]
    for i in range(quantity):
        obj = start_stack.pop()
        dest_stack.append(obj)


def move_objects_part2(quantity, start, dest):
    start_stack = stack_list[start]
    dest_stack = stack_list[dest]

    for obj in start_stack[-quantity:]:
        start_stack.remove(obj)
        dest_stack.append(obj)

if __name__ == '__main__':

    with open("input", "r") as input_list:
        input_data = input_list.read().splitlines()
        # Search Empty line between stacks and moves
        split_line = input_data.index("")

        # l'un ou autre nb_col, a voir si besoin
        # nb_col = input_data[split_line-1][-1:]
        nb_col = len(input_data[split_line-1].replace(" ", ""))
        stack_list = [None] * nb_col # Create list representing stack


        # Iterate on stack, reversed to get last element on top
        for idline, line in reversed(list(enumerate(input_data[:split_line-1]))):
            line_with_size_regularized = line
            while len(line_with_size_regularized) < nb_col*size_slot_character:
                line_with_size_regularized += " "
            fill_stack_list()

        # Iterate on movement to do
        for idline, line in enumerate(input_data[split_line+1:]):
            move_info = line.split(" ")
            quantity = int(move_info[1])
            start_position = int(move_info[3])-1
            end_position = int(move_info[5])-1
            # move_objects_part1(quantity, start_position, end_position)
            move_objects_part2(quantity, start_position, end_position)

        # print(stack_list)
        for stacks in stack_list:
            if stacks:
                score1 += stacks.pop()

        # print(f"Part 1 : {score1}")  #FWNSHLDNZ
        print(f"Part 2 : {score1}")  #RNRGDNFQG
