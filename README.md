11.11.2024
Step #1
Ruslan analyzed crappy plan by Fidel (that new plan wasn't perfect because at least Kubernetes in that architecture cost too much human resources)
Fidel also worried abour Ruslan's architecture with Django Framework
We decided that we rebuild our architecture, but at first we need to make our first step anyway

We need to understand how to communicate with ChatGPT4
we don't need to spent our time to build another architecture right now

Step #1
We returned to our previous script

Step #2
We created our common GitHub Repositor, where both Fidel and Ruslan can push any changes they want, and it is good starting point with cimmuncation (i don't understand why we didn't do it yet)

Step #3
We finally get to the same problem where we was before
We need to solve this issue while executing our test.py script
16.11.2024 finally we did it

Step #4
create cli command which will send the file in the local direction to ChatGPT and then return the response in structured way
this is how i expect it will work

python script.py path_to_pdf_file path_to_the_file_where_promt_stored
exampl
python script.py D:\\FidelLocalPc\\folder\folder\Document.pdf promt.txt
finally we did it
We observed that our prompt consume much more than simple Hello's request
previously we've spent 
13 tokens for request
9 tokens for response

now we spend
47008 tokens for request(it is because we upload huge pdf files)
586 tokens for response(here we see ~x65 cost difference with just simple request processing - that is very interesting)

Now we have very simple prototype, we need to check our balance each time when we send any request (i think it will be better to make request/response more compact, so we will spend less $ for processing and less memory for keeping this data into our database)

Step #5
We need to rebuild our architecture(next Saturday will chech this)
...
Here i see 2 solutions:
1) Make everything from the scratch (less efforts in short time (sorry correct me if I wrong), but much costly to maintain the final system)
-This option also good , but difficult to maintain

2) Use Django framework (more efforts in short time, easier to maintain in the future) - I like this option 
Yes that framework allow to build website much more easier with whole bunch of functionalities

Yes I can start, but i thinkwill be better for me to continue that course
from 20'th December i will fe on vacation till 8th January

Yes i think i can continute that course and in parallel we can start that project with simple html template to build the pages and connect with PostgreSQL database where all our data will be stored

We need to think...
Go meeting on 21st December, or 22nd

before that day
1) Check our promt maybe you have some idea how to make it more compact
2) Download Beyond and Compare app (very easy soft)

Step #6
We build 2 pages /home and /result

Step #7
We need to make corrections on our design little bit
25/01

Step #8
Connect FrontEnd with BackEnd and Deploy into PythonAnywhere (where we already create an account and have an access to the machine)
We will represent our project there
