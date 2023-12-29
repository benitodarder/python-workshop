import re
import sys

def main(args):
  try:
    print("Regex tester")
    if len(args) != 3:
      print(f"Usage: {args[0]} <Source file> <Regex expression>")
      print("Regex between quotes as includes parentesis")
    else:
      file_name = args[1]
      regex = args[2]
      input_text = ""
      with open(file_name, 'r') as input_file:
        line = input_file.readline()
        while line:
          input_text = "".join([input_text, line.strip()])
          line = input_file.readline()
      print(f"Will apply regex: '{regex}', to text: '{input_text}'")
      regex_compiled = re.compile(regex)
      regex_result = regex_compiled.finditer(input_text)
      for match_index, match in enumerate(regex_result):
        for group_index, group in enumerate(match.groups()):
          print(f"Match {match_index}, group: {group_index}, values: {group}")
    print("That's all...")
  except Exception as e:
    if hasattr(e, 'message'):
        msg = e.message
    else:
        msg = e
    print(f"Unexpected exception: {msg}")
  return 0

if __name__ == '__main__':
  sys.exit(main(sys.argv))


