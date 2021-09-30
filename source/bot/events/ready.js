const { Interaction } = require('discord.js');

module.exports = {
    name: "ready",
    once: true,
    async execute(client) {
        const interactionCommands = require('../deploy-commands')
        interactionCommands.execute(client)
        console.log(`Successfully logged in as ${client.user.tag}`);
    }
}