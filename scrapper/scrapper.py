import time, sched

#
# Define steps functions here
#

# main function
def main(sc):
    try:
        print('asdas')
        # Call steps functions here
    except Exception as e:
        print('Exception Occured', e)
    s.enter(30, 1, main, (sc,))


if __name__ == '__main__':
    # sched is used to schedule main function every 30 seconds.
    # for that once  main function executes in end,
    # we again schedule it to run in 30 seconds
    s = sched.scheduler(time.time, time.sleep)
    s.enter(30, 1, main, (s,))
    s.run()

