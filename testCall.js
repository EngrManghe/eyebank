const dotenv = require("dotenv").config();
const axios = require("axios");


const api_key = process.env.CHAT_GPT_API_KEY;

//const api_key = "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"

// console.log({api_key})


async function fetchData() {
    try {

        const response = await axios.post(
            'https://api.openai.com/v1/images/generations',
            // '{\n        "prompt": "A cute baby sea otter",\n        "n": 2,\n        "size": "1024x1024"\n    }',
            {
              'prompt': 'A cute baby sea otter',
              'n': 2,
              'size': '1024x1024'
            },
            {
              headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + api_key
              }
            }
          );
        
          console.log({response})
        
    } catch (error) {
        console.log({error})
    }

}

fetchData()

//node testCall.js