def benchmark_pinecone_extraction(
    rows: int, vectors: int, top_k: list[int]
) -> pd.DataFrame:
    pinecone_extract_df = pd.DataFrame(
        columns=[
            "database_name",
            "k",
            "extraction_time (s)",
            "extraction_speed (rows/s)",
            "record_count",
        ]
    )
    # Create index

    index = pinecone_connection(
        api_key=PINECONE_API_KEY,
        index_name="pinecone_extraction_benchmark",
        vector_dim=vector_size,
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

    for k in top_k:
        time_taken = []
        for _ in range(20):
            start_time = time.time()
            index.query(
                vector=np.random.rand(vectors).tolist(),
                top_k=k,
                include_values=True,
            )
            end_time = time.time()
            time_taken.append(end_time - start_time)
        extraction_time = sum(time_taken) / len(time_taken)

        pinecone_extract_df = pinecone_extract_df.append(
            {
                "database_name": "Pinecone",
                "k": k,
                "extraction_time (s)": f"{extraction_time:.3f}",
                "extraction_speed (rows/s)": f"{rows/extraction_time:.3f} rows/s",
                "record_count": rows,
            },
            ignore_index=True,
        )

    logging.info("Pinecone Extraction Benchmarking complete")

    pinecone.delete_index("pinecone_extraction_benchmark")
    logging.info("Index deleted")

    pinecone_extract_df.to_csv(
        "benchmarking/benchmark_results/02_pinecone_extraction_benchmark.csv",
        index=False,
    )
    logging.info("Results saved")

    return pinecone_extract_df
