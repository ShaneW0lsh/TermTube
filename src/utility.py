"""Everything needed for terminal output is here """

class TColours():
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    MAGENDA = "\u001b[35m"

    mapping = {
        "HEADER": HEADER, 
        "OKBLUE": OKBLUE,
        "OKCYAN": OKCYAN,
        "OKGREEN": OKGREEN,
        "MAGENDA": MAGENDA,
        "WARNING": WARNING,
        "FAIL": FAIL,
        "ENDC": ENDC,
        "BOLD": BOLD,
        "UNDERLINE": UNDERLINE
    }


"""put the string, color(member string of the TColours class), 
   and whether you want the enter or no. """

def LOG(string, state, end): 
    if end == False:
        print(f"{TColours.mapping[state]}{string}{TColours.ENDC}", end="")
    elif end == True:
        print(f"{TColours.mapping[state]}{string}{TColours.ENDC}");
