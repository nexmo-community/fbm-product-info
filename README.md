# fbm-product-info

A simple web app that automates getting info to potential customers
via FaceBook Messenger.

## Example

The user sends Acme a message 'Hi' an automated reply is sent saying:
"Type `info: service` to obtain info". This could also provide a list
of services.

If the user types `info: tank cleaning` or `info: my tanks need
cleaning`, they will be sent correct product info.

## Status

Works fine, but could be vastly improved.

## Uses

* Python/Flask.
* PyJWT

Contains a custom tiny client to send FBM messages until officially
supported.

---
