
repository = ["bags","baggage","banner","bammer", "bugs","banner"]
customerQuery = "bag"

def searchSuggestions(repository, customerQuery):
    # Write your code here

    output = []
    i = 0
    contained = []
    for i in range(len(customerQuery)):
        for item in repository:
            if item.startswith(customerQuery[0:i]):
                output.append(customerQuery[0:i])
                i += 1

    output= max(output,key=len)
    print("The Output is {}".format(output))
    for item in repository:
            if item.startswith(output):
                contained.append(item)


    for each in contained:
        print(each)





print(searchSuggestions(repository,customerQuery))