#Assigning questions to variables
question1 = "What does CCNA stand for?"
question2 = "Which network device is used to forward network traffic between networks"
question3 = "How much bytes does a MAC address consist of?"
question4 = "TCP and ___ are protocols used in layer 4"
question5 = "What is the L3PDU called?"


# Quiz fuction
def quiz():
    score = 0
    print(f"\n{question1}")
    answer1 = input("\nA. Certified Cisco Network Associate"
                    "\nB. Cisco Certified Network Admin"
                    "\nC. Cisco Certified Network Associate"
                    "\nD. Cisco Computer Network Admin"
                    "\nEnter your answer: ").lower()
    if answer1 == "c":
        score += 1
                  
    print(f"\n{question2}")
    answer2 = input("\nA. Router"
                    "\nB. Switch"
                    "\nC. Client"
                    "\nD. UTP Cable"
                    "\nEnter your answer: ").lower()
    if answer2 == "a":
        score += 1        

    print(f"\n{question3}")
    answer3 = input("\nA. 8"
                    "\nB. 48"
                    "\nC. 12"
                    "\nD. 6"
                    "\nEnter your answer: ").lower()
    if answer3 == "d":
        score += 1

    print(f"\n{question4}")
    answer4 = input("\nA. IP"
                    "\nB. ICMP"
                    "\nC. HTTP"
                    "\nD. UDP"
                    "\nEnter your answer: ").lower()
    if answer4 == "d":
        score += 1
        
    print(f"\n{question5}")
    answer5 = input("\nA. Packet"
                    "\nB. Segment"
                    "\nC. Datagram"
                    "\nD. Frame"
                    "\nEnter your answer: ").lower()
    if answer5 == "a":
        score += 1

# Ending and Results
    input("You have completed the quiz. Press any button to see your result.")
    print(f"\nYou got {score}/5.\nThat's {(score /5) * 100} %\n")
    
quiz()