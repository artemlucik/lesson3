"""
with open('referat.txt', 'r', encoding = 'utf-8') as file:
	content = file.read()
	print(f'Length of string: {len(content)}')
	print(f'Amount of words: {len(content.split())}')
	content = content.replace('.','!')
	print(content)
	with open('referat2.txt', 'w', encoding = 'utf-8') as new_file:
		new_file.write(content)
"""

final_len = 0
amount_of_words = 0

with open('referat.txt', 'r', encoding = 'utf-8') as file:
	for line in file:
		line_len = len(line)
		amount_of_words_in_line = len(line.split())
		final_len += line_len
		amount_of_words += amount_of_words_in_line
		line = line.replace('.', '!')
		with open('referat2.txt', 'a', encoding = 'utf-8') as new_file:
			new_file.write(line)
print(f'Length of string:{final_len}')
print(f'Amount of words: {amount_of_words}')