import React from "react"

export default function GPT(){
    const[gptResponse, setGptResponse] = React.useState();

    fetch('https://api.openai.com/v1/chat/completions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + "key"
        },
        body: JSON.stringify({
            model: 'gpt-3.5-turbo',
            messages: [{ role: 'user', content: 'Tell me a little about New York City' }],
            temperature: 0.7
        })
    })
    .then(data => data.json())
    .then(res => console.log(res))
    .catch(error => console.log(error))
    
    return(
        <div>
            GPT
        </div>
    )
}