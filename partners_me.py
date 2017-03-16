import partners
import sys

potential_partners = partners.Partners()

def invalid():
    print("Invalid")
    sys.exit();

input_name = input("Please enter your name: ")
print("Hi", input_name + ".")

print("What is your gender?"
      "\n1) male\n2) female\n3) other\n")
input_gender = input("Please enter your answer: ")

print("What is your sexual preference?"
      "\n1) male\n2) female\n3) other\n")
input_preference = input("Please enter your answer: ")

print("What is your height?"
      "\n1) tall\n2) medium\n3) short\n")
input_height = input("Please enter your answer: ")

print("What height do you prefer your partner to be?"
      "\n1) tall\n2) medium\n3) short\n")
input_partner_height = input("Please enter your answer: ")

print("Do you find it easy to introduce yourself to other people?"
      "\n1) Yes"
      "\n2) Most of the time"
      "\n3) Neutral"
      "\n4) Some times"
      "\n5) No\n")
input_question1 = input("Please enter your answer: ")

print("Do you usually initiate conversations?"
      "\n1) Yes"
      "\n2) Most of the time"
      "\n3) Neutral"
      "\n4) Some times"
      "\n5) No\n")
input_question2 = input("Please enter your answer: ")

print("Do you often do something out of sheer curiosity?"
      "\n1) Yes"
      "\n2) Most of the time"
      "\n3) Neutral"
      "\n4) Some times"
      "\n5) No\n")
input_question3 = input("Please enter your answer: ")

print("Do you prefer being out with a large group of friends rather than spending time on your own?"
      "\n1) Yes"
      "\n2) Most of the time"
      "\n3) Neutral"
      "\n4) Some times"
      "\n5) No\n")
input_question4 = input("Please enter your answer: ")


