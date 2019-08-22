'''Your task is to remove all duplicate words from a string, leaving only single (first) words entries.

Example:

Input:

'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

Output:

'alpha beta gamma delta'
'''
def remove_duplicate_words(s):
    list = []
    element = s.split()
    for e in element:
        if not e in list:
            list.append(e)
    return  ' '.join(list)
