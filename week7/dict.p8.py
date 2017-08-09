def _single_digit_words_sample(sample_integer):
	sample_integer = list(str(sample_integer))
	sample_dict = {	'0' : 'zero',
					'1' : 'one',
					'2' : 'two',
					'3' : 'three',
					'4' : 'four',
					'5' : 'five',
					'6' : 'six',
					'7' : 'seven',
					'8' : 'eight',
					'9' : 'nine'}
	out_list = []
	for integer in sample_integer:
		out_list.append(sample_dict[integer])
	out_str = ' '.join(out_list)
	return out_str
print (_single_digit_words_sample("1375"))