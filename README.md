# MLB Batter Rankings

I built this Python command-line tool to explore how a hitter’s ranking changes when evaluated by different batting metrics.

## How to run

From the repository folder, run `python3 app.py`. The tool uses Python 3’s standard library and reads `batter_state.csv` from the same folder.

- Choose **1** to rank hitters by batting average (AVG), on-base percentage (OBP), slugging percentage (SLG), or on-base plus slugging (OPS).
- Choose **2** to compare rankings for a selected metric with the preseason ranks in the CSV.

## What I found

I ranked the 71 hitters in the sample by AVG and estimated OPS. **40 of 71 hitters ranked at least 10 spots apart** across the two lists. Luis Arraez ranked **7th by AVG** and **57th by estimated OPS**, illustrating how much a hitter’s ranking can change when walks and extra-base hits are also reflected in the metric.

## Data limitations

All rankings are within the 71-hitter sample. The CSV lacks hit-by-pitch counts, so the tool estimates OBP as `(H + BB) / (AB + BB + SF)` and uses that estimate to calculate OPS.

## Project status and next steps

This is an early prototype focused on hitter rankings. As I continue the project, I’d like to use a more complete dataset, compare results across seasons, and add a visualization that makes the largest ranking differences easier to spot.
