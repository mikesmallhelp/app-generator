def generateApplicationComponentHtml(applicationConfiguration):
   print('Generating app component html...')

   try:
      f = open('src/app/app.component.html', 'w')
      f.write('<H1>'+ applicationConfiguration.applicationName  +'</H1>' + '\n')
      f.write('<app-' + applicationConfiguration.cardName + '></app-' + applicationConfiguration.cardName + '>'); 

   finally:
      f.close()

   print('Generating app component html ended')

def addInputs(applicationConfiguration):
   print('Add inputs for card ' + applicationConfiguration.cardName  + '...')

   try:
      f = open('src/app/' + applicationConfiguration.cardName +  '/' + applicationConfiguration.cardName  + '.component.html', 'w')   
      f.write('<H2>'+ applicationConfiguration.cardName  +'</H2>' + '\n')
      f.write('<div><input placeholder = "' + applicationConfiguration.fieldNames[0]  + '"></div>\n')
      f.write('<div><input placeholder = "' + applicationConfiguration.fieldNames[1]  + '"></div>\n')

   finally:
      f.close()

   print('Add inputs for card ' + applicationConfiguration.cardName  + ' ended')