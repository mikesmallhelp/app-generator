import os
import application_configuration_reader
import application_generator

print('Generating app...')

applicationConfiguration = application_configuration_reader.readApplicationConfiguration()
os.system('ng new ' + applicationConfiguration.applicationName + ' --routing=false --style=scss --strict=true')
os.chdir(applicationConfiguration.applicationName)
os.system('ng add @angular/material --defaults=true')
os.system('ng generate component ' + applicationConfiguration.cardName)
application_generator.generateApplicationComponentHtml(applicationConfiguration)
application_generator.addInputs(applicationConfiguration)
os.system('ng serve')

print('Generating application ended')
print('The application is running in the url localhost:4200')
