  

<div style="text-align:center;">
░░░░░░░░░▄░░░░░░░░░░░░░░▄░░░░  <br>
░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌░░░   <br>
░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐░░░   <br>
░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐░░░   <br>
░░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐░░░   <br>
░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌░░░   <br>
░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌░░   <br>
░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐░░   <br>
░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌░   <br>
░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌░   <br>
▀▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐░   <br>
▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌   <br>
▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐░   <br>
░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌░   <br>
░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐░░   <br>
░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌░░   <br>
░░░░▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀░░░   <br>
░░░░░░▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀░░░░░   <br>
░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▀▀░░░░░░░░   <br>
</div> <br>

<div style="text-align:center;">

# MuchScript 0.1.3
https://muchscript.sblip.dev/
  
MADE BY SHAURYA_BLIP

INSPIRED BY DOGE AND DOEGFATHER ELON MUSK

MUCH WOW. MUCH COOL. MUCH CRYPTO.

</div>

```c
    # Print
    PRINT("Hello World!")

    # Variable       Method for finding out the price of crypto
    WOW doge_price = CRYPTO_PRICE("DOGE", "INR")

    # If else statement.
    IF doge_price < 30 THEN 
        PRINT(doge_price)
        PRINT("DOGE SAD.")
    ELSE
        PRINT(doge_price)
        PRINT("DOGE HAPPY!!!!!!!!")
    END

    # Lambda (Almost..)
    FUN add(num1, num2) -> num1 + num2

    # Using the lambda function
    PRINT(add(1,2))

    # List of names
    WOW names = ["Jose", "Maria", "John", "Mary"]
    # Gets the length of the list
    WOW len_of_names = LEN(names)

    # Prints all the names in the list
    # We get object from list by /num not [num]
    FOR i = 0 TO len_of_names THEN
        PRINT("Name: " + names/i)
    END
```

## Installation

Install MuchScript by using pip:

    $ pip install muchscript

Install MuchScript Manually:

    $ git clone https://github.com/shaurya-blip/MuchScript.git
    $ cd MuchScript/
    $ python3 setup.py install

## Running

By installing MuchScript you will install an executable terminal command called 'much' like commands 'python3', 'node', 'go' etc. By running this command you will get:

    $ much

        MUCHSCRIPT 0.1 (BETA)
        Made by muchscript inc. © 2021
        Inspired by Doge and Elon musk
        MUCH WOW. MUCH COOL. MUCH CRYPTO.

        [MUCHSCRIPT]:

This is the interactive mode of muchscript like the python shell. Here you can perform basic one-line operations.

If you want to use the scripting mode, make a new file with a .much extension and paste the sample code above in the file. To run the file just type out:

    $ much [filename].much

        Hello World!
        27.4001
        DOGE HAPPY!!!!!!!!
        3
        Name: Jose
        Name: Maria
        Name: John
        Name: Mary

## Made with love and Python by Sblip.

Feel free to contribute. Needs much help this project does.

© MuchScript 2021 MIT License
