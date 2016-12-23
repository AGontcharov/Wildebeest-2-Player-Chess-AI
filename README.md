# Wildebeest 2 Player Chess AI
> A chess variant alpha-beta pruning AI.

[Wildebeest chess](https://en.wikipedia.org/wiki/Wildebeest_Chess) is a chess variant orginaly created by R. Wayne Schmittberger where the board is 11x10 sqaures. The board consists of the standard chess pieces along with a couple new pieces whose moveset, actions and rules can be found in the table below.

![](header.png)

| Chess Piece                | Moveset  | After Effects  |
| -------------------------- | -------  | -------- |
| (S/s) Serpent              | The serpents moves likes a king however it cannot capture an opposing peice. | |
| (O/o) Old Woman            | The old woman moves and captures like a king. ||
| (E/e) Grand Empress        | The grand Empress moves and captures like a knight, queen and serpent. ||
| (J/j) Prince Joey | Prince Joey moves and captures like a king. | If at any point in time, the total number of pieces (including Prince Joey) in
Prince Joey’s row is evenly divisible by 5, prince Joey explodes and he, and any
adjacent (8-square) pieces (friendly or enemy are removed from the board). |
| (C/c) Catapult             | The catapult moves like a king however it cannot catpure an opposing piece. |          |
| (G/g) Gorilla              | The gorilla moves like a king however it cannot capture an opposing peice. |          |
| (X/x) Golf cart            | The Golf Cart can only move and capture left and right a single square in the bottom and top row. | |
| (H/h) Time Machine         | The time machine cannot move or capture. | As long as the time machine is on the board, the golf cart is charged. |
| (Z/z) Beekerper | The beekeeper moves and captures like a king. | Paralyzes any opoosing adjacent pieces (8 squares) and prevents them from moving by releasing a swarm. A piece can move through the swarmed space or into the swarmed space, but once landed in the swarmed space it will not be able to move. |
| (W/w) King with a Jet Pack | Moves and captures like a bishop. | n/a |

## Installation

OS X & Linux:

```sh
git clone https://github.com/AGontcharov/Wildebeest-2-Player-Chess-AI.git
cd WildebeestChessAI
./AlphaBeta.py boards.txt
```

Windows:

```sh
Not yet available
```

## Usage example

## Meta

Alexander Gontcharov – alexander.goncharov@gmail.com

[https://github.com/AGontcharov/github-link](https://github.com/AGontcharov/)