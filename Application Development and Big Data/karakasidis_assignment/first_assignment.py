from pyspark.sql.functions import col, upper


def execute_first_assignment(volleyball_data):
    percentage_cols = [
        'T1_Srv_Eff', 'T1_Rec_Pos', 'T1_Rec_Perf', 'T1_Att_Kill_Perc',
        'T1_Att_Eff', 'T1_Att_Sum', 'T2_Srv_Eff', 'T2_Rec_Pos', 'T2_Rec_Perf', 'T2_Att_Kill_Perc',
        'T2_Att_Eff', 'T2_Att_Sum'
    ]

    for col_name in percentage_cols:
        volleyball_data = volleyball_data.withColumn(col_name, col(col_name).substr(1, 4))

    volleyball_data = volleyball_data.withColumn("Team_1", upper(col("Team_1")))
    volleyball_data = volleyball_data.withColumn("Team_2", upper(col("Team_2")))

    total_matches = volleyball_data.count()

    volleyball_data = volleyball_data.withColumn("TotalSets", col("T1_Score") + col("T2_Score"))

    matches_per_total_sets = volleyball_data.groupBy("Total_Sets").count()
    matches_per_total_sets.write.csv("matches_per_total_sets.csv")

    team1_matches = volleyball_data.groupBy("Team_1").count()
    team2_matches = volleyball_data.groupBy("Team_2").count()

    team1_matches.write.csv("team1_matches.csv", header=True)
    team2_matches.write.csv("team2_matches.csv", header=True)

    print("First assignment done!")