import time
import praw
import pprint
from pytz import utc, timezone
from datetime import datetime
from scrt import *


def scrape(submission_id, fname):
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=secret,
                         user_agent=agent)
    submission = reddit.submission(id=submission_id)
    print("Replacing more...")
    submission.comments.replace_more(limit=None)
    print("...Replaced more")
    # first_comment = submission.comments.list()[0]
    # pprint.pprint(vars(first_comment))
    # print(first_comment.author.name)
    # print(first_comment.ups)
    # print(first_comment.body)
    with open(fname, 'w') as handler:
        for comment in submission.comments.list():
            raw_date = datetime.utcfromtimestamp(comment.created_utc)
            local_date = utc.localize(raw_date, is_dst=None).astimezone(timezone('Europe/Moscow'))
            handler.write(local_date.strftime("%d.%m.%Y %H:%M:%S") + '\n')
            # handler.write('\n')
            handler.write(comment.author.name + '\n')
            # handler.write('\n')
            handler.write(str(comment.ups) + ' ups\n\n')
            # handler.write('\n\n')
            handler.write(comment.body + '\n\n\n')
            # handler.write('\n\n\n')


if __name__ == '__main__':
    start_time = time.time()
    scrape('1uac3m', 'true_events.txt')
    elapsed_time = time.time() - start_time
    print()
    print()
    print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
