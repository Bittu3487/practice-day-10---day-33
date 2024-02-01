import requests
from twilio.rest import Client
stock_name = "TSLA"
company_name = "Tesla Inc"
stock_end_point = "https://www.alphavantage.co/query"
news_end_point = "https://newsapi.org/v2/everything"
stock_api_Key = "C2Z7HKFLN3JEZA5I"
news_api_key = "50a024a0274443afa7bc377835fc82c8"
account_sid = "ACd86d8e9d84273f4eff4f92d18d21a7ed"
auth_token = "e173a0b689181ce4afeb2aa116ec1c0e"
stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":stock_name,
    "apikey":stock_api_Key,
}

response = requests.get(stock_end_point , params = stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)
yesterday_before_price = data_list[1]
yesterday_before_closing_price = yesterday_before_price["4. close"]
print(yesterday_before_closing_price)
difference = abs(float(yesterday_closing_price) - float(yesterday_before_closing_price))
print(difference)
difference_percent = (difference/float(yesterday_closing_price))*100
print(difference_percent)
if difference_percent > 0:
    news_params = {
        "apikey":news_api_key,
        "qinTitle":company_name,
    }
    news_response = requests.get(news_end_point,params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)
    formated_articles = [f"Headline:{articles['title']}.\nbrief:{articles['description']}" for articles in three_articles]
    client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=formated_articles,
                     from_='+12019926805',
                     to='+918101355806'
                 )

print(message.status)