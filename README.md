# Wildebeest 2 Player Chess AI
> A chess variant alpha-beta pruning AI.

![](WildebeestOverview.png)

[Wildebeest chess](https://en.wikipedia.org/wiki/Wildebeest_Chess) is a chess variant orginaly created by R. Wayne Schmittberger where the board is 11x10 squares. The board consists of the standard chess pieces along with a couple new pieces whose moveset, after effects and rules can be found in the table below. In addition, there are a few special squares on the board which are detailed further down below in another table.

###Starting State of the Board
![](StartingBoard.png)

<br>
###Pieces Information 
| Chess Piece                | Moveset  | After Effects  |
| -------------------------- | -------  | ---------------|
| (P/p) Pawn                 | The Pawn moves and capture likes a regular chess Pawn except the _en passant_ capture move is not allowed. | If any Pawn occupies the row 5 (the middle of the board), the opposing player's Golf Cart becomes fully charged. Furthermore, all pawns are promoted to Time Machines once they reach the end of the board. |
| (B/b)                      | The Bishop moves and captures like in regular chess. | n/a |
| (N/n)                      | The Knight moves and captures like in regular chess. | n/ a |
| (R/r)                      | The Rook moves and captures like in regular chess. | n/a |
| (S/s) Serpent              | The Serpents moves likes a King however it cannot capture an opposing piece. | The Serpent poisons enemy peices as described in the poison section below. |
| (O/o) Old Woman            | The Old Woman moves and captures like a King. | The Old Woman can be converted into a Grand Empress by the poisoning of an adjacent friendly piece see the description of poison below. |
| (E/e) Grand Empress        | The Grand Empress moves and captures like a Knight, queen and Serpent. | The Grand empress poisons enemy pieces as described in the poison section below. |
| (J/j) Prince Joey | Prince Joey moves and captures like a King. | If at any point in time, the total number of pieces (including Prince Joey) in Prince Joey’s row is evenly divisible by 5, prince Joey explodes and he, and any adjacent (8-square) pieces (friendly or enemy are removed from the board). If there are two Prince Joey’s in the same row, the determination of whether each Prince Joey explodes should be performed once, prior to the explosion(s) and removal of pieces. |
| (C/c) Catapult             | The catapult moves like a King however it cannot catpure an opposing piece. Instead of moving it can fling a friendly adjacent piece (8-square) from the piece’s starting position to a location that is in the same direction as the direction from the adjacent piece to the catapult. See more information about the flunged piece in the section below. | n/ a |
| (G/g) Gorilla              | The Gorilla moves like a King however it cannot capture an opposing peice (unless flung), nor can it **be** captured. It does, however, have the ability to push a piece (as long as that piece is not also a Gorilla). It this case, the Gorilla moves into an adjacent square (8-square) occupied by a friendly or opposing piece and that friendly or opposing piece also moves a single square in the same direction as the Gorilla. If the destination square of the pushed piece is not occupied by another Gorilla, then the occupant of the adjacent square is captured (even if it is a friendly piece). | n/a |
| (X/x) Golf Cart            | The Golf Cart can only move and capture left and right a single square in the bottom and top row. | If the Golf cart is charged after a turn, it additionally moves up or down the column capturing all pieces in the column (including friendly pieces and Gorilla). If both Golf carts are in the same column and are both charged everything in that column is removed. |
| (H/h) Time Machine         | The Time Machine cannot move or capture. | As long as the Time Machine is on the board, the Golf cart is charged. |
| (Z/z) Beekerper            | The Beekeeper moves and captures like a King. | Paralyzes any opoosing adjacent pieces (8 squares) and prevents them from moving by releasing a swarm. A piece can move through the swarmed space or into the swarmed space, but once landed in the swarmed space it will not be able to move. |
| (W/w) King with a Jet Pack | Moves and captures like a Bishop. | n/a |

<br>
###Special Board Squares
|Sqaure Symbol | Effect |
|--------------| -------|
|(#) Jet Pack  | If a King lands on the Jeb Pack it becomes a King with a Jet Pack (W/w) (see above). |
|(*) Transporter Pad | There are 4 transporter pads located on the board which teleport pieces to another transporter. The rules for the transporter pads are: <br><br> a. Row 3, Column 9 moves to Row 3, Column 1, (right to left) <br> b. Row 7, Column 1 moves to Row 3, Column 9, (diagonal right) <br>c. Row 7, Column 9 moves to Row 7, Column 1, (right to left) <br>d. Row 3, Column 1 moves to Row 7, Column 9. (diagonal right) |

<br>
### Poison
The Serpent has the ability to poison any opposing, biological, adjacent piece (8-square). Any time it is adjacent to one or more opposing biological, pieces, the opposing, biological pieces are __all__ removed from the board (friendly pieces are unaffected).
<br>
* __1.__ If the Serpent ever poisons a piece that is also adjacent (8-square) to an opposing Old Woman, then the Serpent is captured (removed from the board) and the Old Woman piece is replaced by the Grand Empress piece. All opposing pieces next to the Serpent’s position are still removed.
<br>
* __2.__ The Serpent can poison an opposing Old Woman (if it is directly adjacent). The Serpent can poison a Gorilla.
<br>
* __3.__ If two Serpents are adjacent to each other they will poison each other. If a friendly Old Woman is adjacent to a Serpent that is poisoned by an enemy Serpent, then the friendly Old Woman is converted into a Grand Empress.
<br>
* __4.__ The Golf Cart and Time Machine, cannot be poisoned (and cannot be used to convert the Old Woman into the Grand Empress).
<br>
* __5.__ A Serpent can poison an adjacent Beekeeper, but cannot move out of its swarm.

<br>
### Flung Pieces

The flung piece can move any distance. It can land on an empty square or on an opposing piece (in which case the opposing piece is
captured). The flung piece cannot capture a King or Gorilla. A Gorilla can be flung onto an enemy piece and thereby capture it. A catapult can fling a friendly piece onto a transporter pad. Time Machines and Golf Cart cannot be flunged. A catapult can fling a paralyzed piece unless the catapult is paralyzed. 

<br>
###Order of After Effects
1. Serpent/Grand Empress poison
2. Grand Empress transformation
3. Pawn on row 5 (middle row of the board)
4. Time Machine charge
5. Transporter Pad
6. Serpent/Grand Empress poison after teleportation
7. Prince Joey explosion

## Installation

OS X & Linux:

```sh
git clone https://github.com/AGontcharov/Wildebeest-2-Player-Chess-AI.git
cd WildebeestChessAI
chmod u+x AlphaBeta.py
```

Windows:

```sh
Not yet available
```
## Running

OX X & Linux:

```sh
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

[https://github.com/AGontcharov/](https://github.com/AGontcharov/)
