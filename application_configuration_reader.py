class ApplicationConfiguration:
   applicationName = None
   cardName = None
   fieldNames = []
   
def readApplicationConfiguration():
   print('Reading application configuration...')
   applicationConfiguration = ApplicationConfiguration()

   try:
      f = open("small_help.txt", encoding = 'utf-8')
      
      lineNumber = 1
      for line in f:
         if lineNumber == 1:
            applicationConfiguration.applicationName = line.strip()
         elif lineNumber == 2:
            applicationConfiguration.cardName = line.strip()
         elif lineNumber == 3:
            applicationConfiguration.fieldNames.append(line.strip())
         elif lineNumber == 4:
            applicationConfiguration.fieldNames.append(line.strip())
         lineNumber += 1

   finally:
      f.close()

   print('Reading application configuration ended')
   return applicationConfiguration
