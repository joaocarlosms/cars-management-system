from openai import OpenAI

client = OpenAI(
    api_key='sk-proj-7J8hzCKBCn57ruAeFRbET3BlbkFJQcCU0RfiNDQdaQRLCL1d'
)

def get_car_ai_bio(model, brand, model_year):
    message = '''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.
    Descreva especificações técnicas desse modelo de carro.
    '''

    message.format(brand, model, model_year)
    response = client.chat.completions.create(
        messages=[
            {
                'role':'user',
                'content': message
            }
        ],
        max_tokens=1000,
        model='gpt-3.5-turbo'
    )