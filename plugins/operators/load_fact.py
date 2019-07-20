from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class LoadFactOperator(BaseOperator):

    ui_color = '#F98866'

    @apply_defaults
    def __init__(self,
                 table="",
                 aws_credentials_id="",
                 redshift_conn_id="",
                 sql_query="",
                 *args, **kwargs):

        super(LoadFactOperator, self).__init__(*args, **kwargs)
        self.table = table,
        self.aws_credenitals_id = aws_credentials_id,
        self.redshift_conn_id = redshift_conn_id,
        self.sql_query = sql_query,

    def execute(self, context):
        self.log.info("Loading fact...")
        redshift_hook = PostgresHook(self.redshift_conn_id)
        redshift_hook.run(f"INSERT INTO {self.table} " + str(self.sql_query))
