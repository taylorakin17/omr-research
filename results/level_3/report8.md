# Piece 8 Comparison Results
## ScanScore3
(Desktop Application)

Grade for scanscore: **97.62%**

Number of differences between ground truth and scanscore:       14
( out of 589
)

## PlayScore2

(Mobile-iOS Application)

Grade for playscore: **99.32%**

Number of differences between ground truth and playscore:        4
( out of 589
)

----------------------------------------
## ScanScore Diff Output

```
1d0
< Key Signature: -2
3a3,4
> Slur: <music21.spanner.Slur <music21.note.Note D><music21.note.Note F>>
> Slur: <music21.spanner.Slur <music21.note.Note D><music21.note.Note G>>
64d64
< D4 (0.5) 
149a150,153
> E-4 (0.5) 
> E-4 (0.5) 
> E-4 (0.5) 
> E-4 (0.5) 
167,168d170
< E-4 (1.0) 
< 	Articulation: staccato
177,179c179,182
< E-4 (1/3) 
< G4 (1/3) 
< B-4 (1/3) 
---
> G4 (0.5) 
> B-4 (0.5) 
> G4 (0.5) 
> B-4 (0.5) 
191,193c194,197
< E-4 (1/3) 
< G4 (1/3) 
< B-4 (1/3) 
---
> G4 (0.5) 
> B-4 (0.5) 
> G4 (0.5) 
> B-4 (0.5) 
205,207c209,212
< E-4 (1/3) 
< G4 (1/3) 
< B-4 (1/3) 
---
> G4 (0.5) 
> B-4 (0.5) 
> G4 (0.5) 
> B-4 (0.5) 
216d220
< 	Articulation: tenuto
218d221
< 	Articulation: tenuto
222d224
< 	Articulation: tenuto
310,314d311
< G5 (0.5) 
< G5 (0.5) 
< Rest (0.5) 
< F5 (2.0) 
< Rest (0.5) 
403,404d399
< E-4 (1.0) 
< 	Articulation: staccato
426a422,424
> E-5 (0.5) 
> D5 (0.5) 
> E-5 (0.5) 
```

## PlayScore Diff Output

```
313d312
< F5 (2.0) 
314a314
> F5 (2.0) 
587a588
> Rest (0.5) 
589d589
< B-3 (0.5) 
```

