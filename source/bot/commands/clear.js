const { SlashCommandBuilder } = require('@discordjs/builders');
const { waitForDebugger } = require('inspector');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('clear')
        .setDescription('Clears a number of messages. If no number presented, will delete 100 messages.')
        .addIntegerOption(option => option.setName('int').setDescription('Enter an integer')),
    async execute(client, message, args, Discord, interaction) {

        const wait = require('../helpercommands/timer')
        if(interaction){
            if(!(interaction.member.guild.members.cache.get(interaction.user.id).permissions.has("MANAGE_CHANNELS"))){ 
                interaction.reply({content: "You do not have permission to perform that action", ephemeral: true})
                return;
            }
        }

        try{
             args = interaction.options.get('int').value;
        }catch{}
        if(!args){
            try{
                await interaction.channel.messages.fetch({limit: 100}).then(messages => {
                    interaction.channel.bulkDelete(messages);
                }) 
                await interaction.reply("Messages have been cleared");
                await wait.execute(4000);
                await interaction.deleteReply();
                return;
            } catch {
            await message.channel.messages.fetch({limit: 100}).then(messages => {
                message.channel.bulkDelete(messages)
            })
            return;
        }
        }
        if(args > 100) return message.reply("You cannot delete more than 100 messages");
        
        try{
            await interaction.channel.messages.fetch({limit: args}).then(messages => {
                interaction.channel.bulkDelete(messages);
            })
            await interaction.reply("Messages have been cleared");
            await wait.execute(4000);
            await interaction.deleteReply();
            return;
        } catch {
        await message.channel.messages.fetch({limit: args}).then(messages =>{
            message.channel.bulkDelete(messages);
        })}
        return;
    },
};