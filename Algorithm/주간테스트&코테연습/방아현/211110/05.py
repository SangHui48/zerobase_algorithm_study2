def solution(skill, skill_tress):
	result = 0
	for skill_tree in skill_tress:
		idx = 0
		for s in skill_tree:
			if s not in skill:
				continue
			if skill[idx] != s:
				idx = -1
				break
			idx += 1
		if idx != -1:
			result += 1
	return result



print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
