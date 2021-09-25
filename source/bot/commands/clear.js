const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('clear')
        .setDescription('Clears a number of messages. If no number presented, will delete 100 messages.'),
    async execute(client, message, args, Discord) {
        if(!args[0]){
            await message.channel.messages.fetch({limit: 100}).then(messages => {
                message.channel.bulkDelete(messages)
            })
        }
        if(isNaN(args[0])) return message.reply("Please enter a real number");
        if(args[0] > 100) return message.reply("You cannot delete more than 100 messages");
        if(args[0] < 1) return message.reply("You must delete at least one message");
        
        await message.channel.messages.fetch({limit: args[0]}).then(messages =>{
            message.channel.bulkDelete(messages);
        })
    },
};