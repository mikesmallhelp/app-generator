import os
import app_data

appData = app_data.readAppData()
os.system('ng new ' + appData.appName + ' --routing=false --style=scss')
os.chdir(appData.appName)
os.system('ng generate component ' + appData.cardName)
