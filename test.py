# import spacy
# nlp = spacy.load("en_core_web_sm")
# about_text = "We go around the Sun"
# about_doc = nlp(about_text)
# for token in about_doc:
#     print(
#         f"""
# TOKEN: {str(token)}
# =====
# TAG: {str(token.tag_):10} POS: {token.pos_}
# EXPLANATION: {spacy.explain(token.tag_)}"""
#  	)
b = True
n = int(input("N="))
for i in range(2, n):
	for j in range(2, i):
		if i % j == 0:
			b = False
	if b:
		print(i)
	b = True