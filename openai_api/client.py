import openai

def get_car_ai_bio(model, brand, year):
    prompt = '''
    me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo de carro.
    '''
    openai.api_key = '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'
    prompt = prompt.format(brand, model, year)
    response = openai.completions.create(
        model='text-davinci-003',
        prompt=prompt,
        max_tokens=1000,
    )
    return response['choices'][0]['text']