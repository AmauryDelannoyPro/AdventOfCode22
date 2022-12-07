from pprint import pprint


def get_current_dir(dir_list_to_browse):
    """
    Find our current directory in OS.
    Browse values with keys, contained in dir_list_to_browse
    :param dir_list_to_browse: current path (pwd command)
    :return: dict() element containing current elements
    """
    folder = os_dict
    for key in dir_list_to_browse:
        folder = folder.get(key)
    return folder


def add_dir(folder_path, folder_name):
    """
    Add directory in OS, which is a dict()
    :param folder_path: current path (pwd command)
    :param folder_name: new directory name
    :return: Nothing.
    """
    current_element_in_dict = get_current_dir(folder_path)
    current_element_in_dict.update({folder_name: {}})


def add_file(folder_path, file_name, file_size):
    """
    Add file in OS with its size
    :param folder_path: current path (pwd command)
    :param file_name: new file name
    :param file_size: new file size
    :return: Nothing.
    """
    current_element_in_dict = get_current_dir(folder_path)
    current_element_in_dict.update({file_name: file_size})


def cd_command(argument):
    """
    Interprete cd command, so change our current position
    :param argument: directory to reach
    :return: Nothing.
    """
    global dir_path
    if argument == "..":
        dir_path = dir_path[:-1]
    else:
        dir_path.append(argument)


def ls_command():
    """
    Interprete ls command. Nothing to do
    :return: Nothing
    """
    pass


def add_element_in_os(terminal_display_line):
    """
    When we list element with ls command, we take advantage of this to create
    elements in our OS. Here we determine if we have a dir or a file
    :param terminal_display_line: file or dir element displayed
    :return: Nothing.
    """
    element = terminal_display_line.split(" ")
    match element[0]:
        case "dir":
            add_dir(dir_path, element[1])
        case _:
            add_file(dir_path, element[1], element[0])
    pass


# Represent our OS
os_dict = {}

# Current path, equivalent to 'pwd' command
dir_path = []
if __name__ == '__main__':
    with open("input", "r") as input_list:
        score1, score2 = 0, 0
        add_dir(dir_path, "/")

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
