from common.HashMap import HashMap

class WinApi:

    keymap = HashMap()
    callMap = HashMap()

    keyIndex = 0

    def __init__(self):
        file = open("../data/WinAPIs.txt", "r")

        self.keyIndex = 0
        for line in file:
            if line == "" or line == "\n":
                continue
            if line.startswith(":"):
                continue

            key = line.replace("\n", "").lower()
            self.addApi(key)

    def getCode(self, key):
        tmpKey = key.lower()
        code = self.keymap.get(tmpKey)

        if (code == None):
            print(key + " not found in file. And added to map")
            self.addApi(tmpKey)
            return self.keymap.get(tmpKey.lower())

        return code

    def getAPICode(self, key):
        code = self.getCode(key)
        self.callMap.add(key,code)
        return code

    def addApi(self, key):
        self.keymap.add(key, str(self.keyIndex))
        self.keyIndex += 1


    def writeKeys(self):
        self.keymap.write("../data/result/ApiMap.txt")
        self.callMap.write("../data/result/CallApiMap.txt")