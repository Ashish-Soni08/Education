def benchmark_postgres_insertion(
    num_rows: list[int], vector_dimension: list[int]
) -> pd.DataFrame:
    postgres_insert_df = pd.DataFrame(
        columns=[
            "database_name",
            "row_count",
            "embedding_dimension",
            "insertion_time(s)",
        ]
    )

    engine = postgres_connection(db=DB, user=USER, pw=PW, host=HOST)
    conn = engine.connect()
    print("Connected to Postgres")
    time.sleep(30)

    print("start benchmarking")
    for vector_size in vector_dimension:
        for rows in num_rows:
            data_set = create_fake_dataframe(
                num_rows=rows, vector_dimension=vector_size
            )

            print(
                f"Inserting data into Postgres with {rows} rows and {vector_size} dimensions"
            )

            start_time = time.perf_counter()
            data_set.to_sql(
                "insert_benchmark",
                con=conn,
                if_exists="replace",
                index=False,
                dtype={
                    "id": Integer(),
                    "sentence": Text(),
                    "embeddings": Vector(vector_size),
                },
            )
            end_time = time.perf_counter()

            print(
                f"Insertion of {rows} rows and {vector_size} dimensions into Postgres complete"
            )
            print("-" * 70)
            insertion_time = end_time - start_time

            postgres_insert_df = postgres_insert_df.append(
                {
                    "database_name": "Postgres",
                    "row_count": rows,
                    "embedding_dimension": vector_size,
                    "insertion_time(s)": f"{insertion_time:.3f}",
                },
                ignore_index=True,
            )

        conn.execute("DROP TABLE insert_benchmark")
        print("Table dropped")
        time.sleep(10)

    print("Postgres Insertion Benchmarking complete")

    # Close connection to the database
    conn.close()

    # Save results
    postgres_insert_df.to_csv(
        "benchmarking/benchmark_results/01_postgres_data_insertion_results.csv",
        index=False,
    )

    print("Results saved")

    return postgres_insert_df
