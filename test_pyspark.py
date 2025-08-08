"""Teste simples de inicialização do Spark.

IMPORTANTE: PySpark 3.5.1 ainda NÃO suporta Python 3.13.
Use Python 3.12 (ou 3.11/3.10/3.9) para evitar crash de "Python worker exited unexpectedly".
"""

import os
import sys
import platform
from pyspark.sql import SparkSession


def build_spark():
    builder = (
        SparkSession.builder
        .appName("TestePySpark")
        .master("local[*]")  # usa todos os cores disponíveis
        .config("spark.sql.shuffle.partitions", "4")  # reduz partitions para teste local
        .config("spark.driver.memory", "2g")
        .config("spark.executor.memory", "2g")
    )
    return builder.getOrCreate()


def main():
    # Ajustes de ambiente
    os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
    os.environ.setdefault("PYSPARK_DRIVER_PYTHON", sys.executable)
    os.environ.setdefault("SPARK_LOCAL_IP", "127.0.0.1")  # ajuda em alguns ambientes Windows

    print("Python:", sys.version)
    print("Platform:", platform.platform())
    print("PYSPARK_PYTHON=", os.environ.get("PYSPARK_PYTHON"))
    print("JAVA_HOME=", os.environ.get("JAVA_HOME", "(não definido)"))

    spark = build_spark()
    try:
        df = spark.createDataFrame([(1, "a"), (2, "b")], ["id", "letra"])
        print("Contagem:", df.count())
        df.show(truncate=False)
    finally:
        spark.stop()


if __name__ == "__main__":
    main()
