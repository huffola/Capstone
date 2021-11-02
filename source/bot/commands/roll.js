const { SlashCommandBuilder } = require('@discordjs/builders');
const { waitForDebugger } = require('inspector');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('roll')
        .setDescription('Rolls a random number based on amount of dice, size of the dice, and modifiers')
        .addStringOption(option => option.setName('data').setDescription("Input the desired dice like normal. I.E. 1D20 + modifier")),
    async execute(client, message, args, Discord, interaction) {

        const wait = require('../helpercommands/timer')

        try {
            args = [interaction.options.get('data').value]
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
                let tempArgs = args;
                args = [];
                tempArgs = tempArgs.join('').replace(/ /g, "")
                tempArgs = tempArgs.toLowerCase();
                tempArgs = tempArgs.replace("d", " ").replace("+", " ").replace("-", " -").split(" ");
                args = tempArgs
                if(args[0] === '') args[0] =1;
                if (!args[2]) args[2] = 0;
                for (let i = 0; i < args.length; i++) {
                    args[i] = parseInt(args[i]);
                }
                for (let i = 0; i < args[0]; i++) {
                    temp += Math.floor(Math.random() * args[1]) + 1;
                    temp2 = args[2];
                }
                if (args[2] > 0) {
                    if (temp === 20) return interaction.reply(`You rolled a natural 20.\n**${temp}** + ${temp2}: ${temp + temp2}`);
                    if (temp === 1) return interaction.reply(`You rolled a natural 1. \n **${temp}** + ${temp2}: ${temp + temp2}`);
                    return interaction.reply(`You rolled ${temp}+${temp2}: ${temp + temp2}`);
                }
                if (args[2] < 0) {
                    if (temp === 20) return interaction.reply(`You rolled a natural 20.\n**${temp}** ${temp2}: ${temp + temp2}`);
                    if (temp === 1) return interaction.reply(`You rolled a natural 1. \n **${temp}** ${temp2}: ${temp + temp2}`);
                    return interaction.reply(`You rolled ${temp} ${temp2}: ${temp + temp2}`);
                }
                if(args[2] === 0){
                    if (temp === 20) return interaction.reply(`You rolled a natural 20.\n**${temp}**`);
                    if (temp === 1) return interaction.reply(`You rolled a natural 1. \n **${temp}**`);
                    return interaction.reply(`You rolled ${temp}`);
                }
            } catch {
                temp = 0;
                for (let i = 0; i < args[0]; i++) {
                    temp += Math.floor(Math.random() * args[1]) + 1;
                    temp2 = args[2];
                }
                if (args[2] > 0) {
                    if (temp === 20) return message.reply(`You rolled a natural 20.\n**${temp}** + ${temp2}: ${temp + temp2}`)
                    if (temp === 1) return message.reply(`You rolled a natural 1. \n **${temp}** + ${temp2}: ${temp + temp2}`)
                    return message.reply(`You rolled ${temp}+${temp2}: ${temp + temp2}`)
                }
                if (args[2] < 0) {
                    if (temp === 20) return message.reply(`You rolled a natural 20.\n**${temp}** ${temp2}: ${temp + temp2}`)
                    if (temp === 1) return message.reply(`You rolled a natural 1. \n **${temp}** ${temp2}: ${temp + temp2}`)
                    return message.reply(`You rolled ${temp} ${temp2}: ${temp + temp2}`)
                }
                if(args[2] === 0){
                    if (temp === 20) return message.reply(`You rolled a natural 20.\n**${temp}**`)
                    if (temp === 1) return message.reply(`You rolled a natural 1. \n **${temp}**`)
                    return message.reply(`You rolled ${temp}`)
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