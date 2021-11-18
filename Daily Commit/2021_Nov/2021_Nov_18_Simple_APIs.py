# API lets programs to talk to each other
# REST API = representational state transfer 
# URL = Uniform resource locator 

"""
HTTP Methods

Get = Retrieves data from the server
Post = Submits data to server
Put = Updates data already on server
Delete = Deletes data from server 

""" 


'''
Overview of HTTP 
When you, the client, use a web page your browser sends an HTTP request to the server where the page is hosted. The server tries to find the desired resource by default "index.html". If your request is successful, the server will send the object to the client in an HTTP response. This includes information like the type of the resource, the length of the resource, and other information.

The figure below represents the process. The circle on the left represents the client, the circle on the right represents the Web server. The table under the Web server represents a list of resources stored in the web server. In this case an HTML file, png image, and txt file .

The HTTP protocol allows you to send and receive information through the web including webpages, images, and other web resources. In this lab, we will provide an overview of the Requests library for interacting with the HTTP protocol.



# Uniform Resource Locator: URL
Uniform resource locator (URL) is the most popular way to find resources on the web. We can break the URL into three parts.

scheme this is this protocol, for this lab it will always be http://
Internet address or Base URL this will be used to find the location here are some examples: www.ibm.com and  www.gitlab.com 
route location on the web server for example: /images/IDSNlogo.png
You may also hear the term Uniform Resource Identifier (URI), URL are actually a subset of URIs. Another popular term is endpoint, this is the URL of an operation provided by a Web server.



# Request 
The process can be broken into the request and response process. The request using the get method is partially illustrated below. In the start line we have the GET method, this is an HTTP method. Also the location of the resource /index.html and the HTTP version. The Request header passes additional information with an HTTP request:


# Response
The figure below represents the response; the response start line contains the version number HTTP/1.0, a status code (200) meaning success, followed by a descriptive phrase (OK). The response header contains useful information. Finally, we have the response body containing the requested file, an  HTML  document. It should be noted that some requests have headers.




'''

# Requests is a Python Library that allows you to send <code>HTTP/1.1</code> requests easily. We can import the library as follows:



import requests


import os 
from PIL import Image
from IPython.display import IFrame

url='https://www.ibm.com/'
r=requests.get(url)


# We have the response object r, this has information about the request, like the status of the request. We can view the status code using the attribute status_code.

r.status_code



print(r.request.headers)
You can view the request body, in the following line, as there is no body for a get request we get a None:

print("request body:", r.request.body)
print("request body:", r.request.body)
You can view the HTTP response header using the attribute headers. This returns a python dictionary of HTTP response headers.

header=r.headers
print(r.headers)

# We can obtain the date the request was sent using the key Date

header['date']
# Content-Type indicates the type of data:

header['Content-Type']
# You can also check the encoding:

 r.encoding
# As the Content-Type is text/html we can use the attribute text to display the HTML in the body. We can review the first 100 characters:

r.text[0:100]
# You can load other types of data for non-text requests, like images. Consider the URL of the following image:

# Use single quotation marks for defining string
url='https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png'
# We can make a get request:

r=requests.get(url)
# We can look at the response header:

print(r.headers)
# We can see the 'Content-Type'

r.headers['Content-Type']
# An image is a response object that contains the image as a bytes-like object. As a result, we must save it using a file object. First, we specify the file path and name

path=os.path.join(os.getcwd(),'image.png')
path
# We save the file, in order to access the body of the response we use the attribute content then save it using the open function and write method:

with open(path,'wb') as f:
    f.write(r.content)
# We can view the image:

Image.open(path)  





# In the previous section, we used the wget function to retrieve content from the web server as shown below. Write the python code to perform the same task. The code should be the same as the one used to download the image, but the file name should be 'Example1.txt'.

!wget -O /resources/data/Example1.txt https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt


url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path=os.path.join(os.getcwd(),'example1.txt')
r=requests.get(url)
with open(path,'wb') as f:
    f.write(r.content)
    
 '''
Get Request with URL Parameters 
You can use the GET method to modify the results of your query, for example retrieving data from an API. We send a GET request to the server. Like before we have the Base URL, in the Route we append /get, this indicates we would like to preform a GET request. This is demonstrated in the following table:

Image
The Base URL is for http://httpbin.org/ is a simple HTTP Request & Response Service. The URL in Python is given by:

url_get='http://httpbin.org/get'
A query string is a part of a uniform resource locator (URL), this sends other information to the web server. The start of the query is a ?, followed by a series of parameter and value pairs, as shown in the table below. The first parameter name is name and the value is Joseph. The second parameter name is ID and the Value is 123. Each pair, parameter, and value is separated by an equals sign, =. The series of pairs is separated by the ampersand &.

Image
To create a Query string, add a dictionary. The keys are the parameter names and the values are the value of the Query string.

payload={"name":"Joseph","ID":"123"}
Then passing the dictionary payload to the params parameter of the  get() function:

r=requests.get(url_get,params=payload)
We can print out the URL and see the name and values

r.url
There is no request body

print("request body:", r.request.body)
We can print out the status code

print(r.status_code)
We can view the response as text:

print(r.text)
We can look at the 'Content-Type'.

r.headers['Content-Type']
As the content 'Content-Type' is in the JSON format we can use the method json(), it returns a Python dict:

r.json()
The key args has the name and values:

r.json()['args']
Post Requests 
Like a GET request, a POST is used to send data to a server, but the POST request sends the data in a request body. In order to send the Post Request in Python, in the URL we change the route to POST:

url_post='http://httpbin.org/post'
This endpoint will expect data as a file or as a form. A form is convenient way to configure an HTTP request to send data to a server.

To make a POST request we use the post() function, the variable payload is passed to the parameter  data :

r_post=requests.post(url_post,data=payload)
Comparing the URL from the response object of the GET and POST request we see the POST request has no name or value pairs.

print("POST request URL:",r_post.url )
print("GET request URL:",r.url)
We can compare the POST and GET request body, we see only the POST request has a body:

print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)
We can view the form as well:

r_post.json()['form']
 
 '''