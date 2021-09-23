module.exports ={
    name: 'ping',
    description: "Responds with Pong",
    async execute(client, message, args) {
        message.reply("Pong");
        
    }
}