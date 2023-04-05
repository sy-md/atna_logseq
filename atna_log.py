import os, time
block = "\n- "
page_ref = "[[{}]]"
#####################################################

# bases on the wayscript local files structure
journal = "journals"
t = os.listdir(journal)
my_file = os.path.join(journal,t[-1])

print(my_file)

with open( my_file ,"a") as thought:
    #x = ("{} first test frothon script".format(block))
    pager = page_ref.format("bkdf")
    x = ("{} this is the first page_ref {}".format(block,pager))
    thought.write(x)
    page_file_name = pager[2:-2]
    #page refs are not made intill typing in to

    """
    script will ask if adding a page ref and store it

    or

    or just use __blah__ then page_ref at the end of the     
    """

time.sleep(3)
#########################################################
# bases on the wayscript local files structure
page = "pages"
#t = os.listdir(page)
my_file_page = os.path.join(page,page_file_name+".md")


print(my_file_page)

with open( my_file_page ,"a") as thought:
    x = ("\b{} first test frothon script".format(block))
    thought.write(x)