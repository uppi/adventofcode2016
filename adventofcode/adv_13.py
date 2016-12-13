try:
    import queue
except:
    import Queue as queue


def can_be_passed(x, y, salt):
    if x < 0 or y < 0:
        return False
    val = bin(x * x + 3 * x + 2 * x * y + y + y * y + salt)
    return len([c for c in val if c == "1"]) % 2 == 0


DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def path(start_x, start_y, end_x, end_y, salt):
    if((start_x, start_y) == (end_x, end_y)):
        return []

    visited = set()
    q = queue.Queue()

    visited.add((start_x, start_y))
    q.put((start_x, start_y, None))

    while not q.empty():
        x, y, prev = q.get()
        for dx, dy in DIRECTIONS:
            pos = (x + dx, y + dy)
            if pos not in visited:
                if(pos == (end_x, end_y)):
                    result = [pos, (x, y)]
                    while prev is not None:
                        px, py, prev = prev
                        result.append((px, py))
                    return list(reversed(result))
                visited.add(pos)
                if can_be_passed(pos[0], pos[1], salt):
                    q.put((pos[0], pos[1], (x, y, prev)))

    return None


def location_count(start_x, start_y, salt, max_step_count):
    visited = set()
    q = queue.Queue()

    visited.add((start_x, start_y))
    q.put((start_x, start_y, 0))

    while not q.empty():
        x, y, step_count = q.get()
        for dx, dy in DIRECTIONS:
            pos = (x + dx, y + dy)
            if pos not in visited:
                if can_be_passed(pos[0], pos[1], salt):
                    visited.add(pos)
                    if step_count == max_step_count - 1:
                        continue
                    q.put((pos[0], pos[1], step_count + 1))
    return len(visited)


if __name__ == '__main__':
    salt = 1362
    my_path = path(1, 1, 31, 39, salt)
    if my_path is None:
        print("Unpassable!")
    else:
        print(len(my_path) - 1)
    print(location_count(1, 1, salt, 50))
