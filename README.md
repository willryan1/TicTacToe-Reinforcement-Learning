# TicTacToe-Reinforcement-Learning
> TicTacToe bot using reinforcement learning and a TicTacToe bot that uses logic

## Overview

This repository implements a Tic-Tac-Toe bot that you can play against using reinforcement learning. These files can be 
found under reinforcement_learning. Under manually_trained_bot I included a Tic-Tac-Toe bot that I wrote a couple years ago 
that has the worst outcome being a tie. The code is a little disorganized though.

If you want to save a policy from one of the reinforcement learning bots that wont get overridden by the next run of run.py
you can change the name of the bots run.py.

## Usage

For each of these bots you simply run the python file and you will be able to play the bots.

#### Reinforcement Learning Bot:
```
pip install numpy
```
```
python run.py
```

If you would like to change the amount of episodes change run.py look for line 22:
```python
print("Training...")
state.train(CHANGE ME)
p1.save_policy()
p2.save_policy()
```

Also feel free to change the values of the learning rate, decay_gamma, and exp_rate to see how the results change.

#### Manual Bot

```
python manual_learning.py
```
