def solution(skill, skill_trees):
    answer = 0
    for skill_set in skill_trees:
        tmp =''
        for i in range(len(skill_set)):
            if skill_set[i] in skill:
                tmp += skill_set[i]
        if tmp == skill[0:len(tmp)]:
            answer += 1
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))