function convertChatToMarkdown(chat, title)
{
    let string = "";
    if(title)
    {
        string += "# " + title + "\n";
    }
    else
    {
        string += "# " + "ChatGPT Conversation" + "\n";
    }
    string += "\n"; // two newlines because MD is like that
    let convo = chat;
    for(let i = 0; i < convo.length; i++)
    {
        let speaker = i % 2 === 0 ? "Human" : "Assistant";
        string += "**" + speaker + ":**\n";
        string += convo[i] + "\n";
        string += "\n";
        string += "***\n";
        string += "\n";
    }

    // timestamp
    let date = getDate();
    let time = getTime();

    string += "Exported on " + date + " " + time + ".";

    let blob = encodeStringAsBlob(string);
    return blob;
}