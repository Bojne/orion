import requests
from prefect import flow, task


@task
def call_api(url):
    response = requests.get(url)
    print(response.status_code)
    return response.json()


@task
def parse_fact(response):
    print(response["fact"])
    return


@flow
def api_flow(url):
    fact_json = call_api(url)
    parse_fact(fact_json)
    return


api_flow("https://catfact.ninja/fact")
