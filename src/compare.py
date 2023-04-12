import music21
import argparse
import subprocess
# parse command line arguments to get the id of the piece to be compared (which
# is the name of the file for each piece being compared)
parser = argparse.ArgumentParser()
parser.add_argument('id', type=int, help='id of the piece to be compared')
# add level argument to specify which level of comparison to do, default is 1
parser.add_argument('-l', '--level', type=int, help='level of comparison to do', default=1)
# add a flag to specify whether to delete the resulting files from condensing the scores to strings
parser.add_argument('-rrf', '--removefiles', action='store_true', help='delete the resulting files from condensing the scores to strings', default=False)
# add a flag to request verbose reports (which will print the diff output with -y)
parser.add_argument('-v', '--verbose', action='store_true', help='print verbose reports', default=False)
# add a flag to indicate that we want to run on multiple files, where the id is the first file to run on and the argument is the last file to run on
parser.add_argument('-m', '--multiple', type=int, help='run on multiple files, where the id is the first file to run on and the argument is the last file to run on')
args = parser.parse_args()

def get_score_compare_string(score):
    return_string = ''
    for el in score.flat.elements:
        # level 1: notes, rests, time signatures
        currentType = str(type(el))
        if currentType == "<class 'music21.note.Note'>":
            return_string += el.nameWithOctave + ' (' + str(el.duration.quarterLength) + ') ' + '\n' 
        # if it's a rest, add a rest to the string with its duration
        if currentType == "<class 'music21.note.Rest'>":
            return_string += 'Rest (' + str(el.duration.quarterLength) + ') ' + '\n'
        # if it's a time signature, add a time signature to the string
        if currentType == "<class 'music21.meter.TimeSignature'>":
            return_string += 'Time Signature: ' + str(el.numerator) + '/' + str(el.denominator) + '\n'
        
        # level 2: key signatures, articulations, dynamics
        if args.level < 2:
            continue
        if currentType == "<class 'music21.key.KeySignature'>":
            return_string += 'Key Signature: ' + str(el.sharps) + '\n'
        # articulations and dynamics
        if currentType == "<class 'music21.note.Note'>":
            return_string += 'Dynamic: ' + el.value + '\n'
            for articulation in el.articulations:
                return_string += '\tArticulation: ' + articulation.name + '\n'
        
        # level 3: lines (spanners)
        # types of spanners in music21: https://web.mit.edu/music21/doc/moduleReference/moduleSpanner.html
        if args.level < 3:
            continue
        if currentType == "<class 'music21.spanner.Slur'>":
            return_string += 'Slur: ' + str(el) + '\n'
        # glissandos
        if currentType == "<class 'music21.spanner.Glissando'>":
            return_string += 'Glissando: ' + str(el) + '\n'
        # ties
        if currentType == "<class 'music21.tie.Tie'>":
            return_string += 'Tie: ' + str(el) + '\n'
        # trills
        if currentType == "<class 'music21.spanner.TrillSpanner'>":
            return_string += 'Trill: ' + str(el) + '\n'

        
    
    return return_string

# if we want to run on multiple files, set the start and end variables accordingly
start = args.id
if args.multiple:
    edge = args.multiple
else:
    edge = start

for piece_num in range(start, edge+1):
    # Load scores ground truth, scanscore output, and playscore output for comparison
    ground_truth = music21.converter.parse('../groundtruth/'+ str(piece_num) + '.mxl')
    scanscore = music21.converter.parse('../scanscore_output/'+ str(piece_num) + '.xml')
    playscore = music21.converter.parse('../playscore_output/'+ str(piece_num) + '.xml')

    # Prepare the ground truth string
    ground_truth_string = get_score_compare_string(ground_truth)
    scanscore_string = get_score_compare_string(scanscore)
    playscore_string = get_score_compare_string(playscore)

    # save each string to a file in the same directory with its variable name as the file name
    with open('ground_truth_string.txt', 'w') as f:
        f.write(ground_truth_string)
    with open('scanscore_string.txt', 'w') as f:
        f.write(scanscore_string)
    with open('playscore_string.txt', 'w') as f:
        f.write(playscore_string)

    # count the number of lines in the ground truth string
    cmd = "wc -l ground_truth_string.txt | awk '{print $1}'"
    num_lines = subprocess.check_output(cmd, shell=True, text=True)

    # Run the diff command and capture its output
    if args.verbose:
        cmd = "diff -y ground_truth_string.txt scanscore_string.txt || true"
    else:
        cmd = "diff ground_truth_string.txt scanscore_string.txt || true"
    diff_scanscore = subprocess.check_output(cmd, shell=True, text=True)
    cmd = "diff -U 0 ground_truth_string.txt scanscore_string.txt | grep ^@ | wc -l"
    num_diff_scanscore = subprocess.check_output(cmd, shell=True, text=True)

    # Run the diff command and capture its output
    if args.verbose:
        cmd = "diff -y ground_truth_string.txt playscore_string.txt || true"
    else:
        cmd = "diff ground_truth_string.txt playscore_string.txt || true"
    diff_playscore = subprocess.check_output(cmd, shell=True, text=True)
    cmd = "diff -U 0 ground_truth_string.txt playscore_string.txt | grep ^@ | wc -l"
    num_diff_playscore = subprocess.check_output(cmd, shell=True, text=True)

    div = "----------------------------------------"
    dnl = "\n\n"

    # function that calculate the percentage of differences between the ground truth and scanscore
    def get_percentage(num_diff, num_lines):
        percentage = (int(num_lines) - int(num_diff)) / int(num_lines) * 100
        # round to 2 decimal places
        return str(round(percentage, 2)) + "%"

    results_folder = "../results/level_" + str(args.level) + "/report"
    # Write out results to report[piecenum].txt
    with open(results_folder + str(piece_num) + '.md', 'w') as f:
        # Write Header
        f.write("# Piece " + str(piece_num) + " Comparison Results\n")

        # Scan Score
        f.write("## ScanScore3\n")
        f.write("(Desktop Application)" + dnl)
        f.write("Grade for scanscore: **" + get_percentage(num_diff_scanscore, num_lines) + "**" + dnl)
        f.write("Number of differences between ground truth and scanscore: " + num_diff_scanscore)
        f.write("( out of " + num_lines + ")" + dnl)

        # Play Score
        f.write("## PlayScore2" + dnl)
        f.write("(Mobile-iOS Application)"+ dnl)
        f.write("Grade for playscore: **" + get_percentage(num_diff_playscore, num_lines) + "**" + dnl)
        f.write("Number of differences between ground truth and playscore: " + num_diff_playscore)
        f.write("( out of " + num_lines + ")" + dnl)
        f.write(div + "\n")
        if int(num_diff_scanscore) != 0:
            f.write("## ScanScore Diff Output" + dnl)
            f.write("```" + '\n')
            f.write(diff_scanscore)
            f.write("```" + dnl)
        if int(num_diff_playscore) != 0:
            f.write("## PlayScore Diff Output" + dnl)
            f.write("```" + '\n')
            f.write(diff_playscore)
            f.write("```" + dnl)

    # delete the files
    subprocess.call("rm ground_truth_string.txt", shell=True)
    subprocess.call("rm scanscore_string.txt", shell=True)
    subprocess.call("rm playscore_string.txt", shell=True)


