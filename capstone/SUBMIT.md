# Masar capstone: submission

Name: Raghad Alzkeri
Branch: main
Link: https://github.com/RaghadLOT/masar-lakehouse/tree/main

How to submit: `git add -A && git commit -m "Capstone" && git push`. You push to your own
fork (GitHub creates it on your first push). Send the link above to your trainer. If you
never pushed, send this file and the output of `python -m masar.proof` instead.

## What I built (one line per step)
1. Bronze: landed and profiled bronze
2. Silver (dbt): built silver and passed all quality ckecks
3. Delta control: added constraint and altered schema
4. Gold: built gold mart
5. BI-safe table: data ready to use for BI use cases
6. Pipeline (`make pipeline`): ran the entire procces from the start
7. Proof (counts + time travel):

## Counts per layer
bronze/trips 48,200
bronze/drivers 1,850
bronze/gps_pings 120,000

## Time travel
3      |2026-11-26 10:56:36.098|MERGE                            |5      |NULL   
4      |2026-11-26 10:57:41.897|DELETE                           |NULL   |7      

## Steps the trainer handed over (if any)

## One thing I would improve
