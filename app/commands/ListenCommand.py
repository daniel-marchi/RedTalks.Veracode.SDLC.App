from app.commands.BlabberCommand import BlabberCommand
from typing import override
import sys
import logging

class ListenCommand(BlabberCommand):
    logger = logging.getLogger("VeraDemo:IgnoreCommand")

    cursor = None
    username = None

    def __init__(self, cursor, username):
        super()
        self.cursor = cursor
        self.username = username

    @override
    def execute(self, blabberUsername):
        sqlQuery = "INSERT INTO listeners (blabber, listener, status) values ('%s', '%s', 'Active');"
        self.logger.info(sqlQuery)
        try :
            self.cursor.execute(sqlQuery % (blabberUsername, self.username))

            sqlQuery = "SELECT blab_name FROM users WHERE username = '" + blabberUsername + "'"
            self.logger.info(sqlQuery)
            self.cursor.execute(sqlQuery)
            result = self.cursor.fetchone()

            event = self.username + " started listening to " + blabberUsername + " (" + result[0] + ")"
            sqlQuery = "INSERT INTO users_history (blabber, event) VALUES (\"" + self.username + "\", \"" + event + "\")"
            self.logger.info(sqlQuery)
            self.cursor.execute(sqlQuery)

        except:

            # TODO: Implement exceptions

            self.logger.error("Unexpected error:", sys.exc_info()[0])