
"""
LurkerBot periodically checks a subscribed website/forum/etc.. and repost
new messages to chat.

This Bot uses the Updater class to handle the bot and the JobQueue do the
periodic checking updating of subscriptions.

Usage: (future, currently settings are coded)
/subscribe url=<url> timer=<timer default=300>
TODO: use inline for subscription setup?
Adds a subscription to periodically check for updates.
TODO: Return job uuid for unsubscription?
/forum <baseurl>
/mybb <baseurl> <threadid> <login> <pass>
  {tries to use anonymous?}
/rss <feedurl>

TODO: Make future features configurable...
  class ForumWatcher
    watch_url
    login_url / login()
    parse_post()
  class Post
  class Thread
    last_watched
    last_

LurkerBot, periodically performs some update function and returns output if
not the same as the previous result.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from lurkerbot import LurkerBot
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    # read token from config
    # read persistence_file from config

    # create the persistence object
    #my_persistence = DictPersistence(filename='my_dict')
    # load bot with persistence data
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary

    aedile = LurkerBot('aedile_config.json')
    # def echo2(self, update, context):
    #         update.message.reply_text(update.message.text)
    # setattr(aedile, 'foo', foo)
    aedile.run()
