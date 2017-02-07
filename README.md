Бот "Водий бозор" телеграм канали админлари буюртмаси асосида ишлаб чиқилмоқда

## Ботга қўйилган талаблар
* максимум даражада тез ишлайдиган;
* интерфейс жудаям содда ва осон бўлиши;
* бериладиган эълонни интерактив сўров асосида базага ёзиш;

## Ботни серверга ўрнатиш учун талаблар
* Python 3.6
* asyncio
* aiohttp
* uvloop
* aiotg
* asyncpg
* aiobotocore
* Postgresql 9.6

## Муҳит ўзгарувчилари
* API_TOKEN - бот учун берилган токен
* BOT_NAME - бот номи
* DATABASE_URL - маълумотлари базасига уланиш параметрлари
* AWS_ACCESS_KEY_ID - Amazon S3 учун
* AWS_SECRET_ACCESS_KEY - Amazon S3 учун

## Архитектура

     .───────────────────────────────────────.         .─────────────────────.
    (               Postgresql                )       (       Amazon S3       )
     `───────────────────────────────────────'         `─────────────────────'
                         △                                        △
                        ┌┘                                        │
    ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┼ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┼ ─ ─ ─ ─ ─ ┐  ┌────────┐
                        ▽        asyncio + uvloop                 ▽              │        │
    │    ┌────────────────────────────┐ ┌────────────────┐ ┌─────────────┐    │  │        │
         │                            │ │                │ │             │       │        │
    │    │                            │ │       AI       │ │             │    │  │Телеграм│
         │                            │ │                │ │             │       │ канал  │◀─┐
    │ ┌─▷│          asyncpg           │ │                │ │ aiobotocore │◁─┐ │  │        │  │
      │  │                            │ └────────────────┘ │             │  │    │        │  │
    │ │  │                            │          ●         │             │  │ │  │        │  │
      │  │                            │   ─ ─ ─ ─          │             │  │    └────────┘  │
    │ │  └────────────────────────────┘  ●                 └─────────────┘  │ │       ▲      │
      │  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓  │         │      │
    │ │  ┃                                                               ┃  │ │       │      │
      └─▷┃                Бот (asyncio + aiotg + aiohttp)                ┃──┴─────────┘      │
    │    ┃                                                               ┃    │              │
         ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                   │
    │                                    ▲                                    │              │
     ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┼ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─               │
                ┌────────────────────────┼────────────────────────┐                          │
                │                        │                        │                          │
                ▼                        ▼                        ▼                          │
    ┏━━━━━━━━━━━━━━━━━━━━━━━┓ ┏━━━━━━━━━━━━━━━━━━━━┓ ┏━━━━━━━━━━━━━━━━━━━━━━━━┓              │
    ┃                       ┃ ┃                    ┃ ┃                        ┃              │
    ┃         Админ         ┃ ┃   Эълон берувчи    ┃ ┃      Фойдаланувчи      ┃◀─────────────┘
    ┃                       ┃ ┃                    ┃ ┃                        ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━┛ ┗━━━━━━━━━━━━━━━━━━━━┛ ┗━━━━━━━━━━━━━━━━━━━━━━━━┛
