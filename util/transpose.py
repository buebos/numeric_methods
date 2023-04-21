def transpose(
    inputArr: list[list],
):
    outputArr: list[list] = []

    for i in range(len(inputArr)):
        for j in range(len(inputArr[i])):
            if len(outputArr) <= j:
                outputArr.append([])

            outputArr[j].append(inputArr[i][j])
    return outputArr
