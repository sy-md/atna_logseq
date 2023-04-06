import os
import time
import shutil
import logging as lg

block = "\n- "
journal = "journals"
page = "pages"

# the only thing left is to make a fuzzy finder for the files and know file i want to add to

def journal_entry():
    t = os.listdir(journal)
    my_file = os.path.join(journal,t[-1])
    print(my_file)
    with open( my_file ,"a") as thought:
        print("write your thought:")
        #input_string =("{}first test from the script with athena help [[chatGPT]]".format(block))
        input_string = input("{}".format(block))
        thought.write(input_string)
    time.sleep(3)
    return my_journal_refs(input_string)

def my_journal_refs(input_string): # the jounal string
    start_index = input_string.index("[[") + 2
    end_index = input_string.index("]]")
    word = input_string[start_index:end_index]
    my_file = os.path.join(page,word + ".md")
    with open(my_file ,"w") as file:
        print("write a note:")
        x = input("{}".format(block))
        file.write(x)
    print(f"{word}.md created successfully!")

journal_entry()