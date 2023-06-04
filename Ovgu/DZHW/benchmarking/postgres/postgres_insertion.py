def benchmark_postgres_insertion(
    num_rows: list[int], vector_dimension: list[int]
) -> pd.DataFrame:
    # Dataframe to store results
    postgres_insert_df = pd.DataFrame(
        columns=[
            "database_name",
            "record_count",
            "embedding_dimension",
            "insertion_time (s)",
            "insert_speed (MB/s)",
            "dataset_size_on_disk (MB)",
        ]
    )

    # create a connection to the Postgres database
    engine = create_postgres_connection(db=DB, user=USER, pw=PW, host=HOST)
    conn = engine.connect()

    logging.info("Postgres connection created")

    logging.info("Start Benchmarking")
    for rows in num_rows:
        for vector_size in vector_dimension:
            # create data
            logging.info(
                f"Creating dataframe with {rows} rows and having embedding size of {vector_size} dimensions"
            )

            data_set = create_fake_dataframe(
                num_rows=rows, vector_dimension=vector_size
            )

            # insert data
            logging.info("Inserting data into Postgres")

            start_time = time.time()
            data_set.to_sql(
                "insert_benchmark",
                con=conn,
                if_exists="replace",
                index=False,
                dtype={
                    "id": Integer(),
                    "sentence": Text(),
                    "name": Text(),
                    "mobile": Text(),
                    "embeddings": ARRAY(Float),
                },
            )
            end_time = time.time()

            # Time taken to insert
            insertion_time = (end_time - start_time) / 1000

            # dataset size on disk
            data_size = rows / (1024**2)

            logging.info("Adding results row to the dataframe")
            # Append results to the dataframe

            postgres_insert_df = postgres_insert_df.append(
                {
                    "database_name": "Postgres",
                    "record_count": rows,
                    "embedding_dimension": vector_size,
                    "insertion_time (s)": f"{insertion_time:.3f}",
                    "insert_speed (MB/s)": f"{data_size/insertion_time:.3f} MB/s",
                    "dataset_size_on_disk (MB)": f"{data_size:.2f} MB",
                },
                ignore_index=True,
            )

        conn.execute("DROP TABLE insert_benchmark")
        logging.info("Table dropped")

    logging.info("Posgtres Insertion Benchmarking complete")
    # Close connection to the database

    conn.close()

    logging.info("Postgres connection closed")
    # Save results

    postgres_insert_df.to_csv(
        "benchmarking/benchmark_results/01_postgres_data_insertion_results.csv",
        index=False,
    )

    logging.info("Results saved")

    return postgres_insert_df
