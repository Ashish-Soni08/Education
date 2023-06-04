# DROP TABLES
benchmark_data_table_drop = "DROP TABLE IF EXISTS benchmark_data"
# urvey_questions_table_drop = "DROP TABLE IF EXISTS survey_questions"

# CREATE TABLES

benchmark_data_table_create = (""" CREATE TABLE IF NOT EXISTS benchmark_data (id INT PRIMARY KEY,
                                                            sentence VARCHAR(50),
                                                            name VARCHAR(20),
                                                            mobile VARCHAR(20),
                                                            embeddings FLOAT[1000]);
                            """);

# survey_questions_table_create = (""" CREATE TABLE IF NOT EXISTS survey_questions (survey_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
#                                                                                   survey_name VARCHAR(50) NOT NULL UNIQUE,
#                                                                                   survey_module_name VARCHAR(50) NOT NULL UNIQUE,
#                                                                                   choice_text VARCHAR(500) NOT NULL UNIQUE,
#                                                                                   additional_answer_type VARCHAR(50) NOT NULL,
#                                                                                   answer_type VARCHAR(50) NOT NULL,
#                                                                                   choice_group_text VARCHAR(500) NOT NULL UNIQUE,
                                                                                  
#                                  );""");

# INSERT RECORDS

benchmark_data_table_insert = (""" 
INSERT INTO benchmark_data (id, sentence, name, mobile, embeddings)
VALUES (%s, %s, %s, %s, %s)
""")


# QUERY LISTS

create_table_queries = [benchmark_data_table_create]
drop_table_queries = [benchmark_data_table_drop]