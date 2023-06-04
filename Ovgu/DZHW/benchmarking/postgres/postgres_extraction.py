def benchmark_postgres_extraction(
    rows: int, vectors: int, top_k: list[int]
) -> pd.DataFrame:
    # Dataframe to store results
    postgres_extract_df = pd.DataFrame(
        columns=[
            "database_name",
            "k",
            "extraction_time (s)",
            "extraction_speed (rows/s)",
            "record_count",
        ]
    )

    # create a connection to the Postgres database
    engine = create_postgres_connection(db=DB, user=USER, pw=PW, host=HOST)
    conn = engine.connect()
    logging.info("Postgres connection created")

    logging.info(
        f"Creating dataframe with {rows} rows and having embedding size of {vectors} dimensions"
    )
    # create data
    data_set = create_fake_dataframe(num_rows=rows, vector_dimension=vectors)

    # insert data
    start_time = time.time()
    data_set.to_sql(
        "extract_benchmark",
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
    logging.info(
        f"Inserting data into Postgres with chunksize of 10000 took {(end_time - start_time) / 1000:.3f} seconds"
    )

    logging.info("Start Benchmarking")
    for k in top_k:
        time_taken = []
        for _ in range(20):
            start = time.time()
            query = f"SELECT * FROM extract_benchmark LIMIT {k}"
            df = pd.read_sql(query, con=conn)
            end = time.time()
            time_taken.append(end - start)

        extraction_time = sum(time_taken) / len(time_taken)

        logging.info("Adding results row to the dataframe")
        # Append results to the dataframe
        postgres_extract_df = postgres_extract_df.append(
            {
                "database_name": "Postgres",
                "k": k,
                "extraction_time (s)": f"{extraction_time:.3f}",
                "extraction_speed (rows/s)": f"{round(k/extraction_time)}",
                "record_count": rows,
            },
            ignore_index=True,
        )

    logging.info("Benchmarking complete")
    conn.execute("DROP TABLE extract_benchmark")
    logging.info("Table dropped")
    # Close connection to the database
    conn.close()
    logging.info("Postgres connection closed")
    # Save results
    postgres_extract_df.to_csv(
        "benchmarking/benchmark_results/02_postgres_data_extraction_results.csv",
        index=False,
    )
    logging.info("Results saved")
    return postgres_extract_df
