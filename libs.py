import re
import spacy

getExp = spacy.load("en_core_web_sm")
s = ["NOUN", "PROPN", "PRON"]
soIt = ["she", "he", "it"]
soNhieu = ["i", "we", "you", "they"]

def simplePresent(verb, isPersonSingular):
	if not isPersonSingular:
		return verb
	if verb == "have" or verb == "has":
		return "has"
	elif verb[-1] == 'o' or verb[-1] == 's' or verb[-1] == 'x' or verb[-2]+verb[-1] == 'sh' or verb[-2]+verb[-1] == 'ch':
		return verb + "es"
	elif verb[-1] == 'y':
		if verb[-2] == 'a' or verb[-2] == 'u' or verb[-2] == 'e' or verb[-2] == 'i'  or verb[-2] == 'o':
			return verb + "s"
		else:
			return verb[:-1] + "ies"
	else:
		return verb + "s"

def get_subject_phrase(doc):
    sub = ""
    for token in doc:
        if ("subj" in token.dep_):
            subtree = list(token.subtree)
            start = subtree[0].i
            end = subtree[-1].i + 1
            sub = doc[start:end]

    for i in sub:
    	print(i.pos_)

def solve(quest):
	r = re.compile(r"\((.+?)\)")
	q = r.search(quest)
	start = q.span()[0]
	end = q.span()[1]
	verb = q[1]
	# doc = getExp(quest[:start])
	doc = getExp(quest[:start] + verb + quest[end:])
	tense = "simple present"
	return get_subject_phrase(doc)

	# for i in range(len(doc), 0, -1):
	# 	if doc[i-1].pos_ in s:
	# 		sub = doc[i-1]
	# 		if sub.text.lower() in soIt or doc[i-1].pos_ == "PROPN" or doc[i-1].pos_ == "NOUN":
	# 			isPersonSingular = True
	# 		else:
	# 			isPersonSingular = False
	# 		break

	# if tense == "simple present":
	# 	verb = simplePresent(verb, isPersonSingular)

	# return quest[:start] + verb + quest[end:]

print(solve(quest="My teacher usually (give) us homework."))