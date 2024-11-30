import re
import sys

def main(args):
    EXIT_CODE = 0
    try:
        print("Regex tester")
        if len(args) != 3 and len(args) != 4:
            print(f"Usage: {args[0]} <Source file> <Regex expression> <Optional: MULTILINE>")
            print("Regex between quotes as includes parentesis")
        else:
            file_name = args[1]
            regex = args[2]
            multiline = False
            if len(args) == 4 and args[3] == "MULTILINE":
                print("ta")
                multiline = True
            input_text = ""
            with open(file_name, 'r') as input_file:
                line = input_file.readline()
                while line:
                    if multiline == True: 
                        input_text = "".join([input_text, line])
                    else:
                        input_text = "".join([input_text, line.strip()])
                    line = input_file.readline()
            print(f"Will apply regex:\n\n{regex},\n\nto text:\n\n{input_text}\n")
            regex_compiled = re.compile(regex)
            matches = regex_compiled.findall(input_text)
            for match_index, match in enumerate(matches):
                print(f"Match {match_index}, value: {match}")   
            print("That's all...")
    except Exception as e:
        if hasattr(e, 'message'):
            msg = e.message
        else:
            msg = e
        print(f"Unexpected exception: {msg}")
        EXIT_CODE = 1
    return EXIT_CODE

if __name__ == '__main__':
  sys.exit(main(sys.argv))
