###### 1.unit test cases:

small test cases are written to check single functions or methods in code.

to ensure each smallest part of the code work perfectly.

ex:

def add(a, b):

    return a + b



def test\_add():

    assert add(2, 3) == 5



###### 2.code coverage:

measures how much of your code is executed while running tests.



ex:

1. 100% coverage :-all lines of code are tested correctly
2. 70% coverage :-only 70% of the code are tested.



###### 3.Jenkins:

Automation tool used for continuous integration(CI) and continuous deployment(CD).

automatically builds code, tests, deploy hem whenever changes are made.

Example: After pushing code to GitHub → Jenkins runs tests automatically.



###### 4.TDD(test drive development):

writes tests first then try to make the code pass.

cycle: write test-->test code(fail)-->write code-->test code(pass)-->refactor

5.BDD(behaviour driven development):

similar to TDD but focuses on plain language



###### 5.field function in python:

to define default values or behaviour for fields in data classes.

class Product(BaseModel):

&nbsp;   name: str = Field(..., min\_length=3, max\_length=50)

&nbsp;   code: str = Field(..., pattern=r"^\[A-Z]{3} AA \\d{3}$")





###### 6.client side vs server side validation:

client side validation:

* it happens in the browser (using html/js)
* checking if email is valid before submit
* it gives faster feedback



server side validation:

* it happens on server(python,DB)
* rechecking data after form submission
* more secure and prevents tampering but it will be slow
