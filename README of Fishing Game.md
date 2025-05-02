# Fishing Game

The Fishing Game is a PsychoPy-based experiment where participants make choices between three islands to "catch fish," earning points based on probabilistic rewards. The game features four distinct environments with varying stochasticity and volatility, and it tracks participant performance, including response times and decision strategies.

## Prerequisites

- **PsychoPy**: Install PsychoPy to run the experiment.
- **Python**: Ensure Python is installed, as PsychoPy depends on it.
- **Dependencies**: The script uses the following Python libraries, which are included with PsychoPy:
  - `psychopy`
  - `pandas`
  - `random`
  - `os`
  - `time`
- **Resources**: Ensure the `resources` folder contains:
  - `fishing_trials.csv` (trial data)
  - Images: `island.png`, `anchor.png`, `happy.png`, `sad.png`
  - Sounds: `happy_sound2.wav`, `sad_sound2.wav`, `block_complete.wav`, `experiment_end.wav`

## Installation

1. Download or clone the repository to your local machine.
2. Extract the zip file containing `fishing-game.py` and the `resources` folder.
3. Ensure the `resources` folder is in the same directory as `fishing-game.py`.

## How to Run

To run the Fishing Game, follow these steps:

1. **Extract the Zip**: Unzip the file containing `fishing-game.py` and the `resources` folder.
2. **Open PsychoPy**: Launch the PsychoPy application.
3. **Access PsychoPy Coder**: In PsychoPy, switch to the "Coder" view.
4. **Open the File**:
   - Go to `File` > `Open`.
   - Navigate to the location of `fishing-game.py` and select it.
5. **Run the Experiment**: Click the "Run" button to start the game.

## Game Overview

- **Objective**: Participants select one of three islands to "catch fish." Each island has a probability of yielding a reward (+1 point) or a penalty (-1 point).
- **Environments**: The game consists of four blocks (50 trials each), each with a different environment (Low-Slow, Low-Fast, High-Slow, High-Fast), randomized in order where Low-Slow is interpreted as Low Stochasticity - Slow Volatility. These are based on the `fishing_trials.csv` data file.
- **Input**: Use the mouse to click on an island to make a choice.
- **Feedback**: Visual (happy/sad face) and auditory (sound effects) feedback is provided after each choice.
- **Output**: Results are saved as a CSV file in the `data` folder, named `[Participant_ID]_fishing_results.csv`.

## Output

- **Data Directory**: A `data` folder is created automatically if it doesn't exist.
- **Results File**: For each participant, a CSV file is generated containing:
  - Participant ID
  - Trial number
  - Environment type
  - Chosen island
  - Probability of reward
  - Random value (for reward determination)
  - Reward outcome
  - Cumulative score
  - Response time
  - Behavioral metrics (Win-Stay, Lose-Shift, Exploration, Exploitation)

## Notes

- Ensure the `resources` folder and `fishing_trials.csv` are correctly placed to avoid file-not-found errors.
- The game runs in full-screen mode; press `Escape` during a trial to exit.
- The experiment includes a 30-second pause between blocks, which can be skipped by pressing the spacebar.