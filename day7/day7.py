from pprint import pprint


def get_current_dir(dir_list_to_browse):
    folder = os_dict
    for key in dir_list_to_browse:
        folder = folder.get(key)
    return folder


def add_dir(folder_path, folder_name):
    current_element_in_dict = get_current_dir(folder_path)
    current_element_in_dict.update({folder_name: {}})


def add_file(folder_path, file_name, file_size):
    current_element_in_dict = get_current_dir(folder_path)
    current_element_in_dict.update({file_name: file_size})


def cd_command(argument):
    global dir_path
    # print(f"$ cd {argument}")
    if argument == "..":
        dir_path = dir_path[:-1]
    else:
        dir_path.append(argument)


def ls_command():
    # print("ls")
    pass


def add_element_in_os(terminal_display_line):
    element = terminal_display_line.split(" ")
    match element[0]:
        case "dir":
            add_dir(dir_path, element[1])
        case _:
            add_file(dir_path, element[1], element[0])
    pass


os_dict = {}
dir_path = []
if __name__ == '__main__':
    with open("input", "r") as input_list:
        score1, score2 = 0, 0
        add_dir(dir_path, "/")

        # Test before starting
        # dir_path = ["/"]
        # add_dir(dir_path, "a")
        #
        # # Change repository to /a/
        # dir_path = ["/", "a"]
        # add_file(dir_path, "toto.txt", 1234)
        # add_file(dir_path, "zizi.log", 1231)
        #
        # dir_path = dir_path[:-1]
        # add_dir(dir_path, "B")
        #
        # print(os_dict)

        for line in input_list.read().splitlines():
            # Command input
            if line[0] == "$":
                command = line.split(" ")
                match command[1]:
                    case "cd":
                        cd_command(command[2])
                    case "ls":
                        ls_command()
            else:
                # Command result (ls only)
                add_element_in_os(line)

        # pprint(os_dict)
        print(f"Part 1 : {score1}")  #
        print(f"Part 2 : {score1}")  #
