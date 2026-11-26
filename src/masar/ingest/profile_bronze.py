from pyspark.sql import functions as F
from masar.spark import get_spark

TABLES = [
    ("trips", "./lakehouse/bronze/trips", "trip_id"),
    ("drivers", "./lakehouse/bronze/drivers", "driver_id"),
    ("gps_pings", "./lakehouse/bronze/gps_pings", "ping_id"),
]


def profile_all() -> None:
    spark = get_spark("profile")

    for name, table_path, id_col in TABLES:
        print(f"\n=== {name} ({table_path}) ===")
        df = spark.read.format("delta").load(table_path)
        n = df.count()
        print(f"rows={n:,}  columns={len(df.columns)}")

        if n == 0:
            print("table is empty; skipping null ratios")
            continue

        df.select([
            (F.sum(F.col(c).isNull().cast("int")) / F.lit(n)).alias(c)
            for c in df.columns
        ]).show(truncate=False, vertical=True)

        if id_col in df.columns:
            d = df.groupBy(id_col).count().filter("count > 1").count()
            print(f"duplicate {id_col} groups: {d:,}")


if __name__ == "__main__":
    profile_all()