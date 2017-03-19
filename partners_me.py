import partners
import sys

def user_inputs():
    input_name = input("Please enter your name: ")
    print("Hi", input_name + ".")
    input_gender = input("What is your gender?"
                         "\n1) male\n2) female\n3) other\n"
                         "Please enter your answer: ")
    input_gender_preference = input("What is your gender preference?"
                         "\n1) male\n2) female\n3) other\n"
                         "Please enter your answer: ")
    input_height = input("What is your height?"
                         "\n1) tall\n2) medium\n3) short\n"
                         "Please enter your answer: ")
    input_height_preference = input("What is your height preference?"
                         "\n1) tall\n2) medium\n3) short\n"
                         "Please enter your answer: ")

    input_question1 = input("Do you find it easy to introduce yourself to other people?"
                            "\n1) Yes"
                            "\n2) Most of the time"
                            "\n3) Neutral"
                            "\n4) Some times"
                            "\n5) No\n"
                            "Please enter your answer: ")

    input_question2 = input("Do you usually initiate conversations?"
                            "\n1) Yes"
                            "\n2) Most of the time"
                            "\n3) Neutral"
                            "\n4) Some times"
                            "\n5) No\n"
                            "Please enter your answer: ")

    input_question3 = input("Do you often do something out of sheer curiosity?"
                            "\n1) Yes"
                            "\n2) Most of the time"
                            "\n3) Neutral"
                            "\n4) Some times"
                            "\n5) No\n"
                            "Please enter your answer: ")

    input_question4 = input("Do you prefer being out with a large group of friends rather than spending time on your own?"
                            "\n1) Yes"
                            "\n2) Most of the time"
                            "\n3) Neutral"
                            "\n4) Some times"
                            "\n5) No\n"
                            "Please enter your answer: ")

    personality_value = (int(input_question1) + int(input_question2) + int(input_question3) + int(input_question4)) * 2
    total = [input_gender, input_gender_preference, input_height, input_height_preference, personality_value]
    #print(total)
    return total

user_inputs()
