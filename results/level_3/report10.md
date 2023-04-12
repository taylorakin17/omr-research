# Piece 10 Comparison Results
## ScanScore3
(Desktop Application)

Grade for scanscore: **91.67%**

Number of differences between ground truth and scanscore:       10
( out of 120
)

## PlayScore2

(Mobile-iOS Application)

Grade for playscore: **98.33%**

Number of differences between ground truth and playscore:        2
( out of 120
)

----------------------------------------
## ScanScore Diff Output

```
1d0
< Key Signature: -6
4c3
< Slur: <music21.spanner.Slur <music21.note.Note E-><music21.note.Note D->>
---
> Slur: <music21.spanner.Slur <music21.note.Note G-><music21.note.Note D->>
15c14
< Slur: <music21.spanner.Slur <music21.note.Note E-><music21.note.Note E->>
---
> Slur: <music21.spanner.Slur <music21.note.Note F><music21.note.Note E->>
19c18
< Slur: <music21.spanner.Slur <music21.note.Note E-><music21.note.Note D->>
---
> Slur: <music21.spanner.Slur <music21.note.Note E-><music21.note.Note G->>
48,49d46
< Rest (4.0) 
< Rest (2.0) 
58c55
< B-3 (3.0) 
---
> B-3 (2.0) 
66c63
< D-4 (3.0) 
---
> D-4 (2.0) 
75d71
< E-4 (0.5) 
101d96
< F4 (0.5) 
116c111
< F4 (4.0) 
---
> Rest (4.0) 
```

## PlayScore Diff Output

```
2a3
> 	Articulation: staccatissimo
19c20,21
< Slur: <music21.spanner.Slur <music21.note.Note E-><music21.note.Note D->>
---
> Slur: <music21.spanner.Slur <music21.note.Note D-><music21.note.Note G->>
> Slur: <music21.spanner.Slur <music21.note.Note F><music21.note.Note D->>
```

