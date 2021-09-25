const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('ping')
        .setDescription('Replies with Pong'),
    async execute(client, message, args, Discord) {
        message.channel.send("Pong")
    },
};