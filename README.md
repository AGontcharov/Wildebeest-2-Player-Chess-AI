# Wildebeest 2 Player Chess AI
> A chess variant alpha-beta pruning AI.

[Wildebeest chess](https://en.wikipedia.org/wiki/Wildebeest_Chess) is a chess variant orginaly created by R. Wayne Schmittberger where the board is 11x10 sqaures. The board consists of the standard chess pieces along with a couple new pieces whose moveset, after effects and rules can be found in the table below. In addition, there are a few special squares on the board which are detailed further down below in another table.

![](header.png)

| Chess Piece                | Moveset  | After Effects  |
| -------------------------- | -------  | ---------------|
| (P/p) pawn                 | Moves and capture likes a regular chess pawn except the en passant capture move is not allowed. | If any pawn occupies the row 5 (the middle of the board), the opposing player's golf cart becomes fully charged. |
| (S/s) Serpent              | The serpents moves likes a king however it cannot capture an opposing peice. ||
| (O/o) Old Woman            | The old woman moves and captures like a king. ||
| (E/e) Grand Empress        | The grand Empress moves and captures like a knight, queen and serpent. ||
| (J/j) Prince Joey | Prince Joey moves and captures like a king. | If at any point in time, the total number of pieces (including Prince Joey) in Prince Joey’s row is evenly divisible by 5, prince Joey explodes and he, and any adjacent (8-square) pieces (friendly or enemy are removed from the board). If there are two Prince Joey’s in the same row, the determination of whether each Prince Joey explodes should be performed once, prior to the explosion(s) and removal of pieces. |
| (C/c) Catapult             | The catapult moves like a king however it cannot catpure an opposing piece. In addition, it can fling a friendly adjacent piece (8-square) from the piece’s starting position to a location that is in the same direction as the direction from the adjacent piece to the catapult. See more information about the flinged piece in the special section below. | n/ a |
| (G/g) Gorilla              | The gorilla moves like a king however it cannot capture an opposing peice. ||
| (X/x) Golf cart            | The Golf Cart can only move and capture left and right a single square in the bottom and top row. | If the golf cart is charged after a turn, it additionally moves up or down the column capturing all pieces in the column (including friendly pieces and gorilla). If both golf carts are in the same column and are both charged everything in that column is removed. |
| (H/h) Time Machine         | The time machine cannot move or capture. | As long as the time machine is on the board, the golf cart is charged. |
| (Z/z) Beekerper            | The beekeeper moves and captures like a king. | Paralyzes any opoosing adjacent pieces (8 squares) and prevents them from moving by releasing a swarm. A piece can move through the swarmed space or into the swarmed space, but once landed in the swarmed space it will not be able to move. |
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