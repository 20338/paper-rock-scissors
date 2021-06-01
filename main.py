yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

print("do you know how to play rock paper scissors")

def check_rounds ():
  while True :
    response = input ("how many rounds:")

  round_error = "please type either <enter> " \
   "or an integer that is more than 0 "
  if response != "":
   try :
     response = int (response)

     if reponse < 2 :
       print (round_error)
       continue

    except ValueError :
     print (round_error)
     continue
  return response
  
