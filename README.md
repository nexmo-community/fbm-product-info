# fbm-product-info

A simple web app that automates getting info to potential customers
via FaceBook Messenger.

## Status

Refactored. Now needs testing.

## Example

The user sends Acme a message 'Hi' an automated reply is sent saying:
"Type `info: service` to obtain info". This could also provide a list
of services.

If the user types `info: tank cleaning` or `info: my tanks need
cleaning`, they will be sent correct product info.

## Uses

* Python/Flask.
* PyJWT

## FBM message send

Contains a custom tiny client to send FBM messages until officially
supported.

---
