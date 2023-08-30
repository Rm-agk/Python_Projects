import random
import time
class Magic_8_ball:
    def __init__(self):
        self.responses =  ["Yes!", "My sources say yes!", "Reply hazy, ask again",
                 "I don't think so!", "NO!", "Ask again later", "Impossible", "Hmm not sure",]
        self.response = ""
        self.shake()


    def shake(self):
        val = int(random.random() * len(self.responses))
        self.response = self.responses[val]

    def get_reply(self):
        return self.response


def main():
    name = input("Please enter your name: ")
    time.sleep(2)
    print("Welcome to Magic 8 Ball",name, "where you ask a question to see where your future lies...")
    my_8_ball = Magic_8_ball()

    while True:
        time.sleep(2)
        first_question = input('Enter a YES/NO question: ')

        my_8_ball.shake()
        print(my_8_ball.get_reply())



        attempt2 = input("Would you like to go again? ")
        if attempt2[0].lower() == "n":
            break
    print("Goodbye !", name)

if __name__ == "__main__":
    main()