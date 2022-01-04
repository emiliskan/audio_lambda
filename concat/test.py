import asyncio

from concat import handler


async def test_normal():
    response = await handler(
        {
            "httpMethod": "POST",
            "body": {
                "files": [
                    "AwACAgIAAxkDAAIIJGGqi2wusiROsxHX4Dihw1STcYWKAALzFAACgHpRSSZWdzGLsZn2IgQ",
                    "AwACAgIAAxkDAAIIJmGqi21T_3L65koWRUrsk9K4RLzgAAL1FAACgHpRSa1PlYxVxHXrIgQ",
                    "AwACAgIAAxkBAAII6mHPDEQ8FDiaH4MOhaijcSxB7GzEAAKvEQACj7V4Spn_lwbRnV_BIwQ",
                    "AwACAgIAAxkDAAIIJ2Gqi218TcJl77rRQwapvuYG8vjkAAL2FAACgHpRSTxFqPIvcY0ZIgQ",
                    "AwACAgIAAxkBAAII7GHPDEsdIlllA5nwzzLygvSd_XfQAAKwEQACj7V4SkjIziQlTqQaIwQ",
                    "AwACAgIAAxkDAAIIKGGqi208IjOyNlDIXM8pN-JXhCYtAAL3FAACgHpRSWuenY9DwH9VIgQ",
                    "AwACAgIAAxkBAAII7mHPDE8qJgRlSKUSSSiy8hvFYGL7AAKyEQACj7V4SgLTEqqjumGQIwQ",
                    "AwACAgIAAxkDAAIIJWGqi2xseCQ0jcRBGQRNlEM61UhQAAL0FAACgHpRSdV9ZZoOnnTGIgQ"
                ],
                "finishFilename": "chat_id.wav"
            },
            "isBase64Encoded": False
        },
        {}
    )
    assert response["statusCode"] == 200


async def test_without_files():
    response = await handler(
        {
            "httpMethod": "POST",
            "body": {
                "files": [
                ],
                "finishFilename": "chat_id.wav"
            },
            "isBase64Encoded": False
        },
        {}
    )
    assert response["statusCode"] == 400


async def test():
    await test_normal()
    await test_without_files()


if __name__ == '__main__':
    asyncio.run(test())
