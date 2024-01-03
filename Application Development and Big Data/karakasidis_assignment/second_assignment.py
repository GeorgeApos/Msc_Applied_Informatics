from pyspark.sql.functions import col


def execute_second_assignment(volleyball_data):

    team_statistics = volleyball_data.groupBy("Team1").agg(
        {"Sets1": "sum", "Sets2": "sum", "Points1": "sum", "Points2": "sum", "Matches": "count"}
    )

    team_statistics = team_statistics.withColumnRenamed("sum(Sets1)", "SetsWon")
    team_statistics = team_statistics.withColumnRenamed("sum(Sets2)", "SetsLost")
    team_statistics = team_statistics.withColumnRenamed("sum(Points1)", "PointsWon")
    team_statistics = team_statistics.withColumnRenamed("sum(Points2)", "PointsLost")
    team_statistics = team_statistics.withColumnRenamed("count(Matches)", "TotalMatches")

    team_statistics = team_statistics.orderBy(col("TotalMatches").desc())

    team_statistics.write.csv("team_statistics.csv", header=True)

