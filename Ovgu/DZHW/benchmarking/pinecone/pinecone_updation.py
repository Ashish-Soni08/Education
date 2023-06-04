def benchmark_pinecone_updation(
    rows: int, vectors: int, top_k: list[int]
) -> pd.DataFrame:
    pinecone_update_df = pd.DataFrame(
        columns=[
            "database_name",
            "updation_time (s)",
            "update speed (rows/s)",
            "record_count",
        ]
    )
    # Create index

    index = pinecone_connection(
        api_key=PINECONE_API_KEY,
        index_name="pinecone_update_benchmark",
        vector_dim=vectors,
    )
    df = create_fake_dataframe(num_rows=rows, vector_dimension=vectors)
    upsert_vectors = [
        (
            str(row["id"]),
            row["embeddings"],
            {
                "name": row["name"],
                "mobile": row["mobile"],
                "sentence": row["sentence"],
            },
        )
        for _, row in df.iterrows()
    ]
    start_time = time.time()
    index.upsert(vectors=upsert_vectors)
    end_time = time.time()
    logging.info(f"Data added in {end_time - start_time} seconds")
    old_vector = index.fetch(ids=['1'])
    print("Old vector:", old_vector)
    time_taken = []
    for _ in range(20):
        new_vector = np.random.rand(vectors).tolist()
        start_time = time.time()
        index.update(
            id='1',
            values=new_vector
        )
        end_time = time.time()
        time_taken.append(end_time - start_time)
    
    updation_time = sum(time_taken) / len(time_taken)
    
    new_vector = index.fetch(ids=['1'])
    print("New vector", new_vector)
    
    pinecone_update_df = pinecone_update_df.append(
        {
            "database_name": "Pinecone",
            "updation_time (s)": f"{updation_time:.3f}",
            "update_speed (rows/s)": f"{round(1/updation_time)}",
            "record_count": rows
        },
        ignore_index=True,
    )

    logging.info("Pinecone Updation Benchmarking complete")

    pinecone.delete_index("pinecone_update_benchmark")
    logging.info("Index deleted")

    pinecone_update_df.to_csv(
        "benchmarking/benchmark_results/03_pinecone_updation_benchmark.csv",
        index=False,
    )
    logging.info("Results saved")

    return pinecone_update_df
