from django.shortcuts import render
from django.http import request, HttpResponse
import json
import numpy as np

# Create your views here.

def indexPageView(request) :
   return render(request, 'homepages/index.html')

def employerPageView(request) :
  return render(request, 'homepages/companyhome.html')

def azure_matchbox(request) :
   import urllib
   data = {
    "Inputs": {
      "input1": {
        "ColumnNames": ["user_id", "job_title"],
        "Values": [[
          #request.GET[], 
          '55',
          #request.GET['asin'], 
          'Bus Driver',
          ]]
      }
    }
   }
   body = str.encode(json.dumps(data))

   url = 'https://ussouthcentral.services.azureml.net/workspaces/ba336cb92ebe429bb683ed665d93278b/services/564fd49e781247c5b3eff1cf0bd04464/execute?api-version=2.0&details=true'
   api_key = 'WfZluhvXMTckeff1hiD83S9M62NhLITUUADiZXqt2/QfxTPQelB8lZx/61jfeva22hei9w8vVylsaeAS/RwJcA==' # Replace this with the API key for the web service
   headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

   req = urllib.request.Request(url, body, headers) 
   req.method = "POST"

   response = urllib.request.urlopen(req)
   result = response.read()
   result = json.loads(result) # Convert JSON byte stream into dictionary
   prediction = result['Results']['output1']['value']['Values'][0]
   data = {'matchbox_results':str(f'User: {prediction[0]}, 1.{prediction[1]}, 2.{prediction[2]}, 3.{prediction[3]}, 4.{prediction[4]} <- look up these IDs in the DB and display their product details instead of the ID number')}
   
   context = {
      "prediction1" : prediction[1],
      "prediction2" : prediction[2],
      "prediction3" : prediction[3],
      "prediction4" : prediction[4],
      "prediction5" : prediction[5],
   }
   

   return render(request, 'homepages/matchbox.html', context) 

def azure_matchbox_company(request) :
   import urllib
   data = {
    "Inputs": {
      "input1": {
        "ColumnNames": ["job_title", "FullName"],
        "Values": [[
          #request.GET[], 
          'Bus Driver',
          #request.GET['asin'], 
          'Patricia Bell',
          ]]
      }
    }
   }
   body = str.encode(json.dumps(data))

   url = 'https://ussouthcentral.services.azureml.net/workspaces/ba336cb92ebe429bb683ed665d93278b/services/7e13ad8c6e634485af52e9b405a419c7/execute?api-version=2.0&details=true'
   api_key = '5Vzo1ujzbIDCHSC+QPZY9xWOWYSnUJ6b5aRnwrligMY9MxLocXveqcVZAe2Ky7Jk7S0je8UPb50S0EtNAp4vNg==' # Replace this with the API key for the web service
   headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

   req = urllib.request.Request(url, body, headers) 
   req.method = "POST"

   response = urllib.request.urlopen(req)
   result = response.read()
   result = json.loads(result) # Convert JSON byte stream into dictionary
   prediction = result['Results']['output1']['value']['Values'][0]
   data = {'matchbox_results':str(f'User: {prediction[0]}, 1.{prediction[1]}, 2.{prediction[2]}, 3.{prediction[3]}, 4.{prediction[4]} <- look up these IDs in the DB and display their product details instead of the ID number')}
   
   context = {
      "prediction1" : prediction[1],
      "prediction2" : prediction[2],
      "prediction3" : prediction[3],
      "prediction4" : prediction[4],
      "prediction5" : prediction[5],
   }
   

   return render(request, 'homepages/companymatchbox.html', context) 

def aboutPageView(request) :
    return render(request, 'homepages/about.html')

def employerAboutPageView(request) :
    return render(request, 'homepages/companyabout.html')
    