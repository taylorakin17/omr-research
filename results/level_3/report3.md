# Piece 3 Comparison Results
## ScanScore3
(Desktop Application)

Grade for scanscore: **98.82%**

Number of differences between ground truth and scanscore:        6
( out of 510
)

## PlayScore2

(Mobile-iOS Application)

Grade for playscore: **99.02%**

Number of differences between ground truth and playscore:        5
( out of 510
)

----------------------------------------
## ScanScore Diff Output

```
1d0
< Key Signature: -1
4d2
< Slur: <music21.spanner.Slur <music21.note.Note C><music21.note.Note C>>
6,7d3
< Slur: <music21.spanner.Slur <music21.note.Note F><music21.note.Note F>>
< Slur: <music21.spanner.Slur <music21.note.Note F><music21.note.Note F>>
9,10d4
< Slur: <music21.spanner.Slur <music21.note.Note F><music21.note.Note C>>
< Slur: <music21.spanner.Slur <music21.note.Note C><music21.note.Note C>>
12,13d5
< Slur: <music21.spanner.Slur <music21.note.Note F><music21.note.Note F>>
< Slur: <music21.spanner.Slur <music21.note.Note F><music21.note.Note F>>
54,55c46
< F4 (2.0) 
< F4 (0.25) 
---
> F4 (0.125) 
```

## PlayScore Diff Output

```
3,4d2
< Slur: <music21.spanner.Slur <music21.note.Note F><music21.note.Note C>>
< Slur: <music21.spanner.Slur <music21.note.Note C><music21.note.Note C>>
6,7d3
< Slur: <music21.spanner.Slur <music21.note.Note F><music21.note.Note F>>
< Slur: <music21.spanner.Slur <music21.note.Note F><music21.note.Note F>>
10d5
< Slur: <music21.spanner.Slur <music21.note.Note C><music21.note.Note C>>
13d7
< Slur: <music21.spanner.Slur <music21.note.Note F><music21.note.Note F>>
24a19
> 	Articulation: staccato
```

