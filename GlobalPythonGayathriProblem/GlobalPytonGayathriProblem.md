**@Gayathri**, the first thing is that **global**  keyword is used to refer the global variables declared in the program or to declare any variable as global which is going to appear inside function block (as in your case).

Let you please understand the difference between following 2 code samples.

&raquo; Using **global** keyword:

    i = 10;

    def func():
        global i;
        i = 20; # Modifying global i
        print(i); # 20

    print(i); # 10
    func();
    print(i); # 20

&raquo; Without using **global** keyword:


    i = 10;
    def func():
        i = 20; # It won't modify global i, here i is local to func()
        print(i); # 20

    print(i); # 10
    func(); 
    print(i); # 10

Now, let's focus on the main problem.

✓ In first case, the value of local **person** in `def display(person):` is "Dave" and it is printing `here is Dave` & after that it is creating global **i** and setting its value to 'Jack'. In second call i.e. `display(i)` is passing the set value `Jack` of **i** which is assigned to local **person** variable available in `def display(person):` and therefore it is printing `here is Jack` and no error.



✓ In second case, no explicit assignment or function call for setting value of **i** before function call `display(i)` therefore there's an error.

