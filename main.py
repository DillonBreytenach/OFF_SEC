# FIRST LET'S IMPORT SOME TOOLS
# FROM THE LOCAL DIRECTORY 

# THIS IS WHAT I USE FOR FILE_MANAGEMENT
from File_man import File_Man

# WE WILL USE THIS LATER ON..
from conns import connections


# WE'LL BE RUNNING CMDS IN THE TERMINAL SO.
import subprocess

# NOW LET'S MAKE A CLASS SO WE CAN USE OUR OTHER TOOLS

class InterFace():
    # EACH CLASS NEEDS SOME __INITIALIZING__
    def __init__(self, **kw):
        # SUPER LET'S US USE MULTIPLE IMPORTS AND CONTROL SOME OTHER STUFF
        super(InterFace, self).__init__(**kw)
        # LOCAL_IMPORTS
        self.FM = File_Man()
        # self.CONS = connections()


    # NOW LET'S MAKE AN INTERFACE MAIN
        # REMEMBER TO INCLUDE (self).. ^ YOU'LL NEED IT
    def main(self):
        # ALWAYS DECLARE VARIABLES AHEAD OF TIME..
        # ELSE CAUSES PROBLEMS

        current_dir_tree    = ""
        save_return         = ""
        file_name           = ""
        delim_              = "\n"


        # I LIKE USING TRY: EXCEPT: [LET'S THE CODE KEEP RUNNING]:[AND SHOWS ERRORS]
        try:
            # HERE WE WILL USE A WHILE LOOP TO KEEP THE PROGRAM RUNNING..
            while True:
                # THEN LET'S TAKE INPUT
                cmds = input("[CMDS]:\n>>")

                # AND WE SHOULD ALWAYS START BY CHECKING IF WE WANT TO EXIT THE PROGRAM
                if "Q" in cmds.upper():
                    return
                
                # NOW LET'S RUN 'ls -la' TO CHECK THE CURRENT DIRECTORY TREE AS AN eg.
                if "ll" in cmds:
                    # NOW WE RUN THE CMD AND GET THE RETURN
                    current_dir_tree = subprocess.getoutput("ls -la")
                    print(f"[CURRENT_TREE]:[{current_dir_tree}]")
                    # SO SINCE WE HAVE THE RETURN, WE 'MIGHT' WANT TO SAVE IT SOMEWHERE FOR LATER
                    save_return = input("[SAVE_RETURN]:[Y/n]")
                    # WE DENOTE THAT THE 'Y' is the default as to the 'n'
                    if "N" not in save_return.upper():
                        file_name = input("[FILE_NAME]:\n>>")
                        # NOW USING THE TOOLS, LET'S SAVE THE OUTPUT
                        self.FM.write_file(file_name, current_dir_tree, delim_, "w")



        except Exception as e:
            print(f"[ERROR]:[MAIN]:[{str(e)}]")


        

# AND HERE WE START THE CODE
if __name__=="__main__":
    IF = InterFace()
    IF.main()


