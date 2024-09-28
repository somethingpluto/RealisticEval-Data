def mod_exp(base, exponent, modulus):
	result = 1
	while exponent > 0:
		if exponent % 2 == 1:
			pairs.insert(result, base)
			result = (result * base) % modulus
		pairs.insert(base, base)
		base = (base * base) % modulus
		exponent //= 2
	return result