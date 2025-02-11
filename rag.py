from llmproxy import generate
from llmproxy import pdf_upload
import json

if __name__ == '__main__':
    # response_pdf = pdf_upload(
    #     path = 'lesson_plan.pdf'
    #     session_id = 'GenericSession'
    #     strategy = 'smart'
    # )
    # print(response_pdf)
    num_q = input('Number of questions: ')
    unit_num = input('Which unit? ')
    # lesson_input = input('Give the daily lesson plan topics to create a checkpoint quiz: ')
    #example_input = input ('Are there any example questions to base this off of? (optional)')
    
    query = 'Give me a multiple choice question quiz based on the given unit that is ' + \
            'delimited by triple astriks ***' + unit_num + '***' + \
            'to test the students on their knowledge after learning.' + \
            ' The number of questions is delimited by triple quotes """' + \
            num_q + '""" '
    
    system_constant = 'Evaluate if the number of questions is a valid number.' + \
    'If not, reprompt the number of questions. ' + \
    'Evaluate if the unit number is a valid number.' + \
    'If not, reprompt the unit number. ' + \
    'Answer in a format of question, 4 answer choices. And after all questions, ' + \
    ' give the key. In the key explain each answer like a helpful tutor, ' + \
    'assuming no previous knowledge.'

    print('QUERY::: ' + query + '\n')
    
    response1 = generate(model = '4o-mini',
        system = system_constant,
        query = query,
        temperature=0.0,
        lastk=0,
        session_id='bridgette-rag-test',
        rag_usage = True,
        rag_threshold = '0.2',
        rag_k = 4)
    #print('4o-mini: ')
    #print(response1)
    print(json.dumps(response1, indent=4, ensure_ascii=False))