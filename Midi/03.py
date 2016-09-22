import sys
sys.path.append("library")

from library.mymidi import Tracks



def tune(m):
    m += [61 ,62 ,64 ,64 ,62 ,61 ,{57,61} ,64 ], \
         [8, 8, 8, 8, 8, 8, 16, 16]
    m += [{59,63} ,66 ,{61,64} ,{63,66} ,61 ,62 ,64 ,64 ], \
         [16, 16, 16, 16, 8, 8, 8, 8]
    m += [62 ,61 ,{57,61} ,64 ,{59,63} ,66 ,{61,64} ,{63,66} ], \
         [8, 8, 16, 16, 16, 16, 16, 16]
    m += [0 ,62 ,64 ,66 ,66 ,64 ,62 ,{60,64} ], \
         [16, 8, 8, 8, 8, 8, 8, 16]
    m += [67 ,{62,66} ,69 ,60 ,{64,67} ,62 ,{66,69} ,62 ], \
         [16, 16, 16, 16, 16, 16, 16, 8]
    m += [64 ,66 ,66 ,64 ,62 ,{60,64} ,67 ,{62,66} ], \
         [8, 8, 8, 8, 8, 16, 16, 16]
    m += [69 ,60 ,{64,67} ,62 ,{66,69} ,0 ,64 ,66 ], \
         [16, 16, 16, 16, 16, 16, 8, 8]
    m += [68 ,68 ,66 ,64 ,{64,68} ,71 ,{65,69} ,72 ], \
         [8, 8, 8, 8, 16, 16, 16, 16]
    m += [64 ,{68,71} ,65 ,{69,72} ,64 ,66 ,68 ,68 ], \
         [16, 16, 16, 16, 8, 8, 8, 8]
    m += [66 ,64 ,{64,68} ,71 ,{65,69} ,72 ,64 ,{68,71} ], \
         [8, 8, 16, 16, 16, 16, 16, 16]
    m += [65 ,{69,72} ,0 ,61 ,62 ,64 ,64 ,62 ], \
         [16, 16, 16, 8, 8, 8, 8, 8]
    m += [61 ,{57,61} ,64 ,{59,63} ,66 ,{61,64} ,{63,66} ,61 ], \
         [8, 16, 16, 16, 16, 16, 16, 8]
    m += [62 ,64 ,64 ,62 ,61 ,{57,61} ,64 ,{59,63} ], \
         [8, 8, 8, 8, 8, 16, 16, 16]
    m += [66 ,{61,64} ,{63,66}, 0], \
         [16, 16, 32, 32]

tracks = Tracks("03", 3)
t1 = tracks.addTrack("Track 1")
t2 = tracks.addTrack("Track 2")
t3 = tracks.addTrack("Track 3")
tracks.setTempo(64 * 40)
t1.setInstrument("Orchestral Harp", channel = 1, pitchShift=-12)
t2.setInstrument("Pad 8 (sweep)", channel = 2)
t3.setInstrument("Acoustic Grand Piano", channel = 3, pitchShift=-12)

for t in tracks.getTracks(): tune(t)

tracks.play()