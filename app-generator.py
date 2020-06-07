import os
import app_data

def generateAppComponentHtml(appData):
   print('Start generating app component html')

   try:
      f = open('src/app/app.component.html', 'w')
      f.write('<H1>'+ appData.appName  +'</H1>' + '\n')
      f.write('<app-' + appData.cardName + '></app-' + appData.cardName + '>'); 

   finally:
      f.close()

   print('End generating app component html')

appData = app_data.readAppData()
os.system('ng new ' + appData.appName + ' --routing=false --style=scss')
os.chdir(appData.appName)
os.system('ng add @angular/material --defaults=true')
os.system('ng generate component ' + appData.cardName)
generateAppComponentHtml(appData)
os.system('ng serve')
