from topia.termextract import extract


'''Using the Toperia Term Extractor, this finds keywords, along with their importance to the text as a whole, and
returns them'''
def get_keywords(text):
    if text is None or "" or False:
        return []

    extractor = extract.TermExtractor()
    keywords = sorted(extractor(text))

    filtered_keywords = []
    for keyword in keywords:
        if keyword[1] > 2:
            filtered_keywords.append(keyword[0])

    return filtered_keywords
