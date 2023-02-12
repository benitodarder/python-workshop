ASCII_LF=10
ASCII_CR=13
HEADER_BODY_SEPARATOR="\r\n"
CONTENT_LENGTH="Content-Length: "
import sys

def main(args):
  message = []
  line = ""
  body = ""
  contentLength = 0
  with open(args[1], "r", newline="") as f:
    while len(message) == 0 or message[len(message)-1] != HEADER_BODY_SEPARATOR:
      char = f.read(1)
      line = line + char
      if char == "\r":
        char = f.read(1)
        line = line + char
        if char == "\n":
          message.append(line)
          if line.startswith(CONTENT_LENGTH):
            contentLength = line[len(CONTENT_LENGTH)::].strip()
          line = ""
    for i in range(0, int(contentLength)):
      body = body + f.read(1)
  print("Headers: ");
  for i,line in enumerate(message):
    print(str(i) + " - " + line, end="")
  print(CONTENT_LENGTH + "\n" + str(contentLength))
  print("Body:\n" + body)
  
if __name__ == '__main__':
  sys.exit(main(sys.argv))
