if __name__ == '__main__':
    with open("input", "r") as input_list:
        score1, score2 = 0, 0
        h = (0,0)
        t = (0,0)
        visited = set()
        visited.add(t)

        for line in input_list.read().splitlines():
            direction, quantite = line.split(" ")
            for _ in range(int(quantite)):
                last_h = h
                match direction:
                    case 'U':
                        h = (h[0], h[1] + 1)
                    case 'D':
                        h = (h[0], h[1] - 1)
                    case 'R':
                        h = (h[0] + 1, h[1])
                    case 'L':
                        h = (h[0] - 1, h[1])
                diff_x = h[0] - t[0]
                diff_y = h[1] - t[1]
                if abs(diff_x) > 1 or abs(diff_y) > 1:
                    t = (last_h[0], last_h[1])
                    visited.add(t)

        score1 = len(visited)
        print(f"Part 1 : {score1}")  #5779
        print(f"Part 2 : {score2}")  #
