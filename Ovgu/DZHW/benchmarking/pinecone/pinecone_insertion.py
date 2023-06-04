def benchmark_pinecone_insertion(
    num_rows: list[int], vector_dimension: list[int]
) -> pd.DataFrame:
    pinecone_insert_df = pd.DataFrame(
        columns=[
            "database_name",
            "record_count",
            "embedding_dimension",
            "insertion_time (s)",
            "insert_speed (MB/s)",
            "dataset_size_on_disk (MB)",
        ]
    )
    for rows in num_rows:
        for vector_size in vector_dimension:
            # Create index

            index = pinecone_connection(
                api_key=PINECONE_API_KEY,
                index_name="pinecone_insertion_benchmark",
                vector_dim=vector_size,
            )
            df = create_fake_dataframe(num_rows=rows, dim_vectors=vector_size)
            vectors = [
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
            index.upsert(vectors=vectors)
            end_time = time.time()

            # Time taken to insert
            insertion_time = (end_time - start_time) / 1000

            # dataset size on disk
            data_size = rows / (1024**2)

            pinecone_insert_df = pinecone_insert_df.append(
                {
                    "database_name": "Pinecone",
                    "record_count": rows,
                    "embedding_dimension": vector_size,
                    "insertion_time (s)": f"{insertion_time:.3f}",
                    "insert_speed (MB/s)": f"{data_size/insertion_time:.3f} MB/s",
                    "dataset_size_on_disk (MB)": f"{data_size:.2f} MB",
                },
                ignore_index=True,
            )

    logging.info("Pinecone Insertion Benchmarking complete")

    pinecone.delete_index("pinecone_insertion_benchmark")
    logging.info("Index deleted")

    pinecone_insert_df.to_csv(
        "benchmarking/benchmark_results/01_pinecone_insertion_benchmark.csv",
        index=False,
    )
    logging.info("Results saved")

    return pinecone_insert_df
