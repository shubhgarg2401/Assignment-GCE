ASSIGNMENT-GCE



Assignment  GOOGLE CLOUD ENGINEERING : 

Develop a micro service for google cloud function which will take in two sets of arrays as an input from http request in the form of JSON payload and will combine both the arrays and write the result after sorting and combining both the arrays. Function should complete its executions within 180 seconds. Use python language to execute your code.

APPROACH:  The idea behind the approach was to create a simple google cloud function micro service using the cloud console. While the same task can be performed using the cli, I opted for the cloud console . 
I created the main.py file on my local machine which i have included in the github repo. There was  no need for any requirements.txt file since all the necessary libraries I used came pre-installed in flask.

My main idea was to take input from the json payload, which is the form of a dictionary, then convert that dictionary to a python list and then carry on the simple sorting algo to give out the final result.

PROBLEM : The main problem I encountered was the syntax, since this service is not very popular and I have not worked with it in the past, I was not able to get the syntax correct no matter how many times I tried.

THE solution that i am including is the approach I took, while it might not work on the cloud function test area . It works fine if I use it on my local machine. This was the main problem.
While it was quite easy to use data that included a string as an argument or array as a string, I was not able to use the data in the file input.py to get the wanted result.

I have used the google cloud console to perform the task.


1. Go to the search bar and search for google cloud function api.
Enabling the api will allow us to use google cloud function.

2. Now go to cloud function using the navigation menu in the top left corner.

3. Click on create function when the service finishes loading.

4. I named the function Assignmetgce, with region as “asia-south1”(mumbai) , tick the option for allow unauthorised access to allow anyone from the world with the request url to use the cloud function.
You can also copy the mentioned url to use it to access the function later.
	
5. Leave the rest as default since we do not need much memory to compute our process.

![1](https://user-images.githubusercontent.com/53488130/119222006-cf320f00-bb0f-11eb-9dc7-2d3d6335eb2e.PNG)


6.Select the correct code editor ,(python 3.9), copy paste the contents of the “main.py” file that is included in the repository into the cloud function main.py file along with the contents of the requirements.txt file.
 Change the name of the function to you own function used in the main.py file.
Click run in the bottom to start your function.

![2](https://user-images.githubusercontent.com/53488130/119222027-f5f04580-bb0f-11eb-8b63-cc203fa3044e.PNG)


 After the function finishes deployment, I can right click on the three dots (on the right side) to click on the test function.

This opens the test area where you can put in your json payload dictionary 


ALGORITHM :  The algo is nothing but a simple sort() function that the python included which sorts an array. I simply added the two lists together and then sorted them to give the final result.


