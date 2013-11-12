from django_webtest import WebTest
from django.core.urlresolvers import reverse

from models import *

class QuestionViewsTest(WebTest):

    def test_add_question(self):
        """
        Tests the addition of questions through the add form
        """

        text = "Who's the rapper on the hit 'Thrift Shop'?"
        answer_keywords = "Macklemore"
        
        add_question_page = self.app.get(reverse("questions_add"))
        form = add_question_page.forms['add_question_form']

        # self.fail("Form: %s\nPage: %s" % (repr(form), repr(add_question_page.body)))
        # self.fail("Page: %s\nFields: %s" % (repr(form.fields.values()), repr(add_question_page.body)))
        
        form['question_text'] = text
        form['answer_keywords'] = answer_keywords
        form.submit().follow()

        questions = Question.objects.all()
        self.assertEqual(1, len(questions), "Wrong number of questions, Questions: %s" % repr(questions))
        self.assertEqual(text, questions[0].question_text, "Question text did not match, Question Text: %s" % questions[0].question_text)
        self.assertEqual(answer_keywords, questions[0].answer_keywords, "Answer Keywords did not match, Keywords: %s" % questions[0].answer_keywords)

        
