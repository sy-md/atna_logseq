import os
import time
import shutil
import click
import logging as lg

block = "\n- "
journal = "journals"
page = "pages"

# create a logger
lg.basicConfig(filename="atna_log.log", level=lg.INFO)

def log_seq_app():
    # log that the app was started
    lg.info("app started")
    def my_journal_refs():
        find_journal = os.listdir(journal)
        last_journal = find_journal[-1]
        # log that the journal was found and the name of the journal
        lg.info("journal found: " + last_journal)
        path_to_journal = os.path.join(journal, last_journal)
        # log that the journal was found
        lg.info("journal found")
        with open(path_to_journal, "a") as f: # make sure to change this to "w" when you are done testing
            # log that the user is adding a journal entry to name of journal
            lg.info("adding journal entry to: " + last_journal)
            input_string = click.prompt("Add a journal entry")
            f.write(block + input_string)
            time.sleep(3)
            if input_string.find("[[") == -1:
                question = click.prompt("Did you forget to add a page entry? y/n")
                if question == "y":
                    add_page = click.prompt("Add a page entry")
                    my_page_refs(input_string, forgot_brackets=add_page)
                elif question == "n":
                    quit()
                else:
                    print("Invalid input")

            return my_page_refs(input_string)

        
    def my_page_refs(input_string, forgot_brackets=""):
        if forgot_brackets != "": # if the user forgot to add brackets
            input_string = forgot_brackets

        find_page = input_string.find("[[") + 2 
        find_page2 = input_string.find("]]") 
        word = input_string[find_page:find_page2] 
        my_file = os.path.join(page, word + ".md")
        # log that the page was created
        lg.info("page created")
        with open(my_file, "w") as f:
            input_string = click.prompt("Add a page entry: ")
            f.write(block + input_string)
            lg.info("page entry added")
            time.sleep(3)

    user = click.prompt("press 1 to add a journal entry or 2 to add a page entry")
    if user == "1":
        click.echo("use [[ ]] to add a page entry {for example [[page name]]}")
        my_journal_refs()
    elif user == "2":
        my_page_refs()
    else:
        print("Invalid input")

if __name__ == "__main__":
    log_seq_app()   