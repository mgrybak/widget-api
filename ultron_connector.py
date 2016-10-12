
"""
Connection wrapper for Ultron
@author: egillingham@graphiq.com, nnair@graphiq.com, mrybak@graphiq.com
"""
import MySQLdb
import logging
import requests
import json
import sys

ULTRON_LOGGER = logging.getLogger(__name__)
COMMASPACE = ', '

__version__ = "0.5"

class Ultron(object):
    def __init__(self, app_id, use_result_streaming_cursor=True, fail_if_data_out_of_sync=True):
        self.app_id = app_id
        self.ultron_url = "http://ultron-data.id.giq.io/getConnectionParams.php"
        self.user = ''
        self.password = ''
        self.host = ''
        self.port = None
        self.db = ''
        self.table_name = ''
        self.status = ''
        self.cnx = None
        self.cursor = None
        self.streaming_cursor = use_result_streaming_cursor
        self.fail_old = fail_if_data_out_of_sync
        self.byte_limit = 500000


    def _connect(self):
        """
        Connect (private) method - sets up the objects connection
        :return:
        """
        data_payload = {'appid': self.app_id}
        rq = requests.post(self.ultron_url, data=json.dumps(data_payload))
        connection = rq.json()
        self.cnx = MySQLdb.connect(user=connection.get('userName'), passwd=connection.get('password'),
                              host=connection.get('hostName'), port=int(connection.get('port')),
                              db=connection.get('dbName'), charset='utf8', use_unicode=True)
        self.table_name = connection.get("tablename")

        # if user has decided to fail if data is out of sync
        if self.fail_old:
            ULTRON_LOGGER.info("Asked to fail if data is out of sync")
            ULTRON_LOGGER.info("Replication status: {}".format(connection.get("replication_status")))

        # if data is out of sync and asked to fail - throw exception
        if connection.get("replication_status") == "failing" and self.fail_old:
            raise UltronConnectError("Data out of sync")

    def _get_batch_size(self, query):
        """
        (Private) Method to calculate the appropriate offset count without reading too many rows at once
        :param query:
        :return batch_size:
        """
        temp_query= '{} LIMIT {} OFFSET {}'.format(query, 1,0)
        self.cursor.execute(temp_query)
        row = self.cursor.fetchone()
        size_of_one = sys.getsizeof(row)

        # intended to be rounded - can't do anything with floats
        # TODO: cast if run with python3
        batch_size = self.byte_limit / size_of_one
        return batch_size


    def select(self, fields, where_clause=None):
        """
        Run a select query on the ultron connection
        returns an iterator which is to be used in a loop
        :param fields:
        :param type: list
        :param where_clause:
        :param string:
        :return iterator:
        """
        self._connect()
        assert(type(fields) == list)

        try:
            # construct basic select query
            query = "SELECT {} FROM {}".format(COMMASPACE.join(fields), self.table_name)
            if where_clause:
                query = '{} {}'.format(query, where_clause)

            # dicts are so much easier to work with
            self.cursor = self.cnx.cursor(cursorclass=MySQLdb.cursors.DictCursor)

            # If user has decided to stream - simply keep cursor open and send 1 by 1
            if self.streaming_cursor:
                self.cursor.execute(query)
                row = self.cursor.fetchone()
                while row:
                    yield row
                    row = self.cursor.fetchone()
            else:
                # otherwise identify an appropriate number of rows to get back
                # Find the size of 1 row, and get rows less than byte_limit
                batch_size = self._get_batch_size(query)
                ULTRON_LOGGER.info("Using batch sizes of {}".format(batch_size))
                offset = 0

                # rewrite query with limit and offset
                rewritten_query= '{} LIMIT {} OFFSET {}'.format(query, batch_size, offset)
                self.cursor.execute(rewritten_query)
                rows = self.cursor.fetchall()
                ULTRON_LOGGER.debug("Reading rows {} to {}".format(offset, offset + batch_size))
                while rows:
                    # close and open the cursor for each batch
                    self.cursor.close()
                    for row in rows:
                        yield row
                    offset += batch_size
                    rewritten_query = '{} LIMIT {} OFFSET {}'.format(query, batch_size, offset)
                    self.cursor = self.cnx.cursor(cursorclass=MySQLdb.cursors.DictCursor)
                    self.cursor.execute(rewritten_query)
                    rows = self.cursor.fetchall()
        finally:
            self.cursor.close()
            self.cnx.close()



class UltronConnectError(Exception):
    def __init__(self, error_msg):
        self.error_msg = error_msg
    def __str__(self):
        return repr(self.error_msg)