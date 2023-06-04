def benchmark_pinecone_batch_insertion(
    num_rows: list[int], vectors: int, batch_size: list[int]
) -> pd.DataFrame:
    pinecone_batch_insert_df = pd.DataFrame(
        columns=[
            "database_name",
            "record_count",
            "batch_size",
            "embedding_dimension",
            "insertion_time (s)",
            "insert_speed (MB/s)",
            "dataset_size_on_disk (MB)",
        ]
    )

    def chunks(iterable, batch_size=100):
        """A helper function to break an iterable into chunks of size batch_size."""

    it = iter(iterable)
    chunk = tuple(itertools.islice(it, batch_size))
    while chunk:
        yield chunk
        chunk = tuple(itertools.islice(it, batch_size))
    for rows in num_rows:
        # Create index
        index = pinecone_connection(
            api_key=PINECONE_API_KEY,
            index_name="pinecone_batch_benchmark",
            vector_dim=vectors,
        )
        df = create_fake_dataframe(num_rows=rows, dim_vectors=vectors)

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
        for batch in batch_size:
            for data_chunk in chunks(upsert_vectors, batch_size=batch):
                start_time = time.time()
                index.upsert(vectors=data_chunk)
                end_time = time.time()

            insertion_time = (end_time - start_time) / 1000

            data_size = rows / (1024**2)

            pinecone_batch_insert_df = pinecone_batch_insert_df.append(
                {
                    "database_name": "Pinecone",
                    "record_count": rows,
                    "batch_size": batch,
                    "embedding_dimension": vectors,
                    "insertion_time (s)": f"{insertion_time:.3f}",
                    "insert_speed (MB/s)": f"{data_size/insertion_time:.3f} MB/s",
                    "dataset_size_on_disk (MB)": f"{data_size:.2f} MB",
                },
                ignore_index=True,
            )
        logging.info("Pinecone Batch Insertion Benchmarking complete")

        pinecone.delete_index("pinecone_batch_benchmark")
        logging.info("Index deleted")

    pinecone_batch_insert_df.to_csv(
        "benchmarking/benchmark_results/03_pinecone_batch_insertion_benchmark.csv",
        index=False,
    )

    logging.info("Results saved")

    return pinecone_batch_insert_df
