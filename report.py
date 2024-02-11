import pickle

with open('output.pkl', 'rb') as file:
    visitedURLs, words_dict, longest_url, subdomains = pickle.load(file)

with open('report.txt', 'w') as report:
    report.write("Report:\n")
    # count unique pages
    report.write("\nUnique Pages Found: " + str(len(visitedURLs)) + "\n")
    # writes longest page and its length
    report.write(
        "\nLongest Page (by Word Count): " + longest_url[0] + " (" + str(longest_url[1]) + " words)" + "\n")

    # writes out most common words by sorting by count, then name
    report.write("\n50 Most Common Words:\n")
    count = 0
    for i in sorted(words_dict.items(), key=lambda kv: -kv[1])[:50]:
        report.write(f"{i[0]} = {i[1]}\n")


    # counts and writes all subdomains ordered alphabetically by key and # of unique pages in each domain
    report.write("\n" + str(len(subdomains)) + " Subdomains Found:\n")
    for key, value in sorted(subdomains.items()):
        report.write(key + ", " + str(value) + "\n")