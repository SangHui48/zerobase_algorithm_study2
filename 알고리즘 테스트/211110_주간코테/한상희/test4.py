def solution(dirs):
    x, y = 0, 0
    visit = []
    for i in range(len(dirs)):
        if dirs[i] == 'U':
            if y < 5:
                y += 1
                if ((x, y-1), (x, y)) not in visit:
                    visit.append(((x, y-1), (x, y)))
        elif dirs[i] == 'D':
            if y > -5:
                y -= 1
                if ((x, y), (x, y+1)) not in visit:
                    visit.append(((x, y), (x, y+1)))
        elif dirs[i] == 'R':
            if x < 5:
                x += 1
                if ((x-1, y), (x, y)) not in visit:
                    visit.append(((x-1, y), (x, y)))
        elif dirs[i] == 'L':
            if x > -5:
                x -= 1
                if ((x, y), (x+1, y)) not in visit:
                    visit.append(((x, y), (x+1, y)))
    answer = len(visit)
    return answer

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))