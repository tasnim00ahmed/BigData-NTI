#!/usr/bin/python

import sys
import math

current_id = None

sum_scores = 0
sum_squares = 0
count = 0

for line in sys.stdin:

    line = line.strip()

    course_id, score, square, cnt = line.split("\t")

    score = float(score)
    square = float(square)
    cnt = int(cnt)

    if current_id == course_id:

        sum_scores += score
        sum_squares += square
        count += cnt

    else:

        if current_id is not None:

            avg = sum_scores / count
            variance = (sum_squares / count) - (avg * avg)
            std_dev = math.sqrt(variance)

            print "%s\tTotal=%s\tAverage=%.2f\tStdDev=%.2f" % (
                current_id,
                sum_scores,
                avg,
                std_dev
            )

        current_id = course_id
        sum_scores = score
        sum_squares = square
        count = cnt

if current_id is not None:

    avg = sum_scores / count
    variance = (sum_squares / count) - (avg * avg)
    std_dev = math.sqrt(variance)

    print "%s\tTotal=%s\tAverage=%.2f\tStdDev=%.2f" % (
        current_id,
        sum_scores,
        avg,
        std_dev
    )
