import googlesearch

results = googlesearch.search("hello")


for item in results:
    print("item", item)