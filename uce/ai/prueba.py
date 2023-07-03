import openai
from pydantic import BaseModel


class Document(BaseModel):
    prompt: str = ''


def inference(prompt: str) -> list:
    openai.organization = 'org-FlF7DjfN8kf6smfJafiv4p82'
    openai.api_key = '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'
    print('[PROCESANDO]'.center(40, '-'))

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un calculador factorial y muestrame el resultado correspondiente. Si ingresas algo que no sea un número, debes mostrame: syntax error."
            "E.G: El factorial del número 5 es 120" },
        ],
        temperature=0
    )

    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens

    print('[SE TERMINÓ DE PROCESAR]'.center(40, '-'))
    return [content, total_tokens]

