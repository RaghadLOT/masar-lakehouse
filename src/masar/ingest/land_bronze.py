from pyspark.sql import functions as F
from masar.spark import get_spark

BRONZE = "./lakehouse/bronze"


def _lineage(df):
    return (df.withColumn("_ingested_at", F.current_timestamp())
              .withColumn("_source_file", F.input_file_name()))


def land_trips(source_glob: str) -> None:
    spark = get_spark("land-trips") #new spark sesh
    raw = (spark.read
           .option("header", True) #bring header
           .option("mode", "PERMISSIVE")   # keep malformed rows, do not drop
           .csv(source_glob)) #
    _lineage(raw).write.format("delta").mode("append").save(f"{BRONZE}/trips") #writing data. append in bronze bc we dont edit in bronze

def land_gps(source_glob: str) -> None:
    spark = get_spark("land-gps")
    raw = spark.read.json(source_glob)   # schema-on-read for nested JSON. insted of csv
    _lineage(raw).write.format("delta").mode("append").save(f"{BRONZE}/gps_pings")

def land_drivers(source_glob: str) -> None:
    spark = get_spark("land-drivers")
    raw = (spark.read
            .option("header", True)
            .option("mode", "PERMISSIVE")
            .csv(source_glob)) 
    _lineage(raw).write.format("delta").mode("append").save(f"{BRONZE}/drivers")

def land_payments(source_glob: str) -> None:
    spark = get_spark("land-payments") #new spark sesh
    raw = (spark.read
           .option("header", True) #bring header
           .csv(source_glob)) #
    _lineage(raw).write.format("delta").mode("append").save(f"{BRONZE}/payments")
    
if __name__ == "__main__":
    land_trips("data/raw/trips_2026-*.csv")
    land_gps("data/raw/gps/*.ndjson")
    land_drivers("data/raw/drivers.csv")
    # land_payments("data/raw/payments_2026-*.csv")
    print("landed")