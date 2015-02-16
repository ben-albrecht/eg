#!/usr/bin/env python3

import requests
import sys, time

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool


def main(threads):
    urls = [
      'http://www.python.org',
      'http://www.python.org/about/',
      'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
      'http://www.python.org/doc/',
      'http://www.python.org/download/',
      'http://www.python.org/getit/',
      'http://www.python.org/community/',
      'https://wiki.python.org/moin/',
      'http://planet.python.org/',
      'https://wiki.python.org/moin/LocalUserGroups',
      'http://www.python.org/psf/',
      'http://docs.python.org/devguide/',
      'http://www.python.org/community/awards/'
      ]

    # Make the Pool of workers
    print(threads)
    pool = ThreadPool(threads)

    # Open the urls in their own threads
    # and return the results
    results = pool.map(requests.get, urls)

    #close the pool and wait for the work to finish
    pool.close()
    pool.join()


if __name__ == "__main__":
    time_start = time.time()

    threads = int(sys.argv[1])

    main(threads)

    print(time.time() - time_start)
