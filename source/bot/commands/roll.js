const { SlashCommandBuilder } = require('@discordjs/builders');
const { waitForDebugger } = require('inspector');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('roll')
        .setDescription('Rolls a random number based on amount of dice, size of the dice, and modifiers')
        .addIntegerOption(option => option.setName('amount').setDescription('Enter the amount of dice to roll'))
        .addIntegerOption(option => option.setName('size').setDescription('Enter the size of the dice'))
        .addIntegerOption(option => option.setName('modifiers').setDescription('Enter the modifiers')),
    async execute(client, message, args, Discord, interaction) {

        const wait = require('../helpercommands/timer')

        try {
            args = [interaction.options.get('amount').value, interaction.options.get('size').value, interaction.options.get('modifiers').value]
        } catch { }
        if (args === undefined) args = "";
        if (args.length === 0) {
            try {
                return interaction.reply(`Default 1D20 roll: ${Math.floor(Math.random() * 20 + 1)}`)
            } catch {
                return message.channel.send(`Default 1D20 roll: ${Math.floor(Math.random() * 20 + 1)}`)
            }
        }
        try {
            let temp = 0;
            try {
                for (let i = 0; i < args[0]; i++) {
                    temp += Math.floor(Math.random() * args[1] + 1 + args[2]);
                }
                interaction.reply(`You rolled a: ${temp}`)
            } catch {
                let tempArgs = args;
                args = [];
                tempArgs = tempArgs.join('')
                tempArgs = tempArgs.replace("d", " ").replace("+", " ").replace("-", " -").split(" ");
                args = tempArgs
                if (!args[2]) args[2] = 0;
                for (let i = 0; i < args.length; i++) {
                    args[i] = parseInt(args[i])
                }
                for (let i = 0; i < args[0]; i++) {
                    temp += Math.floor(Math.random() * args[1] + 1);
                    temp2 = args[2];
                }
                if (args[2] > 0) {
                    if (temp === 20) return message.reply(`You rolled a natural 20.\n**${temp}** + ${temp2}: ${temp + temp2}`).then(message.delete())
                    if (temp === 1) return message.reply(`You rolled a natural 1. \n **${temp}** + ${temp2}: ${temp + temp2}`).then(message.delete())
                    return message.reply(`You rolled ${temp}+${temp2}: ${temp + temp2}`).then(message.delete())
                }
                if (args[2] < 0) {
                    if (temp === 20) return message.reply(`You rolled a natural 20.\n**${temp}** ${temp2}: ${temp + temp2}`).then(message.delete())
                    if (temp === 1) return message.reply(`You rolled a natural 1. \n **${temp}** ${temp2}: ${temp + temp2}`).then(message.delete());
                    return message.reply(`You rolled ${temp} ${temp2}: ${temp + temp2}`).then(message.delete())
                }
                
            }
        } catch (e) {
            try {
                interaction.reply("An error has occured. Please check your inputs and try again");
            } catch {
                message.reply("An error has occured. Please check your inputs and try again");
            }
            console.log(e);
        }
    },
};