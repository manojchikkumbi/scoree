import sys

# check if at least one score is passed
if len(sys.argv) < 2:
    print("Usage : python score.py <score1> <score2> ... <scoreN>")
else:
    # convert arguments to float values
    scores = [float(x) for x in sys.argv[1:]]

    total = sum(scores)
    average = total / len(scores)
    maximum = max(scores)
    minimum = min(scores)

    print("Scores :", scores)
    print("Sum =", total)
    print("Average =", average)
    print("Maximum =", maximum)
    print("Minimum =", minimum)

    if average >= 50:
        print("Result : Pass")
    else:
        print("Result : Fail")
