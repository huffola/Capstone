const { CommandInteraction } = require("discord.js");

module.exports = {
    name: "interactionCreate",
   async  execute(interaction, client, message, args, Discord){
    if(!interaction.isCommand()) return;
    
    const command = interaction.client.commands.get(interaction.commandName);
    command.execute(client, message, args, Discord, interaction);
}      
};