def print_pairs(items):
    i = 0
    while i < len(items) - 1:
        j = 0
        while j < len(items):
            if items[i] != items[j] and j > i:
                print(items[i] + ", " + items[j])
            j = j +1
        i = i + 1

items = ["A","B","C"]
print_pairs(items)
