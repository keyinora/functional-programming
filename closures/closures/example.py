def concatter():
	doc = ""
	def doc_builder(word):
		# "nonlocal" tells Python to use the 'doc'
		# variable from the enclosing scope
		nonlocal doc
		doc += word + " "
		return doc
	return doc_builder

# save the returned 'doc_builder' function
# to the new function 'harry_potter_aggregator'
harry_potter_aggregator = concatter()
harry_potter_aggregator("Mr.")
harry_potter_aggregator("and")
harry_potter_aggregator("Mrs.")
harry_potter_aggregator("Dursley")
harry_potter_aggregator("of")
harry_potter_aggregator("number")
harry_potter_aggregator("four,")
harry_potter_aggregator("Privet")

print(harry_potter_aggregator("Drive"))
# Mr. and Mrs. Dursley of number four, Privet Drive
