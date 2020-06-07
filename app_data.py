class AppData:
   appName = None
   cardName = None
   fieldNames = []
   
def readAppData():
   appData = AppData()

   try:
      f = open("mika.gen", encoding = 'utf-8')
      
      lineNumber = 1
      for line in f:
         if lineNumber == 1:
            appData.appName = line.strip()
         elif lineNumber == 2:
            appData.cardName = line.strip()
         lineNumber += 1

   finally:
      f.close()

   return appData
