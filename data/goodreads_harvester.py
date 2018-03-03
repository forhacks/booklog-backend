import goodreads
from goodreads import client

gc = client.GoodreadsClient("ueUMoVwAkXNUPcOA4Y35yA", "R2N1HWPOdt4EEwQionNz0h3BgkY2z0yP5T3eXp8djc")

for i in xrange(0, int(1e9)):
    try:
        book = gc.book(str(i))
        print "Downloaded book %s" % i

        print book.description
        print book.title
        print book.average_rating
        print book.publisher

    except goodreads.request.GoodreadsRequestException:
        print "Couldn't find book %s" % i