const { Interaction } = require('discord.js');

module.exports = {
    name: "ready",
    once: true,
    async execute(client) {
        var guildIds = await client.guilds.cache.map(guild => guild.id);
        var guildMembers = []
        var guildNames = [];
        var memberIDs = [];
        var temp1 = [];
        var temp2 = [];
        for (let i = 0; i < guildIds.length; i++) {
            guildNames[i] = client.guilds.cache.get(guildIds[i]).name
            memberIDs[i] = client.guilds.cache.get(guildIds[i]).members.cache.map(member => member.user.id);
        }
        for(let i = 0; i < memberIDs.length; i++){
            temp1 = String(memberIDs[i])
            temp2 += temp1 + ","
            temp2 = temp2.split(',')
            temp1 = []
        }
        for(let i = 0; i < temp2.length; i++){
            if(temp2[i].length > 0){
                temp1[i] = temp2[i]
            }
        }
        memberIDs = temp1
        for(let i = 0; i < memberIDs.length; i++){
            for(let j = 0; j < guildIds.length; j++){
                guildMembers[i] = client.guilds.cache.get(guildIds[j]).members.cache.find(member => member.user.id === memberIDs[i]);
            }
        }
        const interactionCommands = require('../deploy-commands')
        interactionCommands.execute(client)
        console.log('\x1b[36m%s\x1b[0m', `Successfully logged in as ${client.user.tag}`);
    }
}