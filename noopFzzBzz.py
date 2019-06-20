import json
import requests

print("Please enter url extension:")
extenInput = str(input(" "))
url = "https://api.noopschallenge.com{}".format(extenInput)

while True:
    print("To start NOOPS API press '1'")
    inputParam = str(input(" "))

    def getRequest(urlNew):
        url = "https://api.noopschallenge.com{}".format(urlNew)
        g = requests.get(url)
        print(g.json())
        return g.json()

    getData = getRequest(extenInput)

    def evalJson(jsData):
        numRules = len(getData['rules'])
        print(numRules)
        numJSON1 = getData['rules'][0]['number']
        numJSON2 = getData['rules'][1]['number']
        strJSON1 = getData['rules'][0]['response']
        strJSON2 = getData['rules'][1]['response']
        numbers = getData['numbers']

        if numRules == 3:
            numJSON1 = getData['rules'][0]['number']
            numJSON2 = getData['rules'][1]['number']
            strJSON1 = getData['rules'][0]['response']
            strJSON2 = getData['rules'][1]['response']
            numJSON3 = getData['rules'][2]['number']
            strJSON3 = getData['rules'][2]['response']
            print(strJSON3)
            for i in range(len(numbers)):
                if numbers[i] % numJSON1 == 0 and numbers[i] % numJSON2 == 0 and numbers[i] % numJSON3 == 0:
                    numbers[i] = strJSON1+strJSON2+strJSON3
                elif numbers[i] % numJSON1 == 0 and numbers[i] % numJSON3 == 0:
                    numbers[i] = strJSON1+strJSON3
                elif numbers[i] % numJSON1 == 0 and numbers[i] % numJSON2 == 0:
                    numbers[i] = strJSON1+strJSON2
                elif numbers[i] % numJSON1 == 0:
                    numbers[i] = strJSON1
                elif numbers[i] % numJSON2 == 0:
                    numbers[i] = strJSON2
                elif numbers[i] % numJSON3 == 0:
                    numbers[i] = strJSON3
            print(numbers)
            return numbers
        else:
            for i in range(len(numbers)):
                if numbers[i] % numJSON1 == 0 and numbers[i] % numJSON2 == 0:
                    numbers[i] = strJSON1+strJSON2
                elif numbers[i] % numJSON1 == 0:
                    numbers[i] = strJSON1
                elif numbers[i] % numJSON2 == 0:
                    numbers[i] = strJSON2
            print(numbers)
            return numbers

    numbersEvaled = evalJson(getData)

    def postJSON(numbersEval, urlNew):
        url = "https://api.noopschallenge.com{}".format(urlNew)
        numbersToStr = " ".join(map(str, numbersEval))
        payload = {
            "answer": "{}".format(numbersToStr)}
        p = requests.post(url, json=payload)
        print(p.json())
        return p.json()

    postData = postJSON(numbersEvaled, extenInput)

    urlExtensionNew = postData['nextQuestion']
    print(postData['message'])
    correctOrNot = postData['result']

    if correctOrNot == "correct":
        print("Correct!!")
        print(urlExtensionNew)
        # print("Please enter url extension:")
        extenInput = urlExtensionNew

    if inputParam == "1":
        postJSON(numbersEvaled, extenInput)
