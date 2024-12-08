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

