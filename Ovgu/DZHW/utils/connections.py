# Connect to Postgres Database
def postgres_connection(
    db: str, user: str, pw: str, host: str
) -> sqlalchemy.engine.base.Engine:
    # create a connection to the Postgres database
    engine = create_engine(f"postgresql://{USER}:{PW}@{HOST}:5432/{DB}")
    return engine


# Connect to Pinecone Vector Database
def pinecone_connection(
    api_key: str,
    environment: str = "us-west0-gcp",
    index_name: str = "benchmark_db",
    distance_metric: str = "cosine",
    vector_dimension: int = 7,
):
    pinecone.init(api_key=api_key, environment=environment)
    pinecone.create_index(
        index_name, dimension=vector_dimension, metric=distance_metric, pod_type="p1.x1"
    )
    index = pinecone.Index(index_name)
    return index