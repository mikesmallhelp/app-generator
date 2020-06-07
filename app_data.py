def readAppData():

   try:
      f = open("mika.gen", encoding = 'utf-8')
  
      for line in f:
         appName = line.rstrip()

      #for line in f.read().split('\n')
      #   print(line)

   finally:
      f.close()

   return appName
