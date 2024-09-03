import asyncio
import httpx
import tool_benchmark as tb
from pprint import pprint

wiki_urls = [
    "https://uk.wikipedia.org/wiki/Python",
    "https://uk.wikipedia.org/wiki/Java",
    "https://uk.wikipedia.org/wiki/C%2B%2B",
]


# ========== SYNC ============================================

def get_sync_wiki_page(url):
    with httpx.Client() as client:
        response = client.get(url)
        return response.status_code, response.text


@tb.benchmark
def main():
    result = list()
    for url in wiki_urls:
        page = get_sync_wiki_page(url)
        result.append(f"{page[0]} -- {page[1][:25]}")
    print("\nSYNC result\n")
    pprint(result)


# ========== ASYNC ============================================

async def get_async_wiki_page(url):
    async with httpx.AsyncClient() as aclient:
        response = await aclient.get(url)
        return response.status_code, response.text


@tb.async_benchmark
async def amain():
    tasks = [get_async_wiki_page(url) for url in wiki_urls]
    wiki_response = await asyncio.gather(*tasks)
    result = list()
    for page in wiki_response:
        result.append(f"{page[0]}: {page[1][:25]}")
    print("\nASYNC result\n")
    pprint(result)


if __name__ == "__main__":
    asyncio.run(amain())
    main()
