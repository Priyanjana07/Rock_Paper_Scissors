import random
import streamlit as st
name = input("Enter username:");

point_user , point_comp , i = 0 , 0 , 0
choice = ["rock", "paper", "scissor"]


while(i < 5):
 comp_choice = random.choice(choice)
 player_choice = input("What do you choose? ").lower()
 if player_choice not in choice:
        print("Invalid choice. Please enter rock, paper, or scissor.")
        continue
 if(player_choice == comp_choice):
    print("It's a tie!");
 elif  (player_choice == 'rock' and comp_choice == 'scissor'):
    point_user += 1;
    print (f"rock smashes scissor! point {point_user} to {name}");
 elif (player_choice == 'paper' and comp_choice == 'rock'):
    point_user += 1;
    print(f"paper engulfs rock! point {point_user} to {name}");
 elif(player_choice == 'scissor' and comp_choice == 'paper'):
    point_user += 1;
    print(f"scissor wins! point {point_user} to {name}");
 else:
    point_comp+=1;
    print(f"I win! point {point_comp} to HP Victus!");
 i+=1
print("Thank you for playing!");
if(point_user > point_comp):
    print("You win!");
    print(f"{name}'s points: {point_user}!")
    print(f"My points: {point_comp}!")

elif(point_user == point_comp):
    print("TIE!!");
    print(f"{name}'s points and my points: {point_user}!")
 import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors", page_icon="✊🖐✌", layout="centered")
st.title("🎮 Rock Paper Scissors")

st.write("Choose your move:")

user_choice = st.radio(
    "Your Move",
    options=["Rock", "Paper", "Scissors"],
    horizontal=True
)

if st.button("Play"):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    st.write(f"🧑 You chose: **{user_choice}**")
    st.write(f"💻 Computer chose: **{computer_choice}**")

    if user_choice == computer_choice:
        st.success("It's a draw!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        st.balloons()
        st.success("You win! 🎉")
    else:
        st.error("You lose! 😢")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")



else:
    print("I win!");
    print(f"{name}'s points: {point_user}!")
    print(f"My points: {point_comp}!")
