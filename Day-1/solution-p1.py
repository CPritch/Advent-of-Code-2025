dial_position = 50
zero_count = 0

with open('input.txt', 'r', encoding='utf-8') as file:
    for rotation in file:
        direction = rotation[0]
        amount =  int(float(rotation[1:]))
        dial_position = (dial_position + amount if direction == "R" else dial_position - amount) % 100
        if dial_position == 0:
            zero_count += 1 

print("Final Position: " + str(dial_position))
print("Zero Count: " + str(zero_count))