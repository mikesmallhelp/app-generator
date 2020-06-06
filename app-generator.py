import os
import parameters_reader

appName = parameters_reader.readParameters()
os.system('ng new ' + appName + ' --routing=false --style=scss')
