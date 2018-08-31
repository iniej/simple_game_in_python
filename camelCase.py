
sentence = input('Enter a sentence ')


sentence_title = sentence.title()

camelcased_split = sentence_title.split(' ')
camelcased_string = ''.join(camelcased_split)
camelcased = camelcased_string[0].lower() + camelcased_string[1:]


print(camelcased)
