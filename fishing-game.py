from psychopy import visual, core, event, gui, sound
from psychopy.visual import TextBox2
import pandas as pd
import random
import os
import time

# Get participant name via dialog box
info = {"Participant ID": ""}
dlg = gui.DlgFromDict(dictionary=info, title="Participant Information")
if not dlg.OK:  # User pressed Cancel
    core.quit()
participant_id = info["Participant ID"].strip()

# Create a results directory if it doesn't exist
results_dir = "data"
if not os.path.exists(results_dir):
    os.makedirs(results_dir)

# Load the trial data from the CSV file
csv_filename = "resources/fishing_trials.csv"  # Ensure this CSV exists
try:
    trials = pd.read_csv(csv_filename)
except FileNotFoundError:
    print(f"ERROR: CSV file '{csv_filename}' not found. Please create the trial file.")
    core.quit()

# Setup PsychoPy Window
win = visual.Window(fullscr=True, color="white", units="height")

# Load images (replace with actual file paths)
island1_img = visual.ImageStim(win, image="resources/island.png", pos=(0, 0.2), size=(0.3, 0.3))
island2_img = visual.ImageStim(win, image="resources/island.png", pos=(-0.4, -0.2), size=(0.3, 0.3))
island3_img = visual.ImageStim(win, image="resources/island.png", pos=(0.4, -0.2), size=(0.3, 0.3))
anchor_img = visual.ImageStim(win, image="resources/anchor.png", pos=(0, -0.2), size=(0.16, 0.16))

anchor_box = visual.Rect(win, width=0.14, height=0.14, lineColor="black", pos=anchor_img.pos)

# Feedback images
happy_face = visual.ImageStim(win, image="resources/happy.png", size=(0.1, 0.1))
sad_face = visual.ImageStim(win, image="resources/sad.png", size=(0.1, 0.1))

# Sound effects
happy_sound = sound.Sound("resources/happy_sound2.wav")  # Positive feedback sound
sad_sound = sound.Sound("resources/sad_sound2.wav")  # Negative feedback sound
block_complete_sound = sound.Sound("resources/block_complete.wav")  # Block end sound
experiment_end_sound = sound.Sound("resources/experiment_end.wav")  # Experiment end sound

# Enhanced Title Page
title = visual.TextStim(win, 
                        text="Fishing Game",
                        color="darkblue", 
                        height=0.1, 
                        pos=(0, 0.35),  # Moved up for layout
                        font='Arial',
                        bold=True)

instructions = visual.TextStim(win, 
                               text="Welcome to the Fishing Game!\n\n"
                                    "Your goal is to catch fish by selecting one of three islands.\n"
                                    "Each island may have different rewards.\n"
                                    "- Best Choice: +1 point \n"
                                    "- Other Choices: -1 point \n\n"
                                    "Learn from your choices: islands may change over time.\n",
                               color="black", 
                               height=0.04,  # Smaller font for readability
                               pos=(0, -0.05),  # Centered below title
                               wrapWidth=1.5,  # Wrap text for neatness
                               alignText='center')
                               
spacebar_text = visual.TextStim(win, 
                                text="Press Spacebar to start",
                                color="red",  # Change to desired color (e.g., "blue", "red", "#FF0000")
                                height=0.04, 
                                pos=(0, -0.25),  # Below instructions
                                wrapWidth=1.5, 
                                alignText='center')
                                
transition_text = visual.TextStim(win, 
                                  text="Environment Changed!\n\nPress Spacebar to continue immediately\nor wait 30 seconds.", 
                                  color="black", height=0.06)

# Timer text to display countdown
timer_text = visual.TextStim(win, 
                             text="30", 
                             color="black", 
                             height=0.05, 
                             pos=(0, 0.05))
                             
ending_text = visual.TextStim(win, 
                              text="Game Over!\nThank you for playing.\nPress Spacebar to exit.", 
                              color="black", 
                              height=0.06,
                              pos=(0, 0))

# Function for smooth anchor movement
def move_anchor(target_pos, trial_nums, probabilities, steps=45, duration=0.4):
    start_pos = anchor_img.pos
    for i in range(steps + 1):
        progress = i / steps
        anchor_img.pos = (
            start_pos[0] + (target_pos[0] - start_pos[0]) * progress,
            start_pos[1] + (target_pos[1] - start_pos[1]) * progress
        )
        draw_scene(trial_nums, probabilities)
        win.flip()
        core.wait(duration / steps)

# Function to draw everything
def draw_scene(trial_num, probabilities):
    island1_img.draw()
    island2_img.draw()
    island3_img.draw()
    anchor_box.draw()
    anchor_img.draw()
    
    trial_text = visual.TextStim(win, text=f"Trial: {trial_num}/200", pos=(-0.8, 0.4), color="black", height=0.04)
    prob_text1 = visual.TextStim(win, text=f"{probabilities[0]}%", pos=(0, 0.08), color="black", height=0.05)
    prob_text2 = visual.TextStim(win, text=f"{probabilities[1]}%", pos=(-0.4, -0.32), color="black", height=0.05)
    prob_text3 = visual.TextStim(win, text=f"{probabilities[2]}%", pos=(0.4, -0.32), color="black", height=0.05)
    
#    trial_text.draw()
#    prob_text1.draw()
#    prob_text2.draw()
#    prob_text3.draw()

# Draw title page
title.draw()
instructions.draw()
spacebar_text.draw()
win.flip()

myMouse = event.Mouse()

# Wait for Spacebar to start
while 'space' not in event.getKeys():
    pass  # Wait until spacebar is pressed

event.clearEvents(eventType='mouse')
myMouse = event.Mouse(win=win)
myMouse.clickReset()

# Initialize game variables
score = 0
results = []

# Mouse Input
mouse = event.Mouse(win=win)

previous_choice = None
previous_reward = None

# Define the 4 environments and their trial ranges 
# Low-Slow: interpret as low stochasticity and slow volatility. Similarly others. 
environments = [
    {"type": "Low-Slow", "start": 0, "end": 50},
    {"type": "Low-Fast", "start": 50, "end": 100},
    {"type": "High-Slow", "start": 100, "end": 150},
    {"type": "High-Fast", "start": 150, "end": 200}
]

# Randomize the order of environments
random.shuffle(environments)

# Split trials into 4 blocks (50 trials each)
num_trials = len(trials)
num_blocks = 4
block_size = num_trials // num_blocks

for block, env in enumerate(environments):
    if block > 0:
        core.wait(0.5)
        block_complete_sound.play()
        core.wait(0.5)
        
        transition_text.draw()
        win.flip()
        
        timer = core.Clock()
        timer.reset()
        
        while timer.getTime() < 30:
            remaining_time = max(0, 30 - int(timer.getTime()))
            timer_text.setText(str(remaining_time))
            transition_text.draw()
            timer_text.draw()
            win.flip()
            
            if 'space' in event.getKeys():
                break
            core.wait(0.05)
        event.clearEvents(eventType='mouse')
        myMouse.clickReset()

    for i in range(block_size):
        trial_index = env["start"] + i
        trial = trials.iloc[trial_index]

        probabilities = [trial['Island 1 Prob'], trial['Island 2 Prob'], trial['Island 3 Prob']]
        island_positions = [island1_img.pos, island2_img.pos, island3_img.pos]

        score_text = visual.TextStim(win, text=f"Score: {score}", color="black", pos=(0, 0.4), height=0.05)
        
        if i == 0:
            draw_scene(trial_index + 1, probabilities)
            win.flip()
        else:
            move_anchor((0, -0.2), trial_index + 1, probabilities)
            draw_scene(trial_index + 1, probabilities)
            win.flip()

        trial_start_time = time.time()
        
        timer_text = visual.TextStim(win, text="RT: 0.00 s", color="red", pos=(0.6, 0.4), height=0.05)
        
        selected_island = None
        while selected_island is None:
            current_time = time.time() - trial_start_time
            timer_text.text = f"RT: {current_time:.2f} s"
            draw_scene(trial_index + 1, probabilities)
#            timer_text.draw()
            win.flip()
            
            if mouse.isPressedIn(island1_img):
                selected_island = 0
            elif mouse.isPressedIn(island2_img):
                selected_island = 1
            elif mouse.isPressedIn(island3_img):
                selected_island = 2
            elif 'escape' in event.getKeys():
                filename = os.path.join(results_dir, f"{participant_id}_fishing_results.csv")
                df_results = pd.DataFrame(results)
                df_results.to_csv(filename, index=False)
                print(f"Results saved to {filename}")
                win.close()
                core.quit()

        response_time = time.time() - trial_start_time
        
        move_anchor(island_positions[selected_island], trial_index + 1, probabilities)

        random_value = random.uniform(0, 1)
        if random_value < probabilities[selected_island] / 100:
            reward = 1
            feedback_img = happy_face
            happy_sound.play()
        else:
            reward = -1
            feedback_img = sad_face
            sad_sound.play()

        score += reward

        feedback_img.pos = (island_positions[selected_island][0], island_positions[selected_island][1] + 0.18)
        draw_scene(trial_index + 1, probabilities)
        feedback_img.draw()
        win.flip()
        core.wait(0.2)

        if i == block_size - 1 and block < num_blocks - 1:
            move_anchor((0, -0.2), trial_index + 1, probabilities)
        
        win_stay = (previous_reward == 1 and previous_choice == selected_island)
        lose_shift = (previous_reward == -1 and previous_choice != selected_island)
        exploration = (previous_choice is not None and previous_choice != selected_island)
        exploitation = (previous_choice is not None and previous_choice == selected_island)
        
        results.append({
            "Participant": participant_id,
            "Trial": trial_index + 1,
            "Environment": block + 1,
            "Environment_Type": env["type"],
            "Chosen_Island": selected_island + 1,
            "Probability": probabilities[selected_island],
            "Random_Value": round(random_value, 2),
            "Reward": reward,
            "Score": score,
            "Response_Time": round(response_time, 2),
            "Win-Stay": int(win_stay),
            "Lose-Shift": int(lose_shift),
            "Exploration": int(exploration),
            "Exploitation": int(exploitation)
        })
        
        previous_choice = selected_island
        previous_reward = reward

# Save results to a CSV file with participant name
filename = os.path.join(results_dir, f"{participant_id}_fishing_results.csv")
df_results = pd.DataFrame(results)
df_results.to_csv(filename, index=False)
print(f"Results saved to {filename}")

core.wait(1.0)

# End message with wait for Spacebar
ending_text.draw()
score_text = visual.TextStim(win, text=f"Your Final Score: {score}", color="blue", pos=(0, 0.4), height=0.05)
score_text.draw()

win.flip()
experiment_end_sound.play()
while 'space' not in event.getKeys():
    pass  # Wait until spacebar is pressed

# Cleanup
win.close()
core.quit()