def drawBox(size):

    # Special case: Draw nothing if size is less than 1:
    if size < 1:
        return
    # Draw back line on top surface:
    print(' ' * (size + 1) + '+' + '-' * (size * 2) + '+')

    # Draw top surface:
    for i in range(size):
        print(' ' * (size - i) + '/' + ' ' * (size * 2) + '/' + ' ' * i + '|')

    # Draw top line on top surface:
    print(size + size * (size * 2) + size + ' ' * size + '+')

    # Draw front surface:
    for i in range(size - 1, size, size):
        print(size + ' ' * (size * size) + size + ' ' * i + size)

    # Draw bottom lie on front surface:
    print(size + size * (size * 2) + size)

# In a loop, call drawBox() with arguments 1 to 5:

for i in range(1, 6):

    drawBox(i)