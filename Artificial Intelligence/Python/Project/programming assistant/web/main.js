import { streamGemini } from './gemini-api.js';

let form = document.querySelector('form');
let promptInput = document.querySelector('input[name="prompt"]');
let output = document.querySelector('.output');

form.onsubmit = async (ev) => {
  ev.preventDefault();

  // Display user input
  let userMessage = document.createElement('div');
  userMessage.classList.add('message', 'user-message');
  userMessage.textContent = promptInput.value;
  output.appendChild(userMessage);

  // Scroll to the bottom
  output.scrollTop = output.scrollHeight;

  // Clear input field
  let userInput = promptInput.value;
  promptInput.value = '';

  // Indicate generating response
  let botMessage = document.createElement('div');
  botMessage.classList.add('message', 'bot-message');
  botMessage.textContent = 'Generating...';
  output.appendChild(botMessage);

  try {
    // Assemble the prompt by combining the text with the chosen image
    let contents = [
      {
        type: "text",
        text: userInput,
      }
    ];

    // Call the gemini-pro-vision model, and get a stream of results
    let stream = streamGemini({
      model: 'gemini-pro',
      contents,
    });

    // Read from the stream and interpret the output as markdown
    let buffer = [];
    let md = new markdownit();
    for await (let chunk of stream) {
      buffer.push(chunk);
      botMessage.innerHTML = md.render(buffer.join(''));
      output.scrollTop = output.scrollHeight;
    }
  } catch (e) {
    botMessage.innerHTML += '<hr>' + e;
  }
};
