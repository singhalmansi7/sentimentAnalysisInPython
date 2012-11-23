__author__ = 'msinghal'

import web
from sentiment_analyser_service import SentimentAnalyzingService

render = web.template.render('/home/msinghal/PycharmProjects/sentimentAnalysisInPython/templates')

urls = (
    '/Ok', 'Index'
    )

app = web.application(urls, globals())

class Index(object):

    def GET(self):
        return render.get_text()

    def POST(self):
        form = web.input(paragraph="None")
        textToBeAnalysed = "%s" % (form.paragraph)
        service = SentimentAnalyzingService()

        scoreOfSentimentAnalysis = service.performBasicSentimentAnalysis(textToBeAnalysed)
        return render.show_sentiment(scoreOfSentimentAnalysis)


if __name__ == "__main__":
    app.run()


