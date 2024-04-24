BOT_NAME = "Kili"


def greet():
    print(f"Hello! I'm {BOT_NAME}, a question answering bot who knows answers to"
          " all questions from the 'Jeopardy!' game.")


def main():
    greet()
    input("Ask me something!\n")
    print("Let's play!")


if __name__ == "__main__":
    main()