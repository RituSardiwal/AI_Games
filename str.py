import streamlit as st
import subprocess


def start_tic_tac_toe():
    """Launch the Tkinter-based Tic-Tac-Toe game."""
    # This assumes your Tic-Tac-Toe script is named `tic_tac_toe.py`.
    # Change the path as per your script location.
    subprocess.Popen(['python3', '/Users/ritu/Aigames/game/tictactoe.py'])

def start_rock():
    """Launch the Tkinter-based Rock-paper game."""
    subprocess.Popen(['python3', '/Users/ritu/Aigames/game/rock.py'])    

st.balloons()
# Streamlit Dashboard
st.title("Alpha Game Dashboard")

st.sidebar.title("Login")
st.sidebar.title("signup")
# Add game images and buttons

st.image("tictac.png", caption="Tic-Tac-Toe", use_column_width=False, width=300)
if st.button("Play Tic-Tac-Toe"):
    start_tic_tac_toe()
st.image("rock.jpg", caption="Rock-Paper-Scissor", use_column_width=False, width=300)
if st.button("Play Rock-Paper-Scissor"):
    start_rock()


st.write("More Games Coming soon.")
