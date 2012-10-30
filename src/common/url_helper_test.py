#!/usr/bin/python2.7
#
# Copyright 2012 Google Inc. All Rights Reserved.

"""Unittest to exercise the code in url_helper.py."""




import logging
import StringIO
import time
import unittest
import urllib
import urllib2


from common import url_helper
from third_party.mox import mox


class UrlHelperTest(unittest.TestCase):
  def setUp(self):
    self._mox = mox.Mox()

    self._mox.StubOutWithMock(logging, 'error')
    self._mox.StubOutWithMock(time, 'sleep')
    self._mox.StubOutWithMock(urllib2, 'urlopen')

  def tearDown(self):
    self._mox.UnsetStubs()

  def testUrlOpenInvalidTryCount(self):
    url_helper.logging.error(mox.IgnoreArg(), mox.IgnoreArg())

    self._mox.ReplayAll()

    self.assertEqual(url_helper.UrlOpen('url', max_tries=-1), None)

    self._mox.VerifyAll()

  def testUrlOpenInvalidWaitDuration(self):
    url_helper.logging.error(mox.IgnoreArg(), mox.IgnoreArg())

    self._mox.ReplayAll()

    self.assertEqual(url_helper.UrlOpen('url', wait_duration=-1), None)

    self._mox.VerifyAll()

  def testUrlOpenSuccess(self):
    response = 'True'
    url_helper.urllib2.urlopen(mox.IgnoreArg(), mox.IgnoreArg()).AndReturn(
        StringIO.StringIO(response))

    self._mox.ReplayAll()

    self.assertEqual(url_helper.UrlOpen('url'), response)

    self._mox.VerifyAll()

  def testUrlOpenSuccessAfterFailure(self):
    url_helper.urllib2.urlopen(
        mox.IgnoreArg(), mox.IgnoreArg()).AndRaise(urllib2.URLError('url'))
    time.sleep(mox.IgnoreArg())
    response = 'True'
    url_helper.urllib2.urlopen(mox.IgnoreArg(), mox.IgnoreArg()).AndReturn(
        StringIO.StringIO(response))

    self._mox.ReplayAll()

    self.assertEqual(url_helper.UrlOpen('url', max_tries=2), response)

    self._mox.VerifyAll()

  def testUrlOpenFailure(self):
    url_helper.urllib2.urlopen(
        mox.IgnoreArg(), mox.IgnoreArg()).AndRaise(urllib2.URLError('url'))
    logging.error(mox.IgnoreArg(), mox.IgnoreArg(), mox.IgnoreArg())

    self._mox.ReplayAll()

    self.assertFalse(url_helper.UrlOpen('url'))

    self._mox.VerifyAll()

  def testUrlOpenHTTPError(self):
    url_helper.urllib2.urlopen(
        mox.IgnoreArg(), mox.IgnoreArg()).AndRaise(
            urllib2.HTTPError('url', 0, 'error message', None, None))
    logging.error(mox.IgnoreArg(), mox.IgnoreArg(), mox.IgnoreArg())

    self._mox.ReplayAll()

    # Even though we set max_tries to 5, we should only try once since
    # we get an HTTPError.
    self.assertEqual(url_helper.UrlOpen('url', max_tries=5), None)

    self._mox.VerifyAll()

  def testEnsureCountKeyIncludedInOpen(self):
    attempts = 5
    for i in range(attempts):
      encoded_data = urllib.urlencode({url_helper.COUNT_KEY: i})

      url_helper.urllib2.urlopen(
          mox.IgnoreArg(), encoded_data).AndRaise(urllib2.URLError('url'))
      logging.info(mox.IgnoreArg(), mox.IgnoreArg(), mox.IgnoreArg(),
                   mox.IgnoreArg())
      if i != attempts - 1:
        time.sleep(mox.IgnoreArg())

    logging.error(mox.IgnoreArg(), mox.IgnoreArg(), mox.IgnoreArg())
    self._mox.ReplayAll()

    self.assertEqual(url_helper.UrlOpen('url', max_tries=attempts), None)
    self._mox.VerifyAll()

  def testCountKeyInData(self):
    data = {url_helper.COUNT_KEY: 1}

    logging.error(mox.StrContains('existed in the data'), url_helper.COUNT_KEY)
    self._mox.ReplayAll()

    self.assertEqual(url_helper.UrlOpen('url', data=data), None)
    self._mox.VerifyAll()


if __name__ == '__main__':
  unittest.main()
