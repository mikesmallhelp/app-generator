import os
import application_configuration_reader

def generateApplicationComponentHtml(applicationConfiguration):
   print('Generating app component html...')

   try:
      f = open('src/app/app.component.html', 'w')
      f.write('<H1>'+ applicationConfiguration.applicationName  +'</H1>' + '\n')
      f.write('<app-' + applicationConfiguration.cardName + '></app-' + applicationConfiguration.cardName + '>'); 

   finally:
      f.close()

   print('Generating app component html ended')

def addInputs(cardName, fieldNames):
   print('Add inputs for card ' + cardName  + '...')

   try:
      f = open('src/app/' + applicationConfiguration.cardName +  '/' + applicationConfiguration.cardName  + '.component.html', 'w')   
      f.write('<H2>'+ applicationConfiguration.cardName  +'</H2>' + '\n')
      f.write('<div><input placeholder = "' + fieldNames[0]  + '"></div>\n')
      f.write('<div><input placeholder = "' + fieldNames[1]  + '"></div>\n')

   finally:
      f.close()

   print('Add inputs for card ' + cardName  + ' ended')

print('Generating app...')

applicationConfiguration = application_configuration_reader.readApplicationConfiguration()
os.system('ng new ' + applicationConfiguration.applicationName + ' --routing=false --style=scss --strict=true')
os.chdir(applicationConfiguration.applicationName)
os.system('ng add @angular/material --defaults=true')
os.system('ng generate component ' + applicationConfiguration.cardName)
generateApplicationComponentHtml(applicationConfiguration)
addInputs(applicationConfiguration.cardName, applicationConfiguration.fieldNames)
os.system('ng serve')

print('Generating application ended')
print('The application is running in the url localhost:4200')
