def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """  
    doc_id_set = set()
    for word in query:
        if word in inverseIndex:
            for id in inverseIndex[word]:
                doc_id_set.add(id)
    return doc_id_set

def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    inverseIndex = {}
    for (i, doc) in enumerate(strlist):
        for word in doc.split():
            if word in inverseIndex:
                inverseIndex[word].add(i)
            else:
                inverseIndex[word] = set()
                inverseIndex[word].add(i)
    return inverseIndex

strlis = ['This is first doc', "This is sec doc", 'third doc is here']
ii = makeInverseIndex(strlis)
print(orSearch(ii, ['This','doc']))