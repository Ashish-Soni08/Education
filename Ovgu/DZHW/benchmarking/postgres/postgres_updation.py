def benchmark_postgres_updation(rows: int, vectors: int) -> pd.DataFrame:
    # Dataframe to store results
    postgres_update_df = pd.DataFrame(
        columns=[
            "database_name",
            "updation_time (s)",
            "update_speed (rows/s)",
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
        "update_benchmark",
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
        f"Inserting data into Postgres took {(end_time - start_time) / 1000:.3f} seconds"
    )
    print(
        pd.read_sql_query(
            "SELECT embeddings as old_embedding FROM update_benchmark WHERE id = 1",
            con=conn,
        )
    )
    logging.info("Start Benchmarking")
    time_taken = []
    for _ in range(20):
        new_vector = np.random.rand(vectors).tolist()
        start = time.time()
        query = text(
            "UPDATE update_benchmark SET embeddings = :updated_vector WHERE id = 1"
        )
        conn.execute(query, updated_vector=new_vector)
        end = time.time()
        time_taken.append(end - start)

    # print(pd.read_sql_query("SELECT embeddings as updated_embedding FROM update_benchmark WHERE id = 1", con=conn))
    updation_time = sum(time_taken) / len(time_taken)
    print(
        pd.read_sql_query(
            "SELECT embeddings as updated_embedding FROM update_benchmark WHERE id = 1",
            con=conn,
        )
    )
    logging.info("Adding results row to the dataframe")
    # Append results to the dataframe
    postgres_update_df = postgres_update_df.append(
        {
            "database_name": "Postgres",
            "updation_time (s)": f"{updation_time:.3f}",
            "update_speed (rows/s)": f"{round(1/updation_time)}",
            "record_count": rows,
        },
        ignore_index=True,
    )

    logging.info("Postgres Updation Benchmarking complete")

    conn.execute("DROP TABLE extract_benchmark")
    logging.info("Table dropped")
    # Close connection to the database
    conn.close()
    logging.info("Postgres connection closed")
    # Save results
    postgres_update_df.to_csv(
        "benchmarking/benchmark_results/04_postgres_updation_benchmark_results.csv",
        index=False,
    )
    logging.info("Results saved")
    return postgres_update_df
