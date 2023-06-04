# Convert Data to Haystack Format
def convert_data_to_haystack_format(df: pd.DataFrame) -> list:
        docs = []
        for d in df.iterrows():
                d = d[1]
                # create haystack document object with text content and doc metadata
                doc = Document(
                        content=d["sentence"],
                        content_type="text",
                        meta={"name": d["name"], "mobile": d["mobile"]},
                        id=d["id"],
                        embedding=d["embeddings"]
                )
                docs.append(doc)
        return docs