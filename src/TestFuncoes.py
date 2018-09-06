import funcoes
import sys

def readCSV():
    with open("agendatelefonica.csv") as agenda:
        return agenda.readlines()


def writeCSV(array):
    with open("agendatelefonica.csv", 'w') as agenda:
        for item in array:
            agenda.write(item.lower())

def testADD():
    success = 0
    # before
    array = readCSV()
    # before

    listOfDict = [
          {"testName": "TEST1-KHDIHDIHDHHDHD"  , "testTelfone": "11222233334" , "expected" : True  }
        , {"testName": "TEST2-HDIHDIHDHHDHDHH" , "testTelfone": "11222233334" , "expected" : False }
        , {"testName": "TEST3-KHDIHDIHDHHDHDH" , "testTelfone": "111222233334", "expected" : True }
        , {"testName": "TEST5"                 , "testTelfone": "11122223333" , "expected" : False }
        , {"testName": "TEST6-IHDIHDIHDHHDHDH" , "testTelfone": "11122223333" , "expected" : False }
    ]


    index = 0
    for dict in listOfDict:


        index += 1
        ret = funcoes.adicionar(dict["testName"], dict["testTelfone"])

        if ret == dict["expected"] :
            print(("{}st case successfuly response: {}").format(index, ret))
        else:
            success += 1
            print(("{}st case faillure response: {}").format(index, ret))


    #after
    writeCSV(array)
    # after

    if success > 0:
        sys.exit(1)
    else:
        sys.exit(0)

testADD()
