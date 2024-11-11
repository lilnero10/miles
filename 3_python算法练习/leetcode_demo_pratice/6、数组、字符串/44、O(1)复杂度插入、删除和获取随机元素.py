import random

class RandomizedSet:
    def __init__(self):
        self.val_to_index = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        last_element = self.values[-1]
        idx_to_remove = self.val_to_index[val]

        # Swap the last element with the element to remove
        self.values[idx_to_remove] = last_element
        self.val_to_index[last_element] = idx_to_remove

        # Remove the last element
        self.values.pop()
        del self.val_to_index[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# 示例用法
commands = ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
args = [[], [1], [2], [2], [], [1], [2], []]

randomized_set = RandomizedSet()
results = [None]

for command, arg in zip(commands[1:], args[1:]):
    # zip(commands[1:], args[1:]) ==[('insert', [1]), ('remove', [2]), ('insert', [2]), ('getRandom', []),
    #                                  ('remove', [1]), ('insert', [2]), ('getRandom', [])]
    if command == "insert":
        results.append(randomized_set.insert(arg[0]))
    elif command == "remove":
        results.append(randomized_set.remove(arg[0]))
    elif command == "getRandom":
        results.append(randomized_set.getRandom())

print(results)