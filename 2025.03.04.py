from func import *

# execute_sql_sentence(
#     sentence=f'drop table test'
# )

# execute_sql_sentence(
#     sentence=f'create table test(col_1 text)'
# )
#
# for i in range(5):
#     execute_sql_sentence(
#         sentence=f'insert into test values("{i}")'
#     )

execute_sql_sentence(
    sentence=f'alter table test add column col_2 text'
)

execute_sql_sentence(
    sentence=f'update test set col_2 = col_1'
)