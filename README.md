# Асинхронність 

Асинхронність — це процес обробки введення/виводу, що дозволяє продовжити обробку інших завдань,
не чекаючи завершення попереднього завдання.

### asyncio
У Python за асинхронність відповідає модуль [asyncio](https://docs.python.org/3/library/asyncio.html)  - бібліотека Python 3, що відповідає за неблокуючий введення-виведення.


```python3 
import asyncio
import httpx

wiki_urls = [
    "https://uk.wikipedia.org/wiki/Python",
    "https://uk.wikipedia.org/wiki/Java",
    "https://uk.wikipedia.org/wiki/C%2B%2B",
]

async def get_async_wiki_page(url):
    async with httpx.AsyncClient() as aclient:
        response = await aclient.get(url)
        return response.status_code, response.text


async def amain():
    tasks = [get_async_wiki_page(url) for url in wiki_urls]
    wiki_response = await asyncio.gather(*tasks)
    result = list()
    for page in wiki_response:
        result.append(f"{page[0]}: {page[1][:25]}")
    print(result)
```

