import os
import app_data

appName = app_data.readAppData()
os.system('ng new ' + appName + ' --routing=false --style=scss')
