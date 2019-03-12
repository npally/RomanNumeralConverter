def rn_converter(x):
    count = 0
    index = 0
    max_index = len(x) -1
    for num in x:

        if num == 'I':
            if index == max_index:
                count += 1

            elif x[index + 1] == 'V':
                count -= 1
                index += 1
            else:
                count += 1
                index += 1

        elif num == 'V':
            count += 5
            index += 1

        elif num == 'X':
            if index == max_index:
                count += 10

            elif x[index + 1] == 'L':
                count -= 10
                index += 1
            else:
                count += 10
                index += 1

        elif num == 'L':
            if index == max_index:
                count += 50

            else:
                count += 50
                index += 1

        elif num == 'C':
            if index == max_index:
                count += 100

            elif x[index + 1] == 'D':
                count -= 100
                index += 1
            else:
                count += 100
                index += 1

        elif num == 'D':
            if index == max_index:
                count += 500

            else:
                count += 500
                index += 1

        elif num == 'M':
            if index == max_index:
                count += 1000

            else:
                count += 1000
                index += 1
    return count


print(rn_converter(input('>>')))
