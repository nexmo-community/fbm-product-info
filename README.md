# fbm-product-info

A simple web app that automates getting info to potential customers
via FaceBook Messenger.

## Status

Working.

## Example

1. The user sends the Facebook Page a message 'Hi'.
2. An automated reply is sent back listing products/services or other
   generic message.
3. Use sends back a message containing a keyword.
4. Based on the keyword a tailored response is automatically returned.
5. User can switch off auto mode by sending a message `auto: off`.
6. User can switch on auto mode by sending a message `auto: on`.

## Uses

* Python/Flask.
* PyJWT

## FBM message send

Contains a tiny Python client to send FBM messages until official
support is available.

---
