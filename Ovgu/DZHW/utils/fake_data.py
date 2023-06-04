# Create a fake dataframe
def create_fake_dataframe(num_rows: int, vector_dimension: int) -> pd.DataFrame:
    data = {
            'id': [i for i in range(num_rows)],
            'sentence': [fake.sentence(nb_words = 30, variable_nb_words = True) for _ in range(num_rows)],
            'name': [fake.name() for _ in range(num_rows)],
            'mobile': [fake.phone_number() for _ in range(num_rows)],
            'embeddings': [[round(random.random(), 7) for _ in range(vector_dimension)] for _ in range(num_rows)]    # to replicate the embeddings from different models
            }
    df = pd.DataFrame(data)
    assert df.shape[0] == num_rows, f'Expected {num_rows} rows, but got {df.shape[0]}'
    assert len(df['embeddings'][0]) == vector_dimension, f'Expected {vector_dimension} elements in embeddings column, but got {len(df["embeddings"][0])}'
    return df