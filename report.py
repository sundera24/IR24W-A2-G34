import pickle

with open('output.pkl', 'rb') as file:
    visitedURLs, words_dict, longest_url, subdomains = pickle.load(file)

with open('report.txt', 'w') as report:
    report.write("Final Report:\n")
    # list number of unique pages found
    report.write(f'\nUnique Pages Found: {str(len(visitedURLs))}\n')
    # reports the longest page url and its wordcount
    report.write(f'\nLongest Page (by Word Count): {longest_url[0]}: {str(longest_url[1])} words\n')
    # list 50 most common words by in order of frequency
    report.write("\n50 Most Common Words:\n")
    for i in sorted(words_dict.items(), key=lambda kv: -kv[1])[:50]:
        report.write(f'{i[0]} = {i[1]}\n')
    # lists ics.uci.edu subdomains in alphabetic order
    report.write(f'\n{len(subdomains)} Subdomains Found:\n')
    for key, value in sorted(subdomains.items(), key=lambda x: (x[0][8:].lower() if 'https' in x[0] else x[0][7:].lower(), x[1])):
        report.write(f'{key}, {value}\n')