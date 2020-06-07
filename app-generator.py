import os
import app_data

def generateAppComponentHtml(appData):
   print('Generating app component html...')

   try:
      f = open('src/app/app.component.html', 'w')
      f.write('<H1>'+ appData.appName  +'</H1>' + '\n')
      f.write('<app-' + appData.cardName + '></app-' + appData.cardName + '>'); 

   finally:
      f.close()

   print('Generating app component html ended')

def addInputs(cardName, fieldNames):
   print('Add inputs for card ' + cardName  + '...')

   try:
      f = open('src/app/' + appData.cardName +  '/' + appData.cardName  + '.component.html', 'w')   
      f.write('<H2>'+ appData.cardName  +'</H2>' + '\n')
      f.write('<div><input placeholder = "' + fieldNames[0]  + '"></div>\n')
      f.write('<div><input placeholder = "' + fieldNames[1]  + '"></div>\n')

   finally:
      f.close()

   print('Add inputs for card ' + cardName  + ' ended')

print('Generating app...')

appData = app_data.readAppData()
os.system('ng new ' + appData.appName + ' --routing=false --style=scss')
os.chdir(appData.appName)
os.system('ng add @angular/material --defaults=true')
os.system('ng generate component ' + appData.cardName)
generateAppComponentHtml(appData)
addInputs(appData.cardName, appData.fieldNames)
os.system('ng serve')

print('Generating app ended')
print('The application is running in the url localhost:4200')
