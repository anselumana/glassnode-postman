# Glassnode API Postman

**Glassnode API Postman collection.**

## Disclaimer

This is a **non-official** Postman collection of the Glassnode API.
I am in no way affiliated, associated, authorized, endorsed by, or in any way officially connected with Glassnode, or any of its subsidiaries or its affiliates. The name Glassnode as well as related names, marks, emblems and images are registered trademarks of their respective owners.

## Overview

This is a public repository hosting the Postman collection of the Glassnode API.

## How to import the collection

Here are the simple steps to follow in order to import the collection in Postman.

### 1. Import the collection JSON file

First of all, clone this repository in order the have the collection JSON file on your filesystem (it's under the `./postman/` directory).
Then, if you're unfamiliar with Postman, just follow thier guide at https://learning.postman.com/docs/getting-started/importing-and-exporting-data/#importing-data-into-postman.

### 2. Create an enviroment

The collection relies on a global variable named `url`, which is the base url of the API.
In order to resolve the name, you must create and enviroment and add the following key-value pair: `url`: `https://api.glassnode.com`.
Follow https://learning.postman.com/docs/sending-requests/managing-environments/#creating-environments.

### 3. Add your API Key

If you don't have a Glassnode API key, generate one at https://studio.glassnode.com/settings/api.
For help on Postman auth follow https://learning.postman.com/docs/sending-requests/authorization/#api-key.
For help on how to use the API key follow https://docs.glassnode.com/basic-api/api-key.
*Note: add the API key to the top level Glassnode API folder in order for it to be inherited by all requests.*

And that's it, have fun!