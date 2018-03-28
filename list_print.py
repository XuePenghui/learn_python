movie = ["the holy gray", 1975, "Terry Jone & Terry Henry", 91, ["Graham chapman", ["Michael Palin", "John Cleese"]]]
name = ['a', 'b', ['c', 'd'], 'e', ['f']]
# low method
'''
for item in movie:
    if isinstance(item, list):
        for item1 in item:
            if isinstance(item1, list):
                for item2 in item1:
                    print(item2)
            else:
                print(item1)
    else:
        print(item)
'''

# nested method
def print_item(the_list, indent=False,level=0):
    for content in the_list:
        if isinstance(content, list):
            print_item(content, indent, level+1)
        else:
            if indent:
                for num in range(level):
                    print("\t", end='')
            print(content)

print_item(name, True, 1)