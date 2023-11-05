import copy
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    sm, sc, si = map(int, sys.stdin.readline().split())
    code = list(sys.stdin.readline().strip())
    stream = list(sys.stdin.readline().rstrip())

    bracedict = {}
    code_order = 0
    stream_order = 0
    pointer = 0
    bit_array = [0] * sm
    isLoop = False
    loop_5000 = []
    loop_count = 0
    loop_stack = []

    while code_order < sc:
        if loop_count == 100_000_001:
            break
        if code[code_order] == "+":
            bit_array[pointer] = (bit_array[pointer] + 1) % 256

        elif code[code_order] == "-":
            bit_array[pointer] = (bit_array[pointer] - 1) % 256

        elif code[code_order] == "<":
            pointer = (pointer - 1) % sm

        elif code[code_order] == ">":
            pointer = (pointer + 1) % sm

        elif code[code_order] == ",":
            if stream_order < len(stream):
                bit_array[pointer] = ord(stream[stream_order])
                stream_order += 1
            else:
                bit_array[pointer] = 255


        elif code[code_order] == "]":
            if bit_array[pointer] != 0:
                code_order = loop_stack[-1][0]
                loop_stack[-1][2] += 1

            else:
                temp = loop_stack.pop()
                for i in loop_stack:
                    if i[0] > temp[0] and i[1] < temp[1]:
                        i[2] += temp[2]

        elif code[code_order] == "[":
            if bit_array[pointer] == 0:
                temp_stack = [code_order]
                temp_order = code_order
                while temp_stack:
                    temp_order += 1
                    if code[temp_order] == "[":
                        temp_stack.append(temp_order)
                    elif code[temp_order] == "]":
                        temp_stack.pop()
                code_order = temp_order
            else:
                if code_order in bracedict.keys():
                    temp_order = bracedict[code_order]
                else:
                    temp_stack = [code_order]
                    temp_order = code_order
                    while temp_stack:
                        temp_order += 1
                        if code[temp_order] == "[":
                            temp_stack.append(temp_order)
                        elif code[temp_order] == "]":
                            temp_stack.pop()
                    bracedict[code_order] = temp_order
                loop_stack.append([code_order, temp_order,0])

        if loop_count == 50_000_000:
            loop_5000 = copy.deepcopy(loop_stack)
            for i in range(len(loop_stack)):
                loop_stack[i][2] = 0
            isLoop = True

        loop_count += 1
        code_order += 1

    if not isLoop:
        print("Terminates")
    else:
        loop_stack.sort(key=lambda x: x[1], reverse=True)
        for i in range(len(loop_stack)):
            if loop_stack[i][2] != 0:
                print("Loops", loop_stack[i][0], loop_stack[i][1])
                break
