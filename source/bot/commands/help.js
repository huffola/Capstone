const { SlashCommandBuilder } = require('@discordjs/builders');
const { MessageEmbed } = require('discord.js');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('help')
        .setDescription('Sends a DM with all the commands')
        .addStringOption(option => option.setName('command').setDescription('Command to provide further information on. (Leave empty for complete command list)')),
    async execute(client, message, args, Discord, interaction) {
        const prefix = require('../../env/config/config.json')
        try{
        if (interaction.options._hoistedOptions.length === 0) {
            const title = 'Here\'s a list of all my commands:';
            const description = interaction.client.commands.map(command => command.data.name).join(', ');
            const footer = `You can send \\help [command name] to get info on a specific command!`;
            const helpEmbed = new MessageEmbed()
                .setColor('RANDOM')
                .setAuthor(interaction.user.username, interaction.user.displayAvatarURL({ dynamic: true }))
                .setTitle(title)
                .setDescription(description)
                .setTimestamp()
                .setFooter(footer);
            return interaction.user.send({ embeds: [helpEmbed] })
                .then(() => {
                    if (interaction.channel.type === 'dm') return;
                    interaction.reply({content:'I\'ve sent you a DM with all my commands!', ephemeral: true});
                });
        } else {
            const commandRequested = interaction.options.get('command').value;
            const title = `Here\'s more information on the command: ${commandRequested}`;
            const description = interaction.client.commands.find(command => command.data.name === commandRequested).data.description;
            const footer = `You can send \\help [command name] to get info on a specific command!`;
            const helpEmbed = new MessageEmbed()
                .setColor('RANDOM')
                .setAuthor(interaction.user.username, interaction.user.displayAvatarURL({ dynamic: true }))
                .setTitle(title)
                .setDescription(description)
                .setTimestamp()
                .setFooter(footer);
            return interaction.user.send({ embeds: [helpEmbed] })
                .then(() => {
                    if (interaction.channel.type === 'dm') return;
                    interaction.reply({ content: `I\'ve sent you a DM with information on ${commandRequested}`, ephemeral: true});
                });
        }

        }
        catch {
             if (!args[0]) {
                    const title = 'Here\'s a list of all my commands:';
                    const description = message.client.commands.map(command => command.data.name).join(', ');
                    const footer = `You can send ${prefix.prefix}help [command name] to get info on a specific command!`;
                    const helpEmbed = new MessageEmbed()
                        .setColor('RANDOM')
                        .setAuthor(message.author.tag, message.author.displayAvatarURL({ dynamic: true }))
                        .setTitle(title)
                        .setDescription(description)
                        .setTimestamp()
                        .setFooter(footer);
                    return message.author.send({ embeds: [helpEmbed] })
                        .then(() => {
                            if (message.channel.type === 'dm') return;
                            message.reply('I\'ve sent you a DM with all my commands!');
                        });
                } else {
                    const title = `Here\'s more information on the command: ${args[0]}`;
                    const description = message.client.commands.find(command => command.data.name === args[0]).data.description;
                    console.log(description)
                    const helpEmbed = new MessageEmbed()
                        .setColor('RANDOM')
                        .setAuthor(message.author.tag, message.author.displayAvatarURL({ dynamic: true }))
                        .setTitle(title)
                        .setDescription(description)
                        .setTimestamp();
                    return message.author.send({ embeds: [helpEmbed] })
                        .then(() => {
                            if (message.channel.type === 'dm') return;
                            message.reply(`I\'ve sent you a DM with information on the command: ${args[0]}`);
                        });
                }
            }
    },
};