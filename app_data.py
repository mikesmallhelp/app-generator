class AppData:
   appName = None
   cardName = None
   fieldNames = []
   
def readAppData():
   print('Reading app data...')
   appData = AppData()

   try:
      f = open("small_help.txt", encoding = 'utf-8')
      
      lineNumber = 1
      for line in f:
         if lineNumber == 1:
            appData.appName = line.strip()
         elif lineNumber == 2:
            appData.cardName = line.strip()
         elif lineNumber == 3:
            appData.fieldNames.append(line.strip())
         elif lineNumber == 4:
            appData.fieldNames.append(line.strip())
         lineNumber += 1

   finally:
      f.close()

   print('Reading app data ended')
   return appData
