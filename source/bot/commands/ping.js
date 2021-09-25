const { SlashCommandBuilder } = require('@discordjs/builders');
const { waitForDebugger } = require('inspector');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('ping')
        .setDescription('Replies with Pong'),
    async execute(client, message, args, Discord, interaction) {

        const wait = require('../helpercommands/timer')

        if(!interaction) return message.channel.send("Pong")
        await interaction.deferReply();
        await wait.execute(4000);
        await interaction.editReply({content: 'Pong'});
    },
    
};