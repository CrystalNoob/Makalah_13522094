def KMPSolve(source: str, subset: str) -> bool:
	count: int = 0
	len_src: int = len(source)
	len_sub: int = len(subset)

	if len_src <= len_sub:
		return False

	t_index: int = 0
	size: int = 0
	while t_index <= len_src - len_sub:
		p_index: int = size
		while p_index < len_sub:
			if p_index == len_sub - 1 and subset[p_index] == source[t_index + p_index]:
				count += 1
				return True
			else:
				count += 1
				if subset[p_index] == source[t_index + p_index]:
					p_index += 1
					continue
				else:
					border = BorderFunction(subset[:p_index])
					if p_index == 0:
						t_index += 1
					else:
						t_index += p_index - border
						size = border
					break
	return False

def BorderFunction(word: str) -> int:
	if len(word) <= 1:
		return 0
	else:
		prefix = word[:-1]
		suffix = word[1:]
		while prefix:
			if prefix == suffix:
				return len(prefix)
			else:
				prefix = prefix[:-1]
				suffix = suffix[1:]
		return 0
