import sys
from lib.chatmark import Button

def main(sentence: str) -> str:
    print(f"\n\nDo nothing to the sentence: \n\n{sentence}\n\n")


if __name__ == "__main__":
    main(sys.argv[1])