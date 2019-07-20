from airflow.hooks.postgres_hook import PostgresHook
from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class CreateTablesOperator(BaseOperator):
    uni_color = '#358140'
    sql_file_path = "create_table.sql"

    @apply_dsefaults
    def __init__(self,
                 redshift_conn_id="",
                 *arg, **kwargs):
        super(CreateTablesOperator, self).__init__(*arg, **kwargs)
        self.redshift_conn_id = redshift_conn_id

    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)

        self.log.info("Creating tables...")

        sql_file = ""
        with open(CreateTablesOperator.sql_file_path, 'r') as f:
            sql_file = f.read()
        sql_commands = sql_file.split(";")

        for command in sql_commands:
            redshift.run(command)
