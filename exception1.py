def this_fails():
    x = 1 / 0
try:
    this_fails()
except BaseException as detail:
    print('Handling run-time error:', detail)