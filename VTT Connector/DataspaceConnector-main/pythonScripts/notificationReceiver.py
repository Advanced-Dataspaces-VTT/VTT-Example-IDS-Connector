import tornado.ioloop
import tornado.web
import logging
import requests


class printNotification(tornado.web.RequestHandler):

    async def post(self):
        try:
            print("someone called me")
            payload = self.request.body.decode('utf-8')
            print(payload)

        except Exception as e:
            _logger.info("Error happened: "+ str(e))



application = tornado.web.Application([
    (r'/notify', printNotification),

])



if __name__ == "__main__":
    #_logger.info("Starting tornado server")
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
